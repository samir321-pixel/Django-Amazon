// const response = {
//     "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjQwNTAyOTUsImlhdCI6MTYyNDAzNTg5NSwic3ViIjp7ImlkIjoiOGUzNGIwZTUtNGZiNi00ZDdkLTllYzUtN2VkOTUxYTNlNjQ4IiwiZW1haWwiOiJ0ZXN0ZXJAc2F2YW5hc29sbi5vbm1pY3Jvc29mdC5jb20ifX0.FruOJHjYm5wHFH3aftrsgAY7u5oSxxUVGPyVaeKPxSA"
// };


const response = response.json();
const obj = JSON.parse(response);

token = obj.token;