from walls import Wall, WallObject, Building, Paint
import paint_reader


def get_valid_input(question_text: str, type_to_cast_to=float) -> float | int | str:
    """
    Asks the user a given question, and then accepts user inputs until an input that can be cast to the given data type
    is given
    :param question_text: The question to ask the user
    :param type_to_cast_to: The datatype to cast to. Can be float, int or string. Defaults to float
    :return: returns the users input cast to the correct data type
    """
    while True:
        user_input = input(question_text + " ")
        try:
            float_user_input = type_to_cast_to(user_input)
            return float_user_input
        except ValueError:
            print("Invalid input")


def select_from_list(array: list | tuple, question: str | None = None):
    """
    For a given list, presents all items in the list as options to the user and allows the user to select an item
    :param array: the list to select from
    :param question: the question to ask the user
    :return: the item from the list selected by the user
    """
    if question is not None:
        print(question)
    for i in range(len(array)):
        print(i+1, array[i])
    while True:
        user_input = get_valid_input("Choice:", int)
        if 1 <= user_input <= len(array):
            return array[user_input - 1]
        print("Invalid choice! Selection choice must be between 1 and", len(array))


def get_paints_from_user() -> list:
    """
    Allows the user to input the number of paints, their names and prices per litre
    :return: a list of paint objects
    """
    paints: list = []
    number_of_paints: int = get_valid_input("How many different paints are going to be used? ", int)
    for i in range(number_of_paints):
        name = input("Paint name: ")
        cost_per_litre = get_valid_input("Cost per litre: ")
        paint = Paint(name, cost_per_litre)
        paints.append(paint)
    return paints


if __name__ == "__main__":
    #Gets the paints
    paint_retrieval_method: str = select_from_list(["Load paints", "Input paints manually"])
    if paint_retrieval_method == "Load paints":
        paint_reader_object = paint_reader.PaintReader()
        paints = paint_reader_object.read_paint_files()
    else:
        paints = get_paints_from_user()

    #gets thre number of walls
    number_of_walls = get_valid_input("Number of walls to be painted:", int)


    building: Building = Building()

    for i in range(number_of_walls):
        print("\nNew Wall:\n")
        wall_width: float = get_valid_input("What is the length of the wall in metres?")
        wall_height: float = get_valid_input("What is the height of the wall in metres?")
        paint: Paint = select_from_list(paints, question="Which paint do you want to use on this wall?")
        layers: int = get_valid_input("How many layers do you want to paint this wall with? ",
                                                      type_to_cast_to=int)
        wall = Wall(wall_height, wall_width, paint = paint, number_of_coats=layers)
        number_of_wall_objects: int = get_valid_input("How many immovable objects e.g windows, plugs and doors are on your wall?",
                                                      type_to_cast_to=int)
        for _ in range(number_of_wall_objects):
            wall_object_height: float = get_valid_input("What is the height of your object on the wall in metres?")
            wall_object_width: float = get_valid_input("What is the width of your object on the wall in metres?")
            wall_object: WallObject = WallObject(wall_object_height, wall_object_width)
            wall.add_wall_object(wall_object)
            print("Wall object added to wall")
        building.walls.add(wall)

    print("Paints needed:")
    paint_amounts = building.get_paints_needed()
    for i in paint_amounts:
        print(f"{i}: {paint_amounts[i]} litres")
    print(f"Total cost: £{round(building.get_total_cost(), 2)}")
    a = input("Save Walls? Y/N ")
    if a.lower() in ("y", "yes", "1", "yeah"):
        paint_reader.save_wall_files(building.walls)














































