my_list = ["Burhan", "Farhan", "Furqan","Faizan", "khansahab"]
my_list.append("Rauf")
print(my_list)
target_name = "Rauf"
for name in my_list:
    if name == target_name: 
        print("Found:", name)
        break
else:
   print("Not Found:", name)
#removing an item
removed_name = "Faizan"
for name in my_list:
        if name == target_name:
            my_list.remove(removed_name)
            print("Removed:", removed_name)
            break
print("Updated List:", my_list)