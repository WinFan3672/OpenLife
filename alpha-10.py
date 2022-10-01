def loop():
    global game_name
    i=0
    try:
        while True:
            i+=1
            print(game_name,"Anticheat! #"+str(i))
    except:
        loop()
try:
    global forename_m, forename_f
    #Taken from https://github.com/MustafaKermitsSuicide/BitLife
    forename_m = ["Oliver", "Jacob", "Mason", "Harry", "William", "Alfie",
                        "Jayden", "Charlie", "Noah", "Thomas", "Michael",
                        "Ethan", "Joshua", "Alexander", "George", "Aiden", "James",
                        "Daniel", "Jack", "Bruno", "Donald", "Nick", "Harvey",
                        "Alfie", "Archie", "Ollie", "Louie", "Jenson",
                        "Lewis", "Louis", "Callum", "Freddie", "Theo", "Toby",
                        "Harley", "Reuben", "Kian", "Bobby", "Stanley"]
    forename_f = ["Olivia", "Sophie", "Isabella", "Emily", "Emma", "Lily",
                          "Amelia", "Ava", "Jessica", "Ruby", "Abigail",
                          "Chloe", "Madison", "Grace", "Mia", "Evie", "Laura",
                          "Maisie", "Poppy", "Freya", "Imogen", "Florence", "Rosie",
                          "Hollie", "Isobel", "Niamh", "Harriet", "Tilly", "Maisy",
                          "Holly", "Matilda", "Amelie", "Esme", "Zara", "Tia",
                          "Aimee", "Martha", "Libby"]
    global app_version,sub_version
    app_version=[0,0,7]
    sub_version=1
    global edu_lvl
    edu_lvl=0
    
    from time import strftime
    global year
    year=strftime("%Y")
    year=int(year)
    
    global game_name, version
    global alt_ui
    global juvie_offences
    juvie_offences=0
    global is_depressed
    global degree
    is_depressed=0
    degree=0
    global club_count
    global stress
    global is_sch_gang
    is_sch_gang=0 #teen school gang
    stress=0
    global fake_id, is_drip
    fake_id=0
    is_drip=0
    club_count=0
    alt_ui=0 #set to 1 to get different UI
    game_name="OpenLife"
    version="Alpha 10 [Date: 25 Sep 2022]"
    def casino_menu():
        global money, winnings
        losses=-(winnings)
        if winnings < 0:
            print("Session Losses:",losses)
        else:
            print("Session earnings: £"+str(winnings))
        print("Money: £"+str(money))
        print("[1] Play")
        print("[0] Return")
        try:
            ch=int(input(">"))
        except:
            ch=1
        if ch == 1:
            blackjack()
        else:
            adult()
    def adult_crime():
        global mother_age
        global father_age
        global father_end_age, mother_end_age, money
        div()
        print("[0] Return")
        print("[X] Bank Robbery")
        print("[x] Burglary")
        print("[x] GTA")
        print("[4] Hitman")
        print("[x] Murder")
        print("[6] Pickpocketing")
        print("[x] Shoplifting")
        print("[x] Train Robbery")
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            adult()
        elif ch == 4:
            print("[0] Return")
            if mother_age < mother_end_age:
                print("[1] Kill Mother [£45,000]")
            if father_age < father_end_age:
                print("[2] Kill Father [£45,000]")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 0:
                adult()
            elif ch == 1 and mother_age < mother_end_age:
                if money >= 45000:
                    money-=45000
                    mother_end_age=mother_age+1
                    print("Age up for your mother to die!")
                    div()
                    br()
                    adult()
                elif money < 45000:
                    div()
                    print("Cannot afford.")
                    adult()
                else:
                    adult()
            elif ch == 2 and father_age < father_end_age:
                if money >= 45000:
                    money-=45000
                    father_end_age=father_age+1
                    print("Age up for your father to die!")
                    div()
                    br()
                    adult()
                elif money < 45000:
                    div()
                    print("Cannot afford.")
                    adult()
                else:
                    adult()
    
        elif ch == 6:
            from random import randint
            base=randint(15,30)
            print("You stole £"+str(base))
            money+=base
            adult()
        elif ch == 7:
            print("[0] Return")
            print("[x] Phone [£750]")
            print("[x] Beer")
            print("[x] Cigarettes")
            print("[x] Mars Candy Bar")
            print("[x] Handbag [£250]")
            print("[x] Wallet [£50]")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 0:
                adult()
            else:
                adult()
        elif ch == 8:
            from time import strftime
            from random import randint
            winnings=randint(150,300)
            winnings*=100000
            base=strftime("%H:%M")
            print("Choose a time [Note: This should be the real-life time.")
            print("[1] 0:00 [Midnight]")
            print("[2] 07:00 [7AM]")
            print("[3] 12:00 [12AM]")
            print("[4] 16:20 [4:20PM]")
            print("[5] 19:00 [7PM]")
            print("[6] 21:00 [9PM]")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 1:
                if base == "00:00":
                    div()
                    print("You won £"+str(winnings))
                    money+=winnings
                    div()
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 2:                
                if base == "07:00":
                    div()
                    print("You won £"+str(winnings))
                    money+=winnings
                    div()
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 3:
                if base == "12:00":
                    div()
                    print("You won £"+str(winnings))
                    money+=winnings
                    div()
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 4:
                if base == "16:20":
                    div()
                    print("You won £"+str(winnings))
                    money+=winnings
                    div()
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 5:
                if base == "19:00":
                    div()
                    print("You won £"+str(winnings))
                    money+=winnings
                    div()
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 6:
                div()
                if base == "21:00":
                    print("You won £"+str(winnings))
                    money+=winnings
                    div()
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            else:
                adult()
        else:
            #Place more options on this indent level
            adult()
            
    def uni_start():
        div()
        global uni_end_age, age
        uni_end_age=age+5
        print("You will end uni at age:",uni_end_age)
        print("You cannot go to uni yet :(")
        br()
        adult()
    def uni_check():
        global degree, money
        print("Welcome to University.")
        print("Choose a degree:")
        print("[0] Return")
        print("[1] Finance")
        print("[2] Journalism")
        print("[3] Computer Science")
        print("[4] Education")
        print("[5] Accounting")
        print("[6] Political Science")
        print("[7] Nursing")
        print("[8] Psychology")
        print("[9] Engineering")
        print("[10] Art History")
        print("[11] Commuications")
        print("[12] Graphic Design")
        print("[13] Data Science")
        print("[14] Criminal Justice")
        print("[15] Linguistics")
        print("[16] Marketing")
        div()
        print("The degree you choose influences:")
        print("[-] What job you can get")
        print("[-] What degrees you can get in grad school")
        print("[-] What schools you can get into")
        div()
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            adult()
        else:
            if intel >= 0.75:
                global degree
                degree=ch
                div()
                print("You have been selected for Uni!")
                print("Price: £25,000")
                print("[1] Buy With Cash")
                print("[2] Scholarship")
                print("[3] Ask your mother to pay")
                print("[x] Apply for a student loan")
                print("[0] Return")
                try:
                    ch=int(input(">"))
                except:
                    ch=0
                div()
                if ch == 0:
                    adult()
                elif ch == 1:
                    if money >= 25000:
                        money-=25000
                        print("You bought a university degree.")
                        uni_start()
                    else:
                        print("You cannot afford your degree.")
                        uni_check()
                elif ch == 2:
                    global club_count
                    if club_count >= 2:
                        print("You have been awarded a scholarship!")
                        uni_start()
                elif ch == 3:
                    global mother_rel
                    if mother_rel >= 0.75:
                        print("Your mother agreed to pay for your degree!")
                        uni_start()
                    else:
                        print("Your mother refused to pay for your degree.")
                        uni_check()
                else:
                    adult()
            else:
                div()
                print("You are too dumb.")
                adult()
    def blackjack_init():
        global money, winnings
        winnings=0
        casino_menu()
    def get_card():
        global number
        from random import randint
        number+=randint(1,10)
    def enemy_get_card():
        global enemy_number
        from random import randint
        enemy_number+=randint(1,10)
    def decide():
        global money, number, enemy_number, bet, winnings
        if enemy_number > 21:
            print("Enemy bust!")
            money+=bet
            winnings+=bet
            br()
            casino_menu()
        elif enemy_number > number:
            print("Enemy won")
            money-=bet
            winnings-=bet
            br()
            casino_menu()
    def enemy():
        global money, number, enemy_number
        from time import sleep
        enemy_number=0
        div()
        print("Your enemy begins.")
        #if enemy_number > number:
        #lose
        #else if enemy busts
        #win
        #else [due to error]
        #win
        enemy_get_card()
        print("Your hand:",number)
        print("Enemy hand:",enemy_number)
        div()
        while True:
            if enemy_number > number:
                break
            elif enemy_number > 21:
                break
            else:
                enemy_get_card()
                print("Your hand:",number)
                print("Enemy hand:",enemy_number)
                sleep(0.45)
                div()
        decide()
    def blackjack():
        global money, number, bet, winnings
        try:
            bet=int(input("Enter Bet >"))
        except:
            bet=money
        if bet > money:
            bet=money
        if bet <  1000:
            div()
            print("Bet set to minimum [1000]")
            div()
            bet=1000
        elif bet > 10000000:
            div()
            print("Bet set to maximum [$10 000 000]")
            div()
            bet=10000000
        else:
            div()
            print("You have",bet,"riding on this bet.")
            div()
        number=0
        get_card()
        while True:
            if number > 21:
                print("Bust!")
                winnings-=bet
                money-=bet
                casino_menu()
            print("Your Hand:",number)
            print("[1] Hit Me")
            print("[2] I'll Stand")
            try:
                ch=int(input(">"))
            except:
                ch=1
            if ch == 1:
                get_card()
            elif ch == 2:
                enemy()
    def pause():
        div()
        print("Press ENTER to continue.")
        wer=input
        return True
    def choose_start():
        global age
        from random import randint
        global start_age
        global mother_rel, father_rel
        global mother_age, father_age
        global grades, intel, money
        global mother_end_age, father_end_age
        age=start_age
        mother_age=age+32
        father_age=age+37
        base=randint(15,55)
        mother_end_age=+32+base
        base=randint(15,55)
        father_end_age=37+base
        global happiness, intel
        global stress
        if start_age <= 5:
            infant_start()
        elif start_age >= 6 and start_age < 12:
            mother_rel=1
            father_rel=1
            stress=0.5
            child_init()
        elif age >= 12 and age < 18:
            money=0
            stress=0.65
            mother_rel=0.8
            grades=intel
            father_rel=0.8
            teen_init()
        elif age >= 18:
            global did_tutor
            did_tutor=0
            global edu_lvl
            edu_lvl=1
            money=0
            stress=0
            mother_rel=0.8
            father_rel=0.8
            adult_init()
        else:
            end()
    def die_of_age():
        div()
        print("You died!")
        div()
        print(forename+" "+surname,"died of old age.")
        if age >= 123:
            print("He was",age,"years old, making him the oldest person in the world.")
        else:
            print("He was",age,"years old.")
        div()
        print("Note: In these early builds of",game_name+", your character is always male.")
        div()
        print("[1] Return To menu")
        print("[0] Exit")
        if age < 130:
            print("[2] Respawn")
        try:
            ch=int(input(">"))
        except:
            ch=1
        if ch == 1:
            mainmenu()
        elif ch == 0:
            exit()
        elif ch == 2:
            if age < 130:
                adult()
            else:
                mainmenu()
        else:
            mainmenu()
    def age_up():
        global mother_end_age, father_end_age, money
        global is_depressed, is_anxiety
        global year
        year += 1
        global happiness, intel
        global age
        global money, father_rel
        global did_tutor
        did_tutor=0
        global mother_age, father_age
        age+=1
        mother_age+=1
        father_age+=1
        #when parents die
        if mother_age == mother_end_age:
            div()
            print("Your mother died.")
            print("It is your responsibility to plan the funeral.")
            print("[0] Skip")
            print("[1] Bury [£8500]")
            print("[2] Cremate [£1500]")
            print("[3] Taxidermy [£15 000]")
            print("[4] Donate To Science [£0]")
            try:
                ch=int(input(">"))
            except:
                ch=4
            if ch == 0:
                print("You skipped the funeral.")
            elif ch == 1:
                print("Your mother was buried.")
                money-=8500
            elif ch == 2:
                money-=15000
                print("You cremated your mother.")
                print("Choose what to do with the ashes:")
                print("[1] Sprinkle somewhere special.")
                print("[2] Put in urn")
                print("[0] Throw In Trash")
                ch=input(">")
            elif ch == 3:
                print("You had your mother taxidermied.")
                money-=15000
            elif ch == 4:
                print("Your mother's body was donated to science.")
            else:
                print("You skipped the funeral.")
            from random import randint
            mother_fortune=randint(1000000,3000000)
            div()
            print("You inherited £"+str(mother_fortune))
            money+=mother_fortune
        if father_age == father_end_age:
            div()
            print("Your father died.")
            print("It is your responsibility to plan the funeral.")
            print("[0] Skip")
            print("[1] Bury [£8500]")
            print("[2] Cremate [£1500]")
            print("[3] Taxidermy [£15 000]")
            print("[4] Donate To Science [£0]")
            try:
                ch=int(input(">"))
            except:
                ch=4
            if ch == 0:
                print("You skipped the funeral.")
            elif ch == 1:
                print("Your father was buried.")
                money-=8500
            elif ch == 2:
                money-=15000
                print("You cremated your father.")
                print("Choose what to do with the ashes:")
                print("[1] Sprinkle somewhere special.")
                print("[2] Put in urn")
                print("[0] Throw In Trash")
                ch=input(">")
            elif ch == 3:
                print("You had your father taxidermied.")
                money-=15000
            elif ch == 4:
                print("Your father's body was donated to science.")
            else:
                print("You skipped the funeral.")
            from random import randint
            father_fortune=randint(1000000,3000000)
            div()
            print("You inherited £"+str(father_fortune))
            money+=father_fortune
        #redirect
        if age <= 5:
            happiness+=0.25
            if intel <= 0.75:
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
                if happiness <= 0.1 and is_depressed == 0:
                    is_depressed=1
                    div()
                    print("You are now suffering from DEPRESSION.")
                    div()
                if is_depressed==1:
                    happiness/=4
                if is_depressed == 1 and happiness >= 0.65:
                    div()
                    print("You are no longer suffering from DEPRESSION.")
                    is_depressed=0
                    happiness*=2
                    div()
                child()
        elif age >= 12 and age < 18:
            if age == 12:
                teen_init()
            else:
                if happiness <= 0.1 and is_depressed == 0:
                    is_depressed=1
                    div()
                    print("You are now suffering from DEPRESSION.")
                    div()
                if is_depressed==1:
                    if happiness < 0.65:
                        happiness/=4
                    else:
                        div()
                        print("You are no longer suffering from DEPRESSION!")
                        is_depressed=0
                teen()
        elif age >= 18:
            from random import randint
            if age == 18:
                global edu_lvl
                edu_lvl=1
                adult_init()
            elif age >= 70 and age < 80:
                dc=randint(1,400)
                if dc != 400:
                    pass
                else:
                    dieof_age()
            elif age >= 80 and age < 90:
                #print("80")
                dc=randint(1,20)
                if dc != 20:
                    pass
                else:
                    die_of_age()
            elif age >= 90:
                #print("AGE TEST")
                dc=randint(1,3)
                if dc != 3:
                    pass
                else:
                    die_of_age()
            elif age >= 100 and age < 120:
                dc=randint(1,2)
                if dc == 1:
                    die_of_age()
                else:
                    pass
            elif age >= 120:
                div()
                print("When you reach 121, you will die of old age every year.")
                div()
                die_of_age()
            else:
                adult()
        else:
            end()
    def pbar(percent):
            if percent > 1:
                    percent=1
            percent*=100
            bar="["
            hash=percent/5
            global alt_ui
            hash=int(hash)
            dot=20-hash
            for i in range(hash):
                    bar+="#"
            for i in range(dot):
                    bar+="."
            bar+="]"
            print(bar)
    def div():
        print("====================")
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
                quit()
        else:
            mainmenu()
    def demo():
        print("John Smith")
        div()
        print("Happiness:")
        pbar(happiness)
    def no_condone():
        global game_name
        div()
        print("Warning!")
        div()
        print("The developers of",game_name,"do not condone")
        print("performing any activities played out in",game_name,"in real life.")
        print("It may get you in trouble or even kill you.")
        div()
        br()
        return True
    def emergency_room(might_die):
        global health
        #you get rushed to the ER once your healh is < 0%
        #You have a 50% chance of dying

        #set might_die to 1 for a 50% death chance
        #and 0 for 100% chance of living

        from random import randint
        global health
        if might_die == 1:
            div()
            print("You were rushed to the emergency room.")
            chance=randint(1,2)
            if chance != 2:
                print("You died.")
                end()
            else:
                print("You barely survived.")
                div()
                health=0.1
                br()
                teen()
        elif might_die == 2:
            div()
            print("You were rushed to the emergency room.")
            chance=randint(1,4)
            if chance == 4:
                print("You died.")
                end()
            else:
                print("You barely survived.")
                div()
                health=0.1
                br()
                adult()
        elif might_die == 0:
            div()
            print("You were rushed to the emergency room.")
            print("You barely survived.")
            div()
            health=0.1
            br()
            teen()
        else:
            loop()
    def crime():
        div()
        adult_crime()
    def identity():
        global forename, surname, money
        print("[0] Return")
        print("[1] Name Change [£150]")
        print("[x] Declare Gender")
        print("[x] Declare Sexuality")
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            adult()
        elif ch == 1:
            if money >= 150:
                money-=150
                forename=input("Forename >")
                forename=forename.replace("|","")
                surname=input("Surname >")
                surname=surname.replace("|","")
                adult()
            else:
                div()
                print("You cannot afford that.")
                adult()
    def adult_activities():
        global money, happiness, looks, health, intel
        print("[0] Return")
        print("[1] Gym [£15]")
        print("[2] Library")
        print("[3] Doctor")
        print("[4] Surrender")
        print("[5] Debug Menu")
        print("[6] Crime")
        print("[x] Adoption")
        print("[8] Surgery")
        print("[9] Casino")
        print("[10] Identity")
        print("[x] Licenses")
        print("[x] Lawsuit")
        print("[x] Lottery")
        print("[x] Love")
        print("[x] Movies")
        print("[x] Nightlife")
        print("[x] Vacation")
        print("[x] Last Will And Testament")
        print("[x] Fertility")
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            adult()
        elif ch == 1:
            div()
            print("You went to the gym.")
            print("Enjoyment:")
            money-=15
            pbar(1)
            happiness+=0.25
            health+=0.25
            adult()
        elif ch == 2:
            div()
            print("You visited the library.")
            print("Enjoyment:")
            pbar(0)
            intel+=0.25
            happiness-=0.45
            adult()
        elif ch == 3:
            div()
            print("No doctors available.")
            adult()
        elif ch == 4:
            print("[1] Surrender")
            print("[0] Return")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 0:
                adult()
            elif ch == 1:
                end()
            else:
                adult()
        elif ch == 5:
            div()
            print("Hidden ethics value:")
            pbar(ethics)
            div()
            print("[0] Return")
            print("[1] Max out looks")
            allow_debug=0
            if allow_debug == 1:
                print("[2] Set Money")
                print("[x] Max Out Ethics")
            print("[4] Show Parents' Death Age")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 0:
                adult()
            elif ch == 1:
                looks=1
                adult()
            elif ch == 2:
                if allow_debug == 1:
                    try:
                        money=int(input(">"))
                    except:
                        adult()
                else:
                    adult()
            elif ch == 3:
                adult()
            elif ch == 4:
                global mother_end_age, father_end_age, mother_age, father_age
                print("Mother will die at age",mother_end_age,"[Current age: "+str(mother_age)+"]")
                print("Father will die at age",father_end_age,"[Current age: "+str(father_age)+"]")
                div()
                br()
                adult()
            else:
                adult()
            adult()
        elif ch == 6:
            crime()
        elif ch == 8:
            print("[0] Return")
            print("[1] Get the surgery [£10,000] [+25% looks]")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 0:
                adult()
            elif ch == 1:
                if money < 10000:
                    div()
                    print("You cannot afford it.")
                    adult()
                else:
                    money-=10000
                    looks+=0.25
                    div()
                    print("The surgery was successful.")
                    adult()
            else:
                div()
                adult()
        elif ch == 10:
            identity()
        elif ch == 9:
            if money < 0:
                div()
                print("BOUNCER: Sorry. We cannot let in people who owe us money.")
                print("YOU: But I don't owe YOU money, I owe someone else money!")
                print("BOUNCER: Too bad.")
                div()
                br()
                adult()
            blackjack_init()
        else:
            adult()
    def adult_assets():
        print("Locked.")
        adult()
    def occupation():
        global edu_lvl, money
        global did_tutor
        print("[0] Return")
        print("[1] Education")
        print("[x] Part-Time Jobs")
        print("[3] Freelance")
        print("[x] Job Recruiter")
        print("[x] Jobs")
        print("[x] Special Careers")
        print("[x] Local Gangs")
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            adult()
        elif ch == 1:
            if edu_lvl == 0:
                print("[1] GED [£500]")
                try:
                    ch=int(input(">"))
                except:
                    ch=0
                if ch == 0:
                    adult()
                elif ch == 1:
                    money-=500
                    print("You got a GED and have high school-equivalent education!")
                    edu_lvl=1
                    adult()
            elif edu_lvl == 1:
                print("[1] University [£25,000]")
                print("[0] Return")
                try:
                    ch=int(input(">"))
                except:
                    ch=0
                if ch == 0:
                    adult()
                elif ch == 1:
                    div()
                    uni_check()
                    adult()
            else:
                adult()
        elif ch == 3:
            if did_tutor == 0:
                print("[1] Tutor [£19/h]")
            print("[x] Handyman [£18/h]")
            print("[x] Truck Driver [£17/h]")
            print("[0] Return")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 0:
                adult()
            elif ch == 1:
                if did_tutor == 0:
                    div()
                    print("You did tutoring for 30 hours this week.")
                    base=19*30
                    print("You made £"+str(base))
                    did_tutor=1
                    money+=base
                    div()
                    br()
                    adult()
                else:
                    div()
                    print("You did tutoring already.")
                    div()
                    br()
                    adult()
            elif ch == 2:
                base=18*30
                div()
                adult()
                print("You became a handyman for 30 hours this week.")
                print("You made £"+str(base))
                div()
                br()
                money+=base
                adult()
            elif ch == 3:
                base=30*17
                adult()
                print("You became a truck driver for 30 hours this week.")
                print("You made £"+str(base))
                money+=base
                div()
                br()
                adult()
            else:
                adult()
        else:
            adult()
    def adult_pause():
        global mother_age, father_age
        global mother_name, father_name
        global juvie_offences
        global happiness, health, intel, looks, ethics, grades, clout, socialc
        global mother_rel, father_rel
        div()
        print("Game Paused.")
        div()
        print("[0] Resume")
        print("[1] Save Life")
        print("[x] Load Life")
        print("[3] Exit To Main Menu")
        debug=0
        if debug == 1:
            print("[x] Hidden Debug Menu")
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            adult()
        elif ch == 1:
            sn=input("Enter Save File Name $")
            if sn == "":
                from time import ctime
                sn=ctime()
                sn=sn.replace(":","-")
                sn=sn.replace(" ","_")
            sn+=".oll"
            global money, is_depressed
            #this is incomplete
            save=forename+"|"+surname+"|"+str(age)+"|"+str(happiness)+"|"+str(looks)+"|"+str(health)+"|"+str(ethics)+"|"+str(intel)+"|"+str(mother_rel)+"|"+str(father_rel)+str(money)+"|"+mother_name+"|"+father_name+"|"+str(mother_age)+"|"+str(father_age)
            import codecs
            save=save.encode('utf-8')
            save=codecs.encode(save,"base64_codec")
            f=open(sn,"wb")
            f.write(save)
            f.close()
            print("Saved as",sn)
            br()
            div()
            adult()
        elif ch == 3:
            print("[0] Cancel")
            print("[1] Exit and Save")
            print("[2] Exit Without Saving")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 0:
                adult_pause()
            elif ch == 1:
                sn=input("Enter Save File Name $")
                if sn == "":
                    from time import ctime
                    sn=ctime()
                    sn=sn.replace(":","-")
                    sn=sn.replace(" ","_")
                sn+=".oll"
                #this is incomplete
                save="alpha"+"|"+"10"+"|"+forename+"|"+surname+"|"+str(age)+"|"+str(happiness)+"|"+str(looks)+"|"+str(health)+"|"+str(ethics)+"|"+str(intel)+"|"+str(mother_rel)+"|"+str(father_rel)+str(money)+"|"+mother_name+"|"+father_name+"|"+str(mother_age)+"|"+str(father_age)
                import codecs
                save=save.encode('utf-8')
                save=codecs.encode(save,"base64_codec")
                f=open(sn,"wb")
                f.write(save)
                f.close()
                print("Saved as",sn)
                br()
                div()
                mainmenu()
            elif ch == 2:
                div()
                mainmenu()
            else:
                adult()
        else:
            adult()
    def adult():
        global mother_age, father_age
        global mother_name, father_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel
        global money, is_depressed
        if happiness > 1:
            happiness =1
        if happiness < 0:
            happiness=0
        if health > 1:
            health=1
        if health < 0:
            emergency_room(2)
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
        div()
        print(forename+" "+surname)
        if money >= 5000000:
            print("Independently Wealthy")
        else:
            print("Unemployed")
        div()
        if is_depressed == 1:
            print("Suffers from: Depression")
        print("Age",age)
        print("£"+str("{:,}".format((money))))
        div()
        if edu_lvl == 1:
            print("Education: High School")
        elif edu_lvl == 2:
            print("Education: University")
        elif edu_lvl == 3:
            print("Education: Grad School")
        elif edu_lvl == 0:
            print("Education: N/A")
        print("Work Experience: 0 Years")
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
        print("[5] Pause Menu")
        try:
            ch=int(input(">"))
        except:
            adult()
        if ch == 1:
            occupation()
        elif ch == 2:
            div()
            adult_assets()
        elif ch == 0:
            age_up()
        elif ch == 5:
            adult_pause()
        elif ch == 3:
            div()
            print(mother_name)
            print("Mother [Age "+str(mother_age)+"]")
            pbar(mother_rel)
            print("[1] Interact")
            div()
            print(father_name)
            print("Father [Age "+str(father_age)+"]")
            pbar(father_rel)
            print("[2] Interact")
            div()
            print("[0] Return")
            div()
            try:
                ch=int(input(">>"))
            except:
                adult()
            if ch == 1:
                print(mother_name)
                print("Mother [Age "+str(mother_age)+"]")
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
                    adult()
                elif ch ==1:
                    div()
                    print("You spent time with your mother.")
                    mother_rel+=0.25
                    if mother_rel > 1:
                        mother_rel=1
                    pbar(mother_rel)
                    div()
                    adult()
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
                    adult()
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
                    adult()
            
            elif ch == 2:
                print(father_name)
                print("Father [Age "+str(father_age)+"]")
                pbar(father_rel)
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
                    adult()
                elif ch ==1:
                    div()
                    print("You spent time with your father.")
                    father_rel+=0.25
                    if father_rel > 1:
                        father_rel=1
                    pbar(father_rel)
                    div()
                    adult()
                elif ch == 2:
                    print("You disrespected your father.")
                    father_rel-=0.25
                    happiness-=0.35
                    if father_rel < 0:
                        father_rel=0
                    if happiness < 0:
                        happiness=0
                    pbar(father_rel)
                    div()
                    adult()
                elif ch == 3:
                    print("You hit your father.")
                    print("Damage:")
                    pbar(0.25)
                    div()
                    print("Your father retaliated!")
                    print("Damage:")
                    pbar(0.75)
                    health-=0.75
                    happiness=0
                    div()
                    is_depressed=1
                    print("You are now suffering from DEPRESSION.")
                    div()
                    father_rel-=0.55
                    happiness-=0.75
                    if father_rel < 0:
                        father_rel=0
                    if happiness < 0:
                        happiness=0
                    pbar(father_rel)
                    adult()

            elif ch == 0:
                adult()
        elif ch ==4:
            adult_activities()
        adult()
    def adult_init():
        div()
        print("You are now an adult.")
        print("It is like being a teen but you can go to uni, get a job and live a proper life.")
        div()
        print("Clout and social currency are removed.")
        div()
        print("Press ENTER to continue.")
        wer=input()
        global clout, socialc
        global mother_rel, father_rel
        global stress
        stress=0.65
        from random import randint
        if mother_rel > 0.8:
            mother_rel=0.8
        if father_rel > 0.8:
            father_rel=0.8
        adult()
    def gang_menu():
        global respect, clout, happiness, health, is_drip, money
        global is_sch_gang
        div()
        print("Welcome to the top-secret GANG MENU.")
        print("Here you can earn respect and Gang Points to spend")
        div()
        print("Respect:")
        if respect > 1:
            respect=1
        if respect < 0:
            print("GANGSTER: You have greatly disappointed us.")
            print("YOU: What do you mean?")
            print("GANGSTER: You have broken our Code of Conduct.")
            print("YOU: What are you talking about!")
            print("GANGSTER: You aren't loyal.")
            print("YOU: YES I AM!")
            print("GANGSTER: We're gonna have to kick you out.")
            print("YOU: NO!")
            div()
            global is_sch_gang
            is_sch_gang=0
            happiness=0
            br()        
            teen()
        pbar(respect)
        div()
        print("[0] Return")
        print("[x] Get Fake ID")
        print("[2] Bully Kids")
        print("[x] Enemy Gangs")
        print("[x]  Gang War")
        print("[5] Drink With The Gang")
        if is_drip == 0:
            print("[6] Gang Drip[£1500]")
        print("[7] Leave gang")
        try:
            ch=int(input("\\"))
        except:
            ch=0
        if ch == 0:
            teen()
        elif ch == 1 or ch == 3 or ch == 4:
            div()
            print("Not in game yet.")
            teen()
        elif ch == 2:
            div()
            print("You bullied some kids in the playground.")
            print("You took great pleasure out of doing so.")
            div()
            clout+=0.15
            respect+=0.05
            happiness+=0.25
            br()
            teen()
        elif ch == 5:
            respect+=0.05
            happiness+=0.1
            clout-=0.05
            div()
            print("You had a few with the mates.")
            div()
            br()
            teen()
        elif ch == 6:
            if money >= 1500 and is_drip == 0:
                print("Gang drip allows you to gain 45% more repect and become")
                print("one with the gang.") 
                div()
                print("[1] Purchase [£1500]")
                print("[0] Return [Gang Menu")
                div()
                try:
                    ch=int(input(">"))
                except:
                    ch=0
                if ch == 0:
                    gang_menu()
                elif ch == 1:
                    money-=1500
                    is_drip=1
                    respect+=0.45
                    gang_menu()
                else:
                    gang_menu()
            else:
                div()
                print("A requirement was not fulfilled:")
                if money < 1500:
                    print("You need £1500.")
                elif is_drip != 0:
                    print("You have bought Gang Drip before.")
                else:
                    print("An error occured.")
                div()
                br()
                teen()
        elif ch == 7:
            div()
            print("[1] Confirm")
            print("[0] Return")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 0:
                teen()
            elif ch == 1:
                div()
                print("You left the gang.")
                is_sch_gang=0
                teen()
                      
    def secondary_school_menu():
        global club_count, is_sch_gang, health, happiness
        global grades, intel, happiness, stress
        div()
        print("[0] Return")
        print("[1] Secondary School")
        print("[2] Freelance")
        print("[x] Jobs")
        print("[x] Military")
        print("[x] Part-Time Jobs")
        print("[x] Special Careers")
        print("Stress:")
        pbar(stress)
        div()
        print("In",club_count,"school clubs")
        div()
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            div()
            teen()
        elif ch == 1:
            div()
            print("Grades:")
            pbar(grades)
            div()
            print("[1] Study Harder")
            print("[2] Skip School")
            print("[3] Join Club")
            if is_sch_gang == 0:
                print("[4] Join School Gang")
            else:
                print("[4] School Gang")
            print("[0] Return")
            div()
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 0:
                teen()
            elif ch == 1:
                div()
                print("You studied until you lost your vision.")
                div()
                grades+=0.15
                intel+=0.10
                teen()
            elif ch == 2:
                div()
                print("Insted of going to school, you decided to go bowling instead.")
                div()
                grades-=0.45
                intel-=0.55
                happiness+=0.15
                teen()
            elif ch == 3:
                div()
                print("Are you sure?")
                print("[1] Join [+10% stress]")
                print("[0] NO")
                try:
                    ch=int(input(">"))
                except:
                    ch=0
                if ch == 0:
                    teen()
                elif club_count >= 2:
                    div()
                    print("You cannot join more than 2 clubs.")
                    teen()
                elif ch == 1:
                    club_count+=1
                    stress+=0.1
                    teen()
                else:
                    teen()
            elif ch == 4:
                gang=is_sch_gang
                if gang == 0:
                    div()
                    print("YOU: I'd like to join your gang.")
                    if clout == 1:
                        print("GANGSTER: Sure thing, kid. Come on in.")
                        from time import sleep
                        sleep(1.5)
                        happiness+=0.55
                        print("GANGSTER: I'm sure your input will be valuable.")
                        global respect
                        respect=0.1
                        is_sch_gang=1
                        br()
                        teen()
                    elif clout >= 0.75:
                        print("GANGSTER: No, you're not tough enough.")
                        print("YOU: I respect that.")
                        br()
                        teen()
                    else:
                        print("GANGSTER: HA HA! AS IF!")
                        div()
                        print("The gangster beat you up!")
                        print("Damage:")
                        pbar(0.85)
                        div()
                        happiness-=2.25
                        health-=0.85
                        br()
                        teen()
                elif gang == 1:
                    gang_menu()
                        
            teen()
        else:
            teen()
    def teen_shop():
        div()
        global money, fake_id
        print("£"+str("{:,}".format((money))))
        div()
        print("Welcome. Items labeled with [FID] need a fake ID to be bought.")
        print("Items labeled with [GANG] require you to join the school gang.")
        div()
        print("[0] Return [Assets]")
        print("[1] Fake ID [£450]")
        print("[2] Beer [£10][FID]")
        print("[3] Cigarette pack [£25][FID]")
        print("[4] Knife [£25][GANG]")
        print("[5] ")
    def teen_assets():
        global money, fake_id
        print("Money: £"+str(money))
        div()
        
        print("Item List:")
        div()
        print("[1] Buy Items")
        print("[2] Item List")
        if fake_id >= 1:
            print("[3] Fake ID Hub")
        print("[0] Return")
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            teen()
        elif ch == 1:
            teen_shop()
        elif ch == 2:
            div()
            print("Coming soon!")
            teen()
        elif ch == 3:
            if fake_id >= 1:
                fake_id_hub()
            else:
                div()
                print("Get a fake ID lol")
                teen()
        else:
            teen()
    def teen_activities():
        global happiness, health, intel, looks, ethics, grades, clout, socialc
        global mother_rel, father_rel
        global money
        global juvie_offences
        print("[0] Return")
        print("[1] Gym")
        print("[2] Library")
        print("[3] Doctor")
        print("[4] Surrender")
        print("[5] Debug Mode")
        print("[6] Crime")
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            teen()
        elif ch == 1:
            div()
            print("You went to the gym.")
            happiness+=0.45
            health+=0.35
            print("Enjoyment:")
            pbar(1)
            teen()
        elif ch == 2:
            div()
            print("You visited the library.")
            print("Enjoyment:")
            pbar(0.25)
            happiness-=0.1
            intel+=0.15
            teen()
        elif ch == 3:
            div()
            print("No doctor available.")
            teen()
        elif ch == 4:
            print("[0] Return")
            print("[1] Surrender",forename,surname+"?")
            try:
                ch=int(input("<<"))
            except:
                ch=0
            if ch == 0:
                teen()
            elif ch == 1:
                end()
            else:
                teen()
        elif ch == 5:
            div()
            print("Ethics:")
            pbar(ethics)
            div()
            print("[1] Max Out Relationships")
            print("[2] Max Out Looks")
            print("[3] Get Clout")
            print("[4] Get social currency")
            print("[5] Join gang")
            print("[0] Return")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 0:
                teen()
            elif ch == 1:
                mother_rel=1
                father_rel=1
                teen()
            elif ch == 2:
                looks=1
                teen()
            elif ch == 3:
                clout+= 0.25
                teen()
            elif ch == 4:
                socialc+=0.25
                teen()
            elif ch == 5:
                global is_sch_gang, respect
                respect=0.1
                is_sch_gang=1
            else:
                teen()
        elif ch == 6:
            print("Welcome to the NEW Crime menu.")
            print("You can perform some crimes >:)")
            if juvie_offences > 0:
                div()
                print("You have committed",juvie_offences,"offence[s].")
            div()
            print("[0] Return")
            print("[x] Bank Robbery")
            print("[x] Burglary")
            print("[x] GTA")
            print("[x] Hitman")
            print("[x] Murder")
            print("[1] Loitering")
            print("[2] Delinquence")
            print("[3] Pickpocketing")
            print("[4] Shoplift")
            print("[x] Train Robbery")
            div()
            try:
                ch=int(input("<"))
            except:
                ch=0
            if ch == 0:
                teen()
            elif ch == 1:
                print("You loitered about.")
                clout+=0.1
                teen()
            elif ch == 2:
                print("You harassed people on the street.")
                clout+=0.25
            elif ch == 3:
                from random import randint
                stolen=randint(10,25)
                print("You stole",stolen,"money!")
                money+=stolen
                teen()
            elif ch == 4:
                print("[0] Return")
                print("[1] Cigarettes")
                print("[2] Beer")
                print("[3] Mars candy bar")
                print("[4] Gucci handbag [£150]")
                print("[5] Wallet [£50]")
                print("[6] Smartphone [£500]")
                try:
                    ch=int(input(">"))
                except:
                    ch=0
                div()
                if ch == 0:
                    teen_activities()
                from random import randint
                caught=randint(1,2)
                if ch == 1:
                    if caught == 1:
                        print("You nabbed some cigarettes from the local off-license.")
                        print("That old man had no idea!")
                        print("You enjoyed a nice smoke with your 20 friends.")
                        pause()
                        clout+=0.45
                        teen()
                    else:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        juvie_offences+=1
                        div()
                        pause()
                        clout-=0.45
                        teen()
                elif ch == 2:
                    if caught == 1:
                        print("You took a Budweiser from the local off-license.")
                        print("Sure does taste better when it's free.")
                        clout+=0.35
                        pause()
                        teen()
                    elif caught == 2:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        juvie_offences+=1
                        div()
                        clout-=0.35
                        pause()
                        teen()
                elif ch == 3:
                    print("Five finger discount, am I right?")
                    pause()
                    happiness+=0.15
                    clout+=0.1
                    intel-=0.2
                    teen()
                elif ch == 4:
                    if caught == 1:
                        money+=150
                        clout+=0.55
                        print("You sold the handbag for £150.")
                        pause()
                        teen()
                    else:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        juvie_offences+=1
                        div()
                        clout-=0.55
                        teen()
                elif ch == 5:
                    if caught == 1:
                        print("You got a wallet. Now what?")
                        money+=50
                        clout+=0.15
                        pause()
                        teen()
                    else:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        juvie_offences+=1
                        div()
                        clout-=0.15
                        teen()
                elif ch == 6:
                    if caught == 1:
                        print("Nice phone. Said the person I sold it to XD")
                        money+=500
                        clout+=0.75
                        happiness-=0.45
                    else:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        juvie_offences+=1
                        clout-=0.35
                        pause()
                        teen()
                else:
                    teen()
        else:
            teen()
            
    def teen():
        global mother_name, father_name
        global juvie_offences
        global happiness, health, intel, looks, ethics, grades, clout, socialc
        global mother_rel, father_rel
        global money, is_depressed
        if grades > 1:
            grades=1
        if grades < 0:
            grades=0
        if happiness > 1:
            happiness =1
        if happiness < 0:
            happiness=0
        if health > 1:
            health=1
        if health < 0:
            emergency_room(1)
        if intel > 1:
            intel=1
        if looks > 1:
            looks=1
        if intel < 0:
            intel=0
        if looks < 0:
            looks=0
        if clout > 1:
            clout=1
        if clout < 0:
            clout=0
        if socialc > 1:
            socialc=1
        if socialc < 0:
            socialc=0
        global forename, surname
        global mother_rel, father_rel
        global money
        div()
        print(forename+" "+surname)
        print("Secondary School Student")
        if is_depressed == 1:
            print("Suffers from: Depression")
        print("Age",age)
        print("£"+str("{:,}".format((money))))
        div()
        print("Clout:")
        pbar(clout)
        print("Social Currency:")
        pbar(socialc)
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
            teen()
        if ch == 1:
            secondary_school_menu()
        elif ch == 2:
            div()
            teen_assets()
        elif ch == 0:
            age_up()
        elif ch == 3:
            div()
            print(mother_name)
            print("Mother [Age "+str(age+32)+"]")
            pbar(mother_rel)
            print("[1] Interact")
            div()
            print(father_name)
            print("Father [Age "+str(age+37)+"]")
            pbar(father_rel)
            print("[2] Interact")
            div()
            print("[0] Return")
            div()
            try:
                ch=int(input(">>"))
            except:
                teen()
            if ch == 1:
                print(mother_name)
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
                    teen()
                elif ch ==1:
                    div()
                    print("You spent time with your mother.")
                    mother_rel+=0.25
                    if mother_rel > 1:
                        mother_rel=1
                    pbar(mother_rel)
                    div()
                    teen()
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
                    teen()
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
                    teen()
            
            elif ch == 2:
                print(father_name)
                print("Father [Age "+str(age+32)+"]")
                pbar(father_rel)
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
                    teen()
                elif ch ==1:
                    div()
                    print("You spent time with your father.")
                    father_rel+=0.25
                    if father_rel > 1:
                        father_rel=1
                    pbar(father_rel)
                    div()
                    teen()
                elif ch == 2:
                    print("You disrespected your father.")
                    father_rel-=0.25
                    happiness-=0.35
                    if father_rel < 0:
                        father_rel=0
                    if happiness < 0:
                        happiness=0
                    pbar(father_rel)
                    div()
                    teen()
                elif ch == 3:
                    print("You hit your father.")
                    print("Damage:")
                    pbar(0.25)
                    div()
                    print("Your father retaliated!")
                    print("Damage:")
                    pbar(0.75)
                    health-=0.75
                    happiness=0
                    div()
                    is_depressed=1
                    print("You are now suffering from DEPRESSION.")
                    div()
                    father_rel-=0.55
                    happiness-=0.75
                    if father_rel < 0:
                        father_rel=0
                    if happiness < 0:
                        happiness=0
                    pbar(father_rel)
                    teen()

            elif ch == 0:
                teen()
        elif ch ==4:
            teen_activities()
        teen()
    def teen_init():
        div()
        print("You are now a teenager.")
        print("You can now earn money and spend it on certain items.")
        print("You will be able to commit juvenile crimes, but you can't go to prison for them yet. Make the most of it.")
        print("Enjoy!")
        div()
        print("TIP: You now have 2 new values: CLOUT and SOCIAL CURRENCY.")
        print("CLOUT is earned through crime and parties")
        print("SOCIAL CURRENCY cannot be earned yet.")
        div()
        print("Press ENTER to continue.")
        wer=input()
        global clout, socialc
        global mother_rel, father_rel
        global stress
        stress=0.65
        from random import randint
        if mother_rel > 0.8:
            mother_rel=0.8
        if father_rel > 0.8:
            father_rel=0.8
        socialc=randint(1,100)
        socialc/=100
        clout=0
        teen()
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
        global grades, intel, happiness
        global stress
        div()
        print("[0] Return")
        print("[1] Primary School")
        print("[x] Freelance")
        print("[x] Jobs")
        print("[x] Military")
        print("[x] Part-Time Jobs")
        print("[x] Special Careers")
        print("Stress:")
        pbar(0.5)
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
            print("Grades:")
            pbar(grades)
            div()
            print("[1] Study Harder")
            print("[2] Skip School")
            print("[0] Return")
            div()
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 0:
                child()
            elif ch == 1:
                div()
                print("You studied until you lost your vision.")
                div()
                grades+=0.25
                intel+=0.15
                child()
            elif ch == 2:
                div()
                print("Insted of going to school, you decided to go bowling instead.")
                div()
                grades-=0.25
                intel-=0.35
                happiness-=0.45
                child()
            div()
            child()
        else:
            div()
            child()
    def child():
        global mother_name, father_name
        global happiness, health, intel, looks, ethics, grades
        if grades > 1:
            grades=1
        if grades < 0:
            grades=0
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
        print("£"+str("{:,}".format((money))))
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
            print(mother_name)
            print("Mother [Age "+str(age+32)+"]")
            pbar(mother_rel)
            print("[1] Interact")
            div()
            print(father_name)
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
                print(mother_name)
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
                print(father_name)
                print("father [Age "+str(age+32)+"]")
                pbar(father_rel)
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
                    print("You spent time with your father.")
                    father_rel+=0.25
                    if father_rel > 1:
                        father_rel=1
                    pbar(father_rel)
                    div()
                    child()
                elif ch == 2:
                    print("You disrespected your father.")
                    father_rel-=0.25
                    happiness-=0.35
                    if father_rel < 0:
                        father_rel=0
                    if happiness < 0:
                        happiness=0
                    pbar(father_rel)
                    div()
                    child()
                elif ch == 3:
                    div()
                    print("You hit your father.")
                    print("Damage:")
                    pbar(0.25)
                    father_rel-=0.55
                    happiness-=0.75
                    if father_rel < 0:
                        father_rel=0
                    if happiness < 0:
                        happiness=0
                    pbar(father_rel)
                    child()

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
        global grades, intel
        grades=intel
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
        global mother_name, father_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel, age
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
                print(mother_name)
                print("Mother [Age",str(age+32)+"]")
                pbar(mother_rel)
                print("[1] Interact with")
                div()
                print(father_name)
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
                    print(mother_name)
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
        global forename_m, forename_f
        global mother_name, father_name
        from random import choice
        mother_name=choice(forename_f)
        father_name=choice(forename_m)
        global happiness, health, intel, looks, ethics
        from random import randint
        print("[1] Random Life")
        print("[2] Custom Life")
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
            mother_name+=" "+surname
            father_name+=" "+surname
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
                choose_start()
            choose_start()
        elif ch == 2:
            print("[1] Maxxed-out Values")
            print("[2] 0% Everything")
            print("[3] Custom Values")
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
            try:
                start_age=int(input(">Start Age >"))
            except:
                start_age=0
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
                try:
                    looks=int(input("Looks  $"))
                except:
                    looks=randit(1,100)
                    looks/=100
                ethics=1
                
            else:
                mainmenu()
            choose_start()
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
        print("News! You can now [partially] save the game! [Only during adult stage]")
        print("News! Added adult crime options!")
        print("News! You can now apply [but not go] to university!")
        div()
        print("[1] New Life")
        print("[x] Load Life")
        print("[3] Credits")
        print("[4] Download Latest Challenge")
        #Download location: https://winfan3672.000webhostapp.com/challenge/latest.py
        print("[x] Load Challenge.zip from disk")
        print("[6] Exit")
        print("[x] Changelog")
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
            quit()
            raise KeyboardInterrupt
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
        elif ch == 4:
            import urllib.request
            url="https://winfan3672.000webhostapp.com/challenge/latest.zip"
            print("Downloading challenge...")
            try:
                urllib.request.urlretrieve(url,"challenge.zip")
            except:
                div()
                print("Failed to download challenge.")
                div()
                mainmenu()
            div()
            print("Downloaded challenge.")
            div()
            mainmenu()
        else:
            div()
            print("That option is not available in the current build of the game")
            div()
            mainmenu()
    mainmenu()
except KeyboardInterrupt:
    try:
        while True:
            print("The anticheat caught you.")
            wer=input()
            div()
    except:
        loop()
