
import sqlite3


class SqlConnector(object):

    __SQL_CONNECTION = None

    @staticmethod
    def get_connection():

        if SqlConnector.__SQL_CONNECTION:
            return SqlConnector.__SQL_CONNECTION

        sql_connection = None
        try:
            sql_connection = sqlite3.connect("loginqt.db")

        except sqlite3.Error as error:
            # TODO: Throw exception
            print("Error while connecting to sqlite", error)

        SqlConnector.__SQL_CONNECTION = sql_connection
        return sql_connection

