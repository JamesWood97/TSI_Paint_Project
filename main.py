class WallObject:#window or door
    def __init__(self, height: float, length: float):
        self._shape = "rectangle"
        self._height = height
        self._length = length
        self._area = height*length

    def get_area(self) -> float:
        return self._area


class Wall:
    def __init__(self, height: float, length: float, wall_objects: tuple | set = ()):
        self._height: float = height
        self._length: float = length
        self._area: float = height * length
        self._wall_objects = set([])
        for wall_object in wall_objects:
            self.add_wall_object(wall_object)

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


if __name__ == "__main__":
    wall_width: float = float(input("What is the length of the wall in cm? "))
    wall_height: float = float(input("What is the height of the wall in cm? "))
    number_of_wall_objects: int = int(input("How many immovable objects e.g windows and doors are on your wall? "))
    wall = Wall(wall_height, wall_width)
    for _ in range(number_of_wall_objects):
        wall_object_height: float = float(input("What is the height of your object in cm? "))
        wall_object_width: float = float(input("What is the width of your object in cm? "))
        wall_object: WallObject = WallObject(wall_object_height, wall_object_width)
        wall.add_wall_object(wall_object)

    wall_area: float = wall.get_area()
    wall_area_meters: float = wall_area / 10000
    number_of_layers: int = int(input("How many coats of paint?"))
    paint_liters_needed = number_of_layers*wall_area_meters/12
    print(paint_liters_needed, "litres of paint needed")




class Car:
    def __init__(self, model, colour):
        self.model = model
        self.colour = colour














































