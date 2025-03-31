import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest

from unittest.mock import patch, MagicMock

from src.client.chat_bot import ChatBot

from src.domain.dto.filtro_veiculo_dto import FiltroVeiculo
from src.domain.dto.veiculo_dto import VeiculoDTO

from src.domain.model.veiculo import Veiculo

from src.domain.repository.veiculo_repository import VeiculoRepository

from src.domain.server.veiculo_server import VeiculoServer

from src.domain.util.veiculo_data_generator import VeiculoGenerator

class TestCommom:

    @pytest.fixture
    def mock_server(self):
        return VeiculoServer()

    @pytest.fixture
    def mock_db_session(self):
        return MagicMock()
    
    @pytest.fixture
    def bot(self):
        return ChatBot()
    
    def gerar_veiculos(self, quantidade: int):
        return VeiculoGenerator.gerar_veiculos(quantidade)
    
    def compara_entidades(self, veiculo: Veiculo, veiculo_dto: VeiculoDTO):
        assert veiculo.marca == veiculo_dto.marca
        assert veiculo.modelo == veiculo_dto.modelo
        assert veiculo.ano_fabricacao == veiculo_dto.ano_fabricacao
        assert veiculo.ano_modelo == veiculo_dto.ano_modelo
        assert veiculo.cilindrada == veiculo_dto.cilindrada
        assert veiculo.motorizacao == veiculo_dto.motorizacao
        assert veiculo.potencia == veiculo_dto.potencia
        assert veiculo.transmissao == veiculo_dto.transmissao
        assert veiculo.quilometragem == veiculo_dto.quilometragem
        assert veiculo.tipo_combustivel == veiculo_dto.tipo_combustivel
        assert veiculo.cor == veiculo_dto.cor
        assert veiculo.direcao == veiculo_dto.direcao
        assert veiculo.quantidade_portas == veiculo_dto.quantidade_portas
        assert veiculo.blindado == veiculo_dto.blindado
        assert veiculo.preco == veiculo_dto.preco
        
        acessorios_fabrica_veiculo = [ acessorio.nome for acessorio in veiculo.acessorios_fabrica ]
        assert acessorios_fabrica_veiculo == veiculo_dto.acessorios_fabrica

        acessorios_adicionais_veiculo = [ acessorio.nome for acessorio in veiculo.acessorios_adicionais ]
        assert acessorios_adicionais_veiculo == veiculo_dto.acessorios_adicionais
    
    def comparar_atributos_veiculos(sef, veiculo1: VeiculoDTO, veiculo2: VeiculoDTO):
        
        assert veiculo1.marca == veiculo2.marca
        assert veiculo1.modelo == veiculo2.modelo
        assert veiculo1.ano_fabricacao == veiculo2.ano_fabricacao
        assert veiculo1.ano_modelo == veiculo2.ano_modelo
        assert veiculo1.cilindrada == veiculo2.cilindrada
        assert veiculo1.motorizacao == veiculo2.motorizacao
        assert veiculo1.potencia == veiculo2.potencia
        assert veiculo1.transmissao == veiculo2.transmissao
        assert veiculo1.quilometragem == veiculo2.quilometragem
        assert veiculo1.tipo_combustivel == veiculo2.tipo_combustivel
        assert veiculo1.cor == veiculo2.cor
        assert veiculo1.direcao == veiculo2.direcao
        assert veiculo1.quantidade_portas == veiculo2.quantidade_portas
        assert veiculo1.blindado == veiculo2.blindado
        assert veiculo1.acessorios_fabrica == veiculo2.acessorios_fabrica
        assert veiculo1.acessorios_adicionais == veiculo2.acessorios_adicionais
        assert veiculo1.preco == veiculo2.preco
