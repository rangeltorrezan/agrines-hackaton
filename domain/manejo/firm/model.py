# -*- coding: utf-8 -*-
from sqlalchemy import Column, String
from sqlalchemy.sql.schema import Sequence
from sqlalchemy.sql.sqltypes import Integer

from domain import Base

class Firm(Base):
    __tablename__ = 'FIRM'

    id = Column(Integer, Sequence('SEQFIRM'), primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
