from city.city import City
import random
from city.person import Person
from city.family import Family

class CityList(City):

    def __init__(self, name, count):
        super(CityList, self).__init__(name, count)
        self.__person_list = []


    def add_person(self,p):
        if super(CityList, self).add_person():
            self.__person_list.append(p)

    def add_person_generate(self):
        p = random.randint(1,100)
        s = str(p)
        self.add_person(Person(s,s+s, s+s+s))

    def add_family(self, family):
        if super().add_family(family.count()):
            self.__person_list.append(family.father)
            self.__person_list.append(family.mother)
            for c in family.children:
                self.__person_list.append(c)

    def add_family_generate(self):
        count = random.randint(2, 6)
        
        p = random.randint(1,100)
        s = str(p)
        pm = random.randint(1,100)
        sm = str(pm)
        family = Family(Person(s,s+s, s+s+s),
                        Person(sm, s+s, sm+sm+sm),
                        [Person(str(random.randint(1,100)), s+s, s+s+s+s) for i in range(count - 2)])
        
        self.add_family(family)


    def remove_person(self, i):

        if super(CityList,self).remove_person():
            i = i % len(self.__person_list)
            del self.__person_list[i]

    def __str__(self):
        s1 = super(CityList, self).__str__()

        s = []
        s.append(s1)

        s.append("List of residents \n")
        for (i,v) in enumerate(self.__person_list):
            s.append(" - {} - {} \n".format(i,v))

        return ''.join(s)

    def __del__(self):
        print(len(self.__person_list))
        print("The city {} was deleted from agglomeration".format(self._name))
