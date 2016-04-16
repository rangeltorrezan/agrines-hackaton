from domain.abstract_repository import AbstractRepository
from domain.manejo.farm.model import Farm


class FarmRepository(AbstractRepository):
    __model__ = Farm

