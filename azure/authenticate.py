'''https://docs.microsoft.com/en-us/samples/azure-samples/data-lake-analytics-python-auth-options/authenticating-your-python-application-against-azure-active-directory/
   https://stackoverflow.com/questions/58260616/azure-python-sdk-interact-with-azure-ad
   create service principal account:
     az ad sp create-for-rbac --name ServicePrincipalAccount --skip-assignment --sdk-auth > azure_sigma_sp.json
    setup API Permissions for Azure AD Graph
     Application - ReadWriteAll -> Grant admin consent
     on SP account
    docker run -it mcr.microsoft.com/azure-cli'''

import subprocess
import adal
from msrestazure.azure_active_directory import AADTokenCredentials
from azure.common.credentials import ServicePrincipalCredentials

TENANT_ID = '76db86ca-7aee-4d6a-81f6-46828ef7f1a7'
CLIENT_ID = 'c861bf7a-a674-4a48-a9e1-cff51d4b03b2'
CLIENT_SECRET = 'V_yhCpt940uaayz59Y-bs1-CzDZh5r.R7X'

AUTHORITY_HOST_URI = 'https://login.microsoftonline.com'
AUTHORITY_URI = f'{AUTHORITY_HOST_URI}/{TENANT_ID}'
RESOURCE_URI = 'https://management.core.windows.net/'


def authenticate_device_code():
    '''Authenticate the end-user using device auth.'''
    client_id = '04b07795-8ddb-461a-bbee-02f9e1bf7b46'

    context = adal.AuthenticationContext(AUTHORITY_URI, api_version=None)
    code = context.acquire_user_code(RESOURCE_URI, client_id)
    print(code['message'])
    mgmt_token = context.acquire_token_with_device_code(RESOURCE_URI, code, client_id)
    credentials = AADTokenCredentials(mgmt_token, client_id)
    return credentials


def authenticate_client_key():
    '''Authenticate using service principal w/ key.'''
    context = adal.AuthenticationContext(AUTHORITY_URI, api_version=None)
    mgmt_token = context.acquire_token_with_client_credentials(RESOURCE_URI, CLIENT_ID, CLIENT_SECRET)
    credentials = AADTokenCredentials(mgmt_token, CLIENT_ID)
    return credentials


def authenticate_for_graph():
    '''authenticate for graph usage'''
    resource_uri = 'https://graph.microsoft.com'
    resource_uri = 'https://graph.windows.net'
    context = adal.AuthenticationContext(AUTHORITY_URI, api_version=None)
    mgmt_token = context.acquire_token_with_client_credentials(resource_uri, CLIENT_ID, CLIENT_SECRET)
    credentials = AADTokenCredentials(mgmt_token, CLIENT_ID)
    return credentials


def authenticate_final():
    '''simple authentication'''
    credentials = ServicePrincipalCredentials(
        client_id = CLIENT_ID,
        secret    = CLIENT_SECRET,
        tenant    = TENANT_ID,
        resource  = 'https://graph.windows.net')
    return credentials


def az_shell(cmd):
    '''run az shell cmd'''
    print(cmd)
    result = subprocess.run(cmd, shell=True, capture_output=True, check=True)
    print(result.returncode)


def main():
    '''main'''
    login = f'az login --service-principal -u {CLIENT_ID} -p {CLIENT_SECRET} --tenant {TENANT_ID}'
    az_shell(login)


if __name__ == '__main__':
    main()
