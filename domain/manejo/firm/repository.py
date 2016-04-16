from domain.abstract_repository import AbstractRepository
from domain.manejo.firm.model import Firm


class FirmRepository(AbstractRepository):
    __model__ = Firm

