import subprocess

def get_current_account():
    '''Get current active gcloud user'''
    user_cmd = 'gcloud config get-value core/account'
    active_user = subprocess.run(user_cmd, shell=True, capture_output=True, check=True)
    active_user = str(active_user.stdout, 'utf-8').strip()
    return active_user

def set_active_user(acccount):
    '''Set current active gcloud user'''
    user_cmd = f'gcloud confie set account {account}'
    subprocess.run(user_cmd, shell=True, capture_output=True, check=True)

def revoke_active_user(account):
    '''Revove current active gcloud user'''
    user_cmd = f'gcloud auth revoke {account}'
    subprocess.run(user_cmd, shell=True, capture_output=True, check=True)