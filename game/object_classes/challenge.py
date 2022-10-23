
import game.object_classes.static_consts as sc


class Challenge:
    def __init__(self, skill=None, new_type='Random') -> None:
        self.test_skill = skill
        self.name = 0   # change this later
        self.type = new_type

    def Get_Skill(self):
        return self.test_skill

    def Set_Skill(self, new_skill):
        self.test_skill = new_skill

    def __repr__(self) -> str:
        return "Name: {}, Skill: {}".format(self.name, self.test_skill)
