class ProductAlreadyExistsError(Exception):
    message = {"alerta": "Produto já cadastrado!"}


class EmailAlreadyExistsError(Exception):
    ...


class InvalidKeyError(Exception):
    ...


class InvalidTypeError(Exception):
    ...


class NotFoundError(Exception):
    message = {"alerta": "Nenhum produto encontrada"}


class NotAcessibleError(Exception):
    ...


class StoreAlreadyExistsError(Exception):
    message = {"alerta": "Loja já cadastrada!"}


class StoreInvalidKeys(Exception):
    allowed_keys = ["name", "adress", "store_img", "phone_number", "cnpj", "password"]
    message = {"alerta": f"As chaves permitidas são: {[key for key in allowed_keys]}"}


class UniqueUserError(Exception):
    ...
