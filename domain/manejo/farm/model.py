# -*- coding: utf-8 -*-
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Sequence, ForeignKey
from sqlalchemy.sql.sqltypes import Integer

from domain import Base
from domain.manejo.firm.model import Firm


class Farm(Base):
    __tablename__ = 'FARM'

    id = Column(Integer, Sequence('SEQFARM'), primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    note = Column(String(255), nullable=True)
    firm_id = Column(Integer, ForeignKey("FIRM.id"),nullable=False)
    firm = relationship(Firm)
