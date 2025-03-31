from src.domain.dto.filtro_veiculo_dto import FiltroVeiculo
from src.domain.server.veiculo_server import VeiculoServer
from src.domain.util.input_validate import InputValidator

from src.domain.exceptions.input_validator_exception import InputValidatorException

class ChatBot:

    def __init__(self):
        self.nome_usuario = ""

    def iniciar_chat(self):
        chat_ativo = True

        print(f"🤖(Bot - C2S): Olá! Sou o Bot, da C2S e estou aqui para te ajudar a "
                "encontrar o melhor veículo para atender às suas expectativas.")
        
        while not self.nome_usuario.strip():
            self.nome_usuario = input(f"🤖(Bot - C2S): Antes de iniciarmos, por favor me diga seu nome para que eu possa te identificar: "
                "\n(Este dado não será usado externamente)\n")

        print(f"🤖(Bot - C2S): Muito prazer, { self.nome_usuario }! "
                "Antes de prosseguirmos, aguarde alguns instantes enquanto gero os dados dos veículos...")
        
        server = VeiculoServer()
        server.gerar_dados_veiculos()

        print(f"🤖(Bot - C2S): Já terminei!")
        
        while chat_ativo:
            print(f"🤖(Bot - C2S): Vamos lá! Vou te ajudar a encontrar seu veículo!")
            print(f"🤖(Bot - C2S): Irei fazer algumas perguntas e caso não deseje filtrar um veículo "
                    f"por algum dos campos que eu perguntar, basta apertar a tecla 'ENTER'.")

            validate = InputValidator()
            msg_campo_invalido = f"🤖(Bot - C2S): Por favor, digite um valor válido ou pressione 'ENTER' para pular este campo."

            marca = validate.validar_input_str(f"🤖(Bot - C2S): Me conta, qual a marca que você está buscando?\n")
            modelo = validate.validar_input_str(f"🤖(Bot - C2S): Você já tem um modelo em mente? Se sim, qual?\n")
            tipo_combustivel = validate.validar_input_str(f"🤖(Bot - C2S): Você gostaria de um veículo com qual tipo de combustível?\n")
            
            while True:
                try:
                    ano_min = validate.validar_input_int(f"🤖(Bot - C2S): Posso te apresentar veículos a partir de que ano de fabricação?\n")
                    break
                except InputValidatorException:
                    print(msg_campo_invalido)

            while True:
                try:
                    ano_max = validate.validar_input_int(f"🤖(Bot - C2S): Você gostaria que eu lhe mostrasse modelos de veículos até que ano?\n")
                    break
                except InputValidatorException:
                    print(msg_campo_invalido)

            while True:
                try:
                    preco_min = validate.validar_input_float(f"🤖(Bot - C2S): Você já pensou no valor mínimo que quer investir (em R$)?\n")
                    break
                except InputValidatorException:
                    print(msg_campo_invalido)

            while True:
                try:
                    preco_max = validate.validar_input_float(f"🤖(Bot - C2S): Até quanto está disposto a investir em um veículo (em R$)?\n")
                    break
                except InputValidatorException:
                    print(msg_campo_invalido)

            cor = validate.validar_input_str(f"🤖(Bot - C2S): Existe uma cor específica que você deseja para seu veículo?\n")

            filtro = FiltroVeiculo (
                marca = marca,
                modelo = modelo,
                tipo_combustivel = tipo_combustivel,
                ano_min = ano_min,
                ano_max = ano_max,
                preco_min = preco_min,
                preco_max = preco_max,
                cor = cor
            )

            print(f"🤖(Bot - C2S): Ótimas escolhas, { self.nome_usuario }! Com base nesses dados, irei buscar os melhores veículos para você.")
            
            veiculos: list = server.buscar_veiculos(filtro)

            if len(veiculos) == 0:
                print(f"🤖(Bot - C2S): Poxa. Não encontrei nenhum veículo com essas especificações.")
            else:
                print("🤖(Bot - C2S): Aqui estão as informações dos veículos que encontrei para você:")

                for i, veiculo in enumerate(veiculos, start=1): 
                    print(f"\n______________________________________({ i })______________________________________\n")
                    
                    veiculo.print_dados_veiculo()

            chat_ativo = input(f"\n🤖(Bot - C2S): Deseja realizar uma nova busca?\n").upper().startswith(("S", "Y"))

        print(f"🤖(Bot - C2S): Espero tê-lo ajudado. Se precisar é só me chamar novamente. Até a próxima, { self.nome_usuario }!")
