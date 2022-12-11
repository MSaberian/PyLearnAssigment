import gtts
import os.path

def read_from_file():
    global words_bank

    fname = 'translate.txt'
    if os.path.isfile(fname):
        f = open(fname,'r')
    else:
        print('🈹 database is not find!!')
        exit(0)

    temp = f.read().split('\n')

    words_bank = []
    for i in range(0, len(temp)-1, 2):
        my_dict = {'en': temp[i], 'fa': temp[i+1]}
        words_bank.append(my_dict)
    
    f.close()

def traslate_english_to_persian():
    user_text = input('enter your english text: ')

    user_words = user_text.split(" ")

    output = ""

    for user_word in user_words:
        dot = ' '
        if user_word[-1] == '.':
            user_word = user_word[:-1]
            dot = '. '
        for word in words_bank:
            if user_word == word['en']:
                output = output + word['fa'] + dot
                break
        else:
            output = output + user_word + dot

    print(output)
    gtts.gTTS(output, lang='ar', slow=False).save('voice\_fa_' + output + '.mp3')

def traslate_persian_to_english():
    user_text = input('enter your persian text: ')

    user_words = user_text.split(" ")

    output = ""

    for user_word in user_words:
        dot = ' '
        if user_word[-1] == '.':
            user_word = user_word[:-1]
            dot = '. '
        for word in words_bank:
            if user_word == word['fa']:
                output = output + word['en'] + dot 
                break
        else:
            output = output + user_word + dot

    print(output)
    gtts.gTTS(output, lang='en', slow=False).save('voice\en_' + output + '.mp3')

def add_new_word():
    new_word_en = input('enter english word: ')
    new_word_fa = input('enter persian word: ')
    my_dict = {'en': new_word_en, 'fa': new_word_fa}
    words_bank.append(my_dict)

def write_to_traslate():
    open('translate.txt', 'w').close()
    file_object = open('translate.txt', 'a')
    for word in words_bank:
        file_object.write(word['en'] + "\n" + word['fa'] + "\n")
    file_object.close()

def show_menu():
    print('1- translate english to persian')
    print('2- translate persian to english')
    print('3- add a new word to database')
    print('4- exit')

read_from_file()

print('welcome to MoSa traslate')

while True:
    show_menu()
    choice = int(input('enter your choice: '))

    if choice == 1:
        traslate_english_to_persian()
    elif choice == 2:
        traslate_persian_to_english()
    elif choice == 3:
        add_new_word()
    elif choice == 4:
        write_to_traslate()
        exit(0)
