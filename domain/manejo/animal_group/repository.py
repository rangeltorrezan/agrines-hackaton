from domain.abstract_repository import AbstractRepository
from domain.manejo.animal_group.model import AnimalGroup


class AnimalGroupRepository(AbstractRepository):
    __model__ = AnimalGroup

