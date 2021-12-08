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

class StoreAlreadyExistsError(Exception):
    message = {"error": "Loja já cadastrada!"}

class StoreInvalidKeys(Exception):
    allowed_keys = ["name", "adress", "store_img", "phone_number", "cnpj", "password"]
    message = {"error": f"As chaves permitidas são: {[key for key in allowed_keys]}"}
