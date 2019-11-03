import requests

def auth_nxapi(url,user_name, password, *, verify=False):
    auth_payload = {
        "aaaUser": {
            "attributes": {
                "name": user_name,
                "pwd": password
            }
        }
    }
    response = requests.post(url + '/api/aaaLogin.json', json=auth_payload, verify=verify)
    return dict(Cookie=f"APIC-cookie={response.cookies['APIC-cookie']}")


def nxapi_show_version():
    url = 'https://sbx-nxos-mgmt.cisco.com/ins'
    switchuser = 'admin'
    switchpassword = 'Admin_1234!'

    http_headers = {'Content-type': 'application/json-rpc'}
    payload = [{"jsonrpc": "2.0",
                "method": 'cli',
                "params": {"cmd": 'show version',
                           "version": 1}, "id": 1}]
    
    response = requests.post(url, json=payload, verify=False, headers=http_headers, auth=(switchuser, switchpassword))

    if response:
        version = response.json()['result']['body']['kickstart_ver_str']
        return version
    else:
        print(response.headers['Allow'])
        return None


if __name__ == '__main__':
    result = nxapi_show_version()
    print(result)
