import pandas as pd

PATH1 = "C:\\Users\\acer\\Desktop\\CHANDIGARH UNIVERSITY\\AI ML\\python\\day26\\nato_phonetic_alphabet.csv"

df = pd.read_csv(PATH1)

data_dict = {row.letter : row.code for (index, row) in df.iterrows()}
# print(data_dict)

word = input("Enter the name").upper()

output_list = [data_dict[letter] for letter in word]
print(output_list)