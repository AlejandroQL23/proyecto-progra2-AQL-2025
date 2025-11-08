from Premier_League.src.clases.estadisticasPartido import EstadisticasPartido
from typing import List, Optional

class Jugador:
    """
    clase que representa a un jugador, tiene:
    infor personal y lista de estadisticas por partido.
    """

    def __init__(
            self,
            name: str,
            team: str,
            number: int,
            nation: str,
            position: str,
            age: float,
            estadisticas: Optional[List[EstadisticasPartido]] = None
    ):
        self._name = name
        self._team = team
        self._number = number
        self._nation = nation
        self._position = position
        self._age = age
        self._estadisticas = estadisticas if estadisticas else []

    #getters setters
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.strip()

    @property
    def team(self) -> str:
        return self._team

    @team.setter
    def team(self, value: str):
        self._team = value.strip()

    @property
    def number(self) -> int:
        return self._number

    # raise se usa para "lanzar errores" y detener ejec
    @number.setter
    def number(self, value: int):
        if value < 0 or value > 99:
            raise ValueError("El número debe estar entre 0 y 99")
        self._number = value

    @property
    def nation(self) -> str:
        return self._nation

    @nation.setter
    def nation(self, value: str):
        self._nation = value.strip()

    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, value: str):
        self._position = value.strip()

    @property
    def age(self) -> float:
        return self._age

    @age.setter
    def age(self, value: float):
        self._age = value

    @property
    def estadisticas(self) -> List[EstadisticasPartido]:
        return self._estadisticas

    def __str__(self):
        return f"{self.name} - {self.team} (#{self.number}) - {self.position}"