from enum import Enum


class DistanceUnit(Enum):
    KM = "Kilómetros"


class RaceEditionStatus(Enum):
    COMING_SOON = "Próximamente"
    OPEN = "Inscripciones abiertas"
    SOLD_OUT = "Inscripciones completas"
    IN_PROGRESS = "En progreso"
    FINISHED = "Finalizada"
