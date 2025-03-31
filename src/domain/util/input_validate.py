
from src.domain.exceptions.input_validator_exception import InputValidatorException


class InputValidator:

    def validar_input_str(self, prompt):
       
       while True:
            resposta = input(prompt).strip()
            if resposta == "":
                return None 
            
            return resposta

    def validar_input_int(self, prompt):
        
        while True:
            resposta = input(prompt).strip()
            if resposta == "":
                return None
            
            try:
                valor = int(resposta)
                return valor
            except ValueError:
                raise InputValidatorException(resposta, "int")

    def validar_input_float(self, prompt):
        
        while True:
            resposta = input(prompt).strip()
            if resposta == "":
                return None
            
            try:
                valor = float(resposta)
                return valor
            except ValueError:
                raise InputValidatorException(resposta, "float")
