from src.config.database import Database
from src.domain.dto.filtro_veiculo_dto import FiltroVeiculo
from src.domain.util.veiculo_data_generator import VeiculoGenerator
from src.domain.repository.veiculo_repository import VeiculoRepository

db = Database()

session = db.get_session()

class VeiculoServer:

    def gerar_dados_veiculos(self):
        veiculos_dto = VeiculoGenerator.gerar_veiculos(100)
        
        veiculos = [veiculo_dto.to_model() for veiculo_dto in veiculos_dto]
        
        # Bloco 'with' apenas para garantir 
          # melhor gerenciamento da seção aberta:
        with session() as s:
            veiculo_repository = VeiculoRepository(s)

            veiculo_repository.salvar_veiculos(veiculos)
    
    def buscar_veiculos(self, filtro: FiltroVeiculo):
        # Bloco 'with' apenas para garantir 
          # melhor gerenciamento da seção aberta:
        with session() as s:
            veiculo_repository = VeiculoRepository(s)

            veiculos = veiculo_repository.buscar_veiculos_by_filtro(filtro)

            return [veiculo.to_dto() for veiculo in veiculos]
