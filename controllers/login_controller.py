from controllers.abstract_controller import AbstractLoginController
from PyQt5.QtCore import QObject, pyqtSlot

from model.dao.login_model import LoginModel
from model.sql_operations import SqlOperations
from singleton import singleton


@singleton
class LoginController(AbstractLoginController):


    def __init__(self):
        self._sql_operations = SqlOperations()

    @pyqtSlot(str, str)
    def on_login_request(self, user_name, password) -> tuple[bool, str]:

        login_model = LoginModel()
        login_model.user_name = user_name
        login_model.password = password
        return self._sql_operations.login_request(login_model=login_model)
