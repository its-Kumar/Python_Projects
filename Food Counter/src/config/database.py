import psycopg2

from src.config.enviroment import DBHOST, DB_NAME, DB_USER, DB_PASS


class Conexao(object):
    db = None

    def __init__(self):
        self.db = psycopg2.connect(host=DBHOST, database=DB_NAME, user=DB_USER, password=DB_PASS)

    def manipular(self, sql):
        try:
            cur = self.db.cursor()
            cur.execute(sql)
            cur.close()
            self.db.commit()

        except:
            return False

        return True

    def consultar(self, sql):
        data = None
        try:
            cur = self.db.cursor()
            cur.execute(sql)
            data = cur.fetchall()
        except:
            return None
        return data