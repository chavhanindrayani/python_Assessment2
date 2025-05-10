# Ask the player to enter their name
player_name = input("Enter your name: ")

# i) Print the length of the name
print(f"Length of your name: {len(player_name)}")

# ii) Convert to uppercase and lowercase
print(f"Uppercase: {player_name.upper()}")
print(f"Lowercase: {player_name.lower()}")

# iii) Check if the name starts with a certain letter
letter = input("Enter a letter to check if your name starts with it: ")
if player_name.startswith(letter):
    print(f"Yes, your name starts with '{letter}'.")
else:
    print(f"No, your name does not start with '{letter}'.")

# iv) Reverse the name and print it
reversed_name = player_name[::-1]
print(f"Your name reversed: {reversed_name}")