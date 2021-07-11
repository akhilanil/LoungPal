from abc import ABC, abstractmethod


class AbstractSqlOperations(ABC):

    @abstractmethod
    def login_request(self, login_model):
        # type(LoginModel)->None
        pass
