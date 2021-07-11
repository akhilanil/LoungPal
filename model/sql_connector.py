
import sqlite3


class SqlConnector(object):

    @staticmethod
    def get_connection():
        sql_connection = None
        try:
            sql_connection = sqlite3.connect("loginqt.db")

        except sqlite3.Error as error:
            # TODO: Throw exception
            print("Error while connecting to sqlite", error)
        return sql_connection

