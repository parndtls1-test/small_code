'''azure key stuff
   needs azure cli installed'''
from azure.identity import DefaultAzureCredential#, ClientSecretCredential
from azure.keyvault.keys import KeyClient

TENANT_ID = '76db86ca-7aee-4d6a-81f6-46828ef7f1a7'
CLIENT_ID = ''
# CLIENT_SECRET = '' ???

CREDENTIAL = DefaultAzureCredential()
KEY_VAULT = 'Arndt1' # 'base-vault'
VAULT_URL = f'https://{KEY_VAULT}.vault.azure.net/'
KEY_CLIENT = KeyClient(vault_url=VAULT_URL, credential=CREDENTIAL)


def get_key(keyname):
    '''get key'''
    key = KEY_CLIENT.get_key(keyname)
    print(key)
    print(key.name)
    return key.name


def create_rsa_key(keyname):
    '''create rsa key'''
    rsa_key = KEY_CLIENT.create_rsa_key(keyname, size=2048)
    print(rsa_key.name)
    print(rsa_key.key_type)
    return (rsa_key.name, rsa_key.key_type)


def create_ecurve_key(keyname):
    '''Create elliptic curve key'''
    ec_key = KEY_CLIENT.create_ec_key(keyname, curve="P-256")
    print(ec_key.name)
    print(ec_key.key_type)
    return (ec_key.name, ec_key.key_type)


def disable_key(keyname):
    '''disable key'''
    updated_key = KEY_CLIENT.update_key_properties(keyname, enabled=False)
    print(updated_key.name)
    print(updated_key.properties.enabled)
    return (updated_key.name, updated_key.properties.enabled)


def delete_key(keyname):
    '''delete key'''
    deleted_key = KEY_CLIENT.begin_delete_key(keyname).result()
    print(deleted_key.name)
    print(deleted_key.deleted_date)
    return (deleted_key.name, deleted_key.deleted_date)


def list_keys():
    '''list keys,
       the list doesn't include values or versions of the keys'''
    keys = KEY_CLIENT.list_properties_of_keys()
    print(keys)
    for key in keys:
        print(key.name)
    return [key.name for key in keys]


if __name__ == '__main__':
    #create_rsa_key('test2')
    print()
    get_key('test1')
    get_key('test2')
    print()
    list_keys()
    #credentials = authenticate_device_code(TENANT_ID)
    from azure.graphrbac import GraphRbacManagementClient
    azure_graphrbac_client = GraphRbacManagementClient(credentials=KEY_CLIENT, tenant_id=TENANT_ID)
    print(azure_graphrbac_client)

    app_list = ['app1']

    for app_name in app_list:
        for app in azure_graphrbac_client.applications.list(filter=f'displayName eq {app_name}'):
            appid = azure_graphrbac_client.applications.get(app.object_id)
            owners = azure_graphrbac_client.applications.list_owners(app.object_id)
            print(appid, owners)
