from abc import ABC, abstractmethod


class AbstractLoginController(ABC):

    @abstractmethod
    def on_login_request(self, user_name, pass_word):
        pass

