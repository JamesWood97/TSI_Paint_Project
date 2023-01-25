from paint import Paint

class WallObject:#window or door
    def __init__(self, height: float, length: float):
        self._shape = "rectangle"
        self._height = height
        self._length = length
        self._area = height*length

    def get_area(self) -> float:
        return self._area


class Wall:
    """
    Main Wall class
    """
    def __init__(self, height: float, length: float, wall_objects: tuple | set = (), paint: Paint | None = None,
                       number_of_coats: int = 1):
        self._height: float = height
        self._length: float = length
        self._area: float = height * length
        self._wall_objects = set([])
        for wall_object in wall_objects:
            self.add_wall_object(wall_object)
        self.paint = paint
        self.has_paint = not paint is None
        self.number_of_coats = number_of_coats

    def get_area(self) -> float:
        return self._area

    def add_wall_object(self, wall_object: WallObject):
        if wall_object not in self._wall_objects:
            self._wall_objects.add(wall_object)
            self._area -= wall_object.get_area()

    def remove_wall_object(self, wall_object: WallObject):
        if wall_object in self._wall_objects:
            self._wall_objects.remove(wall_object)
            self._area += wall_object.get_area()

    def get_cost(self) -> float:
        if self.has_paint:
            return self._area * self.paint.cost_per_litre * 1/12 * self.number_of_coats#average wall is approx 12m2, standard wall paint coveres 12-14m2 per liter, most walls need two coats, so 1.5-2 liters is a rough guide for a single wall.
        return 0.0


class Building:
    def __init__(self, walls: tuple | list | set = ()):
        self.walls = set([])
        for wall in walls:
            self.walls.add(wall)

    def get_total_cost(self) -> float:
        total_cost: float = 0
        for wall in self.walls:
            total_cost += wall.get_cost()
        return total_cost