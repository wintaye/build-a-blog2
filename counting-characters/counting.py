def counting_characters(phrase):
    char_list = ""
    accum = 0
    characters_welcome = []
    for i in range(len(phrase)):
        val = phrase[accum]
        if val not in char_list:
            count_choc = phrase.count(val)
            char_list.append(val)
            # characters_welcome.append({val:count_choc})
            accum += 1
            print(val, '\t', count_choc)     

phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."



    