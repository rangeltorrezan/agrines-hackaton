# coding=utf-8
""" init """
# -*- coding: utf-8 -*-
import os

"""
Pacote de testes da camada domain
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from domain import Base

_DATASTORE_URI = 'sqlite:///:memory:'
# _DATASTORE_URI = 'sqlite:///db.db'

def prepara_base_de_testes_domain():
    """Prepara massa de testes"""
    schema_filename = os.path.join(os.path.dirname(__file__), 'manejo', 'schema.sql')
    engine = create_engine(_DATASTORE_URI, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))
    Base.metadata.create_all(bind=engine)

    with engine.connect() as con:
        with open(schema_filename, 'rt') as file:
            schema = file.read()
            dbapi = con.engine.raw_connection()
            dbapi.executescript(schema)

    return db_session
