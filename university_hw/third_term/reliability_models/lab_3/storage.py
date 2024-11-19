import sqlite3


class DBStorage:
    def __init__(self):
        self.conn = sqlite3.connect('storage.db')
        self.cur = self.conn.cursor()

        self.cur.execute('CREATE TABLE IF NOT EXISTS data_db (t_i INTEGER, R_i INTEGER, d_i INTEGER, dr_i REAL)')

        self.conn.commit()

    def store(self, data):
        self.clear_storage()
        for line in data:
            self.cur.execute('INSERT INTO data_db (t_i, R_i, d_i, dr_i) VALUES (?, ?, ?, ?)',
                             (line[0], line[1], line[2], line[3],))
        self.conn.commit()

    def load(self):
        self.cur.execute('SELECT * FROM data_db')
        rows = self.cur.fetchall()

        load_data = []
        for row in rows:
            load_data.append(list(row))

        print(load_data)
        return load_data

    def clear_storage(self):
        self.cur.execute('DELETE FROM data_db')
        self.conn.commit()

    def __del__(self):
        self.conn.close()


class FileStorage:
    def __init__(self):
        ...

    def store(self, data):
        ...

    def load(self):
        ...
