person = {
    "firstName": "Sam",
    "lastName": "Lavigne",
    "age": 1002
}

print person["firstName"]

person["age"] = 5
person["hairCount"] = "not much"

for key in person:
    print key
    print person[key]
