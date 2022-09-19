global app_version,sub_version
app_version=[0,0,0]
sub_version=5
global game_name, version
game_name="OpenLife"
version="Alpha 1"
def age_up():
    global age
    age+=1
    if age <= 5:
        infant()
    else:
        end()
def pbar(percent):
	if percent > 1:
		percent=1
	percent*=100
	bar="["
	hash=percent/5
	hash=int(hash)
	dot=20-hash
	for i in range(hash):
		bar+="#"
	for i in range(dot):
		bar+="."
	bar+="]"
	print(bar)
def div():
    print("===============")
    return True
def br():
    print("Press ENTER to continue")
    wer=input()
    return True
def end():
    print("This is the end of the demo.")
    print("[1] Exit")
    print("[0] Main menu")
    try:
        ch=int(input(">>"))
    except:
        ch=1
    if ch == 1:
        exit()
    else:
        mainmenu()
def demo():
    print("John Smith")
    div()
    print("Happiness:")
    pbar(happiness)
def infant():
    global happiness, health, intel, looks, ethics
    if age > 5:
        child()
    else:
        div()
        print(forename+" "+surname)
        print("Age:",age)
        div()
        print("Happiness:")
        pbar(happiness)
        print("Health:")
        pbar(health)
        print("Smarts:")
        pbar(intel)
        print("Looks:")
        pbar(looks)
        div()
        print("[1] Occupation")
        print("[2] Assets")
        print("[0] Age Up")
        print("[3] Relationships")
        print("[4] Activities")
        try:
            ch=int(input(">"))
        except:
            ch=999
        if ch == 1:
            print("locked.")
        elif ch == 2:
            print("Locked.")
        elif ch == 0:
            age_up()
        elif ch == 3:
            print("Locked.")
        elif ch == 4:
            print("Locked.")
            div()
        infant()
def infant_start():
    global happiness, health, intel, looks, ethics, game_name
    div()
    print("Welcome to",game_name+".")
    print("You will start a new, randomised life as a toddler.")
    print("Changes you make will affect your stats and change your life.")
    print("Since life is [literally] a game, you should try to win it.")
    print("'Winning' can be defined as reaching your life goal.")
    print("That goal can be anything")
    print("\nPress ENTER to continue.")
    global age
    age=0
    wer=input()
    infant()
def life_creator():
    from random import randint
    print("[1] Randomised Life")
    print("[2] Custom Life [Non-Working]")
    try:
        ch=int(input(">"))
    except:
        ch=1
    if ch == 1:
        global forename, surname
        forename=input("Forename >>")
        if forename == "":
            forename="John"
        surname=input("Surname >>")
        if surname == "":
            surname="Smith"
        forename=forename.replace("|","")
        surname=surname.replace("|","")
        global happiness, health, intel, looks, ethics
        happiness=randint(1,100)
        happiness/=100
        health=randint(1,100)
        health/=100
        intel=randint(1,100)
        intel/=100
        looks=randint(1,100)
        looks/=100
        ethics=randint(90,100)
        ethics/=100
        try:
            start_age=int(input("Enter START AGE >"))
            if start_age != 0:
                start_age=0
                print("Start age overriden to",start_age)
        except:
            start_age=0
        infant_start()
    elif ch == 2:
        print("[1] Maxxed-out Values")
        print("[2] 0% Everything")
        print("[x] Custom Values")
        wer=input(">")
        #name=input("Name >>")
        forename=input("Forename >>")
        surname=input("Surname >>")
        forename=forename.replace("|","")
        surname=surname.replace("|","")
        happiness=randint(1,100)
        happiness/=100
        health=randint(1,100)
        health/=100
        intel=randint(1,100)
        intel/=100
        ethics=randint(90,100)
        ethics/=100
        print("The demo is over.")
        end()
    else:
        print("Custom lives not in pre-alpha")
        end()
            
def mainmenu():
    import os
    startpoint=os.getcwd()
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
    print("Version:",version)
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
        print(game_name,"is an attempt at a FULL reimplementation of BitLife.")
        print("BitLife is a life simulator released on mobile platforms.")
        print("The app suffers from:")
        print("- lazy development")
        print("- obvious cash grabs")
        print("- updates/achievements/features locked behind a paywall")
        print("- no PC release")
        print("We aim to rectify that.")
        print("\nWe will make a version of BitLife that:")
        print("- Has more features")
        print("- Is 100% FOSS")
        print("- Has NO paywalls")
        print("- Is multi-platform [since it's in Python]")
        print("- Has no compatibility/performance issues with older devices [since BitLife does not run on Arm32]\n")
        
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
