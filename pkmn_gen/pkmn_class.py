from random import *


class Monster:
    def __init__(self,half1,half2,type_check,ability_check,stat_check,stat):
        self.part_one = half1
        self.part_two = half2
        self.name = ""
        self.type = ""
        self.sec_type = "None"
        self.ability = ""
        self.stat_total = 0
        self.stats = {"HP":0,"ATK":0,"SPATK":0,"DEF":0,"SPDEF":0,"SPD":0}
        self.label_colours = ["#d1502c","#2c6bd1",
                              "#3ad12c","#615546",
                              "#9dafb0","#9c7f59",
                              "#8c9c70","#3a373b",
                              "#583e61","#a3458d",
                              "#c98012","#09b1bd",
                              "#391978","#f576e6",
                              "#666666","#8625cc",
                              "#262626","#aba746"]
        self.col = ""
        self.col_2 = ""

        if type_check:
            self.get_type()
        if ability_check:
            self.get_ability()

        if stat_check:
            self.stat_total = stat
            self.get_stats()

        self.get_halves()
        self.create_name()

    def get_halves(self):
        animal_f = open("ANIMALS.txt",'r')
        animal_list = animal_f.readlines()
        objects_f = open("OBJECTS.txt",'r')
        objects_list = objects_f.readlines()
        if self.part_one == "animal":
            half_num = randint(0,len(animal_list)-1)
            self.part_one = animal_list[half_num][:-1]
        else:
            half_num = randint(0,len(objects_list)-1)
            self.part_one = objects_list[half_num][:-1]

        if self.part_two == "animal":
            half_num = randint(0, len(animal_list)-1)
            self.part_two = animal_list[half_num][:-1]
        else:
            half_num = randint(0, len(objects_list)-1)
            self.part_two = objects_list[half_num][:-1]

        animal_f.close()
        objects_f.close()

    def create_name(self):
        name1 = self.part_one
        name2 = self.part_two
        name2.lower()
        name1.capitalize()
        if len(name1) > 5:
            name1 = name1[:(len(name1) // 2)]
        name2 = name2[len(name2)//2:]

        self.name = name1 + name2

    def print_monster(self):
        return (self.part_one, self.part_two)

    def get_type(self):
        type_num = randint(0,17)
        second = randint(0,1)
        type_f = open('TYPES.txt','r')
        type_list = type_f.readlines()
        self.type = type_list[type_num][:-1]
        self.col = self.label_colours[type_num]
    #getting secondary type
        if second:
            type_num = randint(0, 17)
            while self.type == type_list[type_num][:-1]:
                type_num = randint(0, 17)
            self.sec_type = type_list[type_num][:-1]
            self.col_2 = self.label_colours[type_num]
        type_f.close()

    def print_type(self):
        return (self.type, self.sec_type)

    def print_type_col(self):
        return (self.col,self.col_2)

    def get_ability(self):
        #258 base abilities(including signature abilities) - to remove later
        ability_f = open("ABILITIES.txt","r")
        ability_test = ability_f.readlines()
        ability_num = randint(0,len(ability_test)-1)
        self.ability = ability_test[ability_num][:-1]

    def print_ability(self):
        return self.ability

    def get_stats(self):
        work_total = self.stat_total
        for key in self.stats:
            stat_value = (randint(5,work_total//4) // 5) * 5
            while stat_value > 220:
                stat_value = (randint(5,work_total//4) // 5) * 5
            if key == "SPD":
                self.stats["SPD"] = work_total
            else:
                self.stats[key] = stat_value
                work_total -= stat_value

    def print_stat(self):
        return self.stats

    def print_name(self):
        return self.name
