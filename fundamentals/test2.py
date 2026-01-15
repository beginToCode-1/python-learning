#dictionary
my_self_dictionary = {
    "name": "Burhan",
    "age": 21,
}
print(my_self_dictionary.get("name"))

#adding new key-value pairs
my_self_dictionary["Status"] = "Student"
my_self_dictionary["city"] = "Islamabad"

#updating age
print(my_self_dictionary.update({"age": 22}))

#updated dictionary values only
print(my_self_dictionary.values())
