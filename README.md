# MARKET+ API

A [Market+](https://capstone-api-q3.herokuapp.com/) tem como intuito ajudar a comunidade onde poderá pesquisar os produtos em nosso banco de dados, e atualizar os preços de acordo com os supermercados, ranqueando estes de acordo com o menor preço registrado. 


## Métodos
Requisições para a API devem seguir os padrões:
| Método | Descrição |
|---|---|
| `GET` | Retorna informações de um ou mais registros. |
| `POST` | Utilizado para criar um novo registro. |
| `PATCH` | Atualiza dados de um registro ou altera sua situação. |
| `DELETE` | Remove um registro do sistema. |



<h3 align='center'> Cadastro de usuário</h3>

`POST /register - para cadastro de usuários FORMATO DA REQUISIÇÃO `

```json
{
	"name": "Gabriela",
	"city": "Apucarana",
	"state":"PR",
	"country": "Brasil", 
	"email": "gabriela@email.com",
	"password": "1234"
	
}


```
Caso dê tudo certo, a resposta será assim:

`POST /register - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": ,
  "name": "Gabriela",
  "city": "Apucarana",
  "state": "PR",
  "country": "Brasil",
  "email": "gabriela@email.com"
}
```


`POST /login_users - para login de usuários FORMATO DA REQUISIÇÃO `

```json
{
	"email": "gabrielas@email.com",
	"password": "1234"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /login_users - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA3NDY0MiwianRpIjoiNWExNTFhNjQtNmYzOS00YjU2LTgzZWQtNjQxM2QxN2JlZjhmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MiwibmFtZSI6ImdhYnJpZWxhIiwiY2l0eSI6ImFwdWNhcmFuYSIsInN0YXRlIjoiUFIiLCJjb3VudHJ5IjoiQnJhc2lsIiwiZW1haWwiOiJnYWJyaWVsYXNAZW1haWwuY29tIn0sIm5iZiI6MTYzOTA3NDY0MiwiZXhwIjoxNjM5MDc1NTQyfQ.SU8PBco6gZaLVtsOViDo4werwJHi3GcAkxxsbIZt3rk"
}
```

`GET /users -  FORMATO DA REQUISIÇÃO `

Caso dê tudo certo, a resposta será assim:

`GET /users - FORMATO DA RESPOSTA - STATUS 200`

```json
[
  {
    "id": 1,
    "name": "kaio",
    "city": "brasólia",
    "state": "DF",
    "country": "Brasil",
    "email": "kaio@email.com",
    "sugestions": [],
    "favorite_products": []
  }
]
```

`PATCH /users/1 -  FORMATO DA REQUISIÇÃO `

```json
{
  "name": "Gabriela Rodrigues",
  "city": "Apucarana",
  "state": "PR",
  "country": "Brasil",
  "email": "gabriela@email.com"
}
```

Caso dê tudo certo a resposta será assim:

`PATCH /users/1 - FORMATO DA RESPOSTA - 201`

```json

{
  "id":1,
  "name": "Gabriela Rodrigues",
  "city": "Apucarana",
  "state": "PR",
  "country": "Brasil",
  "email": "gabriela@email.com"
}
```


`DELETE /users/1 -  FORMATO DA REQUISIÇÃO- 201`

Caso dê tudo certo a resposta será assim:

`DELETE /users/1 - FORMATO DA RESPOSTA - 201`
""


