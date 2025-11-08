from datetime import datetime
from typing import Optional

class EstadisticasPartido:
    """
    clase que representa estadisticas de un jugador en un partido, tiene:
    metricas de rendimiento por fecha.
    """

    def __init__(
            self,
            date: datetime,
            minutes: int = 0,
            goals: int = 0,
            assists: int = 0,
            penalty_shoot_on_goal: int = 0,
            penalty_shoot: int = 0,
            total_shoot: int = 0,
            shoot_on_target: int = 0,
            yellow_cards: int = 0,
            red_cards: int = 0,
            touches: int = 0,
            dribbles: int = 0,
            tackles: int = 0,
            blocks: int = 0,
            xg: float = 0.0,
            npxg: float = 0.0,
            xag: float = 0.0,
            shot_creating_actions: int = 0,
            goal_creating_actions: int = 0,
            passes_completed: int = 0,
            passes_attempted: int = 0,
            pass_completion_percent: Optional[float] = None,
            progressive_passes: int = 0,
            carries: int = 0,
            progressive_carries: int = 0,
            dribble_attempts: int = 0,
            successful_dribbles: int = 0
    ):
        self._date = date
        self._minutes = minutes
        self._goals = goals
        self._assists = assists
        self._penalty_shoot_on_goal = penalty_shoot_on_goal
        self._penalty_shoot = penalty_shoot
        self._total_shoot = total_shoot
        self._shoot_on_target = shoot_on_target
        self._yellow_cards = yellow_cards
        self._red_cards = red_cards
        self._touches = touches
        self._dribbles = dribbles
        self._tackles = tackles
        self._blocks = blocks
        self._xg = xg
        self._npxg = npxg
        self._xag = xag
        self._shot_creating_actions = shot_creating_actions
        self._goal_creating_actions = goal_creating_actions
        self._passes_completed = passes_completed
        self._passes_attempted = passes_attempted
        self._pass_completion_percent = pass_completion_percent
        self._progressive_passes = progressive_passes
        self._carries = carries
        self._progressive_carries = progressive_carries
        self._dribble_attempts = dribble_attempts
        self._successful_dribbles = successful_dribbles

    #getters setters
    @property
    def date(self) -> datetime:
        return self._date

    @date.setter
    def date(self, value: datetime):
        self._date = value

    @property
    def minutes(self) -> int:
        return self._minutes

    @minutes.setter
    def minutes(self, value: int):
        self._minutes = value

    @property
    def goals(self) -> int:
        return self._goals

    @goals.setter
    def goals(self, value: int):
        self._goals = value

    @property
    def assists(self) -> int:
        return self._assists

    @assists.setter
    def assists(self, value: int):
        self._assists = value

    @property
    def xg(self) -> float:
        return self._xg

    @xg.setter
    def xg(self, value: float):
        self._xg = value

    @property
    def npxg(self) -> float:
        return self._npxg

    @npxg.setter
    def npxg(self, value: float):
        self._npxg = value

    @property
    def xag(self) -> float:
        return self._xag

    @xag.setter
    def xag(self, value: float):
        self._xag = value

    @property
    def passes_completed(self) -> int:
        return self._passes_completed

    @passes_completed.setter
    def passes_completed(self, value: int):
        self._passes_completed = value

    @property
    def passes_attempted(self) -> int:
        return self._passes_attempted

    @passes_attempted.setter
    def passes_attempted(self, value: int):
        self._passes_attempted = value

    @property
    def pass_completion_percent(self) -> Optional[float]:
        return self._pass_completion_percent

    @pass_completion_percent.setter
    def pass_completion_percent(self, value: Optional[float]):
        self._pass_completion_percent = value

    @property
    def yellow_cards(self) -> int:
        return self._yellow_cards

    @yellow_cards.setter
    def yellow_cards(self, value: int):
        self._yellow_cards = value

    @property
    def red_cards(self) -> int:
        return self._red_cards

    @red_cards.setter
    def red_cards(self, value: int):
        self._red_cards = value
