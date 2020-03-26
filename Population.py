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
                self.individuals.append(Person(i, True, True, movement[i], date_i = 0))
                self.stops = movement[i]

            elif i in inf and i not in isolated:
                self.date_i = 0
                self.individuals.append(Person(i, True , False, movement[i], date_i = 0))

            elif i not in inf and i not in isolated:
                self.individuals.append(Person(i, False, False, movement[i]))
            else:
                self.individuals.append(Person(i, False, True, movement[i]))
        for obj in self.individuals:
            obj.current_loc = [random.randint(0,area1[0]),random.randint(0,area1[1])]
            #plot the objects



        
        for days in range(0,self.end_time):
            for hour in range(0,24):
                for obj in self.individuals:
                    p = np.random.choice([0, 1], size=1, p=[1-obj.p_of_stop, obj.p_of_stop])
                    #each hour 1 or 0 for stop or no stop with given independent probibility
                    print(p)
                    if p == 1:
                        obj.movment()

            loc_list = []

            for obj in self.individuals: #check for new infections//intersecton
                if obj.current_loc not in [x[1] for x in loc_list]:
                    loc_list.append(obj, obj.current_loc)
                else:
                    if obj.infected == False and #loc_list.index(--).infected == False:
                        pass

                    elif obj.infected == False and #loc_list.index(--).infected == True:
                        obj.infected = True
                    elif obj.infected == True and #loc_list.index(--).infected == False:
                        #loc_list.index(--).infected == True
                    else:
                        pass


            #plot


        #dont forget to cure after 14 days


    def contact(self):
        pass

        #individuall objects created. need to model daily individual motion in movement function




class Person(object):
    """docstring for Person."""
    len = 1
    def __init__(self, id,  infected, isolated, stops, date_i = ''):
        super(Person, self).__init__()
        self.date_i = date_i
        self.p_of_stop = stops/96
        self.id = id
        self.infected = infected
        #self.hh_size = hh_size
        self.isolated = isolated
        self.current_loc = ''

    def movment(self):
        new_loc = [random.randint(0,area1[0]),random.randint(0,area1[1])]

        while new_loc == self.current_loc:
            new_loc = [random.randint(0,area1[0]),random.randint(0,area1[1])]

        self.current_loc = new_loc










Houston = Population(10, 4, (5,5), 5, .2, .70, .05, .02, 14, 1)
