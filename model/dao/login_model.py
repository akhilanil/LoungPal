
class LoginModel(object):



    def __init__(self):
        self._user_name = ""
        self._password = ""

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        self._user_name = user_name

    @user_name.deleter
    def user_name(self):
        del self._user_name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @password.deleter
    def password(self):
        del self._password


