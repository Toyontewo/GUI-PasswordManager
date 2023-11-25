#
# fruits = ["Apple", "Pear", "Orange"]
#
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)
#
#
# facebook_posts =[
#     {'Likes': 21, "comments": 2},
#     {"Likes": 13, "Comments": 2, "Shares": 1},
#     {"Likes": 33, "Comments": 8, "Shares": 3},
#     {"Comments": 4, "Shares": 2},
#     {"Comments": 1, "Shares": 1},
#     {"Likes": 19, "Comments": 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post["Likes"]
#     except KeyError:
#         pass
#
# print(total_likes)

import pandas

data = pandas.read_csv("../../6/Day 26 - List Comprehension/NATO-alphabet-start/nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Creeate a list of the phonetic code words from a word that the user inputs.
def gen_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print(f"Sorry, {word} contains integers")
        gen_phonetic()
    else:
        print(output_list)

gen_phonetic()
