from abc import ABCMeta, abstractmethod
import sqlite3

class DB(object, metaclass=ABCMeta):

    @abstractmethod
    def __getitem__(self, item):
        """
        :param item: string
        :return set
        """
        pass

    @abstractmethod
    def __setitem__(self, key, value):
        """
        :param key: string
        :param value: set
        """
        pass

    @abstractmethod
    def __contains__(self, item):
        """

        :param item: string
        :return: True or False
        """
        pass

class OnMemoryDB(DB):
    def __init__(self):
        self._db = dict()

    def __getitem__(self, item):
        return self._db[item]

    def __setitem__(self, key, value):
        self._db[key] = value

    def __contains__(self, item):
        return item in self._db


class SQLiteDB(DB):
    def __init__(self, conf):
        self._conn = sqlite3.connect(conf.DATABASE_PATH)
        c = self._conn.cursor()
        try:
            c.execute('create table if not exists twisets(id text, has_id text)')
            self._conn.commit()
        except Exception as e:
            print(e)

    def __getitem__(self, item):
        c = self._conn.cursor()
        c.execute('select has_id from twisets where id=="%s"' % item)
        data = c.fetchall()
        self._conn.commit()
        return set([d[0] for d in data])

    def __setitem__(self, key, value):
        c = self._conn.cursor()
        sql_values = ""
        for v in value:
            if sql_values != "":
                sql_values += ", "
            sql_values += '("%s", "%s")' % (key, v)

        c.execute('insert into twisets values %s' % sql_values)
        self._conn.commit()

    def __contains__(self, item):
        c = self._conn.cursor()
        c.execute('select has_id from twisets where id=="%s"' % item)
        data = c.fetchall()
        self._conn.commit()
        if len(data) == 0:
            return False
        return True
