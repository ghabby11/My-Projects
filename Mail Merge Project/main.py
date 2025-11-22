PLACEHOLDER = "[name]"
#TODO: Create a letter using starting_letter.txt




#for each name in invited_names.txt
with open ("Input/Names/invited_names.txt") as names:
    name = names.readlines()

with open ("Input/Letters/starting_letter.txt") as letter:
    new_letter = letter.read()
    print(new_letter)
    for nam in name:
        stripped_name = nam.strip()
        let = new_letter.replace(PLACEHOLDER,stripped_name)
        with open(f"Output/ReadyToSend/Letter for {nam}.docx", "w") as file:
            final = file.write(let)







#Replace the [name] placeholder with the actual name.


#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp