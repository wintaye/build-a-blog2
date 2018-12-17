def get_initials(fullname):
    #initials, uppercase
    accum = 0
    new_string = ""
    words = fullname.split(" ")
    for i in words:
        first_letter = (words[accum][0])   
        first_letter = first_letter.capitalize()
        new_string = new_string+first_letter
        accum = accum + 1
    return new_string
def main():
    x = get_initials(fullname)
    print("The initials of '"+fullname+"' are "+x+".")
    
if __name__=="__main__":
    main()



    
    
