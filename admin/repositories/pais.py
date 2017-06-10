from ..model.pais import pais_model



class pais_repository:

    def all_for_select(self):
        return [(p.PA_ID,p.PA_NOMBRE)for p in pais_model.objects.all() ]


