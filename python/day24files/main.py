PATH1 = "C:\\Users\\acer\\Desktop\\CHANDIGARH UNIVERSITY\\AI ML\\python\\day24files\\invited_names.txt"

PATH2 = "C:\\Users\\acer\\Desktop\\CHANDIGARH UNIVERSITY\\AI ML\\python\\day24files\\starting_letter.txt"

PLACEHOLDER = "[name]"

# mode w = erases all the previous content in the file then add the new content 

# mode a = appends the new content in the file 

# with open(PATH, mode='a') as file:
#     file.write("\nNEW text")

# if file doesn't exists then it creates the new file 

# with open(PATH, mode='w') as file:
#     file.write("hello")

with open(PATH1) as names_file:
    names = names_file.readlines()
    print(names)

with open(PATH2) as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"C:\\Users\\acer\\Desktop\\CHANDIGARH UNIVERSITY\\AI ML\\python\\day24files\\letter_for_{stripped_name}.txt", mode='w') as completed_letter:
            completed_letter.write(new_letter)
        

