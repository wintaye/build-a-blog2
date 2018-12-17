alpha_dict = {0: ('A', 'a'), 1: ('B', 'b'), 2: ('C', 'c'), 3: ('D', 'd'), 4: ('E', 'e'), 5: ('F', 'f'), 6: ('G','g'), 7: ('H', 'h'), 8: ('I', 'i'), 9: ('J', 'j'), 10: ('K', 'k'), 11: ('L', 'l'), 12: ('M', 'm'), 13: ('N', 'n'), 14: ('O', 'o'), 15: ('P', 'p'), 16: ('Q', 'q'), 17: ('R', 'r'), 18: ('S', 's'), 19: ('T', 't'), 20: ('U', 'u'), 21: ('V', 'v'), 22: ('W', 'w'), 23: ('X', 'x'), 24: ('Y', 'y'), 25: ('Z', 'z')}
item_and_eve = list(alpha_dict.items())

def alphabet_position(letter):
    item_and_eve = list(alpha_dict.items()) 
    for item in item_and_eve: 
        if item[1][0] == letter or item[1][1] == letter: 
            value = item[0]
            value = int(value)
            return value 
def rotate_character(char, rot):
    if char.isalpha() == True:
        #checks for alpha
        orig_key = alphabet_position(char)
        print(orig_key)
        #runs our first function, returns key\
        new_key = orig_key + int(rot)
        print(new_key)
        #rotates letter, assigns new key 
        for item in item_and_eve:
            if char == item[1][0]: 
        #executes if letter is capitalized
                if new_key > 25:
                    remains = (new_key % 25) - 1
                    new_key = remains
                    new_value = alpha_dict.get(new_key)[0]
                    return new_value
                else:
                    new_value = alpha_dict.get(new_key)[0]
                    return new_value

            if char == item[1][1]: #executes if letter is lowercase
                if new_key > 25:
                    remains = (new_key % 25) - 1
                    new_key = remains
                    new_value = alpha_dict.get(new_key)[1]
                    return new_value
                else:
                    new_value = alpha_dict.get(new_key)[1]
                    return new_value
    else: 
        return char
    
def encrypt(message, code_word):
    new_text = list(message)
    list_of_keys = alpha_dict.keys()
    #1st: create a list of keys based on the code_word
    code_word = list(code_word)
    empty_code_lst = []
    for char in code_word:
        key_returned = alphabet_position(char)
        empty_code_lst.append(key_returned)
    lst_of_new_keys = empty_code_lst
    #2nd: index code_word key list to find corresponding values
    encrypted = ""
    index = 0
    for char in code_word:
        rot = lst_of_new_keys[index]
        rot = int(rot)
        new_encrypted = rotate_character(char, rot)
        new_encrypted = str(new_encrypted)
        index = index + 1
        encrypted = encrypted + new_encrypted
    #3rd: find a way of iterating through the message with "encrypted"/the code word key list
    message = list(message)
    indexy = 0
    new_last_list = ""
    for i in message:
        #create rotating index 
        new_last = rotate_character(i, encrypted[indexy])
        #append message with new value
        new_last_list = new_last_list.append(new_last)
        if indexy == len(message):
            indexy = 0
        return new_last_list
    print(new_last_list)
    
def main():
    message = input("What's the message we must keep safe?")
    code_word = input("Okay, so what's the super secret code word?")
    encrypt(message, code_word)

main()