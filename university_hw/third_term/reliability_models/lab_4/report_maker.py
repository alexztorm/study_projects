import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table
from datetime import datetime


class ReportMaker:
    def __init__(self):
        self.path = './reports'
        self.column_names_holsted = ['Число уникальных операторов программы', 'Число уникальных операндов программы',
                                     'Общее число операторов в программе', 'Общее число операндов в программе',
                                     'Словарь программы', 'Длина программы', 'Теоретическая длина программы',
                                     'Объем программы', 'Уровень качества программирования',
                                     'Сложность понимания программы', 'Трудоемкость кодирования программы',
                                     'Уровень языка выражения', 'Умственные затраты на создание программы']
        self.column_names_chepin = ['Вводимые переменные', 'Модифицируемые переменные', 'Управляющие переменные',
                                    'Паразитные переменные', 'Значение метрики']

    def make_report(self, data):
        data = self.preprocess_data(data)

        tables_data = {}
        for table_number, data_dict, row_label in data:
            if table_number not in tables_data:
                tables_data[table_number] = []
            tables_data[table_number].append((data_dict, row_label))

        current_time = datetime.now().strftime('%H%M%d%m%Y')
        pdf_filename = self.path + f'/report_{current_time}.pdf'

        with plt.ioff():
            num_tables = len(tables_data)
            fig, axs = plt.subplots(nrows=num_tables, ncols=1, figsize=(8, 4 * num_tables))

            for i, (table_number, rows) in enumerate(tables_data.items()):
                data_dicts, row_labels = zip(*rows)
                df = pd.DataFrame(data_dicts, index=row_labels)

                if df.shape[1] > 10:
                    df.columns = self.column_names_holsted
                else:
                    df.columns = self.column_names_chepin

                axs[i].axis('tight')
                axs[i].axis('off')
                tbl = table(axs[i], df, loc='center', cellLoc='center')

                # for key, cell in tbl.get_celld().items():
                #     if key[0] == 0:
                #         cell.set_text_props(rotation=90)

                axs[i].set_title(f'Эксперимент {table_number}')

            plt.savefig(pdf_filename, bbox_inches='tight', pad_inches=0.1)
            plt.close()

    @staticmethod
    def preprocess_data(data):
        for line in data:
            if len(line[1]) > 10:
                for i, key in enumerate(line[1].keys()):
                    if i < 6:
                        line[1][key] = round(line[1][key], 0)
                    else:
                        line[1][key] = round(line[1][key], 2)
            else:
                for key in line[1].keys():
                    line[1][key] = round(line[1][key], 0)

        data.sort(key=lambda x: x[0])

        return data
