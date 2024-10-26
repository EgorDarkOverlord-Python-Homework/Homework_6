
from city.person import Person
from city.city import  City
from city.city_list import CityList


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    p = Person('a', 'b', 'c')

    c1 = City("City1", 10)
    c2 = City("City2", 50)

    c3 = CityList("City_with_named_persons", 15)
    
    for i in range(30):
        s = str(i)
        c3.add_person(Person(s,s+s, s+s+s))
        #c3.add_person()

    print(c3)

    for i in range(2,15,2):
        c3.remove_person(i)

    print(c3)

    for i in range(2):
        c3.add_person_generate()

    print(c3)

    c3.add_family_generate()

    print(c3)

    