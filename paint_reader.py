import csv
import paint


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
