from ..model.equipo import equipo_model


class equipo_repository:

  def equipos_by_pais_comunidades(self,comunidades):
    return equipo_model.objects.filter(comunidades__in=comunidades).distinct()