from ..model.proveedor import proveedor_model


class proveedor_repository:

    def all_for_select(self):
        return [(r.PV_RUT,r.PV_NOMBRE)for r in proveedor_model.objects.all()]

    def all_for_select2(self):
        return [(r.PV_ID,r.PV_NOMBRE)for r in proveedor_model.objects.all()]