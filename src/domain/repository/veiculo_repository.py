from sqlalchemy.orm import joinedload

from src.domain.model.veiculo import Veiculo
from src.domain.dto.filtro_veiculo_dto import FiltroVeiculo

class VeiculoRepository:

    def __init__(self, session):
        self.session = session

    def salvar_veiculo(self, veiculo: Veiculo):
        self.session.add(veiculo)

        self.session.commit()

    def salvar_veiculos(self, veiculos: list):
        for veiculo in veiculos:
            self.salvar_veiculo(veiculo)

    def buscar_veiculos_by_filtro(self, filtro: FiltroVeiculo):
        query = self.session.query(Veiculo).options(
            joinedload(Veiculo.acessorios_fabrica),
            joinedload(Veiculo.acessorios_adicionais)
        )
        
        if filtro.marca:
            query = query.filter(Veiculo.marca.ilike(f"%{ filtro.marca }%"))
        if filtro.modelo:
            query = query.filter(Veiculo.modelo.ilike(f"%{ filtro.modelo }%"))
        if filtro.tipo_combustivel:
            query = query.filter(Veiculo.tipo_combustivel.ilike(f"%{ filtro.tipo_combustivel }%"))
        if filtro.ano_min:
            query = query.filter(Veiculo.ano_fabricacao >= filtro.ano_min)
            query = query.filter(Veiculo.ano_modelo >= filtro.ano_min)
        if filtro.ano_max:
            query = query.filter(Veiculo.ano_fabricacao <= filtro.ano_max)
            query = query.filter(Veiculo.ano_modelo <= filtro.ano_max)
        if filtro.preco_min:
            query = query.filter(Veiculo.preco >= filtro.preco_min)
        if filtro.preco_max:
            query = query.filter(Veiculo.preco <= filtro.preco_max)
        if filtro.cor:
            query = query.filter(Veiculo.cor.ilike(f"%{ filtro.cor }%"))
        
        return query.all()
