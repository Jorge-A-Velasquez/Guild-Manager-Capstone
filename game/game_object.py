
from game.game_math.random import RandomRange
from game.object_classes.challenge import Challenge
from game.object_classes.guild import Guild
from game.object_classes.hero import Hero
from game.object_classes.map_tile import MapTile
from game.object_classes.map import Map



class Game:
    def __init__(self):
        # setting up ID numbers
        self.GUILD_ID = 0
        self.HERO_ID = 0
        self.QUEST_ID = 0
        self.LOCALE_ID = 0
        self.guild = self.Create_Guild()
        self.map = self.Create_Map()
        self.full_hero_list = []
        self.full_quest_list = []


    def Create_Guild(self):
        ret_guild = Guild(self.GUILD_ID)
        self.GUILD_ID += 1
        return ret_guild

    def Get_Heros(self):
        hero_list = []
        for i in range(10):
            hero_list.append(Hero(self.HERO_ID))
            self.HERO_ID += 1
        self.full_hero_list.extend(hero_list)
        return hero_list

    def Find_Hero(self, name):
        for hero in self.full_hero_list:
            if hero.name == name:
                return hero
        return None

    def Hire_Hero(self, name):
        hero = self.Find_Hero(name)
        if hero:
            return self.guild.Hire_Hero(hero)
        return False

    def Guild_Status(self):
        return self.guild

    def Add_Party(self, name, list):
        self.guild.Form_Party(list, name)

    def Get_Quest(self):
        new_quest = Challenge('STR')
        self.full_quest_list.append(new_quest)
        return new_quest

    def Find_Quest(self, name):
        for quest in self.full_quest_list:
            if quest.name == name:
                return quest
        return None

    def Do_Quest(self, quest_name, party_name):
        self.guild.Send_Quest(party_name, self.Find_Quest(quest_name))
    
    def Create_Map(self):
        locales = Map()
        coordinates = []
        while len(coordinates) < 5:
            coords = (RandomRange(0,10), RandomRange(0,10))
            if coords in coordinates:
                continue
            coordinates.append(coords)
            locales.locations[coords] = MapTile(self.LOCALE_ID)
            self.LOCALE_ID += 1
        return locales
