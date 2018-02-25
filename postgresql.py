import os
import sqlalchemy
import config
import pandas as pd

class PostgreSQL:
    def __init__(self):
        self.con, self.meta = self._connect()
        self.food_calories_table = self.meta.tables['food_calories']
        self.activity_calories_table = self.meta.tables['activity_calories']
        self.users_table = self.meta.tables['users']
        # Sample use
        # postgres_obj = postgresql.PostgreSQL()

    @staticmethod
    def _connect():
        url = config.DATABASE_URL
        con = sqlalchemy.create_engine(url, client_encoding='utf8')
        meta = sqlalchemy.MetaData(bind=con, reflect=True)

        return con, meta

    # Insert

    def insert_food_calory(self, food_calory_dictionary):
        clause = self.food_calories_table.insert().values(food_calory_dictionary)
        self.con.execute(clause)
        # Sample use
        # postgres_obj.insert_food_calory({
        #     'food_name' : 'Nasi Goreng',
        #     'calory_amount' : 250
        # })

    # Csv header : no, food_meal, calory_amount

    def batch_insert_food_calories(self, csv_path):
        csv_dataframe = pd.read_csv(csv_path)

        for index, series in csv_dataframe.iterrows():
            food_calory_dict = {}
            for elem in series.iteritems():
                if(elem[0] != 'no'):
                    food_calory_dict[elem[0]] = elem[1]
            self.insert_food_calory(food_calory_dict)
    # Menus
    # def get_menus(self):
    #     raw_menus = self.con.execute(self.menus_table.select()).fetchall()
    #     if raw_menus is None:
    #         return None
    #     menus = []
    #     for raw_menu in raw_menus:
    #         type_menu, name = raw_menu
    #         menu = {
    #             'type_menu': type_menu,
    #             'name': name
    #         }
    #         menus.append(menu)
    #     return menus
    #
    # def set_schedule(self, what_to_set, time):
    #     clause = None
    #
    #     if(what_to_set == 'open_hour'):
    #         clause = self.schedules_table.update().where(
    #             self.schedules_table.c.id == 1
    #         ).values(
    #             open_hour=time
    #         )
    #     elif(what_to_set == 'close_hour'):
    #         clause = self.schedules_table.update().where(
    #             self.schedules_table.c.id == 1
    #         ).values(
    #             close_hour=time
    #         )
    #
    #     if clause is not None:
    #         self.con.execute(clause)
    #
    # def add_abang_id(self, id):
    #     clause = self.users_table.insert().values(
    #         id=id,
    #         role='abang'
    #     )
    #     self.con.execute(clause)

if __name__ == "__main__":
    postgres_obj = PostgreSQL()
    # Batch insert
    # postgres_obj.batch_insert_food_calories("List Makanan.csv")
