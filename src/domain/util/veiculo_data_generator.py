import random
import datetime

from faker import Faker

from src.domain.dto.veiculo_dto import VeiculoDTO

class VeiculoGenerator:

    fake = Faker()

    marcas_modelos = {
        "BYD": ["Dolphin", "Han", "King", "Seal", "Shark", "Song", "Tan", "Yuan"],
        "Chevrolet": ["Equinox", "Ônix", "S-10", "Tracker"],
        "Fiat": ["Argo", "Cronos", "Fastback", "Mobi", "Pulse", "Strada", "Toro", "Titano"],
        "Ford": ["Edge", "F-150", "Fiesta", "Ka", "Mustang", "Ranger"],
        "Honda": ["Civic", "CR-V", "Fit", "HR-V", "WR-V"],
        "Mitsubishi": ["Eclipse", "L200", "Outlander", "Pajero"],
        "Tesla": ["Cybertruck", "Model S", "Model X", "Model Y"],
        "Toyota": ["Corolla", "Corolla Cross", "Hilux", "RAV4", "SW4", "Yaris"],
        "Volkswagen": ["Fox", "Gol", "Golf", "Jetta", "Nivus", "T-Cross", "Taos", "Tiguan", "Virtus"]
    }

    motorizacoes = ["Combustão", "Elétrico", "Híbrido"]

    tipos_combustivel = ["Álcool", "Flex", "Gasolina"]

    cores = ["Amarelo", "Azul", "Branco", "Cinza", "Laranja", "Prata", "Preto", "Verde", "Vermelho"]
    tipos_cor = ["Metálico", "Personalizado", "Sólido"]

    tipos_direcao = ["Elétrica", "Hidráulica", "Mecânica"]

    acessorios = ["Acionamento do motor à distância", "Ajuste elétrico dos bancos dianteiros",
        "Android Auto/Apple CarPlay", "Aquecimento dos bancos", "Ar-Condicionado", "Assistente de direção",
        "Assistente de partida", "Assistente de permanência em faixa", "Câmera 360º", "Câmera de ré",
        "Central multimídia", "Controle de cruzeiro", "Chave presencial", "Faróis de milha",
        "Fechamento elétrico do porta-malas", "Painel soft touch", "Park Assist", "Piloto automático adaptativo",
        "Rebatimento automático dos bancos traseiros", "Rebatimento elétrico dos retrovisores",
        "Sensor de colisão", "Sensor de estacionamento", "Sensor de ponto cego", "Teto solar panorâmico",
        "Travas elétricas", "Vidros elétricos"]

    @staticmethod
    def gerar_veiculos(quantidade: int):
        
        veiculos = []

        for _ in range(quantidade):
            marca = random.choice(list(VeiculoGenerator.marcas_modelos.keys()))
            modelo = random.choice(VeiculoGenerator.marcas_modelos[marca])

            ano_fabricacao = VeiculoGenerator.fake.random_int(min=2010, max=datetime.date.today().year)
            
            motorizacao = random.choice(VeiculoGenerator.motorizacoes)
            
            acessorios_fabrica = VeiculoGenerator.fake.random_elements(elements=VeiculoGenerator.acessorios, length=5, unique=True)
            
            acessorios_restantes = list(set(VeiculoGenerator.acessorios) - set(acessorios_fabrica))
            
            acessorios_adicionais = VeiculoGenerator.fake.random_elements(elements=acessorios_restantes, length=3, unique=True)

            veiculo = VeiculoDTO(
                marca = marca,
                modelo = modelo,
                ano_fabricacao = ano_fabricacao,
                ano_modelo = ano_fabricacao + 1,
                cilindrada = round(VeiculoGenerator.fake.pyfloat(min_value=1.0, max_value=3.0, right_digits=1), 1),
                motorizacao = motorizacao,
                potencia = VeiculoGenerator.fake.random_int(min=100, max=350),
                transmissao = random.choice(["Automático", "Manual"]),
                quilometragem = VeiculoGenerator.fake.pyfloat(min_value=1000, max_value=200000, right_digits=2),
                
                tipo_combustivel = (
                    None if marca in ["BYD", "Tesla"] or motorizacao == "Elétrico" 
                    else random.choice(VeiculoGenerator.tipos_combustivel)
                ),
                
                cor = f"{random.choice(VeiculoGenerator.cores)} {random.choice(VeiculoGenerator.tipos_cor)}",
                direcao = random.choice(VeiculoGenerator.tipos_direcao),
                quantidade_portas = random.choice([2, 4]),
                blindado = VeiculoGenerator.fake.boolean(),
                acessorios_fabrica = acessorios_fabrica,
                acessorios_adicionais = acessorios_adicionais,
                preco = round(VeiculoGenerator.fake.pyfloat(min_value=15000, max_value=200000, right_digits=2), 2),
            )

            veiculos.append(veiculo)

        return veiculos

