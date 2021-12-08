class ProductAlreadyExistsError(Exception):
    message = {"error": "Produto já cadastrado!"}


class EmailAlreadyExistsError(Exception):
    ...


class InvalidKeyError(Exception):
    ...

class InvalidTypeError(Exception):
    ...

class NotFoundError(Exception):
    message = {"error": "Nenhum produto encontrada"}

class NotAcessibleError(Exception):
    ...

class UniqueUserError(Exception):
    ...