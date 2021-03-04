'''reset app registration password
   create service principal account:
     az ad sp create-for-rbac --name ServicePrincipalAccount1 \
         --skip-assignment --sdk-auth
    setup API Permissions for Azure AD Graph
     Application - ReadWriteAll -> Grant admin consent
     on SP account
'''

import subprocess

TENANT_ID = '76db86ca-7aee-4d6a-81f6-46828ef7f1a7'
CLIENT_ID = 'c861bf7a-a674-4a48-a9e1-cff51d4b03b2'
CLIENT_SECRET = 'V_yhCpt940uaayz59Y-bs1-CzDZh5r.R7X'


def az_shell(cmd):
    '''run az shell cmd'''
    print(cmd)
    result = subprocess.run(cmd, shell=True, check=True)
    print(result.returncode)


def main():
    '''main'''
    # object_ids
    obj_list = ['31ea3375-52e2-4c24-b5f7-9db91c321670',
                'dc72b68f-03ca-40a5-bda4-8b0ca685f223']

    login = f'az login --service-principal -u {CLIENT_ID} -p {CLIENT_SECRET} --tenant {TENANT_ID}'
    az_shell(login)
    print()

    for object_id in obj_list:
        print(f'Application ID: {object_id}')
        reset = f'az ad app credential reset --id {object_id} --credential-description new-password'
        az_shell(reset)
        print('------------------------------')

    logout = 'az logout'
    az_shell(logout)


if __name__ == '__main__':
    main()
