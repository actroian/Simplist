class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __repr__(self):
        return ("Name: " +self.name + "\nDuration: " + str(self.duration))
