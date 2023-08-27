import pandas as pd


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
#
#
# dict = {word: len(word) for word in sentence.split()}
# print(dict)
#
# dict2 = {word: l * 2 for (word, l) in dict.items()}
# print(dict2)

df = pd.read_csv("nato_phonetic_alphabet.csv")

#

# ddict = df.to_dict()
# print(ddict)

df_rows = { value.letter:value.code for (key,value) in df.iterrows()}
print(df_rows)

# print(df)
# print(df.letter)

word_typed = "kombajn"

spelling = [df_rows[letter] for letter in word_typed.upper()]

print(spelling)