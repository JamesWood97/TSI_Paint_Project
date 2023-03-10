from paint import Paint
from math import pi


class WallObject:#window or door
    """
    Object that obstructs part of a wall e.g a door or window
    """
    def __init__(self, height: float, length: float, shape: str = "rectangle"):
        """
        Constructor for WallObject class
        :param height: Height of the WallObject.
        :param length: The length of the WallObject.
        :param shape: The shape of the wall object, can be "rectangle" or "oval". For squares and circles use rectangle
        and oval respectively with the same heights and lengths.
        """
        shape = shape.lower()
        if shape not in ("rectangle", "oval"):
            raise Exception("Wall object shape must be rectangle or oval, not ", shape)
        self._shape = shape
        self._height = height
        self._length = length
        self._area = height*length

    def set_height(self, height: float | int):
        """
        Sets the height to the given height and recalculates the WallObjects' area
        :param height: the new height
        """
        self._height = height
        self._calculate_area()

    def set_length(self, length: float | int):
        """
        Sets the length to the given height and recalculates the WallObjects' area
        :param length: the new length
        """
        self._length = length
        self._calculate_area()

    def _calculate_area(self):
        """
        protected function to calculate the shapes area given its length and height and shape, saves area in self._area
        """
        if self._shape == "rectangle":
            self._area = self._height * self._length
        else:#if the shape is oval
            self._area = (self._height / 2) * (self._length / 2) * pi

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
        return 0

    def get_paint_litres(self) -> float | int:
        """
        Gets the amount of paint needed for the wall, assuming length and height are in meters
        :return: the amount of paint needed in litres
        """
        if self._has_paint:
            return self._area * 1 / 12 * self.number_of_coats#average wall is approx 12m2, standard wall paint coveres 12-14m2 per liter, most walls need two coats, so 1.5-2 liters is a rough guide for a single wall.
        return 0

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

    def get_height(self) -> float:
        return self._height

    def get_length(self) -> float:
        return self._length


class Building:
    """
    Building class. Contains a set of walls
    """
    def __init__(self, walls: tuple | list | set = ()):
        """
        Constructor for wall class
        :param walls: An array fo walls to be added. Duplicate walls will be removed
        """
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

    def get_paints_needed(self) -> dict:
        """
        Gets the total amount of all the walls in the building
        :return: a dict containing a paint as a key and its corrisponding amount needed
        """
        paints_needed = {}
        for wall in self.walls:
            if wall.get_has_paint():
                if wall.get_paint() in paints_needed:
                    paints_needed[wall.get_paint()] += wall.get_paint_litres()
                else:
                    paints_needed[wall.get_paint()] = wall.get_paint_litres()
        return paints_needed
