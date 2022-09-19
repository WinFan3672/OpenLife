def end():
    print("You died.")
    print("[1] Exit")
    print("[0] Restart Game")
    ch=int(input(">>"))
    if ch == 1:
        exit()
    else:
        mainmenu()

def life_creator():
    from random import randint
    print("[1] Randomised Life")
    print("[2] Custom Life")
    ch=int(input(">"))
    if ch == 1:
        name=input("Name >>")
        name=name.replace("|","")
        happiness=randint(1,100)
        happiness/=100
        health=randint(1,100)
        health/=100
        intel=randint(1,100)
        intel/=100
        ethics=randint(90,100)
        ethics/=100
        start_age=int(input("Enter START AGE >"))
        print("That is the end of the pre-alpha")
        end()
    else:
        print("Custom lives not in pre-alpha")
        end()
            
def mainmenu():
    challenge_site="" #change this URL if the location changes / you want to add custom challenges
    logo=['________                           .____     .__   _____         ', '\\_____  \\  ______    ____    ____  |    |    |__|_/ ____\\ ____   ', ' /   |   \\ \\____ \\ _/ __ \\  /    \\ |    |    |  |\\   __\\_/ __ \\  ', '/    |    \\|  |_> >\\  ___/ |   |  \\|    |___ |  | |  |  \\  ___/  ', '\\_______  /|   __/  \\___  >|___|  /|_______ \\|__| |__|   \\___  > ', '        \\/ |__|         \\/      \\/         \\/                \\/  ', '                                                                 ']
    for l in logo:
        print(l)
    print("[1] New Life")
    print("[2] Load Life")
    print("[3] Credits")
    print("[4] Download Latest Challenge")
    print("[5] Load Challenge.zip from disk")
    print("[6] Exit")
    print("[0] About Game")
    print("All options are locked.")
    print("Press ENTER to enter the Life Creator.")
    wer=input()
    life_creator()
mainmenu()
