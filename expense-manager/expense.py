class Expense:
    def __init__ (self, name, cost):
        self.name = name
        self.cost = cost
    def to_dict(self):
        return {"name": self.name, "cost": self.cost}
    @staticmethod
    def from_dict(data):
        data = Expense(data["name"], data["cost"])
