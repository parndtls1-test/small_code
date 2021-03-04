import subprocess

TENANT_ID = '76db86ca-7aee-4d6a-81f6-46828ef7f1a7'
CLIENT_ID = 'c861bf7a-a674-4a48-a9e1-cff51d4b03b2'
CLIENT_SECRET = '-953BN.54N1E8R_3B-En7LR92VkGNXzm2B' # does not work with - or quotes around it
CLIENT_SECRET = 'V_yhCpt940uaayz59Y-bs1-CzDZh5r.R7X'

# az login --service-principal -u <app-url> -p <password-or-cert> --tenant <tenant>
login = f'az login --service-principal -u {CLIENT_ID} -p {CLIENT_SECRET} --tenant {TENANT_ID}'
print(login)
res = subprocess.run(login, shell=True, capture_output=True, check=True)
print(res)

remove = 'az ad app credential delete --id 31ea3375-52e2-4c24-b5f7-9db91c321670 --key-id fc6e0e1a-d863-49bf-92a4-c59ae7a5480a'
print(remove)
res = subprocess.run(remove, shell=True, capture_output=True, check=True)
print(res)
