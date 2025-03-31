from tests.commom_test import TestCommom, patch, MagicMock, FiltroVeiculo, VeiculoDTO, VeiculoServer

class TestChatBot(TestCommom):

    respostas = [
        "C2S",
        "Volks",
        "Tiguan",
        "Flex",
        "2015",
        "2025",
        "50000.00",
        "120000.00",
        "Azul",
        "Não"
    ]

    def test_chat_bot(self, bot):
        veiculo_mock = MagicMock(spec=VeiculoDTO)
        veiculo_mock.print_dados_veiculo = MagicMock()

        lista_veiculos = [veiculo_mock, veiculo_mock]

        with patch('builtins.input', side_effect=self.respostas), \
             patch('builtins.print') as mock_print, \
             patch.object(VeiculoServer, 'buscar_veiculos', return_value=lista_veiculos) as mock_buscar_veiculos:

            bot.iniciar_chat()

            filtro_esperado = FiltroVeiculo(
                marca = "Volks",
                modelo = "Tiguan",
                tipo_combustivel = "Flex",
                ano_min = 2015,
                ano_max = 2025,
                preco_min = 50000.00,
                preco_max = 120000.00,
                cor="Azul"
            )
            
            # Verifica se houve chamada à função buscar_veiculos
              # passando os filtros corretos de acordo com as respostas para o chatbot
                # e recupera o filtro passado:
            mock_buscar_veiculos.assert_called_once()
            filtro_chamado = mock_buscar_veiculos.call_args[0][0]

            assert filtro_chamado.marca == filtro_esperado.marca
            assert filtro_chamado.modelo == filtro_esperado.modelo
            assert filtro_chamado.tipo_combustivel == filtro_esperado.tipo_combustivel
            assert filtro_chamado.ano_min == filtro_esperado.ano_min
            assert filtro_chamado.ano_max == filtro_esperado.ano_max
            assert filtro_chamado.preco_min == filtro_esperado.preco_min
            assert filtro_chamado.preco_max == filtro_esperado.preco_max
            assert filtro_chamado.cor == filtro_esperado.cor

            assert lista_veiculos == mock_buscar_veiculos.return_value
