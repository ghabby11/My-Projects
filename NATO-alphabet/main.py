student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass
import turtle
import pandas
student_data_frame = pandas.DataFrame(student_dict)
file = pandas.read_csv("nato_phonetic_alphabet.csv")

screen = turtle.Screen()

screen.title("NATO ALPHABETS")
image = "phonetic-alphabet1.gif"
screen.addshape(image)
turtle.shape(image)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
NATO = {word.letter:word.code for (index,word) in file.iterrows()}
# print(NATO)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate():
    user_input = input("Type a word: ").upper()
    try:
        words = [NATO[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate()
    else:
        print(words)

generate()

screen.exitonclick()