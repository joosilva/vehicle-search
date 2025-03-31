from tests.commom_test import TestCommom, VeiculoDTO

quantidade_veiculos = 1

veiculos = []

class TestGenerator(TestCommom):

    def test_instancia_objeto(self):
        veiculos = self.gerar_veiculos(quantidade_veiculos)

        assert isinstance(veiculos[0], VeiculoDTO)

    def test_quatidade_veiculos(self):
        quantidade_veiculos = 10

        veiculos = self.gerar_veiculos(quantidade_veiculos)

        assert len(veiculos) == quantidade_veiculos

        quantidade_veiculos = 50

        veiculos = self.gerar_veiculos(quantidade_veiculos)

        assert len(veiculos) == quantidade_veiculos

        quantidade_veiculos = 100

        veiculos = self.gerar_veiculos(quantidade_veiculos)

        assert len(veiculos) == quantidade_veiculos

    def test_atributos_objeto(self):
        quantidade_veiculos = 1
        veiculo: VeiculoDTO = self.gerar_veiculos(quantidade_veiculos)[0]

        assert veiculo.marca is not None
        assert veiculo.modelo is not None
        assert veiculo.ano_fabricacao is not None
        assert veiculo.ano_modelo is not None
        assert veiculo.cilindrada is not None
        assert veiculo.motorizacao is not None
        assert veiculo.potencia is not None
        assert veiculo.transmissao is not None
        assert veiculo.quilometragem is not None
        assert veiculo.cor is not None
        assert veiculo.direcao is not None
        assert veiculo.quantidade_portas is not None
        assert veiculo.blindado is not None
        assert veiculo.preco is not None

        assert veiculo.acessorios_fabrica is not None
        assert len(veiculo.acessorios_fabrica) == 5
        assert veiculo.acessorios_adicionais is not None
        assert len(veiculo.acessorios_adicionais) == 3

    def test_regra_instanciacao(self):
            
        for veiculo in veiculos:
            if veiculo.marca in ["BYD", "Tesla"] or veiculo.motorizacao == "Elétrico":
                assert veiculo.tipo_combustivel is None
            else:
                assert veiculo.tipo_combustivel is not None

            assert veiculo.cilindrada >= 1.0 and veiculo.potencia <= 3.0
            assert veiculo.potencia >= 100 and veiculo.potencia <= 350
            assert veiculo.quilometragem >= 1000 and veiculo.quilometragem <= 200000
            assert veiculo.quantidade_portas == 2 or veiculo.quantidade_portas == 4
            assert veiculo.preco >= 15000 and veiculo.preco <= 200000
            assert len(veiculo.acessorios_fabrica) == 5
            assert len(veiculo.acessorios_adicionais) == 3
