# -*- coding: utf-8 -*-
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Sequence, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Enum

from domain import Base
from domain.manejo.farm.model import Farm

situation = ('O', 'C')

class AnimalGroup(Base):
    __tablename__ = 'ANIMAL_GROUP'

    id = Column(Integer, Sequence('SEQANIMALGROUP'), primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    situation =  Column(Enum(*situation, name='SITUATION'), nullable=False, default='O')
    farm_id = Column(Integer, ForeignKey("FARM.id"),nullable=False)
    farm = relationship(Farm)
