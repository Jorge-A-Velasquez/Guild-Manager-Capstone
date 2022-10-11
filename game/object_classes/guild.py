
from object_classes.hero import Hero
from object_classes.party import Party


class Guild:
    def __init__(self) -> None:
        self.hired_heros_list = []
        self.groups_list = []
        self.quest_list = []
        self.quest_history = []
        self.party_list = []
        self.funds = 100

    def __str__(self):
        return "Funds: {}, Heros: {}, Parties: {}, Quests: {}".format(
            self.funds,
            self.hired_heros_list,
            self.party_list,
            self.quest_list
        )

    def __repr__(self) -> str:
        return str(self)

    def Find_Heros(self):
        return [Hero() for i in range(10)]

    def Hire_Hero(self, new_hero: Hero):
        if (self.funds - new_hero.cost < 0):
            return False
        else:
            self.hired_heros_list.append(new_hero)
            self.funds -= new_hero.cost
            return True

    def Form_Party(self, hero_list, name=None):
        if name is not None:
            self.party_list.append(Party(hero_list, name))
        else:
            self.party_list.append(Party(hero_list))

    def Get_Party(self, name):
        for party in self.party_list:
            if party.name == name:
                return party

    def Send_Quest(self, party_name, quest) -> bool:
        party = self.Get_Party(party_name)
        return party.Take_Challenge(quest)