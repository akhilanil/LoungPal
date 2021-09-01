from controllers.abstract_controller import AbstractMapController
from controllers.path_finder import ShortestPathFinder
from model.sql_operations import SqlOperations
from singleton import singleton


@singleton
class MapController(AbstractMapController):

    def __init__(self):
        self._sql_operations = SqlOperations()

    def get_all_location(self) -> dict[tuple[int, int], str]:
        return self._sql_operations.get_all_locations()

    def get_shortest_path(self, total_rows: int, total_columns: int,
                          start_point: tuple[int, int], end_point: tuple[int, int]) -> list[tuple[int, int]]:
        # matrix_map = [[1 for _ in range(total_rows + 1)] for _ in range(total_columns + 1 )]
        # return ShortestPathFinder(matrix_map).get_shortest_path(start=start_point, end=end_point)
        return ShortestPathFinder.get_shortest_path(start=start_point, end=end_point)
