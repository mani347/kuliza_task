=> api/v1/signup
HTTP Method = POST
request payload:
{
    "username": "<username>",
    "email": "<email>",
    "password": "<password>"
}
success HTTP status code = 200


=> api/v1/login
HTTP Method = POST
request payload:
{
    "username": "<username>",
    "password": "<password>"
}
success HTTP status code = 200



=> api/v1/orders
HTTP Method = POST
Headers:
Authorization: Token <token received from login or signup API>
request payload:
{
    "house": "13",
    "lat": 28.094820,
    "long": 78.149590
}
success HTTP status code = 200

HTTP Method = GET
Headers:
Authorization: Token <token received from login or signup API>
success HTTP status code = 200
