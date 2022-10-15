# OpenLife Alpha 12

# OpenLife is a FOSS replacement for BitLife.
# For years, BitLife has become worse and worse, so I decided to step in and
# replace it with this. It's way better. Trust me.
from random import randint as rng
import os
class ExitError(Exception):
    #This one is used to nuke the game by deleting all variables.
    #I had to put everything into an except statement because
    #it would raise 3 errors and not delete anything.
    pass
class reboot(Exception):
    #type raise reboot to reboot the game!
    def __init__(self):
        mainmenu()
class GeneralException(Exception):
    pass
class FeatureNotInGameError(Exception):
    pass
class LifeCreatorError(Exception):
    #used for when an error occurs in the life creation process
    def __init__(self):
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("LifeCreatorError")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("The Life Creator experienced an error and has ended the program.")
        print("The game will restart.")
        input("Press ENTER to continue.")
        mainmenu()
import os
try:
    os.chdir("openlife_saves")
except:
    os.mkdir("openlife_saves")
    os.chdir("openlife_saves")
try:
    def game_init():
        global work_e, work_e_base, promo_base
        work_e=0 #work experience
        promo_base=0
        work_e_base=0 #resets each time you quit your job / hidden value
        promo_base=0
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
        surname= ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller",
            "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson",
            "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez",
            "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker",
            "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez",
            "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson",
            "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips",
            "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart",
            "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell",
            "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox",
            "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James",
            "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood",
            "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry",
            "Powell", "Log", "Patterson", "Hughes", "Flores", "Washington",
            "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander",
            "Russell", "Griffin", "Diaz", "Hayes"]
        try:
            #If you create a file called male.dat in your openlife save folder,
            #You can add custom male forenames. Each forename
            #is split by a new line
            f=open("male.dat","r")
            data=f.read()
            forename_m=data.split("\n")
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("Loaded Custom Male Forenames.")
        except:
            pass
        try:
            f=open("female.dat","r")
            data=f.read()
            forename_f=data.split("\n")
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("Loaded Custom Female Forenames.")
        except:
            pass
        try:
            f=open("surname.dat","r")
            data=f.read()
            surname=data.split("\n")
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("Loaded Custom Surnames.")
        except:
            pass
        global app_version,sub_version
        app_version=[0,0,7]
        sub_version=1
        global edu_lvl, job_id, job_lvl
        edu_lvl=1
        global pension
        pension=0 #yearly pension
        job_id=0
        job_lvl=1


        global allow_debug, allow_test
        allow_debug=0 #Some debug commands are hidden behind this flag, and ExitError spits out a load of debug info upon exiting
        allow_test=0 #Allows for some test features to be enabled.
        
        from time import strftime
        global year
        year=strftime("%Y")
        year=int(year)

        global debt, savings
        savings=0
        debt=0

        global hours, min_hours, salary, expenses
        salary=0
        hours=0
        min_hours=0
        expenses=0
        
        global game_name, version
        global alt_ui
        global juvie_offences
        global is_job
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
        global is_job
        is_job=0
        fake_id=0
        is_drip=0
        club_count=0

        #0=Original UI style [Looks kinda bad when you compare it to the others]
        #1=Experimental UI style [with squares]
        #2=New UI Style [Looks great in cmd]
        alt_ui=2
        
        global alt_logo
        alt_logo=1 #set to 1 for a different logo!

        game_name="OpenLife"
        version="Alpha 12.1 [11 Oct 2022]"
        return True
    def fake_id_hub():
        global debt, savings, money
        print("[0] Return")
        print("[x] Casino")
        print("[2] Lottery")
        print("[3] Loan")
        print("[4] Access Savings Account")
        print("[5] \"Club\"")
        try:
            ch=int(input(">"))
        except:
            ch==0
        if ch == 0:
            teen()
        elif ch == 2:
            lottery(1)
        elif ch == 3:
            try:
                d=int(input("How much to borrow? [Max 10k]>"))
            except:
                d=0
            if debt >= 10000:
                adult()
            if d > 10000:
                d=10000
            debt+=d
            money+=d
            teen()
        elif ch == 4:
            print(f"Savings: £{savings}")
            print("[0] Return")
            print("[1] Take Out Savings")
            try:
                ch=int(input(">"))
            except:
                teen()
            if ch == 1:
                money+=savings
                savings=0
            else:
                teen
            teen()
        else:
            teen()
    def save_game():
        global allow_debug
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age, mother_rel, father_rel
        print("Save Game")
        div()
        print("Saves that are already taken:")
        path=os.getcwd()
        dirlist=os.listdir(path)
        for item in dirlist:
            isFile=os.path.isfile(item)
            if isFile == True and item.endswith(".oll2"):
                item=item.replace(".oll2","")
                print(item)
        div()
        
        #0=Alpha|1=12|2=happiness|3=health|4=intel|5=looks|6=ethics|7=money
        #|8=forename|9=surname|10=age|11=work_e|12=edu_lvl|13=work_e_base|14=promo_base
        #|15=degree|16=hours|17=salary|18=expenses|19=expenses|20=pension
        #|21=is_depressed|22=debt|23=savings|24=year|25=is_job|26=stress
        #|27=mother_name|28=father_name|29=mother_age|30=father_age
        #|31=mother_end_age|32=father_end_age|33=did_tutor
        sn=input("Enter File Name >")
        # Windows illegal filename characters removed
        sn=sn.replace("\\","")
        sn=sn.replace("/","")
        sn=sn.replace("?","")
        sn=sn.replace("*","")
        sn=sn.replace("|","")
        sn=sn.replace("<","")
        sn=sn.replace(">","")
        sn=sn.replace(":","")
        sn=sn.replace("\"","")
        sn+=".oll2" # filename extension
        if sn == "":
            from time import ctime
            sn=ctime()
            sn=sn.replace(":","-")
            sn=sn.replace(" ","_")
        save="Alpha|12|"+str(happiness)+"|"+str(health)+"|"+str(intel)+"|"+str(looks)+"|"+str(ethics)+"|"+str(money)+"|"+forename+"|"+surname+"|"+str(age)+"|"+str(work_e)+"|"+str(edu_lvl)+"|"+str(work_e_base)+"|"+str(promo_base)+"|"+str(degree)+"|"+str(hours)+"|"+str(salary)+"|"+str(expenses)+"|"+str(pension)+"|"+str(is_depressed)+"|"+str(debt)+"|"+str(savings)+"|"+str(year)+"|"+str(is_job)+"|"+str(stress)+"|"+mother_name+"|"+father_name+"|"+str(mother_age)+"|"+str(father_age)+"|"+str(mother_end_age)+"|"+str(father_end_age)
        import codecs
        save=save.encode('utf-8')
        save=codecs.encode(save,"base64_codec")
        f=open(sn,"wb")
        f.write(save)
        f.close()
        print("Saved as",sn)
        br()
        div()
        return True
    def load_game():
        global allow_debug, did_tutor
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary, mother_rel, father_rel
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age
        print("Load Game")
        div()
        print("Available saves:")
        path=os.getcwd()
        dirlist=os.listdir(path)
        for item in dirlist:
            isFile=os.path.isfile(item)
            if isFile == True and item.endswith(".oll2"):
                item=item.replace(".oll2","")
                print(item)
            else:
                continue
        div()
        try:
            #0=Alpha|1=12|2=happiness|3=health|4=intel|5=looks|6=ethics|7=money
            #|8=forename|9=surname|10=age|11=work_e|12=edu_lvl|13=work_e_base|14=promo_base
            #|15=degree|16=hours|17=salary|18=expenses|19=pension
            #|20=is_depressed|21=debt|22=savings|23=year|24=is_job|25=stress
            #|26=mother_name|27=father_name|28=mother_age|29=father_age
            #|30=mother_end_age|31=father_end_age
            sn=input("Enter File Name >")
            # Windows illegal filename characters removed
            sn=sn.replace("\\","")
            sn=sn.replace("/","")
            sn=sn.replace("?","")
            sn=sn.replace("*","")
            sn=sn.replace("|","")
            sn=sn.replace("<","")
            sn=sn.replace(">","")
            sn=sn.replace(":","")
            sn=sn.replace("\"","")
            sn+=".oll2" #file extension
            f=open(sn,"rb")
            import codecs
            ssave=f.read()
            f.close()
            ssave=codecs.decode(ssave,"base64_codec")
            ssave=ssave.decode('utf-8')
            ssave=ssave.split("|")
            save=ssave
            if allow_debug == 1:
                print(save)
            if save[0] == "Alpha" and save[1] == "12":
                happiness=float(save[2])
                health=float(save[3])
                intel=float(save[4])
                looks=float(save[5])
                ethics=float(save[6])
                money=int(save[7])
                forename=save[8]
                surname=save[9]
                age=int(save[10])
                work_e=int(save[11])
                edu_lvl=int(save[12])
                work_e_base=int(save[13])
                promo_base=int(save[14])
                is_depressed=int(save[15])
                debt=int(save[16])
                savings=int(save[17])
                expenses=int(save[18])
                pension=float(save[19])
                pension=int(pension)
                is_depressed=int(save[20])
                debt=int(save[21])
                savings=int(save[22])
                year=int(save[23])
                is_job=int(save[24])
                stress=float(save[25])
                mother_name=save[26]
                father_name=save[27]
                mother_age=int(save[28])
                father_age=int(save[29])
                mother_end_age=int(save[30])
                father_end_age=int(save[31])
                did_tutor=1
                mother_rel=rng(75,100)
                mother_rel/=100
                father_rel=rng(75,100)
                father_rel/=100
                div()
                print("Successfully loaded life.")
                adult()
            else:
                print("This save is incompatible with OpenLife.")
                print("Expected Version: Alpha 12")
                print("Got version:",save[0],save[1])
        except:
            div()
            print("Failed to load game. Exiting.")
            mainmenu()
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
    def job_centre():
        global edu_lvl, looks, salary, hours, is_job, job_id
        div()
        print("These are all elegible jobs.")
        div()
        if edu_lvl >= 1:
            print("[1] Amazon Delivery Driver [£5/h]")
        if edu_lvl >= 2 and degree == 11:
            print("[2] Jr Translator [£10/h]")
        if edu_lvl >= 2 and degree == 5:
            print("[3] Jr Accountant [£30/h]")
        print("[4] Exorcist [£10/h]")
        if edu_lvl >= 2 and degree == 4:
            print("Teacher [£20/h]")
        print("[x] Trainee Pilot")
        if edu_lvl >= 2 and degree == 3:
            print("[6] Jr Game Developer [£40/h]")
        print("[x] Lawyer")
        if edu_lvl >= 2 and degree == 2:
            print("[8] Jr Lawyer [£60/h]")
        if edu_lvl >= 2 and degree == 3:
            print("[9] App Developer [£45/h]")
        if edu_lvl >= 2 and degree == 1:
            print("[10] Jr Banker [£45/h]")
        print("[11] Monk [15/h]")
        print("[12] Wedding Planner [25/h]")
        if edu_lvl >= 2 and degree == 9:
            print("[13] Engineer I [£55/h]")
        if edu_lvl >= 2 and degree == 13:
            print("[14] Data Scientist [75/h]")
        if edu_lvl >= 1:
            print("[15] Private [Army] [£35/h]")
        print("[x] Architect")
        if edu_lvl >= 1:
            print("[17] Cashier [£10/h]")
        if edu_lvl >= 2 and degree == 4:
            print("[18] College Lecturer [£45/h]")
        print("[19] OOhber Driver [£15/h]")
        if edu_lvl >= 2 and degree == 2:
            print("[20] Editor [£25/h]")
        if looks >= 0.8:
            print("[21] Exotic Dancer [£15/h]")
        print("[22] Flight Attendant [£25/h]")
        if edu_lvl >= 1:
            print("[23] Apprentice Hairdresser [£25/h]")
        print("[x] Judge")
        if edu_lvl >= 1:
            print("[25] Librarian [£25]")
        if edu_lvl >= 1:
            print("[26] Nun [£10/h]")
        print("[x] Photographer")
        if edu_lvl >= 1 and looks >= 0.8:
            print("[28] P*rnographer [£35/h]")
        if edu_lvl >= 2 and degree == 1:
            print("[29] Stockbroker [£45/h]")
        if edu_lvl >= 2 and degree == 16:
            print("[30] Publicity Stuntperson [£35/h]")
        try:
            ch=int(input(">"))
        except:
            ch=0
        job_id=ch
        if ch == 0:
            adult()
        elif ch == 1 and edu_lvl >= 1:
            if job_interview():
                salary=5
                hours=60
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 2 and edu_lvl >= 2 and degree == 11:
            if job_interview():
                salary=10
                hours=45
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 3 and edu_lvl >= 2 and degree == 5:
            if job_interview():
                salary=30
                hours=45
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 4:
            if job_interview():
                salary=10
                hours=40
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 5 and edu_lvl >= 2 and degree == 4:
            if job_interview():
                salary=20
                hours=55
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 6 >= 2 and degree == 3:
            if job_interview():
                salary=40
                hours=45
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 8 and degree == 2 and edu_lvl >= 2:
            if job_interview():
                salary=60
                hours=40
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
            print("You got the job.")
            br()
            adult()
        elif ch == 9 and edu_lvl >= 2 and degree == 3:
            if job_interview():
                salary=45
                hours=40
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 10 and degree == 1 and edu_lvl >= 2:
            if job_interview():
                salary=45
                hours=40
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 11:
            if job_interview():
                salary=15
                hours=40
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 12:
            if job_interview():
                salary=25
                hours=45
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 13 and edu_lvl >= 2 and degree == 9:
            if job_interview():
                salary=55
                hours=40
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 14 and edu_lvl >= 2 and degree == 13:
            if job_interview():
                salary=75
                hours=50
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 15 and edu_lvl >= 1:
            if job_interview():
                salary=35
                hours=40
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 17 and edu_lvl >= 1:
            if job_interview():
                salary=10
                hours=40
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 18 and edu_lvl >= 2 and degree == 4:
            if job_interview():
                salary=45
                hours=45
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 19:
            if job_interview():
                salary=15
                hours=60
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 20 and edu_lvl >= 2 and degree == 2:
            if job_interview():
                salary=25
                hours=40
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 21 and looks >= 0.8:
            if job_interview():
                salary=15
                hours=45
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 22:
            if job_interview():
                salary=25
                hours=40
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 23 and edu_lvl >= 1:
            if job_interview():
                salary=25
                hours=40
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 25 and edu_lvl >= 1:
            if job_interview():
                salary=25
                hours=40
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 26 and edu_lvl >= 1:
            if job_interview():
                salary=10
                hours=40
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 28 and edu_lvl >= 1 and looks >= 0.8:
            if job_interview():
                salary=35
                hours=40
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 29 and edu_lvl >= 2 and degree == 1:
            if job_interview():
                salary=45
                hours=35
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 30 and edu_lvl >= 2 and degree == 16:
            if job_interview():
                salary=35
                hours=40
                is_job=1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()           
        else:
            job_id=0
            adult()
        adult()
    def adult_crime():
        global mother_age, age
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
                    age-=1
                    div()
                    age_up()
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
                    age-=1
                    div()
                    age_up()
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
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 2:                
                if base == "07:00":
                    div()
                    print("You won £"+str(winnings))
                    money+=winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 3:
                if base == "12:00":
                    div()
                    print("You won £"+str(winnings))
                    money+=winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 4:
                if base == "16:20":
                    div()
                    print("You won £"+str(winnings))
                    money+=winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 5:
                if base == "19:00":
                    div()
                    print("You won £"+str(winnings))
                    money+=winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 6:
                div()
                if base == "21:00":
                    print("You won £"+str(winnings))
                    money+=winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            else:
                adult()
        else:
            #Place more options on this indent level
            adult()
    def uni_age():
        global mother_age, father_age, father_end_age, mother_end_age, debt, savings, money
        basee=savings/10
        basee=int(basee)
        savings+=basee
        base=int(debt/5)
        debt+=base
        base=int(debt/10)
        money-=base
        mother_age+=1
        father_age+=1
        global age, uni_end_age, work_e_base
        global salary, hours, work_e, promo_base
        #when parents die
        base=salary*hours*52
        money+=base
        money-=(expenses*12)
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
        if hours > 0:
            base=salary*hours
            base*=52
            money+=base
            work_e+=1
            promo_base+=1
            work_e_base+=1
        age+=1
        if age == uni_end_age:
            div()
            global edu_lvl
            edu_lvl=2
            print("You graduated from University.")
            salary=0
            work_e_base=0
            hours=0
            br()
            adult()
        else:
            uni()
    def uni_activities():
        global uni_end_age
        global mother_age, father_age
        global mother_name, father_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel
        global money, is_depressed
        print("[0] Return")
        print("[1] Party")
        print("[2] Do Drugs")
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            university()
        elif ch == 1:
            print("You partied.")
            print("Enjoyment:")
            pbar(0.75)
            happiness+=0.45
            uni()
        elif ch == 2:
            div()
            print("Locked.")
            uni()
        else:
            uni()
    def uni_menu():
        global salary, hours
        print("[1] University")
        print("[2] Part-Time Jobs")
        print("[x] Local Gangs")
        print("[0] Return")
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            uni()
        elif ch == 1:
            div()
            print("[1] Drop Out")
            print("[0] Return")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 0:
                uni()
            elif ch == 1:
                div()
                print("You dropped out of Uni.")
                adult()
            else:
                uni()
        elif ch == 2:
            print("[1] Mall Santa [£15/h] [10h]")
            print("[2] Lab Assistant [£19/h] [15h]")
            print("[3] Receptionist [£9/h] [22h]")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 0:
                uni()
            elif ch == 1:
                salary=15
                hours=10
                div()
                uni()
            elif ch == 2:
                salary=19
                hours=15
                div()
                uni()
            elif ch == 3:
                salary=9
                hours=22
                div()
                uni()
            else:
                uni()
        else:
            uni()
    def uni():
        global uni_end_age
        global mother_age, father_age
        global mother_name, father_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel
        global money, is_depressed, debt
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
        print("University Student")
        div()
        if is_depressed == 1:
            print("Suffers from: Depression")
        print("Age",age)
        print("£"+str("{:,}".format((money))))
        div()
        print("Happiness:",pbar2(happiness),str(int(happiness*100))+"%")
        print("Health:   ",pbar2(health),str(int(health*100))+"%")
        print("Smarts:   ",pbar2(intel),str(int(intel*100))+"%")
        print("Looks:    ",pbar2(looks),str(int(looks*100))+"%")
        div()
        print("Uni end age:",uni_end_age)
        div()
        print("[1] University")
        print("[0] Age Up")
        print("[x] Relationships")
        print("[4] Activities")
        try:
            ch=int(input(">"))
        except:
            uni()
        if ch == 0:
            uni_age()
        elif ch == 1:
            uni_menu()
        elif ch == 3:
            div()
            print("Locked.")
            div()
            uni()
        elif ch == 4:
            uni_activities()
        else:
            uni()
        
    def uni_start():
        div()
        global uni_end_age, age, money
        uni_end_age=age+5
        print("You will end uni at age:",uni_end_age)
        uni()
        br()
    def uni_check():
        global degree, money, debt
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
                print("[4] Apply for a student loan")
                print("[0] Return")
                try:
                    ch=int(input(">"))
                except:
                    ch=0
                div()
                if ch == 0:
                    adult()
                elif ch == 1:
                    money-=25000
                    uni_start()
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
                elif ch == 4:
                    debt+=25000
                    uni_start()
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
        global money, number, enemy_number, bet, winnings, debt
        if enemy_number > 21:
            print("Enemy bust!")
            money+=bet
            winnings+=bet
            br()
            casino_menu()
        elif enemy_number > number:
            print("Enemy won")
            debt+=bet
            winnings-=bet
            br()
            casino_menu()
    def enemy():
        global money, number, enemy_number, debt
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
        global money, number, bet, winnings, allow_debug, debt
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
            print("Bet set to maximum [£10 000 000]")
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
                debt+=bet
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
    def lottery(is_teen):
        global money, allow_test
        from random import randint
        div()
        print("Enter amount of lottery tickets to buy.")
        print("1 ticket = £100")
        base=str("{:,}".format((int(money/100))))
        print("You can afford",base,"tickets.")
        div()
        losses=0
        wins=0
        win_amount=0
        try:
            ticket_count=int(input(">"))
        except:
            ticket_count=0
        price=ticket_count*100
        tmw=ticket_count*1000
        tmw*=1000000
        if price > money:
            div()
            print("You cannot afford that many tickets.")
            if is_teen == 0:
                adult()
            else:
                teen()
        if ticket_count == 0:
            if is_teen == 0:
                adult()
            else:
                teen()
        else:
            try:
                for i in range(ticket_count):
                    money-=100
                    chance=randint(1,100000)
                    if chance == 2345:
                        base=wins+losses
                        base/=ticket_count
                        if allow_test == 0:
                            base*=100
                        if allow_test == 0:
                            print("You won! ["+str("{:,}".format((int(losses)))),"losses] ["+str(int(base))+"%]")
                        else:
                            print("You won!",pbar2(base)+" ["+str("{:,}".format((int(losses)))),"losses]")
                        wins+=1
                        base=randint(250,1000)
                        base*=1000000
                        money+=base
                        win_amount+=base
                    else:
                        losses+=1
            except:
                pass
            print("Tickets Bought:",ticket_count)
            base=str("{:,}".format((int(win_amount))))
            print("Wins:",wins)
            print("Losses:",losses)
            div()
            print("Win Amount: £"+str(base))
            base=str("{:,}".format((int(tmw))))
            print("Theoretical Maximum Win: £"+base)
            br()
            if is_teen == 0:
                adult()
            else:
                teen()
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
        global edu_lvl
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
            global salary, hours
            salary=0
            hours=0
            global did_tutor
            did_tutor=0
            edu_lvl=1
            money=0
            stress=0
            mother_rel=0.8
            father_rel=0.8
            adult_init()
        else:
            raise ExitError
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
        print("[2] Respawn")
        try:
            ch=int(input(">"))
        except:
            ch=1
        if ch == 1:
            mainmenu()
        elif ch == 0:
            raise ExitError
        elif ch == 2:
            adult()
        else:
            mainmenu()
    def age_up():
        global salary, hours, expenses, happiness, health, intel, looks
        global mother_end_age, father_end_age, money
        global is_depressed, is_anxiety, savings, debt
        global year, is_job, work_e_base, pension, promo_base
        year += 1
        global happiness, intel
        global age
        global money, father_rel
        global did_tutor
        did_tutor=0
        #random stat change: if you have 10% or less health, you have a chance of dying!
        happiness+=(rng(-10,10)/100)
        health+=(rng(-10,10)/100)
        intel+=(rng(-10,10)/100)
        looks+=(rng(-10,10)/100)
        if age >= 6:
            basee=savings/10
            basee=int(basee)
            savings+=basee
            base=int(debt/5)
            debt+=base
            base=int(debt/10)
            money-=base
        if pension > 0:
            money+=pension
        global work_e, is_job
        if is_job == 1:
            work_e+=1
            work_e_base+=1
            promo_base+=1
        if promo_base == 5:
            promo_base=0
            promotion()
        global mother_age, father_age, edu_lvl
        age+=1
        mother_age+=1
        father_age+=1
        #when parents die
        if age >= 18 and is_job == 1:
            base=salary*hours*52
            money+=base
            money-=(expenses*12)
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
                    savings+=520
                elif father_rel < 0.75 and father_rel > 0.25:
                    savings+=260
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
            if happiness <= 0.1 and is_depressed == 0:
                is_depressed=1
                div()
                print("You are now suffering from DEPRESSION.")
            if is_depressed==1 and happiness < 0.65:
                happiness/=4
            if is_depressed == 1 and happiness >= 0.65:
                div()
                print("You are no longer suffering from DEPRESSION.")
                is_depressed=0
                happiness*=2
            from random import randint
            if age == 18:
                salary=0
                hours=0
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
            raise ExitError
    def pbar(percent):
            global alt_ui
            if percent > 1:
                    percent=1
            percent*=100
            bar="["
            hash=percent/5
            global alt_ui
            hash=int(hash)
            dot=20-hash
            for i in range(hash):
                    if alt_ui == 1 or alt_ui == 2:
                        bar+="|"
                    else:
                        bar+="#"
            for i in range(dot):
                    if alt_ui == 1 or alt_ui == 2:
                        bar+=" "
                    else:
                        bar+="."
            bar+="]"
            print(bar)
    def pbar2(percent):
            global alt_ui
            if percent > 1:
                    percent=1
            percent*=100
            bar="["
            hash=percent/5
            global alt_ui
            hash=int(hash)
            dot=20-hash
            for i in range(hash):
                    if alt_ui == 1 or alt_ui == 2:
                        bar+="|"
                    else:
                        bar+="#"
            for i in range(dot):
                    if alt_ui == 1 or alt_ui == 2:
                        bar+=" "
                    else:
                        bar+="."
            bar+="]"
            return bar
    def div():
        global alt_ui
        if alt_ui == 2:
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        elif alt_ui == 1:
            print("▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢")
        else:
            print("====================")
        return True
    def br():
        div()
        print("Press ENTER to continue")
        wer=input()
        return True
    def end():
        div()
        print("This menu is obsolete. This used to be the death screen.")
        print("Now, the anticheat gets triggered.")
        div()
        print("[1] Exit")
        print("[0] Main menu")
        try:
            ch=int(input(">>"))
        except:
            ch=1
        if ch == 1:
            while True:
                raise ExitError
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
                raise ExitError
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
                raise ExitError
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
            raise ExitError
    def job_interview():
        i=rng(1,10)
        div()
        print("Interview")
        div()
        if i == 1:
            print("Tea or coffee?")
            div()
            print("[1] Tea")
            print("[2] Coffee")
            print("[3] Both")
            print("[4] Neither")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 1 or ch == 2:
                return True
            else:
                return False
        elif i == 2:
            print("Any more questions?")
            div()
            print("[1] When do I start?")
            print("[2] What's the company ethos?")
            print("[3] How much is the pay?")
            print("[4] What's the corporate structure?")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 2 or ch == 4:
                return True
            else:
                return False
        elif i == 3:
            print("Which of these elements do you most associate with?")
            div()
            print("[1] Fire")
            print("[2] Earth")
            print("[3] Water")
            print("[4] Wind")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 2 or ch == 4:
                return True
            else:
                return False
        elif i == 4:
            print("Which Yu-Gi-Oh! character do you relate to most?")
            div()
            print("[1] Yugi Moto")
            print("[2] Seto Kaiba")
            print("[3] Maximillion Pegasus")
            print("[4] Mai Valentine")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 1 or ch == 2:
                return True
            else:
                return False
        elif i == 5:
            print("Which Harry Potter character do you relate to most?")
            div()
            print("[1] Harry Potter")
            print("[2] Dobby")
            print("[3] Rubeus Hagrid")
            print("[4] Albus Percival Wulfric Brian Dumbledore")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 2 or ch == 4:
                return True
            else:
                return False
        elif i == 6:
            print("Do you like BitLife")
            div()
            print("[1] Never heard of it.")
            print("[2] It's pay-to-win garbage.")
            print("[3] Yes!")
            print("[4] OpenLife is better.") #Not to blow my own trumpet.
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 2 or ch == 4:
                return True
            else:
                return False
        elif i == 7:
            print("What do you most value in a workplace?")
            div()
            print("[1] Cute female employess.")
            print("[2] A good workplace culture.")
            print("[3] Paid leave.")
            print("[4] Collaboration")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 2 or ch == 4:
                return True
            else:
                return False
        elif i == 8:
            print("What are your salary expectations?")
            div()
            print("[1] They align with my qualifications.")
            print("[2] Top dollar.")
            print("[3] What's a salary?")
            print("[4] I expect what's stated on the job offer.")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 1 or ch == 4:
                return True
            else:
                return False
        elif i == 9:
            print("Where do you see yourself in 5 years?")
            div()
            print("[1] Can't even see myself in five minutes!")
            print("[2] In a managerial position here.")
            print("[3] Retired :)")
            print("[4] As your boss.")
            print("[5] Not here!")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 2 or ch == 4:
                return True
            else:
                return False
        elif i == 10:
            print("What are your plans for education?")
            div()
            print("[1] I'll never stop learning.")
            print("[2] I stopped years ago.")
            print("[3] I imagine it'll come as a part of the job.")
            print("[4] I dropped out of primary school.")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 1 or ch == 3:
                return True
            else:
                return False
        else:
            return False
    def crime():
        div()
        adult_crime()
    def vacation():
        global money, happiness, debt
        print("[0] Return")
        print("[1] Cruise [£4 500]")
        print("[2] Vacation [£25 000]")
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            adult()
        elif ch == 1:
            if money >= 4500:
                money-=4500
            else:
                debt+=4500
            happiness+=0.45
            div()
            print("You went for a cruise.")
            print("Enjoyment:")
            pbar(0.65)
            adult()
        elif ch == 2:
            if money >= 25000:
                money-=25000
            else:
                debt+=25000
            happiness+=0.85
            div()
            print("You went for a cruise.")
            print("Enjoyment:")
            pbar(0.90)
            adult()
        else:
            adult()
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
        global money, happiness, looks, health, intel, debt
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age
        print("[0] Return")
        print("[1] Gym [£15f]")
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
        print("[13] Lottery")
        print("[x] Love")
        print("[x] Movies")
        print("[16] Nightlife")
        print("[17] Vacation")
        print("[x] Last Will And Testament")
        print("[19] Fertility")
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
            if money >= 15:
                money-=15
            else:
                debt+=15
            pbar(1)
            happiness+=0.45
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
                raise ExitError
            else:
                adult()
        elif ch == 5:
            div()
            print("Hidden ethics value:")
            pbar(ethics)
            div()
            print("[0] Return")
            print("[1] Max out looks")
            if allow_debug == 1:
                print("[2] Set Money")
                print("[x] Max Out Ethics")
            print("[4] Show Parents' Death Age")
            if allow_debug == 1:
                print("[5] Fix Alpha 12 PR3 Save File")
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
            elif ch == 5 and allow_debug == 1:
                print("WIP")
                div()
                print("Available saves:")
                path=os.getcwd()
                dirlist=os.listdir(path)
                for item in dirlist:
                    isFile=os.path.isfile(item)
                    if isFile == True and item.endswith(".oll2"):
                        item=item.replace(".oll2","")
                        print(item)
                    else:
                        continue
                div()
                #0=Alpha|1=12|2=happiness|3=health|4=intel|5=looks|6=ethics|7=money
                #|8=forename|9=surname|10=age|11=work_e|12=edu_lvl|13=work_e_base|14=promo_base
                #|15=degree|16=hours|17=salary|18=expenses|19=pension
                #|20=is_depressed|21=debt|22=savings|23=year|24=is_job|25=stress
                #|26=mother_name|27=father_name|28=mother_age|29=father_age
                #|30=mother_end_age|31=father_end_age
                sn=input("Enter File Name >")
                # Windows illegal filename characters removed
                sn=sn.replace("\\","")
                sn=sn.replace("/","")
                sn=sn.replace("?","")
                sn=sn.replace("*","")
                sn=sn.replace("|","")
                sn=sn.replace("<","")
                sn=sn.replace(">","")
                sn=sn.replace(":","")
                sn=sn.replace("\"","")
                sn+=".oll2" #file extension
                f=open(sn,"rb")
                try:
                    import codecs
                    ssave=f.read()
                    f.close()
                    ssave=codecs.decode(ssave,"base64_codec")
                    print(save)
                    ssave=ssave.decode('utf-8')
                    print(save)
                    save=ssave
                    print(save)
                    save+="|0"
                    save=save.encode('utf-8')
                    save=codecs.encode(save,"base64_codec")
                    f=open(fn,"wb")
                    f.write(save)
                    f.close()
                    div()
                    print("Save now no longer breaks Freelance section.")
                except:
                    div()
                    print("Failed.")
                    adult()
            elif ch == 3:
                adult()
            elif ch == 4:
                div()
                global mother_end_age, father_end_age, mother_age, father_age
                if mother_age < mother_end_age:
                    print("Mother will die at age",mother_end_age,"[Current age: "+str(mother_age)+"]")
                if father_age < father_end_age:
                    print("Father will die at age",father_end_age,"[Current age: "+str(father_age)+"]")
                br()
                adult()
            else:
                adult()
            adult()
        elif ch == 6:
            crime()
        elif ch == 13:
            lottery(0)
        elif ch == 17:
            vacation()
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
            if debt > 0:
                div()
                print("BOUNCER: Sorry. We cannot let in people who owe us money.")
                print("YOU: But I don't owe YOU money, I owe someone else money!")
                print("BOUNCER: Too bad.")
                br()
                adult()
            blackjack_init()
        elif ch == 16:
            print("[1] Partying")
            print("[x] One-Night Stand")
            print("[3] Drugs")
            print("[0] Return")
            div()
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 0:
                adult()
            if ch == 1:
                print("You partied.")
                print("Enjoyment:")
                pbar(0.85)
                happiness+=0.65
                health-=0.15
                intel-=0.25
                adult()
            elif ch == 3:
                print("[1] Cannabis")
                print("[2] Cocaine")
                print("[3] Heroin")
                print("[4] Gym Candy [Anabolic Stereoids]")
                print("[5] Crack")
                try:
                    ch=int(input(">"))
                except:
                    ch=0
                if ch == 0:
                    adult()
                else:
                    adult()
            else:
                adult()
        elif ch == 19:
            print("[0] Return")
            if age < 45:
                print("[1] Sperm Donation")
            print("[x] Vascetomy [£25 000]")
            try:
                ch=int(input(">"))
            except:
                adult()
            if ch == 0:
                adult()
            elif ch == 1 and age < 45:
                div()
                print("You donated sperm :(")
                print("You earned £25")
                money+=25
                adult()
            else:
                #this one
                adult()
        else:
            #this one
            adult()
    def promotion():
        global job_id, job_lvl, promo_base, salary
        if job_id == 1 or job_id == 4 or job_id == 11 or job_id == 14 or job_id == 17 or job_id == 19 or job_id == 21 or job_id == 22 or job_id == 26 or job_id == 28 or job_id == 29 or job_id == 30:
            job_lvl == 1
            adult()
        elif job_id == 18:
            if job_lvl == 2:
                adult()
            else:
                salary=65
        elif job_id == 18:
            if job_lvl == 23:
                adult()
            else:
                salary=35
        elif job_lvl < 3:
            job_lvl+=1
            print("You got promoted.")
            if job_id == 2:
                if job_lvl == 2:
                    salary=15
                else:
                    salary=20
            elif job_id == 3:
                if job_lvl == 2:
                    salary=40
                else:
                    salary=50
            elif job_id == 6:
                if job_lvl == 2:
                    salary=50
                else:
                    salary=70
            elif job_id == 8:
                if job_lvl==2:
                    salary=70
                else:
                    salary=90
            elif job_id == 9:
                if job_lvl == 2:
                    salary=55
                else:
                    salary=65
            elif job_id == 10:
                if job_lvl == 2:
                    salary=45
                else:
                    salary=55
            elif job_id == 12:
                if job_lvl == 2:
                    salary=40
                else:
                    salary=55
            elif job_id == 13:
                if job_lvl == 2:
                    salary=75
                else:
                    salary=95
            elif job_id == 15:
                if job_lvl == 2:
                    salary=45
                else:
                    salary=65
            elif job_id == 20:
                if job_lvl == 2:
                    salary=55
                else:
                    salary=75
            elif job_id == 25:
                if job_lvl == 2:
                    salary=35
                else:
                    salary=45
            elif job_id == 0:
                adult()
            print("New Salary: £"+str(salary))
            br()
            adult()
        else:
            adult()
    def job_menu():
        global is_job, salary, hours, min_hours, work_e_base, pension
        print("[0] Return")
        print("[1] Resign")
        print("[2] Adjust Hours")
        if work_e_base >= 20:
            print("[3] Retire & Take Pension")
        print("[x] Request Raise")
        print("[x] Request Promotion")
        div()
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            adult()
        elif ch == 1:
            div()
            print("You resigned :(")
            salary=0
            is_job=0
            hours=0
            work_e_base=0
        elif ch == 2:
            try:
                hours=int(input(">"))
            except:
                pass
            if hours < min_hours:
                hours=min_hours
            if hours > 70:
                hours=70
            adult()
        elif ch == 3 and work_e_base >= 20:
            div()
            base=salary*hours*52
            base/=2
            base=int(base)
            print("Your pension is £"+str(base),"per year.")
            pension+=base
            salary=0
            is_job=0
            hours=0
            work_e_base=0
            adult()
        else:
            adult()
    def adult_assets():
        global money, savings, debt
        div()
        print("[0] Return")
        print("[x] Shop")
        print("[x] Item List")
        print("[3] Loan")
        print("[4] Savings")
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            adult()
        elif ch == 3:
            div()
            
            print("Debt: £"+str("{:,}".format((int(debt)))))
            print("20% interest, 10% autopaid per year")
            div()
            print("[1] Loan")
            print("[2] Pay Off")
            print("[0] Return")
            try:
                ch=int(input(">"))
            except:
                adult()
            if ch == 0:
                adult()
            elif ch == 1:
                try:
                    loan=int(input(">"))
                except:
                    adult()
                if loan < 0:
                    loan=0
                debt+=loan
                money+=loan
                adult()
            elif ch == 2:
                if money < debt:
                    debt-=money
                    money=0
                    adult()
                else:
                    money-=debt
                    debt=0
                    adult()
            else:
                adult()
            
        elif ch == 4:
            print("Savings: £"+str("{:,}".format((savings))))
            print("Interest: 10%")
            div()
            print("[0] Return")
            print("[1] Deposit")
            print("[2] Withdraw")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 0:
                adult()
            elif ch == 1:
                print("Money: £"+str("{:,}".format((money))))
                try:
                    dep=int(input(">"))
                except:
                    adult()
                if money < dep:
                    dep=money
                if dep < 0:
                    dep=0
                money-=dep
                savings+=dep
                savings=int(savings)
                adult()
            elif ch == 2:
                print("Savings: £"+str("{:,}".format((savings))))
                try:
                    wit=int(input(">"))
                except:
                    adult()
                if wit > savings:
                    wit=savings
                if wit < 0:
                    wit=0
                money+=wit
                savings-=wit
                adult()
            else:
                adult()
        else:
            adult()
    def occupation():
        global edu_lvl, money, is_job
        global did_tutor, salary, hours
        div()
        print("Salary: £"+str(salary)+"/h")
        print("Hours: "+str(hours))
        print("Salary Per Year: £"+str(salary*hours*52))
        div()
        print("[0] Return")
        print("[1] Education")
        if is_job == 1:
            print("[2] Job Menu")
        print("[x] Part-Time Jobs")
        print("[3] Freelance")
        print("[x] Job Recruiter")
        print("[5] Jobs")
        print("[x] Special Careers")
        print("[x] Local Gangs")
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            adult()
        elif ch == 5:
            job_centre()
        elif ch == 2 and is_job == 1:
            job_menu()
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
                    br()
                    adult()
                else:
                    div()
                    print("You did tutoring already.")
                    br()
                    adult()
            elif ch == 2:
                base=18*30
                div()
                adult()
                print("You became a handyman for 30 hours this week.")
                print("You made £"+str(base))
                br()
                money+=base
                adult()
            elif ch == 3:
                base=30*17
                adult()
                print("You became a truck driver for 30 hours this week.")
                print("You made £"+str(base))
                money+=base
                br()
                adult()
            else:
                adult()
        else:
            adult()
    def adult_load():
        div()
        print("This is obsolete.")
        mainmenu()
        div()
        #      0             1            2                 3               4                5              6           7                   8                 9                 10         11                 12                13                  14           
        #save=forename+"|"+surname+"|"+str(age)+"|"+str(happiness)+"|"+str(looks)+"|"+str(health)+"|"+str(ethics)+"|"+str(intel)+"|"+str(mother_rel)+"|"+str(father_rel)+str(money)+"|"+mother_name+"|"+father_name+"|"+str(mother_age)+"|"+str(father_age)
        #John|Sith|18|1|0.9|0.8|0.7|0.6|1|1|12000|Jill|Shill|32|35
        sn=input("Save Name >")
        sn+=".oll"
        try:
            f=open(sn,"rb")
        except:
            mainmenu()
        import codecs
        save=f.read()
        save=codecs.decode(save,"base64_codec")
        save=save.decode('utf-8')
        save=("John|Sith|18|1|0.9|0.8|0.7|0.6|1|1|12000|Jill|Shill|32|35")
        print(save)
        save=save.replace("||","|")
        save=save.split("|")
        print(save)
        global mother_age, father_age
        global mother_name, father_name
        global juvie_offences
        global happiness, health, intel, looks, ethics, grades, clout, socialc
        global mother_rel, father_rel
        forename=save[2]
        surname=save[3]
        age=int(save[4])
        happiness=float(save[5])
        looks=float(save[6])
        health=float(save[7])
        ethics=float(save[8])
        intel=float(save[9])
        mother_rel=float(save[10])
        father_rel=float(save[11])
        money=int(save[12])
        mother_name=save[13]
        father_name=save[14]
        mother_age=int(save[15])
        father_age=int(save[16])
        br()
        adult()
    def adult_pause():
        global is_depressed, money, happiness, looks, intel, ethics, health, salary, hours
        global mother_age, father_age
        global mother_name, father_name
        global juvie_offences
        global happiness, health, intel, looks, ethics, grades, clout, socialc
        global mother_rel, father_rel, mother_end_age, father_end_age
        global edu_lvl, degree
        div()
        print("Game Paused.")
        div()
        print("[0] Resume")
        print("[1] Save Life")
        print("[2] Load Life")
        print("[3] Exit To Main Menu")
        div()
        print("[x] Download Challenge From Web")
        print("[x] Load Challenge From File")
        print("[x] Check For Updates")
        div()
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            adult()
        elif ch == 1:
            save_game()
            adult()
        elif ch == 2:
            print("[0] Cancel")
            print("[1] Exit and Save")
            print("[2] Exit Without Saving")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 1:
                save_game()
                load_game()
            elif ch == 2:
                load_game()
            else:
                adult_pause()
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
                save_game()
                mainmenu()
            elif ch == 2:
                div()
                mainmenu()
            else:
                adult()
        else:
            adult()
    def adult():
        global edu_lvl, pension, job_lvl
        global salary, hours
        global allow_debug
        global mother_age, father_age
        global mother_name, father_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel
        global money, is_depressed, work_e, is_job
        global job_id, job_lvl
        global money
        money=int(money)
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
        div()
        print(forename+" "+surname)
        if pension > 0:
            print("Pensioner")
        elif money >= 5000000 and is_job == 0 and money < 400000000000:
            print("Independently Wealthy")
        elif is_job == 1:
            if job_id == 1:
                print("Amazon Delivery Driver")
            elif job_id == 2:
                print("Jr Translator")
            elif job_id == 3:
                print("Jr Accountant")
            elif job_id == 4:
                print("Exorcist")
            elif job_id == 5:
                print("Teacher")
            elif job_id == 6:
                print("Jr Game Developer")
            elif job_id == 8:
                print("Jr Lawyer")
            elif job_id == 9:
                print("Jr App Developer")
            elif job_id == 10:
                if job_lvl == 1:
                    print("Jr Banker")
                elif job_lvl == 2:
                    print("Banker")
                else:
                    print("Sr Banker")
            elif job_id == 11:
                print("Monk")
            elif job_id == 12:
                print("Jr Wedding Planner")
            elif job_id == 13:
                if job_lvl == 1:
                    print("Engineer I")
                elif job_lvl == 2:
                    print("Engineer II")
                else:
                    print("Engineer III")
            elif job_id == 14:
                print("Data Scientist")
            elif job_id == 15:
                print("Private [Army]")
            elif job_id == 17:
                print("Cashier")
            elif job_id == 18:
                print("College Lecturer")
            elif job_id == 19:
                print("Oohber Driver")
            elif job_id == 20:
                if job_lvl == 1:
                    print("Jr Editor")
                elif job_lvl == 2:
                    print("Editor")
                else:
                    print("Senior Editor")
            elif job_id == 21:
                print("Exotic Dancer")
            elif job_id == 22:
                print("Flight Attendant")
            elif job_id == 23:
                if job_lvl == 1:
                    print("Apprentice Hairdresser")
                else:
                    print("Hairdresser")
            elif job_id == 25:
                print("Librarian")
            elif job_id == 26:
                print("Nun")
            elif job_id == 28:
                print("P*rnographer")
            elif job_id == 29:
                print("Jr Stockbroker")
            elif job_id == 30:
                print("Publicity Stuntperson")
            else:
                print("Corporate Slave")
        elif money >= 400000000000 and is_job == 0:
            print("Richest In The World")
        else:
            print("Unemployed")
        div()
        print("Age",age)
        print("£"+str("{:,}".format((money))))
        div()
        if edu_lvl == 1:
            print("Education: High School")
        elif edu_lvl == 2 and degree == 1:
            print("Education: University [Finance]")
        elif edu_lvl == 2 and degree == 2:
            print("Education: University [Journalism]")
        elif edu_lvl == 2 and degree == 3:
            print("Education: University [Computer Science]")
        elif edu_lvl == 2 and degree == 4:
            print("Education: University [Education]")
        elif edu_lvl == 2 and degree == 5:
            print("Education: University [Accounting]")
        elif edu_lvl == 2 and degree == 6:
            print("Education: University [Political Science]")
        elif edu_lvl == 2 and degree == 7:
            print("Education: University [Nursing]")
        elif edu_lvl == 2 and degree == 8:
            print("Education: University [Psychology]")
        elif edu_lvl == 2 and degree == 9:
            print("Education: University [Engineering]")
        elif edu_lvl == 2 and degree == 10:
            print("Education: University [Art History]")
        elif edu_lvl == 2 and degree == 11:
            print("Education: University [Communications]")
        elif edu_lvl == 2 and degree == 12:
            print("Education: University [Graphic Design]")
        elif edu_lvl == 2 and degree == 13:
            print("Education: University [Data Science]")
        elif edu_lvl == 2 and degree == 14:
            print("Education: University [Criminal Justice]")
        elif edu_lvl == 2 and degree == 15:
            print("Education: University [Linguistics]")
        elif edu_lvl == 2 and degree == 16:
            print("Education: University [Marketing]")
        elif edu_lvl == 3:
            print("Education: Grad School")
        elif edu_lvl == 0:
            print("Education: N/A")
        print("Work Experience:",work_e,"Years")
        global work_e_base
        if is_depressed == 1:
            div()
            print("Suffers from: Depression")
        div()
        if happiness >= 0.9:
            print("Happiness:",pbar2(happiness),str(int(happiness*100))+"% :D")
        elif happiness <= 0.25:
            print("Happiness:",pbar2(happiness),str(int(happiness*100))+"% :(")
        else:
            print("Happiness:",pbar2(happiness),str(int(happiness*100))+"%")
        if health <= 0.25:
            print("Health:   ",pbar2(health),str(int(health*100))+"% [!]")
        elif health >= 0.9:
            print("Health:   ",pbar2(health),str(int(health*100))+"% <3")
        else:
            print("Health:   ",pbar2(health),str(int(health*100))+"%")
        if intel <= 0.25:
            print("Smarts:   ",pbar2(intel),str(int(intel*100))+"% [!]")
        elif intel >= 0.9:
            print("Smarts:   ",pbar2(intel),str(int(intel*100))+"% :)")
        else:
            print("Smarts:   ",pbar2(intel),str(int(intel*100))+"%")
        if looks >= 0.9:
            print("Looks:    ",pbar2(looks),str(int(looks*100))+"% :O")
        elif looks <= 0.25:
            print("Looks:    ",pbar2(looks),str(int(looks*100))+"% :(")
        else:
            print("Looks:    ",pbar2(looks),str(int(looks*100))+"%")
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
            if mother_end_age > mother_age:
                print(mother_name)
                print("Mother [Age "+str(mother_age)+"]")
                pbar(mother_rel)
                print("[1] Interact")
                div()
            if father_end_age > father_age:
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
            if ch == 1 and mother_end_age > mother_age:
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
            
            elif ch == 2 and father_end_age > father_age:
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
        print("Clout and social currency have been removed.")
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
        global money, fake_id, happiness, health
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
        print("[5] Pistol [£750][GANG]")
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 0:
            teen_assets()
        elif ch == 1:
            if money >= 450 and fake_id ==0:
                money-=450
                fake_id=1
                div()
                print("You bought a fake ID.")
                teen()
            else:
                div()
                print("You cannot afford/already have that!")
                teen()
        elif ch == 2:
            if money >= 10 and fake_id == 1:
                money-=10
                happiness+=0.25
                health-=0.55
                div()
                print("You had a beer.")
                teen()
            else:
                div()
                print("You cannot afford this and/or you don't have a fake ID.")
                teen()
        elif ch == 3:
            if money >= 25 and fake_id == 1:
                money-=25
                happiness+=0.50
                health-=0.75
                div()
                print("You smoked 20 cigarettes at once. Talk about addiction.")
                teen()
            else:
                div()
                print("You cannot afford this and/or you don't have a fake ID.")
                teen()
        elif ch == 4:
            div()
            print("Locked.")
            teen()
        elif ch == 5:
            div()
            print("Locked.")
            teen()
        else:
            teen_assets()
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
                raise ExitError
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
    def teen_pause():
        print("[0] Resume")
        print("[x] Save Life")
        print("[x] Load Life")
        print("[3] Exit To Main Menu")
        div()
        print("[x] Download Challenge From Web")
        print("[x] Load Challenge From File")
        print("[x] Check For Updates")
        div()
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 3:
            print("[x] Exit and Save")
            print("[2] Exit Without Saving")
            print("[0] Resume")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 2:
                mainmenu()
            else:
                teen()
        else:
            teen()
    def child_pause():
        print("[0] Resume")
        print("[x] Save Life")
        print("[x] Load Life")
        print("[3] Exit To Main Menu")
        div()
        print("[x] Download Challenge From Web")
        print("[x] Load Challenge From File")
        print("[x] Check For Updates")
        div()
        try:
            ch=int(input(">"))
        except:
            ch=0
        if ch == 3:
            print("[x] Exit and Save")
            print("[2] Exit Without Saving")
            print("[0] Resume")
            try:
                ch=int(input(">"))
            except:
                ch=0
            if ch == 2:
                mainmenu()
            else:
                child()
        else:
            child()
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
        print("Clout:          ",pbar2(clout),str(int(clout*100))+"%")
        print("Social Currency:",pbar2(socialc),str(int(socialc*100))+"%")
        div()
        print("Happiness:",pbar2(happiness),str(int(happiness*100))+"%")
        print("Health:   ",pbar2(health),str(int(health*100))+"%")
        print("Smarts:   ",pbar2(intel),str(int(intel*100))+"%")
        print("Looks:    ",pbar2(looks),str(int(looks*100))+"%")
        div()
        print("[1] School")
        print("[2] Assets")
        print("[0] Age Up")
        print("[3] Relationships")
        print("[4] Activities")
        print("[5] Paue Menu")
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
        elif ch == 5:
            teen_pause()
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
            raise ExitError
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
        print("Happiness:",pbar2(happiness),str(int(happiness*100))+"%")
        print("Health:   ",pbar2(health),str(int(health*100))+"%")
        print("Smarts:   ",pbar2(intel),str(int(intel*100))+"%")
        print("Looks:    ",pbar2(looks),str(int(looks*100))+"%")
        div()
        print("[1] School")
        print("[2] Assets")
        print("[0] Age Up")
        print("[3] Relationships")
        print("[4] Activities")
        print("[5] Pause Menu")
        try:
            ch=int(input(">"))
        except:
            child()
        if ch == 1:
            primary_school_menu()
        elif ch == 5:
            child_pause()
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
            raise ExitError
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
            print("Happiness:",pbar2(happiness),str(int(happiness*100))+"%")
            print("Health:   ",pbar2(health),str(int(health*100))+"%")
            print("Smarts:   ",pbar2(intel),str(int(intel*100))+"%")
            print("Looks:    ",pbar2(looks),str(int(looks*100))+"%")
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
        global forename_m, forename_f, salary, hours
        salary=0
        hours=0
        global edu_lvl
        edu_lvl=0
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
            raise ExitError
    def mainmenu():
        game_init()
        global alt_logo
        div()
        import os
        startpoint=os.getcwd()
        challenge_site="" #change this URL if the location changes / you want to add custom challenges
        if alt_logo == 1:
            logo=[' .d88888b.                             888      d8b  .d888         ', 'd88P" "Y88b                            888      Y8P d88P"          ', '888     888                            888          888            ', '888     888 88888b.   .d88b.  88888b.  888      888 888888 .d88b.  ', '888     888 888 "88b d8P  Y8b 888 "88b 888      888 888   d8P  Y8b ', '888     888 888  888 88888888 888  888 888      888 888   88888888 ', 'Y88b. .d88P 888 d88P Y8b.     888  888 888      888 888   Y8b.     ', ' "Y88888P"  88888P"   "Y8888  888  888 88888888 888 888    "Y8888  ', '            888                                                    ', '            888                                                    ', '            888                                                    ']
        else:
            logo=['________                           .____     .__   _____         ', '\\_____  \\  ______    ____    ____  |    |    |__|_/ ____\\ ____   ', ' /   |   \\ \\____ \\ _/ __ \\  /    \\ |    |    |  |\\   __\\_/ __ \\  ', '/    |    \\|  |_> >\\  ___/ |   |  \\|    |___ |  | |  |  \\  ___/  ', '\\_______  /|   __/  \\___  >|___|  /|_______ \\|__| |__|   \\___  > ', '        \\/ |__|         \\/      \\/         \\/                \\/  ', '                                                                 ']
        for l in logo:
            print(l)
        div()
        print("[1] New Life")
        print("[2] Load Life")
        print("[3] Credits")
        print("[4] Download Latest Challenge") #Download location: https://winfan3672.000webhostapp.com/challenge/latest.py
        print("[x] Load Challenge.zip from disk")
        print("[6] Exit")
        print("[7] Changelog")
        print("[x] Download Latest Custom Life") #Download location: N/A
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
            raise ExitError
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
        elif ch == 2:
            load_game()
        elif ch == 3:
            div()
            print("99% of the code was written by WinFan3672 [winfan3672@gmail.com]")
            print("The logo for the game was generated by textkool.com.")
            div()
            print("Resources:")
            print("The forenames and surnames were created by MufasaKermitsSuicide.")
            print("The hosting for the challenges is provided by 000webhost.")
            div()
            print("Thank you for playing the most ambitious programming project I have taken on.")
            div()
            print("And special thanks to fungamer2 for:")
            print("[-] Finding my project")
            print("[-] Allowing me to help out on his one [https://github.com/fungamer2-2/Life-Simulator1]")
            print("[-] Generally being a nice guy")
            br()
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
                mainmenu()
            div()
            print("Downloaded challenge.")
            mainmenu()
        elif ch == 7:
            changelog=['Alpha 12: The Job Update Pt. II', '===============', 'Section 0: Introdution', '===============', 'You can ignore this section. It contains no changelog information.', '===============', 'This update is by far the biggest so far, more so than the previous one. I am really proud of the mechanics introduced, and cannot wait for more to come. In fact, this update has added so much, that I barely know what to add now. ', '', "There is a [nearly] working savegame [with a new .OLL2 file extension] that allows you to load 99% of your character into the game, with a few things either set or randomised due to me forgetting to add them to the save file. Sadly, the old .OLL files are obsolete, and may not be back for a while. I will add a conversion utility eventually, but a lot of variables would have to be randomised. It isn't hard to do, it's just that I don't want to add it just yet. It's only an alpha game, after all.", '', 'When new updates come out, backwards compatibility will be a top priority. However, for obvious reasons, forwards compatibility will be impossible. Saves will be able to be converted to the latest version and launched. Naturally, a lot of data will be missing and will have to get added, but it should be doable, unless I rewrite the whole game from scratch or something. ', '', 'This update was originally going to be called "The Teen Update Part II", but I quickly realised how little BitLife has in terms of the teen stage anyway, so I didn\'t have much to add.', '', 'This update took forever to make, and I had so much to do, but I did it. I like how it turned out, and this game feels more and more fleshed out the more I add. ', '', 'Alpha 13 will be the Childbirth Update. It will allow you to:', '[-] Find love', '[-] Make love', '[-] Marry', '[-] Have up to 8 children', '   [-] You will be able to have more in future. ', '===============', 'Section 1: Teen Stage', '[-] Added teen shop', '   [-] Sells basic commodities', '   [-] No items that you can get permanently', '[-] Added Fake ID Hub', '   [-] Allows you to use your fake ID to do things you normally would not be able to.', '===============', 'Section 2: Lottery Tweaks', 'We have made a few "tweaks" to the lottery system to make it more fair.', '[-] Odds changed from 1 in 100 million to 1 in 100 thousand.', '[-] You can only buy as many tickets as you can afford.', '[-] When you win a ticket[s], it shows you how many tickets you have played so far.', '[-] Ticket Price increased from Â£10 to Â£100', '', '===============', 'Infinite Money Exploit', '===============', '1. Loan Â£1,000,000,000', '2. Buy 10,000,000 lottery tickets', '3. Pay off the loan in full, since you can now afford to do that.', '4. Buy lottery tickets for a guaranteed return on investment.', '===============', '', 'Section 3: Jobs', 'We have added even MORE features to jobs in order to win.', '[-] Pensions', '   [-] When you work for a company for 20 years, you can take ', "   a pension. You don't work and earn 50% of your wages.", '[-] Promotions', '   [-] Every 5 years you get promoted if you can be.', '', 'Section 4: Save Game', '[-] Proper working savegame :o', '   [-] Uses .ool2 save format now', '[-] You can LOAD the game!', '===============', 'Notes for old saves [Alpha 11 and older]', '', 'These old saves [with a .oll file extension] DO NOT LOAD. They probably will not have backwards-compatibility due to a lack of saved variables.', "You may be able to reverse-engineer a save file, but it isn't worth it since the game has very few working features.", '', 'I may add a utility to port the save files in future, but that will be way in the future and also quite unlikely.', '', '===============', 'Notes for Alpha 12 Pre-Releases 1-3', '', 'These releases may use the .oll2 file extension used by OpenLife lives, but their saves are incompatible with this release, due to using a different save system. ', '===============', '', 'Section 5: Anticheat Upgrades', '===============', 'The anticheat has become even more powerful. You can no longer do anything, even if you reach the console. This is because ExitError is raised when you exit the game. This wipes every single user-created object from the game, including variables and functions. This means that every single line of game code gets destroyed, making it impossible to edit values without manually rewriting the code into the interpreter.', '', 'Section 6: General Additions', '===============', '[-] Custom forenames/surnames', '   [-] Create male.dat for male forenames', '   [-] female.dat for female forenames', '   [-] surname.dat for surnames', '   [-] Each file can contain a list of custom surnames,', '       each split by a new line.', '   [-] This allows you to enhance the game experience and ', '       have more variety with names.', '[-] In the main menu, there is a new option to download thelatest character. It is currently unused.', '   [-] You will be able to download a .oll2 file from the WinFan3672 FTP server and have a custom life to use in OL.This will be implemented later.', '[-] Loans', '   [-] 20% interest', '      [-] Automatically pays off 10% per year', '      [-] As a result,your debt increases forever unless you pay it off in full. ', '   [-] Can pay off loan at once', '   [-] Used for:', '      [-] Student Loan', '      [-] Loan', '   [-] No Limit', '[-] Savings Account', '   [-] Withdraw / Deposit', '   [-] 5% per year', '   [-] Compound interest', '   [-] No limit', '[-] Vacation', '   [-] Increases happiness', '   [-] Costs money', '[-] Fertility', '   [-] Sperm Donation', '      [-] Pay Â£50 per year', '[-] Random Stat Changes', '   [-] Stats increase between -10% and +10% each year', '   [-] I was an idiot when developing this and forgot to divide by 100, resulting in either max stats or death.', '', 'Section 7: Minor Tweaks/Bug Fixes', '[-] The game now SELF DESTRUCTS when it exits, meaning you cannot cheat anymore :)', '[-] Job #28 requires 80%+ looks to get [as originally intended]', '[-] Fixed pretty much all bugs where things like pensions would carry over to the next life if you exit to the main menu and made a new life', '[-] All currency errors showing dollars are GONE. The pound is now consistent.', "[-] When you bust in Blackjack, all that goes into a loan. That's right, gambling debt.", '[-] Going to the gym increases your happiness by 45%, up from 25%.', '', 'Section 8: Bugs', '===============', '[-] A lot of variables are not saved in the OLL2 save file.', '   [-] This will be rectified in A13.', '   [-] The variables [that I know of] are:', '      [-] mother_rel', '      [-] father_rel', '      [-] did_tutor', '   [-] These will not be fixed right now for compatibility reasons, since Alpha 12 PR3 save files would be broken, and also because I would have a lot of broken save files.', '[-] Not all of the job roles have a text, instead saying "Corporate Slave".', '', 'Section 9: Suspected bugs', '===============', '[-] The anticheat is bypassable, somehow. I just know it.', "[-] The promotions system definitely has issues that I don't know about. Report them, please.", '===============', 'Build Date  : 7 Oct 2022', 'Release Date: 7 Oct 2022', 'Next Update : The Childbirth Update']
            for l in changelog:
                if l == '===============':
                    div()
                else:
                    print(l)
            br()
            mainmenu()
        else:
            div()
            print("That option is not available in the current build of the game")
            div()
            mainmenu()
    mainmenu()
