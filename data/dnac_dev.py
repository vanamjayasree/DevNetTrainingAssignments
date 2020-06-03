import json
import requests

def token(url,passwd):
    payloadData = {}
    header = {'Authorization': 'Basic {}'.format(passwd)}
    resp = requests.request("POST", url, headers=header, data = payloadData)
    token=(resp.json())['Token']
    return(token)

def device(url,token):
    payloadData={}
    header={'x-auth-token' : token}
    resp = requests.request("GET", url, headers=header, data = payloadData)
    return (resp.json())['response']

token = token('https://sandboxdnac2.cisco.com/api/system/v1/auth/token','ZG5hY2RldjpEM3Y5M1RAd0sh')
data=device('https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device',token)
print(data)