
class FiltroVeiculo:

     def __init__(self, marca: str = None, modelo: str = None, tipo_combustivel: str = None, ano_min: int = None, 
            ano_max: int = None, preco_min: int = None, preco_max: int = None, cor: str = None):
        self.marca = marca
        self.modelo = modelo
        self.tipo_combustivel = tipo_combustivel
        self.ano_min = ano_min
        self.ano_max = ano_max
        self.preco_min = preco_min
        self.preco_max = preco_max
        self.cor = cor
