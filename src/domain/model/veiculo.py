from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean, ARRAY
from sqlalchemy.orm import relationship

from src.config.database import Base

class Veiculo(Base):

    __tablename__ = "veiculos"
    
    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, index=True)
    modelo = Column(String)
    ano_fabricacao = Column(Integer)
    ano_modelo = Column(Integer)
    cilindrada = Column(Float)
    motorizacao = Column(String)
    potencia = Column(Integer)
    transmissao = Column(String)
    quilometragem = Column(Float)
    tipo_combustivel = Column(String, nullable=True)
    cor = Column(String)
    direcao = Column(String)
    quantidade_portas = Column(Integer)
    blindado = Column(Boolean)
    preco = Column(Float)

    acessorios_fabrica = relationship("AcessorioFabrica", back_populates="veiculo")
    acessorios_adicionais = relationship("AcessorioAdicional", back_populates="veiculo")


    def to_dto(self):
        from src.domain.dto.veiculo_dto import VeiculoDTO
        
        veiculo = VeiculoDTO (
            
            marca = self.marca,
            modelo = self.modelo,
            ano_fabricacao = self.ano_fabricacao,
            ano_modelo = self.ano_modelo,
            cilindrada = self.cilindrada,
            motorizacao = self.motorizacao,
            potencia = self.potencia,
            transmissao = self.transmissao,
            quilometragem = self.quilometragem,
            tipo_combustivel = self.tipo_combustivel,
            cor = self.cor,
            direcao = self.direcao,
            quantidade_portas = self.quantidade_portas,
            blindado = self.blindado,
            preco = self.preco,

            acessorios_fabrica = [acessorio.nome for acessorio in self.acessorios_fabrica],
        
            acessorios_adicionais = [acessorio.nome for acessorio in self.acessorios_adicionais]
            
        )

        return veiculo

class AcessorioFabrica(Base):
    __tablename__ = "acessorios_fabrica"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    veiculo_id = Column(Integer, ForeignKey('veiculos.id'))

    veiculo = relationship("Veiculo", back_populates="acessorios_fabrica")


class AcessorioAdicional(Base):
    __tablename__ = "acessorios_adicionais"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    veiculo_id = Column(Integer, ForeignKey('veiculos.id'))

    veiculo = relationship("Veiculo", back_populates="acessorios_adicionais")