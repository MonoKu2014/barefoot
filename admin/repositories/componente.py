from ..model.componente import componente_model

class componente_repository:

    def all_for_select(self):
        return [(r.CO_ID,r.CO_NOMBRE)for r in componente_model.objects.all()]