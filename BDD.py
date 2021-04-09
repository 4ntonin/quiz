import sqlite3


class BDD:
    def __init__(self, nom):
        self.conn = sqlite3.connect(f'{nom}.db')
        self.cur = self.conn.cursor()

    def requetesql(self, commande):
        self.cur.execute(commande)
        self.conn.commit()

    def get_tables(self):
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
        tables = [i[0] for i in self.cur.fetchall()]
        return tables
