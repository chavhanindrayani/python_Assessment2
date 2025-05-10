# Sample tuple with mixed values
my_tuple = ("apple", 42, "banana", 42, "apple", 3.14, "cherry")

# i) Count how many times a specific element appears
element_to_count = "apple"
count = my_tuple.count(element_to_count)
print(f"'{element_to_count}' appears {count} time(s) in the tuple.")

# ii) Check if a particular value exists
value_to_check = 3.14
if value_to_check in my_tuple:
    print(f"{value_to_check} exists in the tuple.")
else:
    print(f"{value_to_check} does not exist in the tuple.")

# iii) Extract a slice of the tuple from index 1 to 4 (not including 4)
slice_of_tuple = my_tuple[1:4]
print(f"Slice from index 1 to 4: {slice_of_tuple}")

# iv) Convert to list, add new value, then convert back to tuple
temp_list = list(my_tuple)
temp_list.append("new_item")
new_tuple = tuple(temp_list)
print(f"New tuple after adding an item: {new_tuple}")