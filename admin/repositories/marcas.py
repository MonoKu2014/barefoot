
from ..model.marca import marca_model


class marcas_repositoy:

    def all_for_select(self):
        return [(r.id,r.nombre)for r in marca_model.objects.all()]
