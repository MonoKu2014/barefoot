from ..model.comunidad import comunidad_model


class comunidades_repository:
    def get_comunidades_by_pais(self,id_pais):
        return list(comunidad_model.objects.filter(pais=id_pais))