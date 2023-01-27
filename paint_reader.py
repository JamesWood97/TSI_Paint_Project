import csv
import paint


def save_wall_files(walls: list | tuple | set) -> None:
    """
    Function that takes in an array of walls and saves their details into a csv
    :param walls: A list of walls
    """
    # field names
    fields = ['Height', 'Length', 'Wall objects', "Has paint", 'Paint', "Number of coats"]

    rows = []
    for wall in walls:
        if wall.get_has_paint():
            row = [wall.get_height(), wall.get_length(), [], 1, wall.get_paint().name, wall.number_of_coats]
        else:
            row = [wall.get_height(), wall.get_length(), [], 0, "", wall.number_of_coats]
        rows.append(row)
    # name of csv file
    filename = input("File name? ")

    # writing to csv file
    with open(filename, 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(fields)
        csv_writer.writerows(rows)


class PaintReader:
    def __init__(self, paint_file_name: str = "paints.csv"):
        self.paint_file_name = paint_file_name

    def read_paint_files(self, paint_file_name: str | None = None) -> list:
        paints = []
        if paint_file_name is None:
            paint_file_name = self.paint_file_name
        with open(paint_file_name) as file:
            csv_file = csv.reader(file)
            for line in csv_file:
                paint_name = line[0]
                paint_cost_per_litre = float(line[1])
                paints.append(paint.Paint(paint_name, paint_cost_per_litre))
        return paints
