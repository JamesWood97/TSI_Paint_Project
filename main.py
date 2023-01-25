from walls import Wall, WallObject, Building, Paint


def get_valid_input(question_text: str, type_to_cast_to=float) -> float | int | str:
    while True:
        user_input = input(question_text)
        try:
            float_user_input = type_to_cast_to(user_input)
            return float_user_input
        except ValueError:
            print("Invalid input")

def select_from_list(array):
    for i in range(len(array)):
        print(i+1,array[i])
    while True:
        user_input = get_valid_input("Choice of paint: ", int)
        if 1 <= user_input <= len(array):
            return array[user_input - 1]
        print("Invalid choice! Selection choice must be between 1 and", len(array))


def get_paints_from_user():
    paints = []
    number_of_paints: int = get_valid_input("How many different paints are going to be used? ", int)
    for i in range(number_of_paints):
        name = input("Paint name: ")
        cost_per_litre = get_valid_input("Cost per litre: ")
        paint = Paint(name, cost_per_litre)
        paints.append(paint)
    return paints


if __name__ == "__main__":
    paints = get_paints_from_user()

    number_of_walls = get_valid_input("Number of walls to be painted: ", int)

    building: Building = Building()

    for i in range(number_of_walls):

        paint = select_from_list(paints)

        wall_width: float = get_valid_input("What is the length of the wall in metres? ")
        wall_height: float = get_valid_input("What is the height of the wall in metres? ")
        number_of_wall_objects: int = get_valid_input("How many immovable objects e.g windows, plugs and doors are on your wall? ",
                                                      type_to_cast_to=int)
        wall = Wall(wall_height, wall_width)
        for _ in range(number_of_wall_objects):
            wall_object_height: float = float(input("What is the height of your object in metres? "))
            wall_object_width: float = float(input("What is the width of your object in metres? "))
            wall_object: WallObject = WallObject(wall_object_height, wall_object_width)
            wall.add_wall_object(wall_object)
        building.walls.add(wall)

    print("Total cost: ", building.get_total_cost())














































