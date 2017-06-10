from ..model.tipoc import tipoc_model



class tipoc_repository:
    def all_for_select(self):
        return [(r.TC_ID,r.TC_NOMBRE)for r in tipoc_model.objects.all()]