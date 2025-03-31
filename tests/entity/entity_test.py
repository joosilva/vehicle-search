from tests.commom_test import TestCommom

class TestEntity(TestCommom):

    def test_map_objeto(self):

        veiculo_dto = self.gerar_veiculos(1)[0]

        veiculo =  veiculo_dto.to_model()

        self.compara_entidades(veiculo, veiculo_dto)

        veiculo_dto = veiculo.to_dto()
        
        self.compara_entidades(veiculo, veiculo_dto)
