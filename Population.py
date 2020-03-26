import random
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Population(object):
    """docstring for Population."""

    def __init__(self, size, area, conectivity, p_infected, p_isolated, p_die, loi, len_sim):
        super(Population, self).__init__()
        self.pop = size
        self.area = area
        self.conectivity = conectivity
        self.p_infected = p_infected
        self.p_isolated = p_isolated

        #self.p_recover = p_recover
        self.p_die = p_die
        self.len_i = loi
        self.end_time = len_sim
        self.day_dat = []


        self.individuals = []
        inf = random.sample(range(self.pop),int(self.pop*self.p_infected))
        isolated = random.sample(range(self.pop), int(self.pop*self.p_isolated))
        movement = np.random.random_integers(0,24, self.pop)
        #print(movement)
        self.test_time  = 14
        for i in range(self.pop):
            if i in inf and i in isolated:
                self.date_i = 0
                self.individuals.append(Person(i, True, True, movement[i], self.area, date_i = 0))
                self.stops = movement[i]

            elif i in inf and i not in isolated:
                self.date_i = 0
                self.individuals.append(Person(i, True , False, movement[i], self.area, date_i = 0))

            elif i not in inf and i not in isolated:
                self.individuals.append(Person(i, False, False, movement[i], self.area))
            else:
                self.individuals.append(Person(i, False, True, movement[i], self.area))
        for obj in self.individuals:
            obj.current_loc = [random.randint(0,self.area[0]),random.randint(0,self.area[1])]



        #individuall objects created. need to model daily individual motion in movement function

        for days in range(0,self.end_time):
            for hour in range(0,24):
                for obj in self.individuals:
                    p = np.random.choice([0, 1], size=1, p=[1-obj.p_of_stop, obj.p_of_stop])
                    #each hour 1 or 0 for stop or no stop with given independent probibility
                    #print(p)
                    if p == 1:
                        obj.movment()
                        obj.timer(days)
                    else:
                        if obj.infected ==True:
                            obj.timer(days)
                            #add a day to counter

            loc_list = []

            for obj in self.individuals: #check for new infections//intersecton
                if obj.current_loc not in [x[1] for x in loc_list]:
                    loc_list.append([obj, obj.current_loc])
                else:
                    if obj.infected == False and loc_list[[x[1]for x in loc_list].index(obj.current_loc)][0].infected == False:
                        pass

                    elif obj.infected == False and loc_list[[x[1]for x in loc_list].index(obj.current_loc)][0].infected == True:
                        obj.infected = True
                        obj.date_i = days
                    elif obj.infected == True and loc_list[[x[1]for x in loc_list].index(obj.current_loc)][0].infected == False:
                        loc_list[[x[1]for x in loc_list].index(obj.current_loc)][0].infected = True
                        loc_list[[x[1]for x in loc_list].index(obj.current_loc)][0].date_i = days
                    else:
                        pass
            num_i = 0
            for obj in self.individuals:
                if obj.infected:
                    num_i+=1
            print(num_i)
            #plot


        #dont forget to cure after 14 days



class Person(object):
    """docstring for Person."""
    len = 1
    def __init__(self, id,  infected, isolated, stops, area, date_i = '' ):
        super(Person, self).__init__()
        self.area = area
        self.isolated = isolated
        self.date_i = date_i
        if self.isolated:
            self.p_of_stop = .01
        else:
            self.p_of_stop = stops/96
        self.id = id
        self.infected = infected
        #self.hh_size = hh_size

        self.current_loc = ''

    def movment(self):
        new_loc = [random.randint(0,self.area[0]),random.randint(0,self.area[1])]

        while new_loc == self.current_loc:
            new_loc = [random.randint(0,self.area[0]),random.randint(0,self.area[1])]

        self.current_loc = new_loc
    def timer(self,date):
        if self.infected:
            if date - self.date_i < 14:
                pass
            else:
                self.infected == False




Houston = Population(1000, (100,200), 5, .3, .90, .02, 14, 28)
