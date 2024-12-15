import sqlite3


class DBStorage:
    def __init__(self):
        self.conn = sqlite3.connect('storage.db')
        self.cur = self.conn.cursor()

        self.setup_tables()

        self.holsted_keys = ['n1', 'n2', 'N1', 'N2', 'n', 'N', 'Nt', 'V', 'Lt', 'Ec', 'D', 'yt', 'I']
        self.chepin_keys = []

    def setup_tables(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS data_holsted '
                         '(id INTEGER PRIMARY KEY AUTOINCREMENT, experiment_num INTEGER, n1 INTEGER, n2 INTEGER, '
                         'nb1 INTEGER, nb2 INTEGER, n INTEGER, nb INTEGER, Nt REAL, V REAL, Lt REAL, Ec REAL, D REAL, '
                         'yt REAL, I REAL)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS data_chepin '
                         '(id INTEGER PRIMARY KEY AUTOINCREMENT, experiment_num INTEGER)')
        self.conn.commit()

    def store_holsted(self, data, exp_num):
        insert_query = ('INSERT INTO data_holsted (experiment_num, n1, n2, nb1, nb2, n, nb, Nt, V, Lt, Ec, D, yt, I) '
                        'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
        for line in data:
            values = [exp_num] + list(line.values())
            self.cur.execute(insert_query, values)
        self.conn.commit()

    def store_chepin(self):
        ...

    def load(self):
        ...

    def load_holsted(self):
        self.cur.execute('SELECT * FROM units')
        rows = self.cur.fetchall()

        for row in rows:
            ...

    def load_chepin(self):
        ...

    def clear_storage(self):
        self.cur.execute('DROP TABLE IF EXISTS data_holsted')
        self.cur.execute('DROP TABLE IF EXISTS data_chepin')
        self.conn.commit()

    def __del__(self):
        self.clear_storage()
        self.conn.close()
