# -*- coding: utf-8 -*-
"""Classe abstrata para CRUD padrão"""

class AbstractRepository(object):
    """ CRUD padrão para ser herdado pelas classes."""
    __model__ = None

    def _preprocess_params(self, kwargs):
        """Retorna um dicionário pré-processado de parâmetros. Usado por padrão
        antes de criar uma nova instância ou atualizar uma instância existente.
        :param kwargs: um dicionario de parametros.
        """
        kwargs.pop('csrf_token', None)
        return kwargs

    def save(self, datastore, model):
        """Persiste o objeto no banco de dados e o retorna.
        :param model: objeto a ser persistido.
        """
        datastore.add(model)
        datastore.flush()
        return model

    def save_without_flush(self, datastore, model):
        datastore.add(model)
        return model

    def flush(self, datastore):
        datastore.flush()

    def all(self, datastore):
        """Retorna uma lista de objetos.
        """
        return datastore.query(self.__model__).all()

    def get(self, datastore, id):
        """Retorna o objeto identificado pelo id.
        Retona 'None' se o objeto não existir.
        :param id: id do objeto.
        """
        return datastore.query(self.__model__).get(id)

    def get_all(self, datastore, *ids):
        """Retorna uma lista de objetos correspondentes aos ids.
        :param *ids: ids dos objetos.
        """
        return datastore.query(self.__model__).filter(self.__model__.id.in_(ids)).all()

    def find(self, datastore, kwargs):
        """Retorna uma lista de objetos filtrados pelos parametros.
        :param **kwargs: filtros
        """
        query = self.assembly_query(datastore, kwargs)
        return query.all()

    def first(self, datastore, **kwargs):
        """Retorna o primeiro objeto encontrado do modelo do serviço filtrado pelo
        os argumentos de palavra chave especificada.
        :param **kwargs: filtros
        """
        return datastore.query(self.__model__).filter_by(**kwargs).first()

    def new(self, **kwargs):
        """Retorna uma nova instancia, nao salvos de classe do modelo do serviço.
        :param **kwargs: instance parameters
        """
        return self.__model__(**self._preprocess_params(kwargs))

    def create(self, datastore, **kwargs):
        """Retorna uma nova instancia persistida no banco.
        :param **kwargs: parametros da nova instancia.
        """
        return self.save(datastore, (self.new(**kwargs)))

    def update(self, datastore, model, **kwargs):
        """Retorna uma instancia atualizada do modelo de classe do servico.
        :param model: instancia a ser atualizada.
        :param **kwargs: novos parametros.
        """
        for k, v in self._preprocess_params(kwargs).items():
            setattr(model, k, v)
        self.save(datastore, model)
        return model

    def delete(self, datastore, model):
        """Apaga imediatamente uma instância especificada.
        :param model: objeto.
        """
        datastore.delete(model)
        datastore.flush()
        return model


    def assembly_query(self, datastore, kwargs):

        query =  datastore.query(self.__model__)

        if 'fields' in kwargs:
            attr = []
            for field in kwargs['fields']:
                attr.append(getattr(self.__model__, field))

            query = datastore.query(*(attr))


        if 'filter' in kwargs:
            query = query.filter_by(**kwargs['filter'])


        if 'between' in kwargs:
            range = []
            for field in kwargs['between']:
                query_param = getattr(self.__model__, field).between(*kwargs['between'][field])
                range.append(query_param)

            query = query.filter(*range)


        if 'order' in kwargs:
            order = []
            for field in kwargs['order']:
                order_param = getattr(self.__model__, field[0])
                if len(field) >=2 and 'asc' in field[1]:
                    order_param.asc()
                else:
                    order_param.desc()

                order.append(order_param)

            query = query.order_by(*order)

        if 'limit' in kwargs:
            query = query.limit(kwargs['limit'])


        if 'page' in kwargs:
            offset = (int(kwargs['page']) - 1) * int(kwargs['limit'])
            query = query.offset(offset)

        return query