except KeyboardInterrupt:
    try:
        print("The anticheat caught you.")
        wer=input()
        div()
        print("The game has self-destructed.")
        print("You now cannot cheat, because there is no game :)")
        div()
        print("If you can see this, close the window.")
        div()
        objects = dir()
        for obj in objects:
          if not obj.startswith("__"):
              del globals()[obj]
    except:
        div()
        print("The game has self-destructed.")
        print("You now cannot cheat, because there is no game :)")
        div()
        print("If you can see this, close the window.")
        div()
        objects = dir()
        for obj in objects:
          if not obj.startswith("__"):
              del globals()[obj]
except LifeCreatorError:
    pass
except FeatureNotInGameError:
    div()
    print("FeatureNotInGameError")
    div()
    print("This feature does not exist in the game.")
    br()
    mainmenu()
except ExitError:
    if allow_debug == 1:
        #https://www.geeksforgeeks.org/viewing-all-defined-variables-in-python/
        #Lists all variables in order to quickly see what to add to save file system
        #Very useful for not having to look at the code
        all_variables = dir()
          
        # Iterate over the whole list where dir( )
        # is stored.
        for name in all_variables:
            
            # Print the item if it doesn't start with '__'
            if not name.startswith('__'):
                myvalue = eval(name)
                print(name, "is", type(myvalue), "and is equal to ", myvalue)

    #Code from: https://maschituts.com/how-to-clear-variables-in-python-explained/
    div()
    print("The game has self-destructed.")
    print("You now cannot cheat, because there is no game :)")
    div()
    print("If you can see this, close the window.")
    div()
    objects = dir()
    for obj in objects:
      if not obj.startswith("__"):
          del globals()[obj]
