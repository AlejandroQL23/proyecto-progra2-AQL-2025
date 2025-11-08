from Premier_League.src.clases.jugador import Jugador
from typing import List, Optional

class Equipo:
    """
    clase que representa un equipo, tiene:
    jugadores que pertenecen al equipo
    """

    def __init__(
            self,
            name: str,
            liga: str = "Premier League",
            jugadores: Optional[List[Jugador]] = None
    ):
        self._name = name
        self._liga = liga
        self._jugadores = jugadores if jugadores else []

    # Getters y Setters

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.strip()

    @property
    def liga(self) -> str:
        return self._liga

    @liga.setter
    def liga(self, value: str):
        self._liga = value.strip()

    @property
    def jugadores(self) -> List[Jugador]:
        return self._jugadores

    def total_goles_equipo(self) -> int:
        #total de goles del equipo
        return sum(jugador.total_goles() for jugador in self._jugadores)

    def total_asistencias_equipo(self) -> int:
        #total de asistencias del equipo
        return sum(jugador.total_asistencias() for jugador in self._jugadores)

