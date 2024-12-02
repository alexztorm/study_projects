from app.asm2304.st04.Fullback import FullBack
from app.asm2304.st04.Goalkeeper import Goalkeeper
from app.asm2304.st04.Forward import Forward
from app.asm2304.st04.StorageStrategy import PickleStorage, SQLiteStorage

from flask import render_template


def player_role(position):
    if position == 'goalkeeper':
        return Goalkeeper()
    elif position == 'fullback':
        return FullBack()
    elif position == 'forward':
        return Forward()


class Team:
    def __init__(self):
        self.url = None
        self.path = "asm2304/st04/"
        self.items = dict()
        self.piq_storage = PickleStorage()
        self.sql_storage = SQLiteStorage()
        self.upload_items_db()

    def upload_items_db(self):
        data = self.sql_storage.get_all_items()
        for row in data:
            if row['position'] == 'goalkeeper':
                item = Goalkeeper()
                item.saves = row['saves']
            elif row['position'] == 'fullback':
                item = FullBack()
                item.counters = row['counters']
            else:
                item = Forward()
                item.goals = row['goals']
            item.name = row['name']
            item.number = row['number']
            self.items[row['id']] = item

    def index(self):
        return render_template(self.path + 'index.html', url=self.url)

    def set_url(self, url):
        self.url = url

    def choose_position(self):
        return render_template(self.path + 'chooseposition.html', url=self.url)

    def add_player_get(self, position):
        return render_template(self.path + 'addplayer.html', position=position, url=self.url)

    def add_player_post(self, position):
        item = player_role(position)
        item.read()
        new_id = self.sql_storage.add_player(item)
        self.items[new_id] = item
        return self.index()

    def edit_item_get(self, edit_id):
        return render_template(self.path + 'editgame.html', edit_id=id, player_edit=self.get_item(edit_id), url=self.url)

    def get_item(self, get_id):
        return self.items[get_id]

    def edit_item_post(self, edit_id):
        self.items[edit_id].read()
        self.sql_storage.add_player(self.items[edit_id])
        return self.index()

    def delete_item(self, delete_id):
        del self.items[delete_id]
        self.sql_storage.delete_player(delete_id)
        return self.index()

    def save(self):
        self.piq_storage.save_storage(self.items)
        return render_template(self.path + 'saved.html', url=self.url)

    def load(self):
        self.sql_storage.load(self.piq_storage.load_storage())
        self.items.clear()
        self.upload_items_db()
        return self.index()

    def show_players(self):
        return render_template(self.path + 'team.html', items=self.items, url=self.url)
