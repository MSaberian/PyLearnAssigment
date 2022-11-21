last_char_isnot_alnum = True
number_word = 0
sentence = input("Please enter a sentence: ")

for i in range(len(sentence)):
    if sentence[i].isalnum():
        if (last_char_isnot_alnum):
            number_word += 1
        last_char_isnot_alnum = False
    else:
        last_char_isnot_alnum = True

print("number word is: ", str(number_word))