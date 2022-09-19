global app_version,sub_version
app_version=[0,0,0]
sub_version=5
global game_name, version
game_name="OpenLife"
version="Alpha 2"
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
    global mother_rel, father_rel
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
        print("[0] Age Up")
        print("[1] Relationships")
        try:
            ch=int(input(">"))
        except:
            ch=999
        if ch == 0:
            age_up()
        elif ch == 1:
            print("Mother [Age",str(age+32)+"]")
            pbar(mother_rel)
            print("[1] Interact with")
            div()
            print("Father [Age",str(age+37)+"]")
            pbar(father_rel)
            print("[x] Interact with")
            div()
            print("[0] Return to menu")
            div()
            try:
                ch=int(input(">"))
            except:
                ch==0
            if ch == 0:
                infant()
            elif ch == 1:
                print("Mother [Age ",str(age+32)+"]")
                pbar(mother_rel)
                print("[0] Leave")
                print("[1] Spend Time With")
                print("[2] Disobey")
                print("[3] Attack")
                try:
                    ch=int(input(">"))
                except:
                    ch=0
                if ch == 0:
                    infant()
                elif ch == 1:
                    mother_rel+=0.25
                    if mother_rel > 1:
                        mother_rel=1
                    print("You spent time with your mother.")
                    pbar(mother_rel)
                elif ch == 2:
                    print("You disobeyed your mother.")
                    mother_rel-=0.35
                    happiness-=0.35
                    if happiness < 0:
                        happiness=0
                    if mother_rel < 0:
                        mother_rel=0
                    pbar(mother_rel)
                elif ch == 3:
                    print("You hit your mother!")
                    print("Damage:")
                    pbar(0.15)
                    mother_rel-=0.35
                    if mother_rel < 0:
                        mother_rel=0
                    print("Relationship:")
                    pbar(mother_rel)
                else:
                    infant()
            else:
                infant()
        else:
            div()
            print("Locked.")
            infant()
            div()
        infant()
def infant_start():
    global happiness, health, intel, looks, ethics, game_name
    div()
    global mother_rel, father_rel
    mother_rel=1
    father_rel=1
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
    global happiness, health, intel, looks, ethics
    from random import randint
    print("[1] Randomised Life")
    print("[2] Custom Life [Broken]")
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
        happiness=randint(1,100)
        happiness/=100
        health=randint(1,100)
        health/=100
        intel=randint(1,100)
        intel/=100
        looks=randint(1,100)
        looks/=100
        ethics=1
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
        try:
            wer=int(input(">>"))
        except:
            wer=1
        #name=input("Name >>")
        forename=input("Forename >>")
        if forename == "":
            forename="John"
        surname=input("Surname >>")
        if surname == "":
            surname="Smith"
        forename=forename.replace("|","")
        surname=surname.replace("|","")
        from random import randint
        if wer == 1:
            happiness=randint(1,1)
            health=randint(1,1)
            intel=randint(1,1)
            looks=randint(1,1)
            ethics=1
        elif wer == 2:
            happiness=0
            health=0
            intel=0
            looks=0
            ethics=0
        elif wer == 3:
            from random import randint
            print("Enter the percent amount of each value.")
            try:
                happiness=int(input("Happiness $"))
            except:
                happiness=randint(1,100)
            happiness/=100
            try:
                intel=int(input("Intelligence $"))
            except:
                intel=randint(1,100)
            intel/=100
            try:
                health=int(input("Health $"))
            except:
                health=randint(1,100)
            health/=100
        else:
            mainmenu()
        infant_start()
    else:
        print("An error occured.")
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
