
class InputValidatorException(Exception):
    pass

    def __init__(self, input: str, tipo_campo: str):
        super().__init__(f"Valor inválido! Não foi possível processar { input } para { tipo_campo }")
