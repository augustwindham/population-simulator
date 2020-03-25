import random
from matplotlib import pyplot as plt
from math import sqrt
import numpy as np

area1 = (100,100)

class Population(object):
    """docstring for Population."""



    def __init__(self, size, hh_size, area, conectivity, p_infected, p_isolated, roi, p_die, loi, len_sim):
        super(Population, self).__init__()
        self.pop = size
        self.hh_number = hh_size
        self.area = area
        self.conectivity = conectivity
        self.p_infected = p_infected
        self.p_isolated = p_isolated
        self.roi = roi
        #self.p_recover = p_recover
        self.p_die = p_die
        self.len_i = loi
        self.end_time = len_sim
        self.c_time = 0
        self.movment_array = []


        self.individuals = []
        inf = random.sample(range(self.pop),int(self.pop*self.p_infected))
        isolated = random.sample(range(self.pop), int(self.pop*self.p_isolated))
        movement = np.random.random_integers(0,8+1,self.pop)
        #print(movement)
        self.test_time  = 14
        for i in range(self.pop):
            if i in inf and i in isolated:
                self.date_i = 0
                self.individuals.append(Person(i, True, True, movement[i], date_i = 0))
                self.stops = movement[i]

            elif i in inf and i not in isolated:
                self.date_i = 0
                self.individuals.append(Person(i, True , False, movement[i], date_i = 0))

            elif i not in inf and i not in isolated:
                self.individuals.append(Person(i, False, False, movement[i]))
            else:
                self.individuals.append(Person(i, False, True, movement[i]))

        for days in range(self.end_time):
            obj_day_stops = []
            for obj in range(0, len(self.individuals)):
                obj_day_stops.append([obj,self.individuals[obj].movement(area1[0], area1[1])])
            self.movment_array.append(obj_day_stops)
            print(self.movment_array)
            self.contact()


    def contact(self):
        pass

        #individuall objects created. need to model daily individual motion in movement function




class Person(object):
    """docstring for Person."""

    def __init__(self, id,  infected, isolated, stops, date_i = ''):
        super(Person, self).__init__()
        self.date_i = date_i
        self.num_stops = stops
        self.id = id
        self.infected = infected
        #self.hh_size = hh_size
        self.isolated = isolated

    def movement(self, size1, size2):
        stop_l = []
        for stop in range(int(self.num_stops)):
            stop_l.append([random.randint(0,size1),random.randint(0,size2),24/int(self.num_stops)*stop])

        return stop_l
        print(self.day_stops)





Houston = Population(5000, 4, (100,100), 5, .005, .70, .05, .02, 14, 1)
