from ..model.rol import rol_model


class rol_repositoy:
    def all_for_select(self):
        return [(r.id,r.nombre)for r in rol_model.objects.all()]

    def ing_solar_id(self):
        ing=rol_model.objects.get(ing_solar=1)
        return ing
