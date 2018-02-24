import os
import sqlalchemy
import config
# from flask import current_app

class PostgreSQL:
    def __init__(self):
        self.con, self.meta = self._connect()
        # self.users_table = self.meta.tables['users']
        # self.orders_table = self.meta.tables['orders']
        # self.menus_table = self.meta.tables['menus']
        # self.stocks_table = self.meta.tables['stocks']
        # self.schedules_table = self.meta.tables['schedules']

    @staticmethod
    def _connect():
        url = config.DATABASE_URL
        con = sqlalchemy.create_engine(url, client_encoding='utf8')
        meta = sqlalchemy.MetaData(bind=con, reflect=True)

        return con, meta

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
    raw_data = postgres_obj.con.execute(postgres_obj.meta.tables['food_calories'].select()).fetchall()
    if (raw_data == None):
        print('Empty record')
    else:
        print('Ada')
        print(raw_data)
        for res in raw_data:
            food_name, calory_amount = res
            print(food_name, calory_amount)
