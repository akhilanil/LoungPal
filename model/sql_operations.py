from PyQt5.QtCore import QObject

from model import sql_queries
from model.abstract_sql_operations import AbstractSqlOperations
from model.sql_connector import SqlConnector
from model.dao.login_model import LoginModel
from singleton import singleton


@singleton
class SqlOperations(AbstractSqlOperations):

    def login_request(self, login_model: LoginModel) -> tuple[bool, str]:
        sql_connection = SqlConnector.get_connection()
        cursor = sql_connection.cursor()
        cursor.execute(sql_queries.USER_AUTHENTICATION_QUERY, (login_model.user_name, login_model.password))
        record = cursor.fetchone()

        if record:
            valid_user = True
            msg = "Welcome: " + record[0]
        else:
            valid_user = False
            msg = "Incorrect Username/Password"

        cursor.close()

        return valid_user, msg

    def get_all_locations(self) -> dict[tuple[int, int], str]:

        sql_connection = SqlConnector.get_connection()
        cursor = sql_connection.cursor()
        cursor.execute(sql_queries.ALL_LOCATIONS_QUERY)
        # [(0, 0, KFC), (1,0, BK),....]
        records = cursor.fetchall()

        # Converting list of tuples into dictionary
        location_dict = dict(map(lambda record: ((record[0], record[1]), record[2]), records))

        cursor.close()

        return location_dict



