from unittest.mock import MagicMock
from tests.commom_test import TestCommom, FiltroVeiculo, VeiculoDTO, VeiculoRepository

class TestConnection(TestCommom):

    def test_aberura_conexao(self, mock_server):

        assert mock_server is not None

    def test_resposta_repository(self, mock_db_session):
        
        repo = VeiculoRepository(mock_db_session)
        
        veiculo = self.gerar_veiculos(1)[0]

        repo.salvar_veiculo(veiculo)

        # Verifica se os comandos de persistência foram chamados:
        mock_db_session.add.assert_called_once_with(veiculo)
        mock_db_session.commit.assert_called_once()

        # Simula um retorno real para conseguirmos comparar a instância:
        mock_db_session.query().options().all.return_value = [
            VeiculoDTO(
                marca = veiculo.marca,
                modelo = veiculo.modelo,
                ano_fabricacao = veiculo.ano_fabricacao,
                ano_modelo = veiculo.ano_modelo,
                cilindrada = veiculo.cilindrada,
                motorizacao = veiculo.motorizacao,
                potencia = veiculo.potencia,
                transmissao = veiculo.transmissao,
                quilometragem = veiculo.quilometragem,
                tipo_combustivel = veiculo.tipo_combustivel,
                cor = veiculo.cor,
                direcao = veiculo.direcao,
                quantidade_portas = veiculo.quantidade_portas,
                blindado = veiculo.blindado,
                preco = veiculo.preco,
                acessorios_fabrica = veiculo.acessorios_fabrica,
                acessorios_adicionais = veiculo.acessorios_adicionais
            )
        ]
        
        veiculos = repo.buscar_veiculos_by_filtro(FiltroVeiculo())

        assert isinstance(veiculos[0], VeiculoDTO)

        self.comparar_atributos_veiculos(veiculo, veiculos[0])
