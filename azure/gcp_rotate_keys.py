''' GCP Service Account Key Rotation Utility '''
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from wmt_keywhiz.secrets import Secrets # walmart dependant


class Rotator:
    ''' GCP Service Account Key Rotate '''
    def __init__(self, account):
        ''' Init Key Object '''
        self.account = account
        # Parse Account Name to map name/project_id
        account_pattern = re.match(r"(?P<account_name>.*)@(?P<project_id>[a-zA-z0-9-]*)\..*$", self.account)
        if account_pattern:
            account_parts = account_pattern.groupdict()
            self.project_id = account_parts['project_id']
            self.account_name = account_parts['account_name']
        else:
            # Invalid Account Specified - Mark Key Object as invalid - Take no rotation actions
            print(f"Invalid Account Format - Skipping Rotation for Account: '{account}'")
            self.invalid = True


    def list_keys(self):
        ''' List Service Account Keys '''
        try:
            # Retrieve list of all current 'USER_MANAGED' Account keys
            list_keys_cmd = f"gcloud iam service-accounts keys list --iam-account '{self.account}' --project '{self.project_id}' --format json --filter='keyType=USER_MANAGED'"
            keys_list = subprocess.run(list_keys_cmd, shell=True, capture_output=True, check=True)
            keys = json.loads(keys_list.stdout)
            return keys
        except subprocess.CalledProcessError as err:
            print(err)
        return list()


    def delete_key(self, key):
        ''' Delete Key by Name '''
        try:
            print("\nDeleting Existing Key:")
            print(json.dumps(key, indent=2))
            key_id = key['name'].split('/')[-1]
            delete_cmd = f"gcloud iam service-accounts keys delete '{key_id}' --iam-account '{self.account}' --project '{self.project_id}' --quiet"
            print(f"Command  - '{delete_cmd}'")
            subprocess.run(delete_cmd, shell=True, capture_output=True, check=True)
        except subprocess.CalledProcessError as err:
            print(err)


    def create_key(self, secrets_client):
        ''' Create Key '''
        # Gen temp keyfilepath to store created svc acct key
        key_path = tempfile.mkstemp(prefix=self.account)
        key_path = key_path[1]

        try:
            print(f"\nCreating New Key for: '{self.account}'")
            # Generate key to temp filepath
            create_cmd = f"gcloud iam service-accounts keys create '{key_path}' --iam-account '{self.account}' --project '{self.project_id}'"
            print(f"\nCommand - '{create_cmd}'")
            subprocess.run(create_cmd, shell=True, capture_output=True, check=True)

            # Read Key Datafile
            with open(key_path, 'r') as infile:
                data = infile.read()
                data = data.strip()
            # Load Key Data JSON
            key_json = json.loads(data)
            print(f"\n- New Key created with key id: '{key_json['private_key_id']}'")
            # Write Key Content to Keywhiz
            secret_data = {
                'secret_name': self.account,
                'description': f"Service Account Cred - '{self.account_name}'",
                'content': data,
            }
            secrets_client.manage_secret(**secret_data)
        except subprocess.CalledProcessError as err:
            # Log Error on cmd failure
            print(err)
        finally:
            # Always Cleanup temp filepath if found
            if os.path.exists(key_path):
                print(f"Removing Temporary credential file path at: '{key_path}'")
                os.remove(key_path)


def get_account_keys(filepath, gcs_file=False):
    ''' Parse Service Accounts Input File and Delete/Refresh Keys '''
    # Keywhiz Client Setup
    secret_user = os.environ.get('KEYWHIZ_USER', os.environ.get('USER'))
    secret_app = os.environ.get('KEYWHIZ_APP', 'pca_gcp-accounts_prod')
    # Credential loaded via `CLIENT_SECRET` env var
    print('\nInitializing Keywhiz Secrets Client:')
    secrets = Secrets(username=secret_user, app=secret_app)
    # Auth as Service Key Rotator
    try:
        # Load Credential for gcloud - if not specified as ENV var `ROTATION_ACCOUNT`
        # Will lo
        key_mgmt_account = os.environ.get('ROTATION_ACCOUNT', secret_user)
        # Authenticate via Service Account - retrieve cred from keywhiz
        # Otherwise, will use active loaded `account` from gcloud config
        svc_cred_file = None
        if key_mgmt_account != secret_user:
            svc_cred_file = secrets.get(secret_name=key_mgmt_account, file=True)
            subprocess.run(f"gcloud auth activate-service-account --key-file {svc_cred_file}", shell=True, check=True)
    except subprocess.CalledProcessError as err:
        raise err
    finally:
        # Always remove any Service Account keyfile if retrieved from keywhiz
        if svc_cred_file and os.path.exists(svc_cred_file):
            os.remove(svc_cred_file)
    # Retrieve Target file from GCS - else default to argparse value for args.file
    if gcs_file:
        try:
            subprocess.run(f"gsutil cp {filepath} .", shell=True, check=True)
            filepath = filepath.split('/')[-1]
        except subprocess.CalledProcessError as err:
            raise err

    # Parse Inventory File
    with open(filepath, 'r') as infile:
        all_accounts = infile.readlines()
    # Strip newlines if found
    all_accounts = [account.strip() for account in all_accounts if account]
    print('Targeting Key Rotation and Keywhiz injection for following GCP Service Accounts:')
    print(json.dumps(all_accounts, indent=2))
    rotation_failures = list()

    # Rotate all accounts
    for account in all_accounts:
        try:
            print(f"\nScanning Account: '{account}' for user-managed keys to rotate")
            # Generate Key oobject for Targeted Account
            rotator = Rotator(account=account)
            # Skip if unable to parse account name
            if hasattr(rotator, 'invalid'):
                continue
            # If Existing Keys Found - Delete and refresh
            all_keys = rotator.list_keys()
            if all_keys:
                for key in all_keys:
                    rotator.delete_key(key=key)
                # Create new key and Load into Keywhiz
                rotator.create_key(secrets_client=secrets)
                print(f"Successfully Rotated Keys for Account: '{account}'")
            else:
                print(f"Unable to Access Keys for account '{account}' - Skipping Rotation")
                continue
        except subprocess.CalledProcessError as err:
            # Log rotation failure for account and append to failure list
            print(err)
            rotation_failures.append(account)
    # We were unable to rotate at least one managed key
    # FAIL
    if rotation_failures:
        print('The following keys failed rotation:')
        print(json.dumps(rotation_failures, indent=2))
        sys.exit(1)


def main():
    ''' Main Program for Key Rotation '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=False, default='./service_accounts.txt', type=str, help='File path or GCS Url to input File of Service Account IDs to rotate')
    args = parser.parse_args()
    # Set Flag to retrieve file content from GCS
    gcs_file = False

    if re.match('gs://', args.file):
        gcs_file = True
    # if File not found - exit
    elif not os.path.isfile(args.file):
        print(f'File: {args.file} not found - please pass valid filepath')
        sys.exit(1)
    # Build list of Service Accounts and rotate Keys
    get_account_keys(filepath=args.file, gcs_file=gcs_file)


if __name__ == '__main__':
    main()
    