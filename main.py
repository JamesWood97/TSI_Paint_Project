from walls import Wall, WallObject, Paint


if __name__ == "__main__":
    wall_width: float = float(input("What is the length of the wall in metres? "))
    wall_height: float = float(input("What is the height of the wall in metres? "))
    number_of_wall_objects: int = int(input("How many immovable objects e.g windows, plugs and doors are on your wall? "))
    wall = Wall(wall_height, wall_width)
    for _ in range(number_of_wall_objects):
        wall_object_height: float = float(input("What is the height of your object in metres? "))
        wall_object_width: float = float(input("What is the width of your object in metres? "))
        wall_object: WallObject = WallObject(wall_object_height, wall_object_width)
        wall.add_wall_object(wall_object)

    wall_area: float = wall.get_area()
    wall_area_meters: float = wall_area / 10000
    number_of_layers: int = int(input("How many coats of paint?"))
    paint_liters_needed = number_of_layers*wall_area_meters/12
    print(paint_liters_needed, "litres of paint needed")














































