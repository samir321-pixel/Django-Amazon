client_id = "d716fc52-adcf-461e-9fc4-625a02f5df1b"
app_secret = "-h5131XtDOoIlTtU28xIXz9s_~7Pda-M61"
redirect = "https://seda-dev.mycleancity.nl/admin"
scopes = "openid+User.Read"
state = "session_id()"
response_type = "code"
approval_prompt = "auto"
logout_uri = "http://localhost:8000/admin/logout"
tenant = "d0db0b7e-ceac-44dc-8813-a89c1a10c5a6"
microsoft = "https://login.microsoftonline.com/"
API = microsoft + tenant + "/oauth2/v2.0/authorize?client_id=" + client_id + "&response_type=" + response_type + "&redirect_uri=" + redirect + "&scope=" + scopes

print(API)

url = "https://login.microsoftonline.com/d0db0b7e-ceac-44dc-8813-a89c1a10c5a6/oauth2/v2.0/authorize?client_id=d716fc52-adcf-461e-9fc4-625a02f5df1b&response_type=code&redirect_uri=https%3A%2F%2Fseda-dev.mycleancity.nl%2Fadmin&scope=+offline_access+openid+profile&state=mTRYdgGrIZvfOnLp&nonce=7cfcf1e920038f1f1a7cee14f5fcee298113c01254c45c171e20c8e42eebf737"

token = {
    '"0.AYIAfgvb0KzO3ESIE6icGhDFplL8FtfPrR5Gn8RiWgL13xuCAAA.AQABAAIAAAD--DLA3VO7QrddgJg7WevrK8-42URIupu2u4BtoFN_N7EoqVNMrws3w5gchpSlpOlNln2EQbRnYNd5uQk4k_XQGuVr5SXbsZJsTb3ltxkEZx5O-FzSo9_OgKUZdyjyFRA20z-YIi53f6fNSkF19HF1VEboILxdoeevbZMSC8zAhnWQKIrar9LAEMdStCa4stHi9-oVN3vaPCGl6aYCnP1aeSLRu1DHX6n1mhEUKvFeOp-7Objsa4blKxTN6wgIJ9QYNNwPoh0EGJbocsfVjctnylWIiUKEaOKv7RdcuNLLTWWTuE3SXNoqW1ZLFTrSCuDbIMs5Bruey9u0HOmPVG7BKyo7a-bqu3DTiQOECYrPfwHthDpHCZUkge2W3XJV0xIyG987a8bcXasKFiCLme-t-I_62xbXp4TLwuMPHDTNPGWR-SIXxQGsNHt8LGHl1WtXxdDoB_S2zS9_TDMc_Z5MIHP4NMhI7SaSvF-sdWjyozPxTpzshM5XQO-Vvxmh7IbpQLposwHtKWxaY-M7q4a9G7wmuJfhETlmqOYcG1jKnsT8_ACvVY7NNZyvJLV7c7Jue74XYSt1uHpHsIcgQueg5Qh24GDY3V7qvkHfgjRwvTDo8soPEI9J7hYqrD_EbVEiWlUWkBYBrhLkB6Ge6BSLIfZ6BmRxLqPZIJB50oA4wiAA"': [
        '']}

# print(type(token))

for key in token.keys():
    # print(key)
    code = key

# print(code)
