from scheme_unit import SchemeUnit
import sqlite3


class DBStorage:
    def __init__(self):
        self.conn = sqlite3.connect('storage.db')
        self.cur = self.conn.cursor()
        self.setup_tables()

    def setup_tables(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS units (id INTEGER PRIMARY KEY AUTOINCREMENT, type INTEGER)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS params (unit_id INTEGER, block_num INTEGER,'
                         'distribution TEXT, param1 REAL, param2 REAL)')
        self.conn.commit()

    def store(self, unit_list: list[SchemeUnit]):
        self.clear_storage()

        for i in range(len(unit_list)):
            self.cur.execute('INSERT INTO units (type) VALUES (?)', (unit_list[i].type,))
            for j in range(unit_list[i].number_of_blocks):
                params_list = []
                for key in unit_list[i].distribution[j].params.keys():
                    params_list.append(unit_list[i].distribution[j].params[key])

                if len(params_list) == 1:
                    self.cur.execute('INSERT INTO params (unit_id, block_num, distribution, param1) '
                                     'VALUES (?, ?, ?, ?)',
                                     (i + 1, j, unit_list[i].distribution[j].get_type(), params_list[0],))
                else:
                    self.cur.execute('INSERT INTO params (unit_id, block_num, distribution, param1, param2) '
                                     'VALUES (?, ?, ?, ?, ?)',
                                     (i + 1, j, unit_list[i].distribution[j].get_type(),
                                      params_list[0], params_list[1]))

        self.conn.commit()

    def load(self) -> list[SchemeUnit]:
        self.cur.execute('SELECT * FROM units')
        rows = self.cur.fetchall()
        ids, types = [x[0] for x in rows], [x[1] for x in rows]

        self.cur.execute('SELECT * FROM params')
        rows = self.cur.fetchall()

        load_data = []

        for i in range(len(ids)):
            new_unit = SchemeUnit(types[i])
            for row in rows:
                if row[0] > ids[i]:
                    break
                elif row[0] == ids[i]:
                    new_unit.distribution[row[1]].change_distribution_type(row[2])

                    if row[4] is not None:
                        params = [float(row[3]), float(row[4])]
                        new_unit.distribution[row[1]].change_params(params)
                    else:
                        params = [float(row[3])]
                        new_unit.distribution[row[1]].change_params(params)
            load_data.append(new_unit)

        return load_data

    def clear_storage(self):
        self.cur.execute('DROP TABLE IF EXISTS units')
        self.cur.execute('DROP TABLE IF EXISTS params')
        self.conn.commit()
        self.setup_tables()

    def __del__(self):
        self.conn.close()


class FileStorage:
    def __init__(self):
        self.file_name = 'storage.txt'

    def store(self, unit_list: list[SchemeUnit]):
        with open(self.file_name, 'w') as save_file:
            save_file.write(f'{len(unit_list)}\n')
            for unit in unit_list:
                save_file.write(f'{unit.type}\n')

                for i in range(unit.number_of_blocks):
                    save_file.write(f'{unit.distribution[i].get_type()}')
                    for key in unit.distribution[i].params.keys():
                        save_file.write(f';{unit.distribution[i].params[key]}')
                    save_file.write('\n')

    def load(self) -> list[SchemeUnit]:
        load_data = []

        with open(self.file_name, 'r') as load_file:
            data = load_file.read().split('\n')
            line_id = 1

            for i in range(int(data[0])):
                new_unit = SchemeUnit(int(data[line_id]))
                for j in range(new_unit.number_of_blocks):
                    block_line = data[line_id + j + 1].split(';')
                    new_unit.distribution[j].change_distribution_type(block_line[0])
                    params = [float(x) for x in block_line[1:]]
                    new_unit.distribution[j].change_params(params)
                load_data.append(new_unit)

                line_id += new_unit.number_of_blocks + 1

        return load_data
