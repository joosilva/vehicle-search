
class VeiculoDTO:

    def __init__(self, marca: str, modelo: str, ano_fabricacao: int, ano_modelo: int, cilindrada: float, motorizacao: str,
            potencia: int, transmissao: str, quilometragem: int, cor: str, direcao: str, quantidade_portas: int, blindado: bool, 
            preco: float, tipo_combustivel: str = None, acessorios_fabrica: list = None, acessorios_adicionais: list = None):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.ano_modelo = ano_modelo
        self.cilindrada = cilindrada
        self.motorizacao = motorizacao
        self.potencia = potencia
        self.transmissao = transmissao
        self.quilometragem = quilometragem
        self.tipo_combustivel = tipo_combustivel
        self.cor = cor
        self.direcao = direcao
        self.quantidade_portas = quantidade_portas
        self.blindado = blindado
        self.acessorios_fabrica = acessorios_fabrica if acessorios_fabrica is not None else []
        self.acessorios_adicionais = acessorios_adicionais if acessorios_adicionais is not None else []
        self.preco = preco

    def print_dados_veiculo(self):
        print(f"{ self.marca } { self.modelo } ({ self.ano_fabricacao }/{ self.ano_modelo })\n")

        print(f"Motor: { round(self.cilindrada, 1) } - { self.motorizacao } com { self.potencia }cv de potência.")
        print(f"Combustível: { self.tipo_combustivel if self.tipo_combustivel is not None else '-' }.")
        print(f"Transmissão: { self.transmissao }.")

        print(f"\nInformações Adicionais:")
        print(f"\tQuilometragem: { round(self.quilometragem, 1) }km.")
        print(f"\tCor: { self.cor }.")
        print(f"\tDireção: { self.direcao }.")
        print(f"\tQuantidade de Portas: { self.quantidade_portas }.")
        print(f"\tVeículo blindado? { "Sim" if self.blindado else "Não" }.")

        print(f"\nAcessórios de Fábrica:")
        for acessorio in sorted(self.acessorios_fabrica):
            print(f"\t- { acessorio }")

        print(f"\nAcessórios Adicionais:")
        for acessorio in sorted(self.acessorios_adicionais):
            print(f"\t- { acessorio }")

        print(f"\nPreço: R${ round(self.preco, 2) }")

    def to_model(self):
        from src.domain.model.veiculo import Veiculo, AcessorioFabrica, AcessorioAdicional

        veiculo = Veiculo()

        veiculo.marca = self.marca
        veiculo.modelo = self.modelo
        veiculo.ano_fabricacao = self.ano_fabricacao
        veiculo.ano_modelo = self.ano_modelo
        veiculo.cilindrada = self.cilindrada
        veiculo.motorizacao = self.motorizacao
        veiculo.potencia = self.potencia
        veiculo.transmissao = self.transmissao
        veiculo.quilometragem = self.quilometragem
        veiculo.tipo_combustivel = self.tipo_combustivel
        veiculo.cor = self.cor
        veiculo.direcao = self.direcao
        veiculo.quantidade_portas = self.quantidade_portas
        veiculo.blindado = self.blindado
        veiculo.preco = self.preco

        veiculo.acessorios_fabrica = [AcessorioFabrica(nome=acessorio) for acessorio in self.acessorios_fabrica]
        veiculo.acessorios_adicionais = [AcessorioAdicional(nome=acessorio) for acessorio in self.acessorios_adicionais]

        return veiculo
