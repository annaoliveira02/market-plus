class ProductAlreadyExistsError(Exception):
    message = {"error": "Produto já cadastrado!"}


class EmailAlreadyExistsError(Exception):
    ...


class InvalidKeyError(Exception):
    ...


class NotFoundError(Exception):
    message = {"error": "Nenhum produto encontrada"}

class NotAcessibleError(Exception):
    ...