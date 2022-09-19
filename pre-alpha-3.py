def div():
    print("===============")
    return True
def br():
    print("Press ENTER to continue")
    wer=input()
    return True
def end():
    print("You died.")
    print("[1] Exit")
    print("[0] Restart Game")
    try:
        ch=int(input(">>"))
    except:
        ch=1
    if ch == 1:
        exit()
    else:
        mainmenu()

def life_creator():
    from random import randint
    print("[1] Randomised Life")
    print("[x] Custom Life")
    try:
        ch=int(input(">"))
    except:
        ch=1
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
        try:
            start_age=int(input("Enter START AGE >"))
        except:
            start_age=0
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
    div()
    print("[1] New Life")
    print("[x] Load Life")
    print("[3] Credits")
    print("[x] Download Latest Challenge")
    print("[x] Load Challenge.zip from disk")
    print("[6] Exit")
    print("[0] About Game")
    div()
    print("Version: Pre-Alpha 3")
    div()
    try:
        ch=int(input(">>"))
    except:
        ch=1
    if ch == 1:
        life_creator()
    elif ch == 6:
        exit()
    elif ch == 0:
        div()
        print("OpenLife is an attempt at a FULL reimplementation of BitLife.")
        print("BitLife is a life simulator released on mobile platforms.")
        print("The app suffers from:")
        print("- lazy development")
        print("- obvious cash grabs")
        print("- updates/achievements/features locked behind a paywall")
        print("- no PC release")
        print("We aim to rectify that.")
        br()
        div()
        mainmenu()
    elif ch == 3:
        div()
        print("Created By: WinFan3672")
        print("Logo by: Textkool.com")
        div()
        mainmenu()
    else:
        div()
        print("That option is not available in the current build of the game")
        div()
        mainmenu()
mainmenu()
