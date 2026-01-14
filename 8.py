#dictionaries
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red"
}
print("Keys::",car.keys())
print("Values::",car.values())
print("items with keys::",car.items())
print(car.update({"color" : "silver gray"}))
print(car)
print(car.get("brand"))