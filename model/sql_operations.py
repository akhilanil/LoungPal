from PyQt5.QtCore import QObject

from model import sql_queries
from model.abstract_sql_operations import AbstractSqlOperations
from model.sql_connector import SqlConnector
from model.dao.login_model import LoginModel
from singleton import singleton


@singleton
class SqlOperations(AbstractSqlOperations):

    def login_request(self, login_model: LoginModel) -> str:
        sql_connection = SqlConnector.get_connection()
        cursor = sql_connection.cursor()
        cursor.execute(sql_queries.USER_AUTHENTICATION_QUERY, (login_model.user_name, login_model.password))
        record = cursor.fetchone()

        if record:
            msg = "Welcome: " + record[0]
        else:
            msg = "Incorrect Username/Password"

        cursor.close()

        return msg
