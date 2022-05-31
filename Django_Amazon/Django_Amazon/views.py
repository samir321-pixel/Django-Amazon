from django.http import HttpResponse
import datetime
from django.shortcuts import redirect, render


def microsoft(request):
    client_id = "d716fc52-adcf-461e-9fc4-625a02f5df1b"
    app_secret = "-h5131XtDOoIlTtU28xIXz9s_~7Pda-M61"
    redirect_url = "https://seda-dev.mycleancity.nl/admin"
    scopes = [""]
    authority = "https://login.microsoftonline.com/d0db0b7e-ceac-44dc-8813-a89c1a10c5a6",
    valid_email_domains = [""]
    logout_uri = "http://localhost:8000/admin/logout"
    tenant = "d0db0b7e-ceac-44dc-8813-a89c1a10c5a6"
    microsoft = "https://login.microsoftonline.com/"
    url = "https://login.microsoftonline.com/d0db0b7e-ceac-44dc-8813-a89c1a10c5a6/oauth2/v2.0/authorize?client_id=d716fc52-adcf-461e-9fc4-625a02f5df1b&response_type=code&redirect_uri=https%3A%2F%2Fseda-dev.mycleancity.nl%2Fadmin&scope=+offline_access+openid+profile&state=mTRYdgGrIZvfOnLp&nonce=7cfcf1e920038f1f1a7cee14f5fcee298113c01254c45c171e20c8e42eebf737"
    API = microsoft + tenant + "/oauth2/v2.0/authorize?client_id=" + client_id + "&response_type=code&redirect_uri=" + redirect_url + "&scope=+offline_access+openid+profile"

    # print(API)
    url = "https://login.microsoftonline.com/d0db0b7e-ceac-44dc-8813-a89c1a10c5a6/oauth2/v2.0/authorize?client_id=d716fc52-adcf-461e-9fc4-625a02f5df1b&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fadmin&scope=+offline_access+openid+profile&state=yMDWsoBHxwmPEiUN&nonce=595f0bf9da2b53373b1586afba882d30bae721972bae1a0b4441cc26acf30d60"
    response = redirect(url)
    return response


import requests

urrl = "https://login.microsoftonline.com/d0db0b7e-ceac-44dc-8813-a89c1a10c5a6/oauth2/v2.0/token"


def adminfunction(request):
    parameter = request.GET.get("code")
    # print(parameter, "this is parameter")
    data = {
        "grant_type": "authorization_code",
        "client_id": "d716fc52-adcf-461e-9fc4-625a02f5df1b",
        "redirect_uri": "http://localhost:8000/admin",
        "code": parameter,
        "client_secret": "-h5131XtDOoIlTtU28xIXz9s_~7Pda-M61",
    }
    # res = requests.post(urrl, data=data,
    #                     headers={'Content-Type': 'application/x-www-form-urlencoded', 'Content-Length': "1029"})
    res = requests.post(urrl, data=data)
    # print(res)
    # print(res.json())
    data = res.json()
    url3 = "https://graph.microsoft.com/v1.0/me"
    # print("this is needed", data['access_token'])
    headers = {'Authorization': 'Bearer {}'.format(data['access_token'])}
    res2 = requests.get(url3, headers=headers)
    print("2nd response of azure ", res2.json())
    data2 = res2.json()
    print(data2["userPrincipalName"])
    return HttpResponse("ok")


def get_content_length(data):
    length = len(data.keys()) * 2 - 1
    total = ''.join(list(data.keys()) + list(data.values()))
    length += len(total)
    print(length, "length is ")
    return length
