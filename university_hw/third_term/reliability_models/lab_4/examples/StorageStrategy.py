import pickle
import sqlite3


class PickleStorage:
    @staticmethod
    def load_storage():
        with open('data/asm2304/st04/team.data', 'rb') as f:
            return pickle.load(f)

    @staticmethod
    def save_storage(data):
        with open('data/asm2304/st04/team.data', 'wb') as f:
            pickle.dump(data, f)


class SQLiteStorage:
    def __init__(self):
        self.path = "data/asm2304/st04/team.db"

        db, db_cursor = self.open_connection()

        db.execute("""
                create table if not exists team (
                    id integer primary key autoincrement,
                    name text,
                    number integer,
                    position text,
                    saves integer,
                    counters integer,
                    goals integer
                    )""")

        db.close()

    def open_connection(self):
        db = sqlite3.connect(self.path, detect_types=sqlite3.PARSE_DECLTYPES)
        db.row_factory = sqlite3.Row
        db_cursor = db.cursor()
        return db, db_cursor

    def get_all_items(self):
        db, db_cursor = self.open_connection()
        db_cursor.execute('select * from team')
        items = db_cursor.fetchall()
        db.close()
        return items

    def add_player(self, item):
        db, db_cursor = self.open_connection()
        if item.position == 'goalkeeper':
            db_cursor.execute(
                "INSERT INTO team (name,number,position,saves) VALUES(?,?,?,?) RETURNING id",
                (item.name, item.number, item.position, item.saves))
        elif item.position == 'fullback':
            db_cursor.execute(
                "INSERT INTO team (name,number,position,counters) VALUES(?,?,?,?) RETURNING id",
                (item.name, item.number, item.position, item.counters))
        else:
            db_cursor.execute(
                "INSERT INTO team (name,number,position,goals) VALUES(?,?,?,?) RETURNING id",
                (item.name, item.number, item.position, item.goals))
        new_id = db_cursor.fetchone()['id']
        db.commit()
        db.close()
        return new_id

    def delete_player(self, delete_id):
        db, db_cursor = self.open_connection()
        db_cursor.execute("DELETE FROM team where id=?", (delete_id,))
        db_cursor.execute("delete from sqlite_sequence where name='team'")
        db.commit()
        db.close()

    def delete_all_items(self):
        db, db_cursor = self.open_connection()
        db_cursor.execute('DELETE FROM team')
        db_cursor.execute("delete from sqlite_sequence where name='team'")
        db.commit()
        db.close()

    def load(self, items):
        self.delete_all_items()
        for item in items.values():
            self.add_player(item)
