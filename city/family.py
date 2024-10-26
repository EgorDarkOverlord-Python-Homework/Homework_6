class Family:

    def __init__(self, father, mother, children):
        self.father = father
        self.mother = mother
        self.children = children

    def count(self):
        return 2 + len(self.children)
    