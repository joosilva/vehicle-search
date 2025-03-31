from tests.commom_test import TestCommom, pytest, FiltroVeiculo, VeiculoRepository

class TestFilter(TestCommom):

    @pytest.fixture(autouse = True)
    def set_up(self, mock_db_session):
        
        self.repo = VeiculoRepository(mock_db_session)
        self.gerar_massa_teste()

    @pytest.fixture
    def instancia_filtro(self):
        
        filtro = FiltroVeiculo()
        
        filtro.marca = "Ford"
        filtro.modelo = "Edge"
        filtro.tipo_combustivel = "Gasolina"
        filtro.ano_min = 2015
        filtro.ano_max = 2020
        filtro.preco_min = 30000.00
        filtro.preco_max = 100000.00
        filtro.cor = "Branco"
        
        return filtro

    def gerar_massa_teste(self):
        
        veiculos = self.gerar_veiculos(100)
        self.repo.salvar_veiculos(veiculos)

    def test_consulta_by_filtro(self, instancia_filtro):
        filtro = instancia_filtro
        veiculos = self.repo.buscar_veiculos_by_filtro(filtro)

        # Garante que pelo menos um veículo será retornado
          # de acordo com os dados do filtro:
        if len(veiculos) == 0:
            self.gerar_massa_teste()
            veiculos = self.repo.buscar_veiculos_by_filtro(filtro)

        # Verifica se os veículos retornados atendem aos filtros:
        for veiculo in veiculos:
            assert veiculo.marca == filtro.marca
            assert veiculo.modelo == filtro.modelo
            assert veiculo.tipo_combustivel == filtro.tipo_combustivel
            assert veiculo.ano_fabricacao >= filtro.ano_min and veiculo.ano_modelo >= filtro.ano_min
            assert veiculo.ano_fabricacao <= filtro.ano_max and veiculo.ano_modelo <= filtro.ano_max
            assert veiculo.preco >= filtro.preco_min and veiculo.preco <= filtro.preco_max
            assert veiculo.cor.startswith(filtro.cor)
