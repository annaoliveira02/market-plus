# Market+ API - Documentação
## Introdução
O **Market+** surgiu da necessidade de facilitar a pesquisa de preço entre supermercados, trazendo praticidade ao consumidor, através de uma aplicação que concentra, mapeia e compara os valores dos principais produtos nos supermercados mais próximos ao usuário, em um trabalho colaborativo com esses estabelecimentos.

Esta API é o backend da aplicação **Market+**, feita em padrão REST. O objetivo é organizar as requisições de forma intuitiva e personalizável, afim de oferecer o máximo de informações, da melhor forma possível. Através dela, é possível obter e criar informações sobre produtos, lojas, preços e muito mais.

## Métodos
Requisições para a API devem seguir os padrões:

| Método | Descrição |
|-----------|------------|
| `GET` | Retorna informações de um ou mais registros. |
| `POST` | Utilizado para criar um novo registro. |
| `PATCH` | Atualiza dados de um registro ou altera sua situação.|
| `DELETE` | Remove um registro do sistema. |

## Endpoints

A API tem um total de 8 endpoints, que estão em torno principalmente do usuário (user) e da loja (store) - podendo cadastrar seus perfis, e realizar requisições específicas.

O url base da API é [https://capstone-api-q3.herokuapp.com/](https://capstone-api-q3.herokuapp.com/)

### Criando usuário
`POST /register - FORMATO DA REQUISIÇÃO `

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

### Login do usuário

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

### Buscar usuários
`GET /users -  FORMATO DA REQUISIÇÃO `

Caso dê tudo certo, a resposta será assim:

`GET /users - FORMATO DA RESPOSTA - STATUS 200`

```json
[
  {
    "id": 1,
    "name": "kaio",
    "city": "brasília",
    "state": "DF",
    "country": "Brasil",
    "email": "kaio@email.com",
    "sugestions": [],
    "favorite_products": []
  }
]
```

### Editar informações do usuário

Esta rota precisa de permissão específica, tendo em mente que apenas o usuário logado consegue editar o próprio perfil. Deve ser informado no cabeçalho da requisição o campo "Authorization", dessa forma:

> Authorization: Bearer {token}

`PATCH /users -  FORMATO DA REQUISIÇÃO `

```json
{
  "name": "Gabriela Rodrigues"
}
```

Caso dê tudo certo a resposta será assim:

`PATCH /users - FORMATO DA RESPOSTA - 201`

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

### Remover usuário

Deve ser informado no cabeçalho da requisição o campo "Authorization", dessa forma:

> Authorization: Bearer {token}

`DELETE /users/1 - FORMATO DA REQUISIÇÃO`

Caso dê tudo certo a resposta será assim (sem mensagem):

`DELETE /users/1 - FORMATO DA RESPOSTA - 204`


### Cadastrando supermercado
`POST /stores - FORMATO DA REQUISIÇÃO `

```json
{
	"name": "Pão de Açúcar",
	"address": "Rua das Flores, 74",
	"state": "PR",
	"city": "Apucarana",
	"phone_number": "99742841",
	"cnpj": "71110987654321",
	"password": "123456"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /stores - FORMATO DA RESPOSTA - STATUS 201`

```json
{
	"id": 1,
	"name": "Pão de Açúcar",
	"address": "Rua das Flores, 74",
	"city": "Apucarana",
	"state": "PR",
	"phone_number": "99742841",
	"cnpj": "71110987654321"
}
```

### Login do supermercado

`POST /login_store - FORMATO DA REQUISIÇÃO `

```json
{
	"cnpj": "71110987654321",
	"password": "123456"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /login_store - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA3NDY0MiwianRpIjoiNWExNTFhNjQtNmYzOS00YjU2LTgzZWQtNjQxM2QxN2JlZjhmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MiwibmFtZSI6ImdhYnJpZWxhIiwiY2l0eSI6ImFwdWNhcmFuYSIsInN0YXRlIjoiUFIiLCJjb3VudHJ5IjoiQnJhc2lsIiwiZW1haWwiOiJnYWJyaWVsYXNAZW1haWwuY29tIn0sIm5iZiI6MTYzOTA3NDY0MiwiZXhwIjoxNjM5MDc1NTQyfQ.SU8PBco6gZaLVtsOViDo4werwJHi3GcAkxxsbIZt3rk"
}
```

### Buscar supermercados

A resposta do endpoint contém as informações da loja que estavam presentes no cadastro, além dos produtos que esta loja possui.

`GET /stores -  FORMATO DA REQUISIÇÃO `

Caso dê tudo certo, a resposta será assim:

`GET /stores - FORMATO DA RESPOSTA - STATUS 200`

```json
[
	{
		"id": 1,
		"name": "Pão de Açúcar",
		"address": "Rua das Flores, 74",
		"city": "Apucarana",
		"state": "PR",
		"phone_number": "12223344",
		"cnpj": "71110987654321",
		"products": []
	},
	{
		"id": 2,
		"name": "Líder",
		"address": "Travessa Senador Lemos",
		"city": "Belém",
		"state": "PA",
		"phone_number": "91991919191",
		"cnpj": "12345678912123",
		"products": [
			{
				"name": "Pão integral",
				"category": "Alimentos"
			},
			{
				"name": "Café",
				"category": "Alimentos"
			}
		]
	},
	{
		"id": 3,
		"name": "Assaí",
		"address": "Rua do lado da BR",
		"city": "Niterói",
		"state": "RJ",
		"phone_number": "12223344",
		"cnpj": "12345678901234",
		"products": []
	}
]
```


### Buscar supermercado específico (id)

`GET /stores/2 -  FORMATO DA REQUISIÇÃO `

Caso dê tudo certo, a resposta será assim:

`GET /stores/2 - FORMATO DA RESPOSTA - STATUS 200`

```
{
	"id": 9,
	"name": "Líder",
	"address": "Travessa Senador Lemos",
	"city": "Belém",
	"state": "PA",
	"phone_number": "91991919191",
	"cnpj": "12345678912123"
}
```


### Remover supermercado

Deve ser informado no cabeçalho da requisição o campo "Authorization", dessa forma:

> Authorization: Bearer {token}

`DELETE /stores/1 - FORMATO DA REQUISIÇÃO`

Caso dê tudo certo a resposta será assim (sem mensagem):

`DELETE /stores/1 - FORMATO DA RESPOSTA - 204`


### Buscar produtos

`GET /products -  FORMATO DA REQUISIÇÃO `

Caso dê tudo certo, a resposta será assim:

`GET /products - FORMATO DA RESPOSTA - STATUS 200`

```json
[
	{
	"id": 1,
	"name": "Sabonete Dove",
	"category": "Limpeza",
	"price": 1.99
	},
	{
	"id": 2,
	"name": "Doritos",
	"category": "Salgadinhos",
	"price": 4.99
	},
	{
	"id": 3,
	"name": "Coca-cola 2L",
	"category": "Bebidas",
	"price": 6.99
	}
]
```


### Buscar produto específico (id)

`GET /products/1 -  FORMATO DA REQUISIÇÃO `

Caso dê tudo certo, a resposta será assim:

`GET /products/1 - FORMATO DA RESPOSTA - STATUS 200`

```
{
	"id": 1,
	"name": "Sabonete Dove",
	"category": "Limpeza",
	"price": 1.99
}
```


### Criando produto
Esta rota precisa de permissão específica, tendo em mente que apenas um supermercado pode adicionar um produto. Deve ser informado no cabeçalho da requisição o campo "Authorization", dessa forma:

> Authorization: Bearer {token}

`POST /products - FORMATO DA REQUISIÇÃO `

```json
{
	"name": "Café Solúvel Três Corações 60g",
	"category": "Alimentos",
	"price": 4.99
}
```

Caso dê tudo certo, a resposta será assim:

`POST /products - FORMATO DA RESPOSTA - STATUS 201`

```json
{
	"id": 4,
	"name": "Café Solúvel Três Corações",
	"category": "Alimentos",
	"price": 4.99
}
```

### Atualizar produto (id)

Esta rota precisa de permissão específica, tendo em mente que apenas um supermercado pode adicionar um produto. Deve ser informado no cabeçalho da requisição o campo "Authorization", dessa forma:

> Authorization: Bearer {token}

`PATCH /products/1 -  FORMATO DA REQUISIÇÃO `

```json
{
	"price": 7.42
}
```

Caso dê tudo certo a resposta será assim:

`PATCH /products/1 - FORMATO DA RESPOSTA - 201`

```json
{
	"id": 1,
	"name": "Sabonete Dove",
	"category": "Limpeza",
	"price": 7.42
}
```

### Remover produto

Deve ser informado no cabeçalho da requisição o campo "Authorization", dessa forma:

> Authorization: Bearer {token}

`DELETE /products/1- FORMATO DA REQUISIÇÃO`

Caso dê tudo certo a resposta será assim (sem mensagem):

`DELETE /products/1 - FORMATO DA RESPOSTA - 204`


### Listar sugestões

As sugestões são mensagem enviadas pelos usuários, tendo como objetivo mapear produtos ou mercados faltantes na aplicação, bem como críticas/avaliações sobre o Market+ em si.

`GET /sugestions -  FORMATO DA REQUISIÇÃO `

Caso dê tudo certo, a resposta será assim:

`GET /sugestions - FORMATO DA RESPOSTA - STATUS 200`

```
[
	{
		"id": 1,
		"type": "Market+",
		"message": "Gostaria que o aplicativo funcionasse melhor no celular",
		"users_id": 4
	},
	{
		"id": 2,
		"type": "Supermercados",
		"message": "Olá, moro em Fortaleza e não encontrei o Supermercado Cometa na lista, por favor adicionem.",
		"users_id": 2
	}
]
```

### Publicar sugestão
Deve ser informado no cabeçalho da requisição o campo "Authorization", dessa forma:

> Authorization: Bearer {token}

`POST /sugestions - FORMATO DA REQUISIÇÃO `

```json
{
	"type": "Produtos",
	"message": "O refrigerante Kuat 2L não está no catálogo, favor adicionar."
}
```

Caso dê tudo certo, a resposta será assim:

`POST /sugestions - FORMATO DA RESPOSTA - STATUS 201`

```json
{
	"id": 4,
	"type": "Produtos",
	"message": "O refrigerante Kuat 2L não está no catálogo, favor adicionar.",
	"users_id": 1
}
```


### Adicionar aos favoritos (id do produto)
O usuário cadastrado pode escolher produtos que ele deseja manter em destaque no seu perfil. Deve ser informado no cabeçalho da requisição o campo "Authorization", dessa forma:

> Authorization: Bearer {token}

`POST /favorites/2 - FORMATO DA REQUISIÇÃO `

Caso dê tudo certo, a resposta será assim:

`POST /favorites/2 - FORMATO DA RESPOSTA - STATUS 204`

### Remover dos favoritos (id do produto)
Deve ser informado no cabeçalho da requisição o campo "Authorization", dessa forma:

> Authorization: Bearer {token}

`DELETE /favorites/2 - FORMATO DA REQUISIÇÃO `

Caso dê tudo certo, a resposta será assim:

`DELETE /favorites/2 - FORMATO DA RESPOSTA - STATUS 204`

