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
                         'yt REAL, I REAL, file_name TEXT)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS data_chepin '
                         '(id INTEGER PRIMARY KEY AUTOINCREMENT, experiment_num INTEGER)')
        self.conn.commit()

    def store_holsted(self, data, exp_num, file_names):
        insert_query = ('INSERT INTO data_holsted (experiment_num, n1, n2, nb1, nb2, n, nb, Nt, V, Lt, Ec, D, yt, I, '
                        'file_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
        for i in range(len(data)):
            values = [exp_num] + list(data[i].values()) + [file_names[i]]
            self.cur.execute(insert_query, values)
        self.conn.commit()

    def store_chepin(self):
        ...

    def load(self):
        return self.load_holsted(), self.load_chepin()

    def load_holsted(self):
        self.cur.execute('SELECT * FROM data_holsted')
        rows = self.cur.fetchall()

        output = []
        for row in rows:
            output_line = [row[1]]
            new_dict = {}
            for i in range(len(self.holsted_keys)):
                new_dict[self.holsted_keys[i]] = row[i + 2]
            output_line.append(new_dict)
            output_line.append(row[15])
            output.append(output_line)

        return output

    def load_chepin(self):
        return []

    def clear_storage(self):
        self.cur.execute('DROP TABLE IF EXISTS data_holsted')
        self.cur.execute('DROP TABLE IF EXISTS data_chepin')
        self.conn.commit()

    def __del__(self):
        self.clear_storage()
        self.conn.close()
