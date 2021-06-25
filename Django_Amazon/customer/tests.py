import getpass
import requests
from pprint import pprint

# Ask for password
# user = getpass.getuser()
# password = getpass.getpass("Password for "+user+": ")
password = "Haru18444"
user = "tester@savanasoln.onmicrosoft.com"

# # Get an access token
# payload = {
#     "grant_type": "password",
#     "client_id": "d716fc52-adcf-461e-9fc4-625a02f5df1b",
#     "scope":"User.read",
#     "response_type":"code",
#     "username": user,
#     "password": password,
# }
# from rest_framework_jwt.settings import api_settings

# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#
# payload = jwt_payload_handler(user)
# jwt_token = jwt_encode_handler(payload)
# print(jwt_token)


urrl = "https://login.microsoftonline.com/d0db0b7e-ceac-44dc-8813-a89c1a10c5a6/oauth2/v2.0/token"

url3 = "https://graph.microsoft.com/v1.0/me"

data = {
    "code":"D0.AYIAfgvb0KzO3ESIE6icGhDFplL8FtfPrR5Gn8RiWgL13xuCAAA.AQABAAIAAAD--DLA3VO7QrddgJg7Wevr2OluwxUi8pgz9pJKm7HM0XzEemZIV7hYO-H-FAx30KMIrvOxaqe7XFJEKA0yjGLzQJ3RgPnZrzXvtGJDr4JIP21YXx00CGev5KKlm6ZROVWlU9Lil3ITukceI9oLh-PsZlfQSwHH7HW0wymNmWWM0wXR89JIR9d_IdtUnGQPtWd7KgYLJPXdViwdq50V5f_eFoiwwUMpiKNxlJftsm44Bf0vI8Om9eiokNEq88URRae3ch4H4elCWKjAFUUDRk1xXpn5_OpoZPuchZiX7agrjOsQH7RaMHx02Bocnq_jM0M1faihvJIN9xKAO74_M-KfDUg4Fhf6-B3WtCjgbQNVpiOwJJjNeRYgQ32vyNBKbh8TmBK4ko4X66vmYIHNEhe3GkXtcqyzQ7nQume0OyFR3jUZfA6j61fe-dT4QsR5s8XNusVIKR-nuxaJqcoj4YWdH85FX2MBClh4fisf4EJJ2mfogMVd1j37I4CX5CHeLaj5zYVhtcWamwRsfIKpP1ThuLTBRwu3OTpO0cROOvcc767RBX7wbHSCIP3GG46oJED3HBF1h8MoAatesWC5uYf52yTyBahnuenswyOzduXf3wMTfHkFu3p-Akw1ojUmruAraPa6QjarUc9U8b0xIL6WgDcLaWxVlmguLubFA_plVfTzx7sBWC5pJBRMpVBvD7qEzbgo1UsQ8BAtHe74o-pjfqPpShmVhZcztQlQi4tM_PwRdon2_gAS65Zkph5M9S97HE4OUgFrVqZd-nmfSEUjIAA%26state%3DWctZHlXGOFJhfUkP",
    "grant_type": "password",
    "username": "tester@savanasoln.onmicrosoft.com",
    "password": password,
    "client_id": "d716fc52-adcf-461e-9fc4-625a02f5df1b",
    "scope": "User.read",
    "client_secret":"-h5131XtDOoIlTtU28xIXz9s_~7Pda-M61",
    "session_state":"3D78a9756c-f210-423c-85a0-ea764cab8ca2"
}
res = requests.post(urrl, data=data)
print(res.json())
data2=res.json()
token = data2["access_token"]
print(token)
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {}'.format(token)}
url2 = "https://graph.microsoft.com/v1.0/me"
res2 = requests.get(url2, headers=headers)
print("this is second rresponse", res2.json())
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
