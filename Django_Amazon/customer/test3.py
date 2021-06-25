import getpass
import requests
from pprint import pprint

# Ask for password
# user = getpass.getuser()
# password = getpass.getpass("Password for "+user+": ")
password = "Haru18444"
user = "tester@savanasoln.onmicrosoft.com"

urrl = "https://login.microsoftonline.com/d0db0b7e-ceac-44dc-8813-a89c1a10c5a6/oauth2/v2.0/token"

url3 = "https://graph.microsoft.com/v1.0/me"
data = {'grant_type': 'authorization_code',
        'client_id': 'd716fc52-adcf-461e-9fc4-625a02f5df1b',
        'redirect_uri': 'https://seda-dev.mycleancity.nl/admin',
        'code': '0.AYIAfgvb0KzO3ESIE6icGhDFplL8FtfPrR5Gn8RiWgL13xuCAAA.AQABAAIAAAD--DLA3VO7QrddgJg7Wevrh34Th4TitTztYz72MUltT6d7yRVERHN3YpxizPSA_vwO0L6xBa5CC0bD0swB7b_G5CJCXU6GB7ExDtc9gcCJFZqYAN5nZ_VmDHD-VgJ67llWQhUEzvFEFqxLt9aWhXclGlLFjSbZx5cffn7zl5F9ftXIVY7J7FhDufnZha9VdwQMGlHTWuFIMnOXhMzBkf_F9EQ1KyQ3bl5Swb2SRW9BZzfc-XKsBMdqAKj4N4GPlqh0MVXFZdx-wmlnOM2j15AI4LKJfewpZq8bwIT-xuTErF0FKCcNOZphA56AGOSj8Q41qwjIAixVbmTobEO7pQfoxgUg681U63CMIDYQKRzu2YxJFw3JMVRsePmX0WMmXx59WGFrdW0OdUdBsQlN0qpW7rnK_m0ntHkZ_JZ7OErTLkb3m2B2IiuZmf7EIohRbDt35WyCimhmPoiR1Bqmq9sQR3EVzJ8CHqPr_Y6RZ5Fh7IZC-axZn32VYyTXFK44uT8IRagDHp00lqN-KDP85DfKJnxSb9uBEMRB0ZLaD5O6rJd_YmagVExdLg46KzdvFChFy34w6izNFzMqoRfIZf2FTNfz0cs2h0POH_SoNtcALrGnVMWHmtj3zwyCn057s3V4NwaIwDNH1kzm4aU1jWFyIAA',
        'client_secret': '-h5131XtDOoIlTtU28xIXz9s_~7Pda-M61'}

res = requests.post(urrl, data=data)
print(res.json())



# data2 = res.json()
# token = data2["access_token"]
# print(token)
# headers = {'Content-Type': 'application/json',
#            'Authorization': 'Bearer {}'.format(token)}
# url2 = "https://graph.microsoft.com/v1.0/me"
# res2 = requests.get(url2, headers=headers)
# print("this is second rresponse", res2.json())
# response = requests.post(
#     'https://login.microsoftonline.com/d0db0b7e-ceac-44dc-8813-a89c1a10c5a6/oauth2/v2.0/authorize',
#     data=payload,
#     verify=False
# )
# print(response, "First Response")
# response.raise_for_status()
# response_data = response.json()
# access_token = response_data['access_token']
#
# # Make a request towards this API
# headers = {
#     'Accept': 'application/json',
#     'Authorization': 'Bearer ' + access_token,
# }
# response = requests.get(
#     'https://login.microsoftonline.com/d0db0b7e-ceac-44dc-8813-a89c1a10c5a6/oauth2/v2.0/authorize?',
#     headers=headers,
#     verify=False
# )
# pprint(response)
