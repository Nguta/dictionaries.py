car = {
    "brand": "Mercedes",
    "model": "G-wagon",
    "year" : 2021
}
x = car ["model"]
print (x)
x = car.keys()
print (x)
x = car.values()
print(x)
if "model" in car:
    print ("Yes, 'model'lets gooo")
car["model"] = 2020
print (car)
car["color"]= "violet"
print(car)
car.pop("model")
#car.popitem()
#del car ["model"]
car.clear()
for x in car:
    print(x)
for x in car.values():
    print(x)
#nested dictionaries
child1 = {
    "name" : "Kimie",
    "year" : "1996"
}
child2 = {
    "name" : "Johari",
    "year" : "1997"
}
child3 = {
    "name" : "Nguta",
    "year" : "1999"
}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3,
}
