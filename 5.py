my_list = ["Burhan", "Farhan", "Furqan","Faizan", "khansahab"]
target_name = "Faizan"
for name in my_list:
    if name == target_name: 
        print("Found:", name)
        break
else:
   print("Not Found:", name)