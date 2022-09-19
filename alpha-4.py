global app_version,sub_version
app_version=[0,0,0]
sub_version=5
global game_name, version
game_name="OpenLife"
version="Alpha 4 [Date: 19 Sep 2022]"
def choose_start():
    global age
    global start_age
    age=start_age
    global happiness, intel
    if start_age <= 5:
        infant_start()
    elif start_age >= 6 and start_age < 12:
        global mother_rel, father_rel
        mother_rel=1
        father_rel=1
        child_init()
    else:
        end()
def age_up():
    global happiness, intel
    global age
    global money, father_rel
    age+=1
    if age <= 5:
        happiness+=0.25
        intel+=0.25
        infant()
    elif age >= 6 and age < 12:
        if age == 6:
            child_init()
        else:
            if father_rel>=0.75:
                money+=520
            elif father_rel < 0.75 and father_rel > 0.25:
                money+=260
            child()
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
        while True:
            exit()
    else:
        mainmenu()
def demo():
    print("John Smith")
    div()
    print("Happiness:")
    pbar(happiness)
def child_activities():
    global happiness, health, intel, looks, ethics
    global mother_rel, father_rel
    global money
    div()
    print("Activities:")
    print("[0] Return")
    print("[1] Gym")
    print("[2] Library")
    print("[3] Doctor")
    print("[4] Surrender")
    print("[5] Debug Mode")
    try:
        ch=int(input("<"))
    except:
        ch=0
    if ch == 0:
        child()
    elif ch == 1:
        div()
        happiness+=0.35
        health+=0.25
        print("You visited the gym.")
        print("Enjoyment:")
        pbar(1)
        div()
        child()
    elif ch == 2:
        div()
        print("You visited the library.")
        print("Enjoyment:")
        pbar(0.8)
        intel+=0.25
        div()
        child()
    elif ch == 3:
        div()
        print("No doctor available.")
        div()
        child()
    elif ch == 4:
        end()
    elif ch == 5:
        div()
        print("Hidden ethics value:")
        pbar(ethics)
        div()
        print("[1] Max out Relationships")
        print("[2] Max out looks")
        print("[0] Return")
        div()
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            child()
        elif ch == 1:
            father_rel=1
            mother_rel=1
        elif ch == 2:
            looks=1
        else:
            child()
        child()
def primary_school_menu():
    div()
    print("[0] Return")
    print("[1] Primary School")
    print("Stress:")
    pbar(0.45)
    div()
    try:
        ch=int(input(">"))
    except:
        ch=0
    if ch == 0:
        div()
        child()
    elif ch == 1:
        div()
        print("Unavailable right now.")
        div()
        child()
    else:
        div()
        child()
def child():
    global happiness, health, intel, looks, ethics
    if happiness > 1:
        happiness =1
    if happiness < 0:
        happiness=0
    if health > 1:
        health=1
    if health < 0:
        health=0
    if intel > 1:
        intel=1
    if looks > 1:
        looks=1
    if intel < 0:
        intel=0
    if looks < 0:
        looks=0
    global forename, surname
    global mother_rel, father_rel
    global money
    print(forename+" "+surname)
    print("Primary School Student")
    print("Age",age)
    print("£"+str(money))
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
    print("[1] School")
    print("[2] Assets")
    print("[0] Age Up")
    print("[3] Relationships")
    print("[4] Activities")
    try:
        ch=int(input(">"))
    except:
        child()
    if ch == 1:
        primary_school_menu()
    elif ch == 2:
        div()
        print("Locked.")
        div()
    elif ch == 0:
        age_up()
    elif ch == 3:
        div()
        print("Mother [Age "+str(age+32)+"]")
        pbar(mother_rel)
        print("[1] Interact")
        div()
        print("Father [Age "+str(age+37)+"]")
        pbar(father_rel)
        print("[2] Interact")
        div()
        print("[0] Return")
        div()
        try:
            ch=int(input(">>"))
        except:
            child()
        if ch == 1:
            print("Mother [Age "+str(age+32)+"]")
            pbar(mother_rel)
            print("[0] Return")
            print("[1] Spend Time")
            print("[2] Disrespect")
            print("[3] Attack")
            try:
                ch=int(input(">>"))
            except:
                ch=0
            div()
            if ch == 0:
                child()
            elif ch ==1:
                div()
                print("You spent time with your mother.")
                mother_rel+=0.25
                if mother_rel > 1:
                    mother_rel=1
                pbar(mother_rel)
                div()
                child()
            elif ch == 2:
                print("You disrespected your mother.")
                mother_rel-=0.25
                happiness-=0.35
                if mother_rel < 0:
                    mother_rel=0
                if happiness < 0:
                    happiness=0
                pbar(mother_rel)
                div()
                child()
            elif ch == 3:
                print("You hit your mother.")
                print("Damage:")
                pbar(0.65)
                div()
                mother_rel-=0.55
                happiness-=0.75
                if mother_rel < 0:
                    mother_rel=0
                if happiness < 0:
                    happiness=0
                pbar(mother_rel)
                div()
                child()
        
        elif ch == 2:
            div()
            print("Locked.")
            div()
            child()
        elif ch == 0:
            child()
    elif ch ==4:
        child_activities()
    child()
def child_init():
    global mother_rel, father_rel
    print("You are now a child. You have more activities to do and can also use money.")
    print("Once you hit 12, you'll be a teen.")
    print("Hint: Don't die")
    mother_rel-=0.3
    if mother_rel < 0:
        mother_rel=0
    father_rel-=0.3
    if father_rel<=0:
        father_rel=0
    div()
    global money
    money=0
    print("You have now joined Primary School")
    div()
    wer=input("Press ENTER to continue. ")
    child()
def infant_activities():
    print("[1] Surrender")
    print("[2] Return To Menu")
    print("[0] Exit")
    try:
        ch=int(input(">"))
    except:
        ch=0
    if ch == 0:
        infant()
    elif ch == 1:
        end()
    elif ch ==2:
        mainmenu()
def infant():
    global happiness, health, intel, looks, ethics
    global mother_rel, father_rel
    if happiness > 1:
        happiness =1
    if happiness < 0:
        happiness=0
    if health > 1:
        health=1
    if health < 0:
        health=0
    if intel > 1:
        intel=1
    if looks > 1:
        looks=1
    if intel < 0:
        intel=0
    if looks < 0:
        looks=0
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
        print("[2] Activities")
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
        elif ch == 2:
            infant_activities()
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
    print("That goal can be anything. Getting your dream job, becoming rich,")
    print("living a fulfilling life, etc.")
    print("\nPress ENTER to continue.")
    global age
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
        global start_age
        try:
            start_age=int(input("Enter START AGE >"))
        except:
            start_age=0
        choose_start()
        try:
            start_age=int(input("Enter START AGE >"))
            choose_start()
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
