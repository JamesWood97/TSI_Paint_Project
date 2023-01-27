class Paint:
    """
    Main paint class
    """
    def __init__(self, name: str, cost_per_litre: float):
        self.name = name
        self.cost_per_litre = cost_per_litre

    def __str__(self):
        return self.name
