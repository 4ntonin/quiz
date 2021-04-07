import sqlite3


class BDD:
    def __init__(self, nom):
        self.conn = sqlite3.connect(f'{nom}.db')
        self.cur = self.conn.cursor()

    def requetesql(self, commande):
        self.cur.execute(commande)
        self.conn.commit()
