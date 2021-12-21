# raka = ["Raka Ardhi", 28, "CurDev", 2265]
# spock = ["Spock", 35, "Science Officer", 2254]
# mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

# print("Daftar Nama   : ", raka[0], spock[0], mccoy[0])
# print("Daftar Umur   : ", raka[1], spock[1], mccoy[1])
# print("Daftar Jabatan: ", raka[2], spock[2], mccoy[2])
# print("Daftar NIK    : ", raka[3], spock[3])

# class Dog:
#     # Class attribute
#     species = "Canis familiaris"

#     def __init__(sen, name, age, breed):
#         sen.name = name
#         sen.age = age
#         sen.breed = breed

#     # Instance method
#     def description(sen):
#         return f"{sen.name} is {sen.age} years old"

#     # Another instance method
#     def speak(sen, sound):
#         return f"{sen.name} says {sound}"


# # dog_1 = Dog("Buddy", 9)
# # dog_2 = Dog("Miles", 4)
# # dog_3 = Dog("Scooby doo", 8)

# # print(dog_1.name, dog_1.age, dog_1.species)
# # print(dog_2.name, dog_2.age, dog_2.species)
# # print(dog_3.name, dog_3.age, dog_3.species)

# # miles = Dog("Miles", 4,)

# # print(miles.description())
# # print(miles.speak("Woof Woof"))

# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")

# print(jim.speak("Woof"))
# print(jim.description())

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
       

    def __repr__(self):
        return f"Dog(Name={self.name} ,Age={self.age}, breed={self.breed})"

    def __str__(self):
        return f"{self.name} is {self.age} years olds"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class JackRussellTerrier(Dog):
    # pass
    def speak(self, sound):
        return f"{self.name} says {sound}"


class Dachshund(Dog):
    def speak(self):
        return f"{self.name} says Yap yap"


class Bulldog(Dog):
    def __init__(self, name, age, breed, lbs):
        super().__init__(name, age, breed,)
        self.lbs = lbs
        
    def speak(self):
        return f"{self.name} says Woof woof"
    
    def __add__(self, other):
        return self.lbs + other.lbs


# miles = JackRussellTerrier("Miles", 4)
# buddy = Dachshund("Buddy", 9)
# jack = Bulldog("Jack", 3)
# jim = Bulldog("Jim", 5)


# miles = JackRussellTerrier("Miles", 4, "Jack Russell Terrier")
# buddy = Dachshund("Buddy", 9, "Dachshund")
# jack = Bulldog("Jack", 3, "Bulldog")
# jim = Bulldog("Jim", 5, "Bulldog")

# print(jim.speak())
# print(miles.speak("arf"))
# print(buddy.speak())

# print(repr(jim))


scobby = Bulldog('Scooby', 2, 'Bulldog', 15)
scobby_jr = Bulldog('Scooby JR', 1, 'Bulldog', 8)
print(scobby.lbs)
print(scobby.name)
print(scobby_jr.lbs)