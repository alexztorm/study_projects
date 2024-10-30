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
                    new_unit.times[j] = int(block_line[0])
                    new_unit.distribution[j].change_distribution_type(block_line[1])
                    params = [float(x) for x in block_line[2:]]
                    new_unit.distribution[j].change_params(params)
                load_data.append(new_unit)

                line_id += new_unit.number_of_blocks + 1

        return load_data
