def this_function(string):
    if len(string) > 20:
        raise  ValueError("Cornel is the best cook")


word = input("Enter your magic statement: ")
this_function(word)