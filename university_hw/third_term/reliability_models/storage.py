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
            save_file.write(f'{len(unit_list)}\n')
            for unit in unit_list:
                save_file.write(f'{unit.type}\n')

                for i in range(unit.number_of_blocks):
                    save_file.write(f'{unit.times[i]};{unit.distribution[i].get_type()}')
                    for key in unit.distribution[i].params.keys():
                        save_file.write(f';{key};{unit.distribution[i].params[key]}')

    def load(self) -> list[SchemeUnit]:
        load_data = []

        with open(self.file_name, 'r') as load_file:
            data = load_file.read().split('\n')
            line_id = 1

            for i in range(int(data[0])):
                new_unit = SchemeUnit(int(data[line_id]))
                for j in range(new_unit.number_of_blocks):
                    new_unit.times[j] = data[line_id + j]

                line_id += new_unit.number_of_blocks

        return load_data

    def clear_storage(self):
        ...
