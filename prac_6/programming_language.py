class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection=0, year=""):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing.upper() == "DYNAMIC":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}". format(self.name, self.typing, self.reflection, self.year)

    def __repr__(self):
        return "{}".format(self.name)
