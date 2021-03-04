import subprocess

TENANT_ID = '76db86ca-7aee-4d6a-81f6-46828ef7f1a7'
CLIENT_ID = 'c861bf7a-a674-4a48-a9e1-cff51d4b03b2'
CLIENT_SECRET = 'V_yhCpt940uaayz59Y-bs1-CzDZh5r.R7X'

login = f'az login --service-principal -u {CLIENT_ID} -p {CLIENT_SECRET} --tenant {TENANT_ID}'
print(login)
res = subprocess.run(login, shell=True, capture_output=True, check=True)
print(res)

app_list = ['app1']#, 'app2']#, 'app3', 'app4', 'app5']

for app in app_list:
    getid = f'az ad app list --display-name {app}'
    print(getid)
    res = subprocess.run(getid, shell=True, capture_output=True, check=True)    
    for line in res.stdout.decode('utf-8').rstrip():
        print(line)


