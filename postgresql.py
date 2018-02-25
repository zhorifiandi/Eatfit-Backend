import os
import sqlalchemy
import config
# import pandas as pd
import json
from flask import jsonify

# Sample use
# import postgresql
# postgres_obj = postgresql.PostgreSQL()
class PostgreSQL:
    def __init__(self):
        self.con, self.meta = self._connect()
        self.food_calories_table = self.meta.tables['food_calories']
        self.activity_calories_table = self.meta.tables['activity_calories']
        self.users_table = self.meta.tables['users']

    @staticmethod
    def _connect():
        # url = config.Config.DATABASE_URL
        url = 'postgresql://eatfitadmin@eatfit-db:Lerpekadut_82@eatfit-db.postgres.database.azure.com:5432/eatfit'
        con = sqlalchemy.create_engine(url, client_encoding='utf8')
        meta = sqlalchemy.MetaData(bind=con, reflect=True)

        return con, meta

    # Insert

    # Sample use
    # postgres_obj.insert_food_calory({
    #     'food_name' : 'Nasi Goreng',
    #     'calory_amount' : 250
    # })
    def insert_user(self, user_dictionary):
        clause = self.users_table.insert().values(user_dictionary)
        self.con.execute(clause)
        user_json = json.dumps(user_dictionary)
        return jsonify (
            msg='Signup succesful',
            user=user_json
        )

    # Sample use
    # postgres_obj.insert_food_calory({
    #     'username' : 'geraldzakwan',
    #     'email' : 'geraldi.dzakwan@gmail.com',
    #     'password' : 'lerpekadutanjing',
    # })
    def insert_food_calory(self, food_calory_dictionary):
        clause = self.food_calories_table.insert().values(food_calory_dictionary)
        self.con.execute(clause)

    # Sample use
    # postgres_obj.batch_insert_food_calories('List Makanan.csv')
    # Csv header : no, food_meal, calory_amount
    # def batch_insert_food_calories(self, csv_path):
    #     csv_dataframe = pd.read_csv(csv_path)
    #
    #     for index, series in csv_dataframe.iterrows():
    #         food_calory_dict = {}
    #         for elem in series.iteritems():
    #             if(elem[0] != 'no'):
    #                 food_calory_dict[elem[0]] = elem[1]
    #         self.insert_food_calory(food_calory_dict)

    # Login sample use
    # postgres_obj.authenticate {
    #   'username' : 'geraldzakwan'
    #   'password' : 'lerpekadutanjing'
    # }
    def authenticate(self, login_dictionary):
        # if('username' in login_dictionary):
        #     clause = self.users_table.select().where(
        #         self.users_table.c.username == login_dictionary['username']
        #     )
        #     user = self.con.execute(clause).fetchone()
        # elif('email' in login_dictionary):
        #     clause = self.users_table.select().where(
        #         self.users_table.c.email == login_dictionary['email']
        #     )
        #     user = self.con.execute(clause).fetchone()
        # else:
        #     return 'Authentication error - missing username/email'
        #
        # user_json = json.dumps(user.items())
        # if(user['password'] == login_dictionary['password']):
        #     return jsonify(
        #         msg='Authentication succesful',
        #         user=user_json
        #     )
        # else:
        #     return jsonify(
        #         msg='Authentication failed - wrong password'
        #     )
        return jsonify(
            msg='Authentication failed - wrong password'
        )
