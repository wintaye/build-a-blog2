alpha_dict = {0: ('A', 'a'), 1: ('B', 'b'), 2: ('C', 'c'), 3: ('D', 'd'), 4: ('E', 'e'), 5: ('F', 'f'), 6: ('G','g'), 7: ('H', 'h'), 8: ('I', 'i'), 9: ('J', 'j'), 10: ('K', 'k'), 11: ('L', 'l'), 12: ('M', 'm'), 13: ('N', 'n'), 14: ('O', 'o'), 15: ('P', 'p'), 16: ('Q', 'q'), 17: ('R', 'r'), 18: ('S', 's'), 19: ('T', 't'), 20: ('U', 'u'), 21: ('V', 'v'), 22: ('W', 'w'), 23: ('X', 'x'), 24: ('Y', 'y'), 25: ('Z', 'z')}
item_and_eve = list(alpha_dict.items())

def alphabet_position(letter):
    alpha_dict = {0: ('A', 'a'), 1: ('B', 'b'), 2: ('C', 'c'), 3: ('D', 'd'), 4: ('E', 'e'), 5: ('F', 'f'), 6: ('G','g'), 7: ('H', 'h'), 8: ('I', 'i'), 9: ('J', 'j'), 10: ('K', 'k'), 11: ('L', 'l'), 12: ('M', 'm'), 13: ('N', 'n'), 14: ('O', 'o'), 15: ('P', 'p'), 16: ('Q', 'q'), 17: ('R', 'r'), 18: ('S', 's'), 19: ('T', 't'), 20: ('U', 'u'), 21: ('V', 'v'), 22: ('W', 'w'), 23: ('X', 'x'), 24: ('Y', 'y'), 25: ('Z', 'z')}
    item_and_eve = list(alpha_dict.items())
    for item in item_and_eve: 
        if item[1][0] == letter or item[1][1] == letter: 
            value = item[0]
            return value 
def rotate_character(char, rot):
    alpha_dict = {0: ('A', 'a'), 1: ('B', 'b'), 2: ('C', 'c'), 3: ('D', 'd'), 4: ('E', 'e'), 5: ('F', 'f'), 6: ('G','g'), 7: ('H', 'h'), 8: ('I', 'i'), 9: ('J', 'j'), 10: ('K', 'k'), 11: ('L', 'l'), 12: ('M', 'm'), 13: ('N', 'n'), 14: ('O', 'o'), 15: ('P', 'p'), 16: ('Q', 'q'), 17: ('R', 'r'), 18: ('S', 's'), 19: ('T', 't'), 20: ('U', 'u'), 21: ('V', 'v'), 22: ('W', 'w'), 23: ('X', 'x'), 24: ('Y', 'y'), 25: ('Z', 'z')}
    item_and_eve = list(alpha_dict.items())
    #print(type(rot))
    if char.isalpha() == True:
        #checks for alpha
        letter = char
        orig_key = alphabet_position(letter)
        #runs our first function, returns key
        new_key = rot + orig_key #rotates letter, assigns new key 
        for item in item_and_eve:
            if char == item[1][0]: 
        #executes if letter is capitalized
                if orig_key > 25:
                    remains = (orig_key % 25) -1
                    new_key = remains
                    new_value = alpha_dict.get(orig_key)[0]
                    return new_value
                else:
                    new_value = alpha_dict.get(orig_key)[0]
                    return new_value
            if char == item[1][1]: #executes if letter is lowercase
                if orig_key > 25:
                    remains = (orig_key % 25) - 1
                    new_key = remains
                    new_value = alpha_dict.get(orig_key)[1]
                    return new_value
                else:
                    new_value = alpha_dict.get(orig_key)[1]
                    return new_value
        
    else: 
        return char