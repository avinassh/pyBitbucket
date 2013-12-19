import json

import requests
from requests.auth import HTTPBasicAuth

# to create a new repository : 
# curl -X POST -u BB_USERNAME:BB_PASSWORD -H "Content-Type: application/json" https://api.bitbucket.org/2.0/repositories/BB_USERNAME/NEW_REPO_NAME -d '{"scm": "git", "is_private": true}'
# 

# to invite a new user to the private repo
# curl --user BB_USERNAME:BB_PASSWORD --request POST https://bitbucket.org/api/1.0/invitations/BB_USERNAME/REPO_NAME/email_of_the_invitee --data permission=write
#

# to delete a repo
# curl -X DELETE --user BB_USERNAME:BB_PASSWORD https://api.bitbucket.org/2.0/repositories/BB_USERNAME/REPO_NAME

BB_USERNAME = ''
BB_PASSWORD = ''
REPO_API_URL = 'https://api.bitbucket.org/2.0/repositories/'
INVITE_API_URL = 'https://bitbucket.org/api/1.0/invitations/'

def create_repo(repo_name):
    auth = HTTPBasicAuth(BB_USERNAME, BB_PASSWORD)
    url = REPO_API_URL+BB_USERNAME+'/'+repo_name
    payload = { "scm": "git", "is_private": "true"}
    headers = {'content-type': 'application/json'}
    response = requests.post(url=url, data=payload, auth=auth)
    print repo_name, response.status_code
    #print response.text
    #print '\n'

def invite_user_to_repo(repo_name, invitee_email):
    auth = HTTPBasicAuth(BB_USERNAME, BB_PASSWORD)
    url = INVITE_API_URL+BB_USERNAME+'/'+repo_name+'/'+invitee_email
    payload = { "permission" : "write" } 
    response = requests.post(url=url, data=payload, auth=auth)
    print repo_name, response.status_code
    #print response.text
    print '\n'

if __name__ == '__main__':
    for i in range(1, 180):
        create_repo(str(i))
        invite_user_to_repo(str(i), 'some_email@some_email.com')




