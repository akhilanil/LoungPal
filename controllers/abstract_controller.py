from abc import ABC, abstractmethod


class AbstractLoginController(ABC):

    @abstractmethod
    def on_login_request(self, user_name, pass_word):
        pass


class AbstractMapController(ABC):

    @abstractmethod
    def get_all_location(self):
        pass

    @abstractmethod
    def get_shortest_path(self, total_rows: int, total_columns: int,
                          start_point: tuple[int, int], end_point: tuple[int, int]) -> list[tuple[int, int]]:
        pass




