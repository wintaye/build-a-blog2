
from helpers import alphabet_position, rotate_character
    
def encrypt(message, code_word):
    alpha_dict = {0: ('A', 'a'), 1: ('B', 'b'), 2: ('C', 'c'), 3: ('D', 'd'), 4: ('E', 'e'), 5: ('F', 'f'), 6: ('G','g'), 7: ('H', 'h'), 8: ('I', 'i'), 9: ('J', 'j'), 10: ('K', 'k'), 11: ('L', 'l'), 12: ('M', 'm'), 13: ('N', 'n'), 14: ('O', 'o'), 15: ('P', 'p'), 16: ('Q', 'q'), 17: ('R', 'r'), 18: ('S', 's'), 19: ('T', 't'), 20: ('U', 'u'), 21: ('V', 'v'), 22: ('W', 'w'), 23: ('X', 'x'), 24: ('Y', 'y'), 25: ('Z', 'z')}
    item_and_eve = list(alpha_dict.items())
    new_text = list(message)
    list_of_keys = alpha_dict.keys()
    #1st: create a list of keys based on the code_word
    code_word = list(code_word)
    empty_code_lst = []
    for char in code_word:
        key_returned = (alphabet_position(char))
        key_returned = int(key_returned)
        empty_code_lst.append(key_returned)
    lst_of_new_keys = empty_code_lst
    #2nd: create a list of keys based on the message
      empty_message_lst = []
    for item in new_text:
        message_keys = (alphabet_position(item))
        message_keys = int(key_returned)
        empty_message_lst.append(message_keys)
    lst_of_message_keys = empty_message_lst
    #3rd: rotate message key list by code word keys list
    encrypted = ""
    index = 0
    for i in lst_of_message_keys:
        rotation = lst_of_new_keys[index]
        rot = alphabet_position(i)
        rot = rot + rotation
        new_encrypted = rotate_character(char, rot)
        new_encrypted = str(new_encrypted)
        index = index + 1
        encrypted += new_encrypted
        if index == len(lst_of_new_keys):
            index = 0
    return encrypted

def main():
    alpha_dict = {0: ('A', 'a'), 1: ('B', 'b'), 2: ('C', 'c'), 3: ('D', 'd'), 4: ('E', 'e'), 5: ('F', 'f'), 6: ('G','g'), 7: ('H', 'h'), 8: ('I', 'i'), 9: ('J', 'j'), 10: ('K', 'k'), 11: ('L', 'l'), 12: ('M', 'm'), 13: ('N', 'n'), 14: ('O', 'o'), 15: ('P', 'p'), 16: ('Q', 'q'), 17: ('R', 'r'), 18: ('S', 's'), 19: ('T', 't'), 20: ('U', 'u'), 21: ('V', 'v'), 22: ('W', 'w'), 23: ('X', 'x'), 24: ('Y', 'y'), 25: ('Z', 'z')}
    item_and_eve = list(alpha_dict.items())

    message = input("What's the message we must keep safe?")
    code_word = input("Okay, so what's the super secret code word?")
    encrypt(message, code_word) 

main()