from paint import Paint

class WallObject:#window or door
    """
    Object that obstructs part of a wall e.g a door or window
    """
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
    def __init__(self, height: float, length: float, wall_objects: list | tuple | set = (), paint: Paint | None = None,
                       number_of_coats: int = 1):
        """
        Constructor for Wall class
        :param height: Height of the wall
        :param length: Length of the wall
        :param wall_objects: Objects/obstructions on the wall, needs to be a list, tuple or set. Any duplicate wall
         objects will be removed
        :param paint: The paint to go on the wall. Must be a paint object or None for no paint
        :param number_of_coats: number of coats of paint. Defaults to 1
        """
        self._height: float = height
        self._length: float = length
        self._area: float = height * length
        self._wall_objects = set([])
        for wall_object in wall_objects:
            self.add_wall_object(wall_object)
        self._has_paint = False
        self._paint = None
        if paint is not None:
            self.set_paint(paint)
        self.number_of_coats = number_of_coats

    def get_area(self) -> float:
        """
        Gets the area
        :return: the area
        """
        return self._area

    def add_wall_object(self, wall_object: WallObject, throw_error_if_duplicate: bool = False):
        """
        Adds a WallObject object to the set of WallObjects on the wall. If the wallObject is already on the wall,
         it does nothing unless throw_error_if_duplicate is True, in which case it raises an error
        :param wall_object: The wall object to be added
        :param throw_error_if_duplicate: if an error should be thrown if the object is already on
        the wall
        :return: None
        """
        if wall_object not in self._wall_objects:
            self._wall_objects.add(wall_object)
            self._area -= wall_object.get_area()
        elif throw_error_if_duplicate:
            raise Exception("Tried to add", wall_object, "to", self, "when", wall_object, "was already on it")

    def remove_wall_object(self, wall_object: WallObject, throw_error_if_not_on_wall: bool = False):
        if wall_object in self._wall_objects:
            self._wall_objects.remove(wall_object)
            self._area += wall_object.get_area()
        elif throw_error_if_not_on_wall:
            raise Exception("Attempted to remove", WallObject, "from", self,
                            "but the given WallObject was not on the wall")

    def get_cost(self) -> float:
        """
        Gets the cost to paint the wall
        :return: the cost
        """
        if self._has_paint:
            return self._area * self._paint.cost_per_litre * 1 / 12 * self.number_of_coats#average wall is approx 12m2, standard wall paint coveres 12-14m2 per liter, most walls need two coats, so 1.5-2 liters is a rough guide for a single wall.
        return 0.0

    def set_paint(self, paint: Paint):
        """
        Sets the paint of the wall to a given Paint object
        :param paint: The paint to be added
        """
        if type(paint) is not Paint:
            raise Exception(paint, "is not paint")
        self._paint = paint
        self._has_paint = True

    def remove_paint(self):
        """
        Removes paint from a wall
        :return:
        """
        self._has_paint = False
        self._paint = None

    def get_has_paint(self) -> bool:
        """
        Returns true if the wall has a paint object
        :return: Bool indicating if the wall has a paint object
        """
        return self._has_paint

    def get_paint(self) -> Paint | None:
        return self._paint

class Building:
    """
    Building class. Contains a set of walls
    """
    def __init__(self, walls: tuple | list | set = ()):
        self.walls = set([])
        for wall in walls:
            self.walls.add(wall)

    def get_total_cost(self) -> float:
        """
        Gets the total cost of all the walls in the building
        :return: cost of all the walls as a float
        """
        total_cost: float = 0
        for wall in self.walls:
            total_cost += wall.get_cost()
        return total_cost
