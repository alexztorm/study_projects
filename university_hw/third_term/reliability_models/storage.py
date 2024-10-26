from scheme_unit import SchemeUnit


class DBStorage:
    def __init__(self):
        ...

    def store(self):
        ...

    def load(self):
        ...

    def clear_storage(self):
        ...


class FileStorage:
    def __init__(self):
        self.file_name = 'storage.txt'

    def store(self, unit_list: list[SchemeUnit]):
        with open(self.file_name, 'w') as save_file:
            save_file.write(f'{len(unit_list)} \n')
            for unit in unit_list:
                ...

    def load(self):
        ...

    def clear_storage(self):
        ...
