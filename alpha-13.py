# OpenLife Alpha 13

# OpenLife is a FOSS replacement for BitLife.
# For years, BitLife has become worse and worse, so I decided to step in and
# replace it with this. It's way better. Trust me.
from random import randint as rng
from random import choice
import os


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = 0
        self.relation = 1
        self.end_age = rng(35, 85)


class SpouseRecompile:
    # This is a class that is used in load_game()
    # in order to rebuild the spouse object
    def __init__(self, name, rel, lvl, age, end):
        self.name = name
        self.age = age
        self.end = end
        self.rel = rel
        self.lvl = lvl


class Spouse:
    def __init__(self, name, relation, relationship_level, your_age):
        # This class is used for creating a spouse.
        # It includes all necessary data.
        # The `your age` parameter refers to the player character's age
        self.name = name
        self.age = your_age + rng(-5, 5)
        if self.age < 19:
            self.age = 19
        self.end = (
            rng(10, 35) + self.age
        )  # This means you will [almost] always outlive your spouse.
        self.rel = relation

        # Level 1 = Girlfriend/Boyfriend
        # Level 2 = Married
        self.lvl = relationship_level

    def recompile(self, name, rel, rel_lvl, age, end):
        # Used for loading the game
        # It rebuilds the `spouse` object as necessary
        self.name = name
        self.age = age
        self.end = end
        self.rel = rel
        self.lvl = rel_lvl


class Parent:
    def __init__(self, name, gender, end_age, relations, char_age):
        self.gender = gender
        if self.gender == 1:
            self.age = char_age + 32
        else:
            self.age = char_age + 37
        self.name = name
        self.end_age = rng(50, 85)
        self.relations = 0.75


class ExitError(Exception):
    # This one is used to nuke the game by deleting all variables.
    # I had to put everything into an except statement because
    # it would raise 3 errors and not delete anything.
    pass


class reboot(Exception):
    # type raise reboot to reboot the game!
    def __init__(self):
        mainmenu()


class GeneralException(Exception):
    pass


class FeatureNotInGameError(Exception):
    pass


class LifeCreatorError(Exception):
    # used for when an error occurs in the life creation process
    def __init__(self):
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("LifeCreatorError")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("The LifeCreator experienced an error and has exit the program.")
        print("The game will restart.")
        input("Press ENTER to continue.")
        mainmenu()


openlife_dir = "openlife_saves"
try:
    os.chdir(openlife_dir)
except:
    os.mkdir(openlife_dir)
    os.chdir(openlife_dir)
try:

    def game_init():

        # Configurable data
        # used by me [and potentially you!] to configure how the game works
        # I am putting it at the top for quick and easy access
        # No more CTRL+F :>

        # Debug options
        global allow_debug, allow_test
        allow_debug = 0  # Some debug commands are hidden behind this flag, and ExitError spits out a load of debug info upon exiting
        allow_test = (
            0  # Allows for some test features to be enabled. Currently does nothings
        )

        # 0=Original UI style [Looks kinda bad when you compare it to the others]
        # 1=Experimental UI style [with squares] [Never used] [Ugly]
        # 2=New UI Style [Looks great in cmd]
        # 3= "Throwback Mode" [a tribute to the original theme]

        # It is set to `2` by default

        global alt_ui
        alt_ui = 2

        global alt_logo, game_name, version
        # 0= Original logo [Alphas 1-10]
        # 1= Current logo
        # 2= "Throwback Mode" logo

        # It is set to `1` by default
        alt_logo = 1

        global game_name, version
        game_name = "OpenLife"
        version = "Alpha 13 [26 Oct 2022]"

        global app_version, sub_version
        app_version = [0, 0, 13]
        sub_version = 0

        # Set this to 0 to hide the loaded forenames message
        verbose_message = 1

        # Non-configurable data
        global currency
        currency = "£"  # this works across the entire platform
        global child_count
        child_count = 0
        global work_e, work_e_base, promo_base
        work_e = 0  # work experience
        promo_base = 0
        work_e_base = 0  # resets each time you quit your job & is a hidden value
        promo_base = 0
        global is_spouse
        is_spouse = 0
        global part_time_salary, teen_salary, teen_hours
        part_time_salary = 0
        teen_salary = 0
        teen_hours = 0
        global forename_m, forename_f, surnames, gang_names
        global auto_deposit
        auto_deposit = 0  # Set to 1 to automatically send all your money to savings account every year
        # Taken from https://github.com/MustafaKermitsSuicide/BitLife
        forename_m = [
            "Oliver",
            "Jacob",
            "Mason",
            "Harry",
            "William",
            "Alfie",
            "Jayden",
            "Charlie",
            "Noah",
            "Thomas",
            "Michael",
            "Ethan",
            "Joshua",
            "Alexander",
            "George",
            "Aiden",
            "James",
            "Daniel",
            "Jack",
            "Bruno",
            "Donald",
            "Nick",
            "Harvey",
            "Alfie",
            "Archie",
            "Ollie",
            "Louie",
            "Jenson",
            "Lewis",
            "Louis",
            "Callum",
            "Freddie",
            "Theo",
            "Toby",
            "Harley",
            "Reuben",
            "Kian",
            "Bobby",
            "Stanley",
        ]
        forename_f = [
            "Olivia",
            "Sophie",
            "Isabella",
            "Emily",
            "Emma",
            "Lily",
            "Amelia",
            "Ava",
            "Jessica",
            "Ruby",
            "Abigail",
            "Chloe",
            "Madison",
            "Grace",
            "Mia",
            "Evie",
            "Laura",
            "Maisie",
            "Poppy",
            "Freya",
            "Imogen",
            "Florence",
            "Rosie",
            "Hollie",
            "Isobel",
            "Niamh",
            "Harriet",
            "Tilly",
            "Maisy",
            "Holly",
            "Matilda",
            "Amelie",
            "Esme",
            "Zara",
            "Tia",
            "Aimee",
            "Martha",
            "Libby",
        ]
        surnames = [
            "Smith",
            "Johnson",
            "Williams",
            "Jones",
            "Brown",
            "Davis",
            "Miller",
            "Wilson",
            "Moore",
            "Taylor",
            "Anderson",
            "Thomas",
            "Jackson",
            "White",
            "Harris",
            "Martin",
            "Thompson",
            "Garcia",
            "Martinez",
            "Robinson",
            "Clark",
            "Rodriguez",
            "Lewis",
            "Lee",
            "Walker",
            "Hall",
            "Allen",
            "Young",
            "Hernandez",
            "King",
            "Wright",
            "Lopez",
            "Hill",
            "Scott",
            "Green",
            "Adams",
            "Baker",
            "Gonzalez",
            "Nelson",
            "Carter",
            "Mitchell",
            "Perez",
            "Roberts",
            "Turner",
            "Phillips",
            "Campbell",
            "Parker",
            "Evans",
            "Edwards",
            "Collins",
            "Stewart",
            "Sanchez",
            "Morris",
            "Rogers",
            "Reed",
            "Cook",
            "Morgan",
            "Bell",
            "Murphy",
            "Bailey",
            "Rivera",
            "Cooper",
            "Richardson",
            "Cox",
            "Howard",
            "Ward",
            "Torres",
            "Peterson",
            "Gray",
            "Ramirez",
            "James",
            "Watson",
            "Brooks",
            "Kelly",
            "Sanders",
            "Price",
            "Bennett",
            "Wood",
            "Barnes",
            "Ross",
            "Henderson",
            "Coleman",
            "Jenkins",
            "Perry",
            "Powell",
            "Log",
            "Patterson",
            "Hughes",
            "Flores",
            "Washington",
            "Butler",
            "Simmons",
            "Foster",
            "Gonzales",
            "Bryant",
            "Alexander",
            "Russell",
            "Griffin",
            "Diaz",
            "Hayes",
        ]
        gang_names = ["[PLACEHOLDER]"]
        global enemy_gang_name, enemy_gang_rel, enemy_gang_lead
        enemy_gang_name = choice(gang_names)
        enemy_gang_lead = 1
        enemy_gang_rel = 0.5
        try:
            # If you create a file called male.dat in your openlife save folder,
            # You can add custom male forenames. Each forename
            # is split by a new line
            f = open("male.dat", "r")
            data = f.read()
            forename_m = data.split("\n")
            if verbose_message == 1:
                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                print("Loaded Custom Male Forenames.")
        except:
            pass
        try:
            # If you create a file called female.dat in your openlife save folder,
            # You can add custom female forenames. Each forename
            # is split by a new line
            f = open("female.dat", "r")
            data = f.read()
            forename_f = data.split("\n")
            if verbose_message == 1:
                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                print("Loaded Custom Female Forenames.")
        except:
            pass
        try:
            f = open("surname.dat", "r")
            data = f.read()
            surname = data.split("\n")
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("Loaded Custom Surnames.")
        except:
            pass

        global edu_lvl, job_id, job_lvl
        edu_lvl = 1

        global pension
        pension = 0  # yearly pension
        job_id = 0
        job_lvl = 1

        from time import strftime

        global year
        year = strftime("%Y")
        year = int(year)

        global debt, savings
        savings = 0
        debt = 0

        global hours, min_hours, salary, expenses
        salary = 0
        hours = 0
        min_hours = 0
        expenses = 0

        global juvie_offences
        global is_job
        juvie_offences = 0
        global is_depressed
        global degree
        is_depressed = 0
        degree = 0
        global club_count
        global stress
        global is_sch_gang
        is_sch_gang = 0  # teen school gang
        stress = 0
        global fake_id, is_drip
        global is_job
        is_job = 0
        fake_id = 0
        is_drip = 0
        club_count = 0

        return True

    def die(reason):
        global age, forename, surname, is_depressed
        div()
        print(f"{game_name} Times")
        print("The *best* newspaper since 2022 AD")
        if reason == 0:
            div()
            print(f"{forename} {surname} commits suicide, aged {age}")
            div()
            print(
                f"{forename} {surname} recently died of an alleged suicide while at their home."
            )
            print(
                "Family members are reportedly distraght as a result of hearing the news."
            )
            print(
                f"\n{forename} {surname} lived a long, happy life, which they wasted in an instant by performing the act of suicide."
            )
            print(
                "They will be missed by their friends and will simultaneously be known as a coward who threw everything away for no reason."
            )
            print(
                "\nThey could have lived happily for the rest of a potentially long life, but they threw it away anyway."
            )
            if is_depressed == 1:
                print(
                    "\nThey were diagnosed with depression a few years ago, so perhaps that is the underlying cause of their untimely death."
                )
            div()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if age < 130:
                print("[2] Respawn")
            div()
            try:
                ch = int(input(">"))
            except:
                mainmenu()
            if ch == 0:
                raise ExitError
            elif ch == 2 and age < 130:
                if age <= 5:
                    infant()
                elif age >= 6 and age < 12:
                    child()
                elif age >= 12 and age < 18:
                    teen()
                else:
                    adult()
            else:
                mainmenu()
        elif reason == 1:
            div()
            print(f"{forename} {surname} dies of natural cases aged {age}")
            div()
            print(f"{forename} {surname} has died of natural causes while sleeping.")
            if age > 123:
                print(
                    f"They were aged {age}, making them the oldest person in the world at the time."
                )
            print("\nThey lived a long, happy life, surrounded by great people.")
            print("They will be missed by friends and family.")
            div()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if age < 130:
                print("[2] Respawn")
            div()
            try:
                ch = int(input(">"))
            except:
                mainmenu()
            if ch == 0:
                raise ExitError
            elif ch == 2 and age < 130:
                if age <= 5:
                    infant()
                elif age >= 6 and age < 12:
                    child()
                elif age >= 12 and age < 18:
                    teen()
                else:
                    adult()
            else:
                mainmenu()
        elif reason == 2:
            div()
            print(f"{forename} {surname} dies of heart attack aged {age}")
            div()
            print(
                f"{forename} {surname} passed away as a result of a tragic heart attack last night."
            )
            print(
                f"Their death was extremely untimely and is a tragic loss that will be felt by the entire {game_name} community."
            )
            print(
                f"\nHopefully such heart attacks are seen less and less in the community and that the players of {game_name} do not overwork themselves like {forename} {surname} did."
            )
            div()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if age < 130:
                print("[2] Respawn")
            div()
            try:
                ch = int(input(">"))
            except:
                mainmenu()
            if ch == 0:
                raise ExitError
            elif ch == 2 and age < 130:
                if age <= 5:
                    infant()
                elif age >= 6 and age < 12:
                    child()
                elif age >= 12 and age < 18:
                    teen()
                else:
                    adult()
            else:
                mainmenu()
        elif reason == 3:
            div()
            print(f"{forename} {surname} dies of cancer aged {age}")
            div()
            print(
                f"{forename} {surname} has died due to complications as a result of a years-long battle with cancer."
            )
            print(
                f"The {game_name} community will be feeling the loss of {forename} {surname} for many years to come."
            )
            print("We will miss you, {forename} {surname}.")
            div()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if age < 130:
                print("[2] Respawn")
            div()
            try:
                ch = int(input(">"))
            except:
                mainmenu()
            if ch == 0:
                raise ExitError
            elif ch == 2 and age < 130:
                if age <= 5:
                    infant()
                elif age >= 6 and age < 12:
                    child()
                elif age >= 12 and age < 18:
                    teen()
                else:
                    adult()
            else:
                mainmenu()
        elif reason == 4:
            print(f"{forename} {surname} dies in hospital aged {age}")
            div()
            print(
                f"{forename} {surname} has died in hospital as a result of health complications."
            )
            print(
                f"They had allegedly suffered from deteriorating physical health for years before this incident."
            )
            print(
                f"They collapsed onto the floor in their home and was immediately rushed to hospital."
            )
            print(f"Unfortunately, attempts to revive them were eventually futile.")
            print(
                f"The community will deeply miss {forename} {surname} for many years to come."
            )
            div()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if age < 130:
                print("[2] Respawn")
            div()
            try:
                ch = int(input(">"))
            except:
                mainmenu()
            if ch == 0:
                raise ExitError
            elif ch == 2 and age < 130:
                if age <= 5:
                    infant()
                elif age >= 6 and age < 12:
                    child()
                elif age >= 12 and age < 18:
                    teen()
                else:
                    adult()
            else:
                mainmenu()
        else:
            raise FeatureNotInGameError

    def spouse_interact():
        global spouse, happiness, is_spouse, money, debt, currency
        div()
        print(f"{spouse.name}")
        if spouse.lvl == 1:
            print("Girlfriend")
        elif spouse.lvl == 2:
            print("Wife")
        print(f"Age: {spouse.age}")
        pbar(spouse.rel)
        div()
        print("[0] Return")
        print("[1] Spend Time")
        print("[2] Compliment")
        print("[3] Conversation")
        print("[x] Break Up")
        print("[5] Insult")
        print("[x] Make Love")
        print("[x] Movies")
        if spouse.lvl == 1:
            print(f"[8] Marriage [{currency}75,000]")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 1:
            div()
            print(f"You spent time with {spouse.name}")
            spouse.rel += 0.25
            adult()
        elif ch == 2:
            div()
            print("You called your spouse spiffing!")
            happiness += 0.25
            spouse.rel += 0.25
            if spouse.rel > 0.75:
                print("Your spouse called you incredible!")
                happiness += 0.45
            adult()
        elif ch == 8 and spouse.lvl == 1:
            div()
            if spouse.rel >= 0.75:
                if money >= 75000:
                    money -= 75000
                else:
                    debt += 75000
                print("You married your spouse!")
                spouse.lvl = 2
                spouse.rel = 1
                adult()
            else:
                print("Your spouse refused to marry you.")
                adult()

        elif ch == 3:
            argument_chance = rng(1, 4)
            if argument_chance == 1:
                div()
                print("You had a conversation about whether tea or coffee is better.")
                print("Agreement: ", pbar2(0))
                spouse.rel -= 0.45
                happiness -= 0.55
                adult()
            else:
                div()
                print("You had a conversation about whether tea or coffee is better.")
                print("Agreement: ", pbar2(0.75))
                spouse.rel += 0.25
                happiness += 0.45
                adult()
        elif ch == 4:
            div()
            print("You broke up with your spouse.")
            is_spouse = 0
            del spouse
        elif ch == 5:
            div()
            print("You called your spouse a dickhead!")
            spouse.rel -= 0.55
            if spouse.rel < 0.25:
                print("Your spouse called you a lazy asshole!")
                spouse.rel -= 0.25
                happiness -= 0.85
            adult()
        else:
            adult()

    def pickname(gender):
        global forename_m, forename_f, surnames
        from random import choice

        if gender == 0:
            n1 = choice(forename_m)
            n2 = choice(surnames)
            n = n1 + " " + n2
            return n
        else:
            n1 = choice(forename_f)
            n2 = choice(surnames)
            n = n1 + " " + n2
            return n

    def find_love():
        global age, spouse, surnames
        div()
        # name, age, relation, relationship_level, your_age
        print("While at the gym, a chick asks you out.")
        spouse = Spouse(pickname(1), (rng(50, 75) / 100), 1, age)
        print(f"Name: {spouse.name}")
        print(f"Age: {spouse.age}")
        div()
        print("[1] Ask on a date")
        print("[0] Ignore")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 1:
            return spouse
        else:
            return False

    def pension_questions():
        per = rng(1, 4)
        if per == 1:
            print("Why do you want to leave?")
            div()
            print("[1] I would've quit.")
            print("[2] I'm tired of work.")
            print("[3] I have put enough effort into my job already.")
            print("[4] I deserve a break.")
            try:
                ch = int(input(">"))
            except:
                pass
            return True
        if per == 2:
            print("What will you do once you retire?")
            div()
            print("[1] Die.")
            print("[2] Go on permanent holiday.")
            print("[3] Go to another job.")
            print("[4] I don't want to think about it.")
            try:
                ch = int(input(">"))
            except:
                pass
            return True
        if per == 3:
            print("How was working at our company?")
            div()
            print("[1] It was great!")
            print("[2] Average.")
            print("[3] It was shit. I'm glad to go, dickhead.")
            print("[4] No comment.")
            try:
                ch = int(input(">"))
            except:
                pass
            return True
        if per == 4:
            print(
                "Are you actually willing to lose your salary for what is essentially a holiday?"
            )
            div()
            print("[1] I wanted to do this from the start.")
            print("[2] I had no choice.")
            print("[3] I deserve a break.")
            try:
                ch = int(input(">"))
            except:
                pass
            return True

    def fake_id_hub():
        global debt, savings, money, currency
        print("[0] Return")
        print("[x] Casino")
        print("[2] Lottery")
        print("[3] Loan")
        print("[4] Access Savings Account")
        print('[5] "Club"')
        try:
            ch = int(input(">"))
        except:
            ch == 0
        if ch == 0:
            teen()
        elif ch == 2:
            lottery(1)
        elif ch == 3:
            try:
                d = int(input("How much to borrow? [Max 10k]>"))
            except:
                d = 0
            if debt >= 10000:
                adult()
            if d > 10000:
                d = 10000
            debt += d
            money += d
            teen()
        elif ch == 4:
            print(f"Savings: {currency}{savings}")
            print("[0] Return")
            print("[1] Take Out Savings")
            try:
                ch = int(input(">"))
            except:
                teen()
            if ch == 1:
                money += savings
                savings = 0
            else:
                teen
            teen()
        else:
            teen()

    def save_game():
        global allow_debug, spouse, is_spouse
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age, mother_rel, father_rel
        print("Save Game")
        div()
        print("Saves that are already taken:")
        path = os.getcwd()
        dirlist = os.listdir(path)
        for item in dirlist:
            isFile = os.path.isfile(item)
            if isFile == True and item.endswith(".oll2"):
                item = item.replace(".oll2", "")
                print(item)
        div()

        # 0=Alpha|1=12|2=happiness|3=health|4=intel|5=looks|6=ethics|7=money
        # |8=forename|9=surname|10=age|11=work_e|12=edu_lvl|13=work_e_base|14=promo_base
        # |15=degree|16=hours|17=salary|18=expenses|19=expenses|20=pension
        # |21=is_depressed|22=debt|23=savings|24=year|25=is_job|26=stress
        # |27=mother_name|28=father_name|29=mother_age|30=father_age
        # |31=mother_end_age|32=father_end_age|33=did_tutor
        sn = input("Enter File Name >")
        # Windows illegal filename characters removed
        sn = sn.replace("\\", "")
        sn = sn.replace("/", "")
        sn = sn.replace("?", "")
        sn = sn.replace("*", "")
        sn = sn.replace("|", "")
        sn = sn.replace("<", "")
        sn = sn.replace(">", "")
        sn = sn.replace(":", "")
        sn = sn.replace('"', "")
        sn += ".oll2"  # filename extension
        if sn == "":
            from time import ctime

            sn = ctime()
            sn = sn.replace(":", "-")
            sn = sn.replace(" ", "_")
        if is_spouse == 0:
            spouse = Spouse("N/A", 1, 1, age)
        save = (
            "Alpha|13|"
            + str(happiness)
            + "|"
            + str(health)
            + "|"
            + str(intel)
            + "|"
            + str(looks)
            + "|"
            + str(ethics)
            + "|"
            + str(money)
            + "|"
            + forename
            + "|"
            + surname
            + "|"
            + str(age)
            + "|"
            + str(work_e)
            + "|"
            + str(edu_lvl)
            + "|"
            + str(work_e_base)
            + "|"
            + str(promo_base)
            + "|"
            + str(degree)
            + "|"
            + str(hours)
            + "|"
            + str(salary)
            + "|"
            + str(expenses)
            + "|"
            + str(pension)
            + "|"
            + str(is_depressed)
            + "|"
            + str(debt)
            + "|"
            + str(savings)
            + "|"
            + str(year)
            + "|"
            + str(is_job)
            + "|"
            + str(stress)
            + "|"
            + mother_name
            + "|"
            + father_name
            + "|"
            + str(mother_age)
            + "|"
            + str(father_age)
            + "|"
            + str(mother_end_age)
            + "|"
            + str(father_end_age)
            + "|"
            + str(did_tutor)
            + "|"
            + str(mother_rel)
            + "|"
            + str(father_rel)
            + "|"
            + str(is_spouse)
            + "|"
            + str(spouse.name)
            + "|"
            + str(spouse.age)
            + "|"
            + str(spouse.end)
            + "|"
            + str(spouse.lvl)
            + "|"
            + str(spouse.rel)
            + "|"
            + str(enemy_gang_rel)
            + "|"
            + str(enemy_gang_lead)
            + "|"
            + enemy_gang_name
            + "|"
            + str(part_time_salary)
            + "|"
            + str(teen_hours)
            + "|"
            + str(teen_salary)
        )
        import codecs

        save = save.encode("utf-8")
        save = codecs.encode(save, "base64_codec")
        f = open(sn, "wb")
        f.write(save)
        f.close()
        print("Saved as", sn)
        br()
        div()
        return True

    def load_game():
        global allow_debug, did_tutor, degree, is_spouse, spouse, part_time_salary
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary, mother_rel, father_rel
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age
        print("Load Game")
        div()
        print("Available saves:")
        path = os.getcwd()
        dirlist = os.listdir(path)
        for item in dirlist:
            isFile = os.path.isfile(item)
            if isFile == True and item.endswith(".oll2"):
                item = item.replace(".oll2", "")
                print(item)
            else:
                continue
        # try:
        div()
        # 0=Alpha|1=12|2=happiness|3=health|4=intel|5=looks|6=ethics|7=money
        # |8=forename|9=surname|10=age|11=work_e|12=edu_lvl|13=work_e_base|14=promo_base
        # |15=degree|16=hours|17=salary|18=expenses|19=pension
        # |20=is_depressed|21=debt|22=savings|23=year|24=is_job|25=stress
        # |26=mother_name|27=father_name|28=mother_age|29=father_age
        # |30=mother_end_age|31=father_end_age
        sn = input("Enter File Name >")
        # Windows illegal filename characters removed
        sn = sn.replace("\\", "")
        sn = sn.replace("/", "")
        sn = sn.replace("?", "")
        sn = sn.replace("*", "")
        sn = sn.replace("|", "")
        sn = sn.replace("<", "")
        sn = sn.replace(">", "")
        sn = sn.replace(":", "")
        sn = sn.replace('"', "")
        sn += ".oll2"  # file extension
        try:
            f = open(sn, "rb")
        except:
            raise ExitError
        import codecs

        ssave = f.read()
        f.close()
        ssave = codecs.decode(ssave, "base64_codec")
        ssave = ssave.decode("utf-8")
        ssave = ssave.split("|")
        save = ssave
        if allow_debug != 0:
            print(save)
        if save[0] == "Alpha" and save[1] == "13":
            happiness = float(save[2])
            health = float(save[3])
            intel = float(save[4])
            looks = float(save[5])
            ethics = float(save[6])
            money = int(save[7])
            forename = save[8]
            surname = save[9]
            age = int(save[10])
            work_e = int(save[11])
            edu_lvl = int(save[12])
            work_e_base = int(save[13])
            promo_base = int(save[14])
            is_depressed = int(save[15])
            debt = int(save[16])
            savings = int(save[17])
            expenses = int(save[18])
            pension = float(save[19])
            pension = int(pension)
            is_depressed = int(save[20])
            debt = int(save[21])
            savings = int(save[22])
            year = int(save[23])
            is_job = int(save[24])
            stress = float(save[25])
            mother_name = save[26]
            father_name = save[27]
            mother_age = int(save[28])
            father_age = int(save[29])
            mother_end_age = int(save[30])
            father_end_age = int(save[31])
            did_tutor = int(save[32])
            mother_rel = float(save[33])
            father_rel = float(save[34])
            is_spouse = int(save[35])
            spouse = SpouseRecompile(
                save[36], float(save[40]), int(save[39]), int(save[37]), int(save[38])
            )
            enemy_gang_rel = float(save[41])
            enemy_gang_lead = float(save[42])
            enemy_gang_name = save[43]
            part_time_salary = int(save[44])
            teen_hours = int(save[45])
            teen_salary = int(save[46])

            div()
            print("Successfully loaded life.")
            adult()
        elif save[0] == "Alpha" and save[1] == "12":
            div()
            print("This save file is incompatible with", game_name + ".")
            print("In order to play, you need to convert it to a supported format.")
            print(
                "You can do this automatically, but this will [sadly] require adding default data."
            )
            print(
                "Also, you will not be able to play this on that older version of",
                game_name,
            )
            div()
            print("[0] Cancel to Main Menu")
            print("[1] Convert")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1:
                load_game_a12(sn)
            else:
                mainmenu()
        else:
            if allow_debug == 1:
                print(save)
            print("This save is incompatible with OpenLife.")
            print("Expected Version: Alpha 13")
            print("Got version:", save[0], save[1])
            br()
            mainmenu()

    def encode_save():
        # this INTERNAL function base64 encodes a plaintext save, for revsersing what a backwards compatible conversion did.
        save = [
            "Alpha",
            "12",
            "0.96",
            "0.8000000000000002",
            "0.15999999999999998",
            "1",
            "1",
            "104432268",
            "Rick",
            "Astley",
            "69",
            "22",
            "2",
            "0",
            "22",
            "9",
            "0",
            "0",
            "0",
            "57200.0",
            "0",
            "0",
            "0",
            "2087",
            "0",
            "0.65",
            "Hedda Astley",
            "Emerson Astley",
            "101",
            "106",
            "86",
            "86",
        ]
        base = ""
        for item in save:
            base += item
            base += "|"
        print(base)
        br()

    def load_game_a12(sn):
        global allow_debug, did_tutor
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary, mother_rel, father_rel
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age
        print("Convert Save [A12] --> [A13]")
        # load stage
        div()
        f = open(sn, "rb")
        ssave = f.read()
        f.close()
        print(ssave)
        f = open(sn + ".bak", "wb")
        f.write(ssave)
        f.close()
        div()
        print("Backed up as", sn + ".bak")
        div()
        import codecs

        ssave = codecs.decode(ssave, "base64_codec")
        ssave = ssave.decode("utf-8")
        save = ssave
        # convert stage
        # save+="" [This is the part where it adds default stuff]
        save = save.split("|")
        print(save)
        save[0] = "Alpha"
        save[1] = "13"
        base = ""
        for item in save:
            base += item
            base += "|"
        l = len(base)
        base = base[: l - 1]
        base += "|1|0.75|0.75|0|SGCU Converted Imaginary Girlfriend|0|0|0|0|0|0|[PLACEHOLDER]|0|0|0"
        save = base
        save = save.encode("utf-8")
        save = codecs.encode(save, "base64_codec")
        f = open(sn, "wb")
        f.write(save)
        f.close()
        print("Converted save successfully.")
        div()
        load_game()

    def casino_menu():
        global money, winnings, currency
        losses = -(winnings)
        if winnings < 0:
            print("Session Losses:", losses)
        else:
            print(f"Session earnings: {currency}" + str(winnings))
        print(f"Money: {currency}" + str(money))
        print("[1] Play")
        print("[0] Return")
        try:
            ch = int(input(">"))
        except:
            ch = 1
        if ch == 1:
            blackjack()
        else:
            adult()

    def job_centre():
        global edu_lvl, looks, salary, hours, is_job, job_id, currency
        div()
        print("These are all elegible jobs.")
        div()
        if edu_lvl >= 1:
            print(f"[1] Amazon Delivery Driver [{currency}5/h]")
        if edu_lvl >= 2 and degree == 11:
            print(f"[2] Jr Translator [{currency}10/h]")
        if edu_lvl >= 2 and degree == 5:
            print(f"[3] Jr Accountant [{currency}30/h]")
        print(f"[4] Exorcist [{currency}10/h]")
        if edu_lvl >= 2 and degree == 4:
            print(f"Teacher [{currency}20/h]")
        print("[x] Trainee Pilot")
        if edu_lvl >= 2 and degree == 3:
            print(f"[6] Jr Game Developer [{currency}40/h]")
        print("[x] Lawyer")
        if edu_lvl >= 2 and degree == 2:
            print(f"[8] Jr Lawyer [{currency}60/h]")
        if edu_lvl >= 2 and degree == 3:
            print(f"[9] App Developer [{currency}45/h]")
        if edu_lvl >= 2 and degree == 1:
            print(f"[10] Jr Banker [{currency}45/h]")
        print(f"[11] Monk [{currency}15/h]")
        print(f"[12] Wedding Planner [{currency}25/h]")
        if edu_lvl >= 2 and degree == 9:
            print(f"[13] Engineer I [{currency}55/h]")
        if edu_lvl >= 2 and degree == 13:
            print(f"[14] Data Scientist [{currency}75/h]")
        if edu_lvl >= 1:
            print(f"[15] Private [Army] [{currency}35/h]")
        print("[x] Architect")
        if edu_lvl >= 1:
            print(f"[17] Cashier [{currency}10/h]")
        if edu_lvl >= 2 and degree == 4:
            print(f"[18] College Lecturer [{currency}45/h]")
        print(f"[19] OOhber Driver [{currency}15/h]")
        if edu_lvl >= 2 and degree == 2:
            print(f"[20] Editor [{currency}25/h]")
        if looks >= 0.8:
            print(f"[21] Exotic Dancer [{currency}15/h]")
        print(f"[22] Flight Attendant [{currency}25/h]")
        if edu_lvl >= 1:
            print(f"[23] Apprentice Hairdresser [{currency}25/h]")
        print("[x] Judge")
        if edu_lvl >= 1:
            print(f"[25] Librarian [{currency}25]")
        if edu_lvl >= 1:
            print(f"[26] Nun [{currency}10/h]")
        print("[x] Photographer")
        if edu_lvl >= 1 and looks >= 0.8:
            print(f"[28] P*rnographer [{currency}35/h]")
        if edu_lvl >= 2 and degree == 1:
            print(f"[29] Stockbroker [{currency}45/h]")
        if edu_lvl >= 2 and degree == 16:
            print(f"[30] Publicity Stuntperson [{currency}35/h]")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        job_id = ch
        if ch == 0:
            adult()
        elif ch == 1 and edu_lvl >= 1:
            if job_interview():
                salary = 5
                hours = 60
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 2 and edu_lvl >= 2 and degree == 11:
            if job_interview():
                salary = 10
                hours = 45
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 3 and edu_lvl >= 2 and degree == 5:
            if job_interview():
                salary = 30
                hours = 45
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 4:
            if job_interview():
                salary = 10
                hours = 40
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 5 and edu_lvl >= 2 and degree == 4:
            if job_interview():
                salary = 20
                hours = 55
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 6 >= 2 and degree == 3:
            if job_interview():
                salary = 40
                hours = 45
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 8 and degree == 2 and edu_lvl >= 2:
            if job_interview():
                salary = 60
                hours = 40
                is_job = 1
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
                salary = 45
                hours = 40
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 10 and degree == 1 and edu_lvl >= 2:
            if job_interview():
                salary = 45
                hours = 40
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 11:
            if job_interview():
                salary = 15
                hours = 40
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 12:
            if job_interview():
                salary = 25
                hours = 45
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 13 and edu_lvl >= 2 and degree == 9:
            if job_interview():
                salary = 55
                hours = 40
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 14 and edu_lvl >= 2 and degree == 13:
            if job_interview():
                salary = 75
                hours = 50
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 15 and edu_lvl >= 1:
            if job_interview():
                salary = 35
                hours = 40
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 17 and edu_lvl >= 1:
            if job_interview():
                salary = 10
                hours = 40
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 18 and edu_lvl >= 2 and degree == 4:
            if job_interview():
                salary = 45
                hours = 45
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 19:
            if job_interview():
                salary = 15
                hours = 60
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 20 and edu_lvl >= 2 and degree == 2:
            if job_interview():
                salary = 25
                hours = 40
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 21 and looks >= 0.8:
            if job_interview():
                salary = 15
                hours = 45
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 22:
            if job_interview():
                salary = 25
                hours = 40
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 23 and edu_lvl >= 1:
            if job_interview():
                salary = 25
                hours = 40
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 25 and edu_lvl >= 1:
            if job_interview():
                salary = 25
                hours = 40
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 26 and edu_lvl >= 1:
            if job_interview():
                salary = 10
                hours = 40
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 28 and edu_lvl >= 1 and looks >= 0.8:
            if job_interview():
                salary = 35
                hours = 40
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 29 and edu_lvl >= 2 and degree == 1:
            if job_interview():
                salary = 45
                hours = 35
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        elif ch == 30 and edu_lvl >= 2 and degree == 16:
            if job_interview():
                salary = 35
                hours = 40
                is_job = 1
                print("You got the job.")
                br()
                adult()
            else:
                print("You were not offered the position.")
                br()
                adult()
        else:
            job_id = 0
            adult()
        adult()

    def adult_crime():
        global mother_age, age
        global father_age
        global father_end_age, mother_end_age, money, currency
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
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        elif ch == 4:
            print("[0] Return")
            if mother_age < mother_end_age:
                print(f"[1] Kill Mother [{currency}45,000]")
            if father_age < father_end_age:
                print(f"[2] Kill Father [{currency}45,000]")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            elif ch == 1 and mother_age < mother_end_age:
                if money >= 45000:
                    money -= 45000
                    mother_end_age = mother_age + 1
                    age -= 1
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
                    money -= 45000
                    father_end_age = father_age + 1
                    age -= 1
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

            base = randint(15, 30)
            print(f"You stole {currency}" + str(base))
            money += base
            adult()
        elif ch == 7:
            print("[0] Return")
            print(f"[x] Phone [{currency}750]")
            print("[x] Beer")
            print("[x] Cigarettes")
            print("[x] Mars Candy Bar")
            print(f"[x] Handbag [{currency}250]")
            print(f"[x] Wallet [{currency}50]")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            else:
                adult()
        elif ch == 8:
            from time import strftime
            from random import randint

            winnings = randint(150, 300)
            winnings *= 100000
            base = strftime("%H:%M")
            print("Choose a time [Note: This should be the real-life time.")
            print("[1] 0:00 [Midnight]")
            print("[2] 07:00 [7AM]")
            print("[3] 12:00 [12AM]")
            print("[4] 16:20 [4:20PM]")
            print("[5] 19:00 [7PM]")
            print("[6] 21:00 [9PM]")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1:
                if base == "00:00":
                    div()
                    print(f"You stole {currency}" + str(winnings))
                    money += winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 2:
                if base == "07:00":
                    div()
                    print(f"You stole {currency}" + str(winnings))
                    money += winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 3:
                if base == "12:00":
                    div()
                    print(f"You stole {currency}" + str(winnings))
                    money += winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 4:
                if base == "16:20":
                    div()
                    print(f"You stole {currency}" + str(winnings))
                    money += winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 5:
                if base == "19:00":
                    div()
                    print(f"You stole {currency}" + str(winnings))
                    money += winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 6:
                div()
                if base == "21:00":
                    print(f"You stole {currency}" + str(winnings))
                    money += winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            else:
                adult()
        else:
            # Place more options on this indent level
            adult()

    def uni_age():
        global mother_age, father_age, father_end_age, mother_end_age, debt, savings, money, currency
        basee = savings / 10
        basee = int(basee)
        savings += basee
        base = int(debt / 5)
        debt += base
        base = int(debt / 10)
        money -= base
        mother_age += 1
        father_age += 1
        global age, uni_end_age, work_e_base
        global salary, hours, work_e, promo_base
        # when parents die
        base = salary * hours * 52
        money += base
        money -= expenses * 12
        if mother_age == mother_end_age:
            div()
            print("Your mother died.")
            print("It is your responsibility to plan the funeral.")
            print("[0] Skip")
            print(f"[1] Bury [{currency}8500]")
            print(f"[2] Cremate [{currency}1500]")
            print(f"[3] Taxidermy [{currency}15 000]")
            print(f"[4] Donate To Science [{currency}0]")
            try:
                ch = int(input(">"))
            except:
                ch = 4
            if ch == 0:
                print("You skipped the funeral.")
            elif ch == 1:
                print("Your mother was buried.")
                money -= 8500
            elif ch == 2:
                money -= 15000
                print("You cremated your mother.")
                print("Choose what to do with the ashes:")
                print("[1] Sprinkle somewhere special.")
                print("[2] Put in urn")
                print("[0] Throw In Trash")
                ch = input(">")
            elif ch == 3:
                print("You had your mother taxidermied.")
                money -= 15000
            elif ch == 4:
                print("Your mother's body was donated to science.")
            else:
                print("You skipped the funeral.")
            from random import randint

            mother_fortune = randint(1000000, 3000000)
            div()
            print(f"You inherited {currency}" + str(mother_fortune))
            money += mother_fortune
        if father_age == father_end_age:
            div()
            print("Your father died.")
            print("It is your responsibility to plan the funeral.")
            print("[0] Skip")
            print(f"[1] Bury [{currency}8500]")
            print(f"[2] Cremate [{currency}1500]")
            print(f"[3] Taxidermy [{currency}15 000]")
            print(f"[4] Donate To Science [{currency}0]")
            try:
                ch = int(input(">"))
            except:
                ch = 4
            if ch == 0:
                print("You skipped the funeral.")
            elif ch == 1:
                print("Your father was buried.")
                money -= 8500
            elif ch == 2:
                money -= 15000
                print("You cremated your father.")
                print("Choose what to do with the ashes:")
                print("[1] Sprinkle somewhere special.")
                print("[2] Put in urn")
                print("[0] Throw In Trash")
                ch = input(">")
            elif ch == 3:
                print("You had your father taxidermied.")
                money -= 15000
            elif ch == 4:
                print("Your father's body was donated to science.")
            else:
                print("You skipped the funeral.")
            from random import randint

            father_fortune = randint(1000000, 3000000)
            div()
            print(f"You inherited {currency}" + str(father_fortune))
            money += father_fortune
        if hours > 0:
            base = salary * hours
            base *= 52
            money += base
            work_e += 1
            promo_base += 1
            work_e_base += 1
        age += 1
        if age == uni_end_age:
            div()
            global edu_lvl
            edu_lvl = 2
            print("You graduated from University.")
            salary = 0
            work_e_base = 0
            hours = 0
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
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            uni()
        elif ch == 1:
            print("You partied.")
            print("Enjoyment:")
            pbar(0.75)
            happiness += 0.45
            uni()
        elif ch == 2:
            div()
            print("Locked.")
            uni()
        else:
            uni()

    def uni_menu():
        global salary, hours, currency
        print("[1] University")
        print("[2] Part-Time Jobs")
        print("[x] Local Gangs")
        print("[0] Return")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            uni()
        elif ch == 1:
            div()
            print("[1] Drop Out")
            print("[0] Return")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                uni()
            elif ch == 1:
                div()
                print("You dropped out of Uni.")
                adult()
            else:
                uni()
        elif ch == 2:
            print(f"[1] Mall Santa [{currency}15/h] [10h]")
            print(f"[2] Lab Assistant [{currency}19/h] [15h]")
            print(f"[3] Receptionist [{currency}9/h] [22h]")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                uni()
            elif ch == 1:
                salary = 15
                hours = 10
                div()
                uni()
            elif ch == 2:
                salary = 19
                hours = 15
                div()
                uni()
            elif ch == 3:
                salary = 9
                hours = 22
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
        global money, is_depressed, debt, currency
        if happiness > 1:
            happiness = 1
        if happiness < 0:
            happiness = 0
        if health > 1:
            health = 1
        if health < 0:
            emergency_room(2)
        if intel > 1:
            intel = 1
        if looks > 1:
            looks = 1
        if intel < 0:
            intel = 0
        if looks < 0:
            looks = 0
        global forename, surname
        global mother_rel, father_rel
        global money
        div()
        print(forename + " " + surname)
        print("University Student")
        div()
        if is_depressed == 1:
            print("Suffers from: Depression")
        print("Age", age)
        print(f"{currency}" + str("{:,}".format((money))))
        div()
        print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "%")
        print("Health:   ", pbar2(health), str(int(health * 100)) + "%")
        print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "%")
        print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "%")
        div()
        print("Uni end age:", uni_end_age)
        div()
        print("[1] University")
        print("[0] Age Up")
        print("[x] Relationships")
        print("[4] Activities")
        try:
            ch = int(input(">"))
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
        global uni_end_age, age
        uni_end_age = age + 5
        print("You will end uni at age:", uni_end_age)
        uni()
        br()

    def uni_check():
        global degree, money, debt, currency
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
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        else:
            if intel >= 0.75:
                global degree
                degree = ch
                div()
                print("You have been selected for Uni!")
                print(f"Price: {currency}25,000")
                print("[1] Buy With Cash")
                print("[2] Scholarship")
                print("[3] Ask your mother to pay")
                print("[4] Apply for a student loan")
                print("[0] Return")
                try:
                    ch = int(input(">"))
                except:
                    ch = 0
                div()
                if ch == 0:
                    adult()
                elif ch == 1:
                    global debt
                    debt += 25000
                    uni_start()
                elif ch == 1:
                    if money >= 25000:
                        money -= 25000
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
                    debt += 25000
                    uni_start()
                else:
                    adult()
            else:
                div()
                print("You are too dumb.")
                adult()

    def blackjack_init():
        global money, winnings
        winnings = 0
        casino_menu()

    def get_card():
        global number
        from random import randint

        number += randint(1, 10)

    def enemy_get_card():
        global enemy_number
        from random import randint

        enemy_number += randint(1, 10)

    def decide():
        global money, number, enemy_number, bet, winnings, debt
        if enemy_number > 21:
            print("Enemy bust!")
            money += bet
            winnings += bet
            br()
            casino_menu()
        elif enemy_number > number:
            print("Enemy won")
            debt += bet
            winnings -= bet
            br()
            casino_menu()

    def enemy():
        global money, number, enemy_number, debt
        from time import sleep

        enemy_number = 0
        div()
        print("Your enemy begins.")
        # if enemy_number > number:
        # lose
        # else if enemy busts
        # win
        # else [due to error]
        # win
        enemy_get_card()
        print("Your hand:", number)
        print("Enemy hand:", enemy_number)
        div()
        while True:
            if enemy_number > number:
                break
            elif enemy_number > 21:
                break
            else:
                enemy_get_card()
                print("Your hand:", number)
                print("Enemy hand:", enemy_number)
                sleep(0.45)
                div()
        decide()

    def blackjack():
        global money, number, bet, winnings, allow_debug, debt, currency
        try:
            bet = int(input("Enter Bet >"))
        except:
            bet = money
        if bet > money:
            bet = money
        if bet < 1000:
            div()
            print(f"Bet set to minimum [{currency}1000]")
            div()
            bet = 1000
        elif bet > 10000000:
            div()
            print(f"Bet set to maximum [{currency}10 000 000]")
            div()
            bet = 10000000
        else:
            div()
            print(f"You have {currency}" + str(bet) + " riding on this bet.")
            div()
        number = 0
        get_card()
        while True:
            if number > 21:
                print("Bust!")
                winnings -= bet
                debt += bet
                casino_menu()
            print("Your Hand:", number)
            print("[1] Hit Me")
            print("[2] I'll Stand")
            try:
                ch = int(input(">"))
            except:
                ch = 1
            if ch == 1:
                get_card()
            elif ch == 2:
                enemy()

    def lottery(is_teen):
        global money, allow_test, currency
        from random import randint

        div()
        print("Enter amount of lottery tickets to buy.")
        print(f"1 ticket = {currency}100")
        base = str("{:,}".format((int(money / 100))))
        print("You can afford", base, "tickets.")
        div()
        losses = 0
        wins = 0
        win_amount = 0
        try:
            ticket_count = int(input(">"))
        except:
            ticket_count = 0
        price = ticket_count * 100
        tmw = ticket_count * 1000
        tmw *= 1000000
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
                    money -= 100
                    chance = randint(1, 100000)
                    if chance == 2345:
                        base = wins + losses
                        base /= ticket_count
                        base *= 100
                        print(
                            "You won! [" + str("{:,}".format((int(losses)))),
                            "losses] [" + str(int(base)) + "%]",
                        )
                        wins += 1
                        base = randint(250, 1000)
                        base *= 1000000
                        money += base
                        win_amount += base
                    else:
                        losses += 1
            except:
                pass
            print("Tickets Bought:", ticket_count)
            base = str("{:,}".format((int(win_amount))))
            print("Wins:", wins)
            print("Losses:", losses)
            div()
            print(f"Win Amount: {currency}" + str(base))
            base = str("{:,}".format((int(tmw))))
            print(f"Theoretical Maximum Win: {currency}" + base)
            br()
            if is_teen == 0:
                adult()
            else:
                teen()

    def pause():
        div()
        print("Press ENTER to continue.")
        wer = input
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
        age = start_age
        mother_age = age + 32
        father_age = age + 37
        base = randint(15, 55)
        mother_end_age = +32 + base
        base = randint(15, 55)
        father_end_age = 37 + base
        global happiness, intel
        global stress
        if start_age <= 5:
            infant_start()
        elif start_age >= 6 and start_age < 12:
            mother_rel = 1
            father_rel = 1
            stress = 0.5
            child_init()
        elif age >= 12 and age < 18:
            money = 0
            stress = 0.65
            mother_rel = 0.8
            grades = intel
            father_rel = 0.8
            teen_init()
        elif age >= 18:
            global salary, hours
            salary = 0
            hours = 0
            global did_tutor
            did_tutor = 0
            edu_lvl = 1
            money = 0
            stress = 0
            mother_rel = 0.8
            father_rel = 0.8
            adult_init()
        else:
            raise ExitError

    def age_up():
        global salary, hours, expenses, happiness, health, intel, looks, teen_salary, teen_hours
        global mother_end_age, father_end_age, money
        global is_depressed, is_anxiety, savings, debt
        global year, is_job, work_e_base, pension, promo_base, currency
        year += 1
        global happiness, intel
        global age
        global money, father_rel
        global did_tutor, auto_deposit
        did_tutor = 0
        # random stat change: if you have 10% or less health, you have a chance of dying!
        happiness += rng(-10, 10) / 100
        health += rng(-10, 10) / 100
        intel += rng(-10, 10) / 100
        looks += rng(-10, 10) / 100
        if age >= 12 and age < 18:
            money += (teen_salary * teen_hours) * 52
        if age >= 6:
            basee = savings / 10
            basee = int(basee)
            savings += basee
            base = int(debt / 5)
            debt += base
            base = int(debt / 10)
            money -= base
        if pension > 0:
            money += pension
        global work_e, is_job
        if age >= 18:
            money += part_time_salary * 520
        if is_job == 1:
            work_e += 1
            work_e_base += 1
            promo_base += 1
        if promo_base == 5:
            promo_base = 0
            promotion()
        global mother_age, father_age, edu_lvl
        age += 1
        mother_age += 1
        father_age += 1
        # when parents die
        if age >= 18 and is_job == 1:
            base = salary * hours * 52
            money += base
            money -= expenses * 12
        if mother_age == mother_end_age:
            div()
            print("Your mother died.")
            print("It is your responsibility to plan the funeral.")
            print("[0] Skip")
            print(f"[1] Bury [{currency}8500]")
            print(f"[2] Cremate [{currency}1500]")
            print(f"[3] Taxidermy [{currency}15 000]")
            print(f"[4] Donate To Science [{currency}0]")
            try:
                ch = int(input(">"))
            except:
                ch = 4
            if ch == 0:
                print("You skipped the funeral.")
            elif ch == 1:
                print("Your mother was buried.")
                money -= 8500
            elif ch == 2:
                money -= 15000
                print("You cremated your mother.")
                print("Choose what to do with the ashes:")
                print("[1] Sprinkle somewhere special.")
                print("[2] Put in urn")
                print("[0] Throw In Trash")
                ch = input(">")
            elif ch == 3:
                print("You had your mother taxidermied.")
                money -= 15000
            elif ch == 4:
                print("Your mother's body was donated to science.")
            else:
                print("You skipped the funeral.")
            from random import randint

            mother_fortune = randint(1000000, 3000000)
            div()
            print(f"You inherited {currency}" + str(mother_fortune))
            money += mother_fortune
        if father_age == father_end_age:
            div()
            print("Your father died.")
            print("It is your responsibility to plan the funeral.")
            print("[0] Skip")
            print(f"[1] Bury [{currency}8500]")
            print(f"[2] Cremate [{currency}1500]")
            print(f"[3] Taxidermy [{currency}15 000]")
            print(f"[4] Donate To Science [{currency}0]")
            try:
                ch = int(input(">"))
            except:
                ch = 4
            if ch == 0:
                print("You skipped the funeral.")
            elif ch == 1:
                print("Your father was buried.")
                money -= 8500
            elif ch == 2:
                money -= 15000
                print("You cremated your father.")
                print("Choose what to do with the ashes:")
                print("[1] Sprinkle somewhere special.")
                print("[2] Put in urn")
                print("[0] Throw In Trash")
                ch = input(">")
            elif ch == 3:
                print("You had your father taxidermied.")
                money -= 15000
            elif ch == 4:
                print("Your father's body was donated to science.")
            else:
                print("You skipped the funeral.")
            from random import randint

            father_fortune = randint(1000000, 3000000)
            div()
            print(f"You inherited {currency}" + str(father_fortune))
            money += father_fortune
        if auto_deposit == 1 and age >= 6:
            savings += money
            money = 0
        # redirect
        if age <= 5:
            happiness += 0.25
            if intel <= 0.75:
                intel += 0.25
            infant()
        elif age >= 6 and age < 12:
            if age == 6:
                child_init()
            else:
                if father_rel >= 0.75:
                    savings += 520
                elif father_rel < 0.75 and father_rel > 0.25:
                    savings += 260
                if happiness <= 0.1 and is_depressed == 0:
                    is_depressed = 1
                    div()
                    print("You are now suffering from DEPRESSION.")
                    div()
                if is_depressed == 1:
                    happiness /= 4
                if is_depressed == 1 and happiness >= 0.65:
                    div()
                    print("You are no longer suffering from DEPRESSION.")
                    is_depressed = 0
                    happiness *= 2
                    div()
                child()
        elif age >= 12 and age < 18:
            if age == 12:
                teen_init()
            else:
                if happiness <= 0.1 and is_depressed == 0:
                    is_depressed = 1
                    div()
                    print("You are now suffering from DEPRESSION.")
                    div()
                if is_depressed == 1:
                    if happiness < 0.65:
                        happiness /= 4
                    else:
                        div()
                        print("You are no longer suffering from DEPRESSION!")
                        is_depressed = 0
                teen()
        elif age >= 18:
            if happiness <= 0.1 and is_depressed == 0:
                is_depressed = 1
                div()
                print("You are now suffering from DEPRESSION.")
            if is_depressed == 1 and happiness < 0.65:
                happiness /= 4
            if is_depressed == 1 and happiness >= 0.65:
                div()
                print("You are no longer suffering from DEPRESSION.")
                is_depressed = 0
                happiness *= 2
            from random import randint

            if age == 18:
                salary = 0
                hours = 0
                edu_lvl = 1
                adult_init()
            elif age >= 70 and age < 80:
                dc = randint(1, 400)
                if dc != 400:
                    pass
                else:
                    die(1)
            elif age >= 80 and age < 90:
                # print("80")
                dc = randint(1, 20)
                if dc != 20:
                    pass
                else:
                    die(1)
            elif age >= 90:
                # print("AGE TEST")
                dc = randint(1, 3)
                if dc != 3:
                    pass
                else:
                    die(1)
            elif age >= 100 and age < 120:
                dc = randint(1, 2)
                if dc == 1:
                    die(1)
                else:
                    pass
            elif age >= 120:
                div()
                print("When you reach 121, you will die of old age every year.")
                div()
                die(1)
            else:
                adult()
        else:
            raise ExitError

    def pbar(percent):
        global alt_ui
        if percent > 1:
            percent = 1
        percent *= 100
        bar = "["
        hash = percent / 5
        global alt_ui
        hash = int(hash)
        dot = 20 - hash
        for i in range(hash):
            if alt_ui == 1 or alt_ui == 2 or alt_ui == 4:
                bar += "|"
            else:
                bar += "#"
        for i in range(dot):
            if alt_ui == 1 or alt_ui == 2 or alt_ui == 3 or alt_ui == 4:
                bar += " "
            else:
                bar += "."
        bar += "]"
        print(bar)

    def pbar2(percent):
        global alt_ui
        if percent > 1:
            percent = 1
        percent *= 100
        bar = "["
        hash = percent / 5
        global alt_ui
        hash = int(hash)
        dot = 20 - hash
        for i in range(hash):
            if alt_ui == 1 or alt_ui == 2:
                bar += "|"
            else:
                bar += "#"
        for i in range(dot):
            if alt_ui == 1 or alt_ui == 2 or alt_ui == 3:
                bar += " "
            else:
                bar += "."
        bar += "]"
        return bar

    def cls():
        # code from https://github.com/fungamer2-2/Life-Simulator1
        os.system("cls" if platform == "win32" else "clear")
        return True

    def div():
        global alt_ui
        if alt_ui == 2:
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        elif alt_ui == 1:
            print("▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢")
        elif alt_ui == 3:
            print("--------------------")
        elif alt_ui == 4:
            print("|------------------|")
        else:
            print("====================")
        return True

    def br():
        div()
        print("Press ENTER to continue")
        wer = input()
        return True

    def end():
        div()
        print("This menu is obsolete. This used to be the death screen.")
        print("Now, the anticheat gets triggered.")
        div()
        print("[1] Exit")
        print("[0] Main menu")
        try:
            ch = int(input(">>"))
        except:
            ch = 1
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
        print("The developers of", game_name, "do not condone")
        print("performing any activities played out in", game_name, "in real life.")
        print("It may get you in trouble or even kill you.")
        br()
        return True

    def emergency_room(might_die):
        global health
        # you get rushed to the ER once your healh is < 0%
        # You have a 50% chance of dying

        # set might_die to 1 for a 50% death chance
        # and 0 for 100% chance of living

        from random import randint

        global health
        if might_die == 1:
            div()
            print("You were rushed to the emergency room.")
            chance = randint(1, 2)
            if chance != 2:
                print("You died.")
                die(4)
            else:
                print("You barely survived.")
                div()
                health = 0.1
                br()
                teen()
        elif might_die == 2:
            div()
            print("You were rushed to the emergency room.")
            chance = randint(1, 4)
            if chance == 4:
                print("You died.")
                die(4)
            else:
                print("You barely survived.")
                div()
                health = 0.1
                br()
                adult()
        elif might_die == 0:
            div()
            print("You were rushed to the emergency room.")
            print("You barely survived.")
            div()
            health = 0.1
            br()
            teen()
        else:
            raise ExitError

    def job_interview():
        i = rng(1, 12)
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
                ch = int(input(">"))
            except:
                ch = 0
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
                ch = int(input(">"))
            except:
                ch = 0
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
                ch = int(input(">"))
            except:
                ch = 0
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
                ch = int(input(">"))
            except:
                ch = 0
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
                ch = int(input(">"))
            except:
                ch = 0
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
            print("[4] OpenLife is better.")  # Not to blow my own trumpet.
            try:
                ch = int(input(">"))
            except:
                ch = 0
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
                ch = int(input(">"))
            except:
                ch = 0
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
                ch = int(input(">"))
            except:
                ch = 0
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
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 2 or ch == 3:
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
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1 or ch == 3:
                return True
            else:
                return False
        elif i == 11:
            print("How did you hear about this position?")
            div()
            print("[1] Indeed.com")
            print("[2] I'm not sure")
            print("[3] I saw a posting online")
            print("[4] I heard about it from your competitor.")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1 or ch == 3:
                return True
            else:
                return False
        elif i == 12:
            print("How do you deal with stressful situations?")
            div()
            print("[1] I never stress.")
            print("[2] I don't.")
            print("[3] I meditate.")
            print("[4] I step back and consider my options.")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 3 or ch == 4:
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
        print(f"[1] Cruise [{currency}4 500]")
        print(f"[2] Vacation [{currency}25 000]")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        elif ch == 1:
            if money >= 4500:
                money -= 4500
            else:
                debt += 4500
            happiness += 0.45
            div()
            print("You went for a cruise.")
            print("Enjoyment:")
            pbar(0.65)
            adult()
        elif ch == 2:
            if money >= 25000:
                money -= 25000
            else:
                debt += 25000
            happiness += 0.85
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
        print(f"[1] Name Change [{currency}150]")
        print("[x] Declare Gender")
        print("[x] Declare Sexuality")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        elif ch == 1:
            if money >= 150:
                money -= 150
                forename = input("Forename >")
                forename = forename.replace("|", "")
                surname = input("Surname >")
                surname = surname.replace("|", "")
                adult()
            else:
                div()
                print("You cannot afford that.")
                adult()

    def love():
        global money, happiness, looks, health, intel, debt, spouse, is_spouse
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age
        print("[0] Return")
        print("[1] Find Love")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 1:
            find_love()
            if False:
                adult()
            else:
                div()
                is_spouse = 1
                print(f"You are now dating {spouse.name}")
                adult()
        else:
            adult()

    def adult_activities():
        global money, happiness, looks, health, intel, debt, auto_deposit, allow_debug
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age
        print("[0] Return")
        print(f"[1] Gym [{currency}15f]")
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
        print("[14] Love")
        print("[x] Movies")
        print("[16] Nightlife")
        print("[17] Vacation")
        print("[x] Last Will And Testament")
        print("[19] Fertility")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        elif ch == 1:
            div()
            print("You went to the gym.")
            print("Enjoyment:")
            if money >= 15:
                money -= 15
            else:
                debt += 15
            pbar(1)
            happiness += 0.45
            health += 0.25
            adult()
        elif ch == 2:
            div()
            print("You visited the library.")
            print("Enjoyment:")
            pbar(0)
            intel += 0.25
            happiness -= 0.45
            adult()
        elif ch == 3:
            div()
            print("No doctors available.")
            adult()
        elif ch == 4:
            print("[1] Surrender")
            print("[0] Return")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            elif ch == 1:
                die(0)
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
            # if allow_debug == 1:
            #    print("[5] Fix Alpha 12 PR3 Save File")
            print("[6] Set AutoDeposit")
            print("[7] AllowDebug3")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            elif ch == 7:
                if allow_debug == 3:
                    allow_debug = 0
                else:
                    allow_debug = 3
            elif ch == 1:
                looks = 1
                adult()
            elif ch == 2:
                if allow_debug == 1:
                    try:
                        money = int(input(">"))
                    except:
                        adult()
                else:
                    adult()
            elif ch == 6:
                try:
                    auto_deposit = int(input(">"))
                except:
                    auto_deposit = 0
                adult()
            elif ch == 5 and allow_debug == 1:
                print("WIP")
                div()
                print("Available saves:")
                path = os.getcwd()
                dirlist = os.listdir(path)
                for item in dirlist:
                    isFile = os.path.isfile(item)
                    if isFile == True and item.endswith(".oll2"):
                        item = item.replace(".oll2", "")
                        print(item)
                    else:
                        continue
                div()
                # 0=Alpha|1=12|2=happiness|3=health|4=intel|5=looks|6=ethics|7=money
                # |8=forename|9=surname|10=age|11=work_e|12=edu_lvl|13=work_e_base|14=promo_base
                # |15=degree|16=hours|17=salary|18=expenses|19=pension
                # |20=is_depressed|21=debt|22=savings|23=year|24=is_job|25=stress
                # |26=mother_name|27=father_name|28=mother_age|29=father_age
                # |30=mother_end_age|31=father_end_age
                sn = input("Enter File Name >")
                # Windows illegal filename characters removed
                sn = sn.replace("\\", "")
                sn = sn.replace("/", "")
                sn = sn.replace("?", "")
                sn = sn.replace("*", "")
                sn = sn.replace("|", "")
                sn = sn.replace("<", "")
                sn = sn.replace(">", "")
                sn = sn.replace(":", "")
                sn = sn.replace('"', "")
                sn += ".oll2"  # file extension
                f = open(sn, "rb")
                try:
                    import codecs

                    ssave = f.read()
                    f.close()
                    ssave = codecs.decode(ssave, "base64_codec")
                    print(save)
                    ssave = ssave.decode("utf-8")
                    print(save)
                    save = ssave
                    print(save)
                    save += "|0"
                    save = save.encode("utf-8")
                    save = codecs.encode(save, "base64_codec")
                    f = open(fn, "wb")
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
                    print(
                        "Mother will die at age",
                        mother_end_age,
                        "[Current age: " + str(mother_age) + "]",
                    )
                if father_age < father_end_age:
                    print(
                        "Father will die at age",
                        father_end_age,
                        "[Current age: " + str(father_age) + "]",
                    )
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
            print(f"[1] Get the surgery [{currency}10,000] [+25% looks]")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            elif ch == 1:
                if money < 10000:
                    div()
                    print("You cannot afford it.")
                    adult()
                else:
                    money -= 10000
                    looks += 0.25
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
        elif ch == 14:
            love()
        elif ch == 16:
            print("[1] Partying")
            print("[x] One-Night Stand")
            print("[3] Drugs")
            print("[0] Return")
            div()
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            if ch == 1:
                print("You partied.")
                print("Enjoyment:")
                pbar(0.85)
                happiness += 0.65
                health -= 0.15
                intel -= 0.25
                adult()
            elif ch == 3:
                print("[1] Cannabis")
                print("[2] Cocaine")
                print("[3] Heroin")
                print("[4] Gym Candy [Anabolic Stereoids]")
                print("[5] Crack")
                try:
                    ch = int(input(">"))
                except:
                    ch = 0
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
            print(f"[x] Vascetomy [{currency}25 000]")
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 0:
                adult()
            elif ch == 1 and age < 45:
                div()
                print("You donated sperm :(")
                print(f"You earned {currency}25")
                money += 25
                adult()
            else:
                # this one
                adult()
        else:
            # this one
            adult()

    def promotion():
        global job_id, job_lvl, promo_base, salary
        if (
            job_id == 1
            or job_id == 4
            or job_id == 11
            or job_id == 14
            or job_id == 17
            or job_id == 19
            or job_id == 21
            or job_id == 22
            or job_id == 26
            or job_id == 28
            or job_id == 29
            or job_id == 30
        ):
            job_lvl == 1
            adult()
        elif job_id == 18:
            if job_lvl == 2:
                adult()
            else:
                salary = 65
        elif job_id == 18:
            if job_lvl == 23:
                adult()
            else:
                salary = 35
        elif job_lvl < 3:
            job_lvl += 1
            print("You got promoted.")
            if job_id == 2:
                if job_lvl == 2:
                    salary = 15
                else:
                    salary = 20
            elif job_id == 3:
                if job_lvl == 2:
                    salary = 40
                else:
                    salary = 50
            elif job_id == 6:
                if job_lvl == 2:
                    salary = 50
                else:
                    salary = 70
            elif job_id == 8:
                if job_lvl == 2:
                    salary = 70
                else:
                    salary = 90
            elif job_id == 9:
                if job_lvl == 2:
                    salary = 55
                else:
                    salary = 65
            elif job_id == 10:
                if job_lvl == 2:
                    salary = 45
                else:
                    salary = 55
            elif job_id == 12:
                if job_lvl == 2:
                    salary = 40
                else:
                    salary = 55
            elif job_id == 13:
                if job_lvl == 2:
                    salary = 75
                else:
                    salary = 95
            elif job_id == 15:
                if job_lvl == 2:
                    salary = 45
                else:
                    salary = 65
            elif job_id == 20:
                if job_lvl == 2:
                    salary = 55
                else:
                    salary = 75
            elif job_id == 25:
                if job_lvl == 2:
                    salary = 35
                else:
                    salary = 45
            elif job_id == 0:
                adult()
            print(f"New Salary: {currency}" + str(salary))
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
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        elif ch == 1:
            div()
            print("You resigned :(")
            salary = 0
            is_job = 0
            hours = 0
            work_e_base = 0
        elif ch == 2:
            try:
                hours = int(input(">"))
            except:
                pass
            if hours < min_hours:
                hours = min_hours
            if hours > 70:
                hours = 70
            adult()
        elif ch == 3 and work_e_base >= 20:
            div()
            pension_questions()
            base = salary * hours * 52
            base /= 2
            base = int(base)
            print(
                f"Your pension is {currency}" + str("{:,}".format((base))), "per year."
            )
            pension += base
            salary = 0
            is_job = 0
            hours = 0
            work_e_base = 0
            adult()
        else:
            adult()

    def adult_assets():
        global money, savings, debt
        print("[0] Return")
        print("[x] Shop")
        print("[x] Item List")
        print("[3] Loan")
        print("[4] Savings")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        elif ch == 3:
            div()

            print(f"Debt: {currency}" + str("{:,}".format((int(debt)))))
            print("20% interest, 10% autopaid per year")
            div()
            print("[1] Loan")
            print("[2] Pay Off")
            print("[0] Return")
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 0:
                adult()
            elif ch == 1:
                try:
                    loan = int(input(">"))
                except:
                    adult()
                if loan < 0:
                    loan = 0
                debt += loan
                money += loan
                adult()
            elif ch == 2:
                if money < debt:
                    debt -= money
                    money = 0
                    adult()
                else:
                    money -= debt
                    debt = 0
                    adult()
            else:
                adult()

        elif ch == 4:
            print(f"Savings: {currency}" + str("{:,}".format((savings))))
            print("Interest: 10%")
            div()
            print("[0] Return")
            print("[1] Deposit")
            print("[2] Withdraw")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            elif ch == 1:
                print(f"Money: {currency}" + str("{:,}".format((money))))
                try:
                    dep = int(input(">"))
                except:
                    adult()
                if money < dep:
                    dep = money
                if dep < 0:
                    dep = 0
                money -= dep
                savings += dep
                savings = int(savings)
                adult()
            elif ch == 2:
                print(f"Savings: {currency}" + str("{:,}".format((savings))))
                try:
                    wit = int(input(">"))
                except:
                    adult()
                if wit > savings:
                    wit = savings
                if wit < 0:
                    wit = 0
                money += wit
                savings -= wit
                adult()
            else:
                adult()
        else:
            adult()

    def occupation():
        global edu_lvl, money, is_job, stress, part_time_salary
        global did_tutor, salary, hours
        div()
        print(f"Salary: {currency}" + str(salary) + "/h")
        print("Hours: " + str(hours))
        print(f"Salary Per Year: {currency}" + str(salary * hours * 52))
        div()
        print("Stress:", pbar2(stress))
        div()
        print("[0] Return")
        print("[1] Education")
        if is_job == 1:
            print("[2] Job Menu")
        print("[3] Part-Time Jobs")
        print("[4] Freelance")
        print("[x] Job Recruiter")
        print("[5] Jobs")
        print("[x] Special Careers")
        print("[x] Local Gangs")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        elif ch == 5:
            job_centre()
        elif ch == 2 and is_job == 1:
            job_menu()
        elif ch == 1:
            if edu_lvl == 0:
                print(f"[1] GED [{currency}500]")
                try:
                    ch = int(input(">"))
                except:
                    ch = 0
                if ch == 0:
                    adult()
                elif ch == 1:
                    money -= 500
                    print("You got a GED and have high school-equivalent education!")
                    edu_lvl = 1
                    adult()
            elif edu_lvl == 1:
                print(f"[1] University [{currency}25,000]")
                print("[0] Return")
                try:
                    ch = int(input(">"))
                except:
                    ch = 0
                if ch == 0:
                    adult()
                elif ch == 1:
                    div()
                    uni_check()
                    adult()
            else:
                adult()
        elif ch == 3:
            print("[0] Return")
            print(f"[1] Secretary [{currency}15/h] [10h]")
            print(f"[2] Mall Santa [{currency}25/h] [10h]")
            print(f"[3] None [{currency}0/h] [0h]")
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 1:
                div()
                print("You are now a secretary.")
                print(f"Salary: {currency}15/h")
                part_time_salary = 15
                adult()
            elif ch == 2:
                div()
                print("You are now a mall santa.")
                print(f"Salary: {currency}25/h")
                part_time_salary = 25
                adult()
            elif ch == 3:
                div()
                print("No longer working part-time.")
                part_time_salary = 0
                adult()
            else:
                adult()
        elif ch == 4:
            if did_tutor == 0:
                print(f"[1] Tutor [{currency}19/h]")
            print(f"[x] Handyman [{currency}18/h]")
            print(f"[x] Truck Driver [{currency}17/h]")
            print("[0] Return")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            elif ch == 1:
                if did_tutor == 0:
                    div()
                    print("You did tutoring for 30 hours this week.")
                    base = 19 * 30
                    print(f"You made {currency}" + str(base))
                    did_tutor = 1
                    money += base
                    br()
                    adult()
                else:
                    div()
                    print("You did tutoring already.")
                    br()
                    adult()
            elif ch == 2:
                base = 18 * 30
                div()
                adult()
                print("You became a handyman for 30 hours this week.")
                print(f"You made {currency}" + str(base))
                br()
                money += base
                adult()
            elif ch == 3:
                base = 30 * 17
                adult()
                print("You became a truck driver for 30 hours this week.")
                print(f"You made {currency}" + str(base))
                money += base
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
        # save=forename+"|"+surname+"|"+str(age)+"|"+str(happiness)+"|"+str(looks)+"|"+str(health)+"|"+str(ethics)+"|"+str(intel)+"|"+str(mother_rel)+"|"+str(father_rel)+str(money)+"|"+mother_name+"|"+father_name+"|"+str(mother_age)+"|"+str(father_age)
        # John|Sith|18|1|0.9|0.8|0.7|0.6|1|1|12000|Jill|Shill|32|35
        sn = input("Save Name >")
        sn += ".oll"
        try:
            f = open(sn, "rb")
        except:
            mainmenu()
        import codecs

        save = f.read()
        save = codecs.decode(save, "base64_codec")
        save = save.decode("utf-8")
        save = "John|Sith|18|1|0.9|0.8|0.7|0.6|1|1|12000|Jill|Shill|32|35"
        print(save)
        save = save.replace("||", "|")
        save = save.split("|")
        print(save)
        global mother_age, father_age
        global mother_name, father_name
        global juvie_offences
        global happiness, health, intel, looks, ethics, grades, clout, socialc
        global mother_rel, father_rel
        forename = save[2]
        surname = save[3]
        age = int(save[4])
        happiness = float(save[5])
        looks = float(save[6])
        health = float(save[7])
        ethics = float(save[8])
        intel = float(save[9])
        mother_rel = float(save[10])
        father_rel = float(save[11])
        money = int(save[12])
        mother_name = save[13]
        father_name = save[14]
        mother_age = int(save[15])
        father_age = int(save[16])
        br()
        adult()

    def edit_configuration():
        global alt_ui, auto_deposit
        print("[1] Auto-Deposit")
        print(
            "[Every year, all of your money gets automatically sent to your savings account]"
        )
        div()
        print("[2] Change Theme")
        print(
            f"[Change the look of {game_name}. Does not persist when you exit to main menu.]"
        )
        div()
        print("[0] Return")
        try:
            ch = int(input(">"))
        except:
            return True
        if ch == 1:
            print("[1] Enable")
            print("[0] Disable")
            try:
                ch = int(input(">"))
            except:
                auto_deposit = 0
            if ch == 1:
                auto_deposit = 1
            else:
                auto_deposit = 0
            return True
        elif ch == 2:
            print("[1] Original Theme [Alpha 10]")
            print("[2] Default Theme [Alpha 11]")
            print("[3] Throwback Mode [Alpha 13]")
            try:
                ch = int(input(">"))
            except:
                alt_ui = 2
            if ch == 1:
                alt_ui = 0
            elif ch == 2:
                alt_ui = 2
            elif ch == 3:
                alt_ui = 3
            else:
                alt_ui = 2
            return True
        else:
            return True

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
        if allow_debug == 1:
            div()
            print("[x] Create Debug Log")
            print("[8] DumpGameData")
        div()
        print("[9] Options")
        div()
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        elif ch == 1:
            save_game()
            adult()
        elif ch == 9:
            edit_configuration()
        elif ch == 8 and allow_debug == 1:
            # https://www.geeksforgeeks.org/viewing-all-defined-variables-in-python/
            # This code spits out all variables in memory
            # in a format I can filter using a special program in order to list them by type :) [used when developing save system]
            # Very, very useful and very, very specialised.
            all_variables = dir()

            # Iterate over the whole list where dir()
            # is stored.
            for name in all_variables:

                # Print the item if it doesn't start with '__'
                if not name.startswith("__"):
                    myvalue = eval(name)
                    print(name, "|", type(myvalue))
                    # print(name, "is", type(myvalue), "and is equal to ", myvalue)
        elif ch == 2:
            print("[0] Cancel")
            print("[1] Exit and Save")
            print("[2] Exit Without Saving")
            try:
                ch = int(input(">"))
            except:
                ch = 0
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
                ch = int(input(">"))
            except:
                ch = 0
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
        global edu_lvl, pension, job_lvl, is_spouse, spouse
        global salary, hours
        global allow_debug
        global mother_age, father_age
        global mother_name, father_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel, part_time_salary
        global money, is_depressed, work_e, is_job
        global job_id, job_lvl
        global money
        money = int(money)
        if happiness > 1:
            happiness = 1
        if happiness < 0:
            happiness = 0
        if health > 1:
            health = 1
        if health < 0:
            emergency_room(2)
        if intel > 1:
            intel = 1
        if looks > 1:
            looks = 1
        if intel < 0:
            intel = 0
        if looks < 0:
            looks = 0
        try:
            if spouse.rel > 1:
                spouse.rel = 1
        except:
            pass
        try:
            if spouse.rel < 0:
                spouse.rel = 0
        except:
            pass
        global forename, surname
        global mother_rel, father_rel
        div()
        print(forename + " " + surname)
        try:
            if spouse.lvl == 2:
                print(f"[Married to {spouse.name}]")
        except:
            pass
        if pension > 0 and money < 400000000000:
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
            if part_time_salary == 0:
                print("Unemployed")
        if part_time_salary > 0:
            print("Working Part-Time")
        div()
        print("Age", age)
        print(f"{currency}" + str("{:,}".format((money))))
        if pension < 1:
            div()
        if edu_lvl == 1 and pension < 1:
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
        if pension < 1:
            print("Work Experience:", work_e, "Years")
        global work_e_base
        if is_depressed == 1:
            div()
            print("Suffers from: Depression")
        div()
        if happiness >= 0.9:
            print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "% :D")
        elif happiness <= 0.25:
            print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "% :(")
        else:
            print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "%")
        if health <= 0.25:
            print("Health:   ", pbar2(health), str(int(health * 100)) + "% [!]")
        elif health >= 0.9:
            print("Health:   ", pbar2(health), str(int(health * 100)) + "% <3")
        else:
            print("Health:   ", pbar2(health), str(int(health * 100)) + "%")
        if intel <= 0.25:
            print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "% [!]")
        elif intel >= 0.9:
            print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "% :)")
        else:
            print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "%")
        if looks >= 0.9:
            print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "% :O")
        elif looks <= 0.25:
            print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "% :(")
        else:
            print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "%")
        div()
        print("[1] Occupation")
        print("[2] Assets")
        print("[0] Age Up")
        print("[3] Relationships")
        print("[4] Activities")
        print("[5] Pause Menu")
        try:
            ch = int(input(">"))
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
                print("Mother [Age " + str(mother_age) + "]")
                pbar(mother_rel)
                print("[1] Interact")
                div()
            if father_end_age > father_age:
                print(father_name)
                print("Father [Age " + str(father_age) + "]")
                pbar(father_rel)
                print("[2] Interact")
                div()
            if is_spouse == 1 and spouse.end > spouse.age:
                print(spouse.name)
                print(f"[3] Spouse [Age {spouse.age}]")
                pbar(spouse.rel)
                div()
            print("[0] Return")
            div()
            try:
                ch = int(input(">>"))
            except:
                adult()
            if ch == 1 and mother_end_age > mother_age:
                print(mother_name)
                print("Mother [Age " + str(mother_age) + "]")
                pbar(mother_rel)
                print("[0] Return")
                print("[1] Spend Time")
                print("[2] Disrespect")
                print("[3] Attack")
                try:
                    ch = int(input(">>"))
                except:
                    ch = 0
                div()
                if ch == 0:
                    adult()
                elif ch == 1:
                    div()
                    print("You spent time with your mother.")
                    mother_rel += 0.25
                    if mother_rel > 1:
                        mother_rel = 1
                    pbar(mother_rel)
                    div()
                    adult()
                elif ch == 2:
                    print("You disrespected your mother.")
                    mother_rel -= 0.25
                    happiness -= 0.35
                    if mother_rel < 0:
                        mother_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(mother_rel)
                    div()
                    adult()
                elif ch == 3:
                    print("You hit your mother.")
                    print("Damage:")
                    pbar(0.65)
                    div()
                    mother_rel -= 0.55
                    happiness -= 0.75
                    if mother_rel < 0:
                        mother_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(mother_rel)
                    div()
                    adult()

            elif ch == 2 and father_end_age > father_age:
                print(father_name)
                print("Father [Age " + str(father_age) + "]")
                pbar(father_rel)
                print("[0] Return")
                print("[1] Spend Time")
                print("[2] Disrespect")
                print("[3] Attack")
                try:
                    ch = int(input(">>"))
                except:
                    ch = 0
                div()
                if ch == 0:
                    adult()
                elif ch == 1:
                    div()
                    print("You spent time with your father.")
                    father_rel += 0.25
                    if father_rel > 1:
                        father_rel = 1
                    pbar(father_rel)
                    div()
                    adult()
                elif ch == 2:
                    print("You disrespected your father.")
                    father_rel -= 0.25
                    happiness -= 0.35
                    if father_rel < 0:
                        father_rel = 0
                    if happiness < 0:
                        happiness = 0
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
                    health -= 0.75
                    happiness = 0
                    div()
                    is_depressed = 1
                    print("You are now suffering from DEPRESSION.")
                    div()
                    father_rel -= 0.55
                    happiness -= 0.75
                    if father_rel < 0:
                        father_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(father_rel)
                    adult()
            elif ch == 3 and is_spouse == 1 and spouse.end > spouse.age:
                spouse_interact()

            elif ch == 0:
                adult()
        elif ch == 4:
            adult_activities()
        adult()

    def adult_init():
        div()
        print("You are now an adult.")
        print(
            "It is like being a teen but you can go to uni, get a job and live a proper life."
        )
        div()
        print("Clout and social currency have been removed.")
        div()
        print("Press ENTER to continue.")
        wer = input()
        global clout, socialc
        global mother_rel, father_rel
        global stress
        stress = 0.65
        from random import randint

        if mother_rel > 0.8:
            mother_rel = 0.8
        if father_rel > 0.8:
            father_rel = 0.8
        adult()

    def gang_menu():
        global respect, clout, happiness, health, is_drip, money, enemy_gang_name, enemy_gang_rel, enemy_gang_lead
        global is_sch_gang
        div()
        print("Welcome to the top-secret GANG MENU.")
        print("Here you can earn respect and Gang Points to spend")
        div()
        print("Respect:")
        if respect > 1:
            respect = 1
        if respect < 0:
            print("GANGSTER: You have greatly disappointed us.")
            print("YOU: What do you mean?")
            print("GANGSTER: You have broken our Code of Conduct.")
            print("YOU: What are you talking about!")
            print("GANGSTER: You aren't loyal.")
            print("YOU: YES I AM!")
            print("GANGSTER: We're gonna have to kick you out.")
            print("YOU: NO!")
            global is_sch_gang
            is_sch_gang = 0
            happiness = 0
            br()
            teen()
        pbar(respect)
        div()
        print("[0] Return")
        print("[x] Get Fake ID")
        print("[2] Bully Kids")
        print("[3] Enemy Gangs")
        print("[x] Gang War")
        print("[5] Drink With The Gang")
        if is_drip == 0:
            print(f"[6] Gang Drip[{currency}1500]")
        print("[7] Leave gang")
        print("[8] Rob Children")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            teen()
        elif ch == 1:
            div()
            print("Not in game yet.")
            teen()
        elif ch == 3:
            print(enemy_gang_name)
            div()
            print("Relations: ", pbar2(enemy_gang_rel))
            print("Enemy Lead:", pbar2(enemy_gang_lead))
            br()
            teen()
        elif ch == 4:
            print(enemy_gang_name)
            div()
            print("Relations: ", pbar2(enemy_gang_rel))
            print("Enemy Lead:", pbar2(enemy_gang_lead))
            div()
            print(f"You had a gang war with {enemy_gang_name}.")
            enemy_gang_rel -= 0.5
            base = rng(-50, 50) / 100
            base2 = -(base)
            enemy_gang_lead += base
            clout += base2
            respect += base2
            div()
            if enemy_gang_rel < 0:
                enemy_gang_rel = 0
            if enemy_gang_lead > 1:
                enemy_gang_lead = 1
            if enemy_gang_lead < 0:
                enemy_gang_lead = 0
            print("Relations: ", pbar2(enemy_gang_rel))
            print("Enemy Lead:", pbar2(enemy_gang_lead))
            br()
            teen()

        elif ch == 8:
            child_amount = rng(10, 50)
            take = 0
            for i in range(child_amount):
                take += rng(10, 20)
            your_take = int(take / 10)
            print(
                f"You and the gang went on a rampage in the school playground, demanding money from innocent children."
            )
            print(f"You stole {currency}{take} from {child_amount} children.")
            print(f"Since there are 10 of you, you get 10% of the take.")
            print(f"You got {currency}{your_take} as your share.")
            money += your_take
            happiness += 0.45
            respect += 0.2
            br()
            teen()
        elif ch == 2:
            div()
            print("You bullied some kids in the playground.")
            print("You took great pleasure out of doing so.")
            div()
            clout += 0.15
            respect += 0.05
            happiness += 0.25
            br()
            teen()
        elif ch == 5:
            respect += 0.05
            happiness += 0.1
            clout -= 0.05
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
                print(f"[1] Purchase [{currency}1500]")
                print("[0] Return [Gang Menu")
                div()
                try:
                    ch = int(input(">"))
                except:
                    ch = 0
                if ch == 0:
                    gang_menu()
                elif ch == 1:
                    money -= 1500
                    is_drip = 1
                    respect += 0.45
                    gang_menu()
                else:
                    gang_menu()
            else:
                div()
                print("A requirement was not fulfilled:")
                if money < 1500:
                    print(f"You need {currency}1500.")
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
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                teen()
            elif ch == 1:
                div()
                print("You left the gang.")
                is_sch_gang = 0
                teen()

    def secondary_school_menu():
        global club_count, is_sch_gang, health, happiness
        global grades, intel, happiness, stress, teen_hours, teen_salary
        div()
        print("[0] Return")
        print("[1] Secondary School")
        print("[2] Freelance")
        print("[x] Jobs")
        print("[x] Military")
        print("[5] Part-Time Jobs")
        print("[x] Special Careers")
        print("Stress:")
        pbar(stress)
        div()
        print("In", club_count, "school clubs")
        div()
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            div()
            teen()
        elif ch == 5:
            print(f"[0] Return")
            print(f"[1] Pizza Delivery [{currency}10/h] [10h]")
            print(f"[2] Newspaper Delivery [{currency}15/h] [15h]")
            print(f"[3] Lawn Mower [{currency}25/h] [5h]")
            print(f"[4] Car Washer [{currency}35/h] [10h]")
            print(f"[5] None [{currency}0/h] [0h]")
            try:
                ch = int(input(">"))
            except:
                teen()
            if ch == 1:
                teen_salary = 10
                teen_hours = 10
                teen()
            elif ch == 2:
                teen_salary = 15
                teen_hours = 15
                teen()
            elif ch == 3:
                teen_salary = 25
                teen_hours = 5
                teen()
            elif ch == 4:
                teen_salary = 35
                teen_hours = 10
                teen()
            elif ch == 5:
                teen_salary = 0
                teen_hours = 0
                teen()
            else:
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
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                teen()
            elif ch == 1:
                div()
                print("You studied until you lost your vision.")
                div()
                grades += 0.15
                intel += 0.10
                teen()
            elif ch == 2:
                div()
                print("Insted of going to school, you decided to go bowling instead.")
                div()
                grades -= 0.45
                intel -= 0.55
                happiness += 0.15
                teen()
            elif ch == 3:
                div()
                print("Are you sure?")
                print("[1] Join [+10% stress]")
                print("[0] NO")
                try:
                    ch = int(input(">"))
                except:
                    ch = 0
                if ch == 0:
                    teen()
                elif club_count >= 2:
                    div()
                    print("You cannot join more than 2 clubs.")
                    teen()
                elif ch == 1:
                    club_count += 1
                    stress += 0.1
                    teen()
                else:
                    teen()
            elif ch == 4:
                gang = is_sch_gang
                if gang == 0:
                    div()
                    print("YOU: I'd like to join your gang.")
                    if clout == 1:
                        print("GANGSTER: Sure thing, kid. Come on in.")
                        from time import sleep

                        sleep(1.5)
                        happiness += 0.55
                        print("GANGSTER: I'm sure your input will be valuable.")
                        global respect
                        respect = 0.1
                        is_sch_gang = 1
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
                        happiness -= 2.25
                        health -= 0.85
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
        print(f"{currency}" + str("{:,}".format((money))))
        div()
        print("Welcome. Items labeled with [FID] need a fake ID to be bought.")
        print("Items labeled with [GANG] require you to join the school gang.")
        div()
        print("[0] Return [Assets]")
        print(f"[1] Fake ID [{currency}450]")
        print(f"[2] Beer [{currency}10][FID]")
        print(f"[3] Cigarette pack [{currency}25][FID]")
        print(f"[4] Knife [{currency}25][GANG]")
        print(f"[5] Pistol [{currency}750][GANG]")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            teen_assets()
        elif ch == 1:
            if money >= 450 and fake_id == 0:
                money -= 450
                fake_id = 1
                div()
                print("You bought a fake ID.")
                teen()
            else:
                div()
                print("You cannot afford/already have that!")
                teen()
        elif ch == 2:
            if money >= 10 and fake_id == 1:
                money -= 10
                happiness += 0.25
                health -= 0.55
                div()
                print("You had a beer.")
                teen()
            else:
                div()
                print("You cannot afford this and/or you don't have a fake ID.")
                teen()
        elif ch == 3:
            if money >= 25 and fake_id == 1:
                money -= 25
                happiness += 0.50
                health -= 0.75
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
        print(f"Money: {currency}" + str(money))
        div()

        print("Item List:")
        div()
        print("[1] Buy Items")
        print("[2] Item List")
        if fake_id >= 1:
            print("[3] Fake ID Hub")
        print("[0] Return")
        try:
            ch = int(input(">"))
        except:
            ch = 0
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
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            teen()
        elif ch == 1:
            div()
            print("You went to the gym.")
            happiness += 0.45
            health += 0.35
            print("Enjoyment:")
            pbar(1)
            teen()
        elif ch == 2:
            div()
            print("You visited the library.")
            print("Enjoyment:")
            pbar(0.25)
            happiness -= 0.1
            intel += 0.15
            teen()
        elif ch == 3:
            div()
            print("No doctor available.")
            teen()
        elif ch == 4:
            print("[0] Return")
            print("[1] Surrender", forename, surname + "?")
            try:
                ch = int(input("<<"))
            except:
                ch = 0
            if ch == 0:
                teen()
            elif ch == 1:
                die(0)
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
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                teen()
            elif ch == 1:
                mother_rel = 1
                father_rel = 1
                teen()
            elif ch == 2:
                looks = 1
                teen()
            elif ch == 3:
                clout += 0.25
                teen()
            elif ch == 4:
                socialc += 0.25
                teen()
            elif ch == 5:
                global is_sch_gang, respect
                respect = 0.1
                is_sch_gang = 1
            else:
                teen()
        elif ch == 6:
            print("Welcome to the NEW Crime menu.")
            print("You can perform some crimes >:)")
            if juvie_offences > 0:
                div()
                print("You have committed", juvie_offences, "offence[s].")
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
                ch = int(input("<"))
            except:
                ch = 0
            if ch == 0:
                teen()
            elif ch == 1:
                print("You loitered about.")
                clout += 0.1
                teen()
            elif ch == 2:
                print("You harassed people on the street.")
                clout += 0.25
            elif ch == 3:
                from random import randint

                stolen = randint(10, 25)
                print("You stole", stolen, "money!")
                money += stolen
                teen()
            elif ch == 4:
                print("[0] Return")
                print("[1] Cigarettes")
                print("[2] Beer")
                print("[3] Mars candy bar")
                print(f"[4] Gucci handbag [{currency}150]")
                print(f"[5] Wallet [{currency}50]")
                print(f"[6] Smartphone [{currency}500]")
                try:
                    ch = int(input(">"))
                except:
                    ch = 0
                div()
                if ch == 0:
                    teen_activities()
                from random import randint

                caught = randint(1, 2)
                if ch == 1:
                    if caught == 1:
                        print("You nabbed some cigarettes from the local off-license.")
                        print("That old man had no idea!")
                        print("You enjoyed a nice smoke with your 20 friends.")
                        pause()
                        clout += 0.45
                        teen()
                    else:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        juvie_offences += 1
                        div()
                        pause()
                        clout -= 0.45
                        teen()
                elif ch == 2:
                    if caught == 1:
                        print("You took a Budweiser from the local off-license.")
                        print("Sure does taste better when it's free.")
                        clout += 0.35
                        pause()
                        teen()
                    elif caught == 2:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        juvie_offences += 1
                        div()
                        clout -= 0.35
                        pause()
                        teen()
                elif ch == 3:
                    print("Five finger discount, am I right?")
                    pause()
                    happiness += 0.15
                    clout += 0.1
                    intel -= 0.2
                    teen()
                elif ch == 4:
                    if caught == 1:
                        money += 150
                        clout += 0.55
                        print(f"You sold the handbag for {currency}150.")
                        pause()
                        teen()
                    else:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        juvie_offences += 1
                        div()
                        clout -= 0.55
                        teen()
                elif ch == 5:
                    if caught == 1:
                        print("You got a wallet. Now what?")
                        money += 50
                        clout += 0.15
                        pause()
                        teen()
                    else:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        juvie_offences += 1
                        div()
                        clout -= 0.15
                        teen()
                elif ch == 6:
                    if caught == 1:
                        print("Nice phone. Said the person I sold it to XD")
                        money += 500
                        clout += 0.75
                        happiness -= 0.45
                    else:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        juvie_offences += 1
                        clout -= 0.35
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
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 3:
            print("[x] Exit and Save")
            print("[2] Exit Without Saving")
            print("[0] Resume")
            try:
                ch = int(input(">"))
            except:
                ch = 0
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
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 3:
            print("[x] Exit and Save")
            print("[2] Exit Without Saving")
            print("[0] Resume")
            try:
                ch = int(input(">"))
            except:
                ch = 0
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
            grades = 1
        if grades < 0:
            grades = 0
        if happiness > 1:
            happiness = 1
        if happiness < 0:
            happiness = 0
        if health > 1:
            health = 1
        if health < 0:
            emergency_room(1)
        if intel > 1:
            intel = 1
        if looks > 1:
            looks = 1
        if intel < 0:
            intel = 0
        if looks < 0:
            looks = 0
        if clout > 1:
            clout = 1
        if clout < 0:
            clout = 0
        if socialc > 1:
            socialc = 1
        if socialc < 0:
            socialc = 0
        global forename, surname
        global mother_rel, father_rel
        global money
        div()
        print(forename + " " + surname)
        print("Secondary School Student")
        if is_depressed == 1:
            print("Suffers from: Depression")
        print("Age", age)
        print(f"{currency}" + str("{:,}".format((money))))
        div()
        print("Clout:          ", pbar2(clout), str(int(clout * 100)) + "%")
        print("Social Currency:", pbar2(socialc), str(int(socialc * 100)) + "%")
        div()
        print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "%")
        print("Health:   ", pbar2(health), str(int(health * 100)) + "%")
        print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "%")
        print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "%")
        div()
        print("[1] School")
        print("[2] Assets")
        print("[0] Age Up")
        print("[3] Relationships")
        print("[4] Activities")
        print("[5] Paue Menu")
        try:
            ch = int(input(">"))
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
            print("Mother [Age " + str(age + 32) + "]")
            pbar(mother_rel)
            print("[1] Interact")
            div()
            print(father_name)
            print("Father [Age " + str(age + 37) + "]")
            pbar(father_rel)
            print("[2] Interact")
            div()
            print("[0] Return")
            div()
            try:
                ch = int(input(">>"))
            except:
                teen()
            if ch == 1:
                print(mother_name)
                print("Mother [Age " + str(age + 32) + "]")
                pbar(mother_rel)
                print("[0] Return")
                print("[1] Spend Time")
                print("[2] Disrespect")
                print("[3] Attack")
                try:
                    ch = int(input(">>"))
                except:
                    ch = 0
                div()
                if ch == 0:
                    teen()
                elif ch == 1:
                    div()
                    print("You spent time with your mother.")
                    mother_rel += 0.25
                    if mother_rel > 1:
                        mother_rel = 1
                    pbar(mother_rel)
                    div()
                    teen()
                elif ch == 2:
                    print("You disrespected your mother.")
                    mother_rel -= 0.25
                    happiness -= 0.35
                    if mother_rel < 0:
                        mother_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(mother_rel)
                    div()
                    teen()
                elif ch == 3:
                    print("You hit your mother.")
                    print("Damage:")
                    pbar(0.65)
                    div()
                    mother_rel -= 0.55
                    happiness -= 0.75
                    if mother_rel < 0:
                        mother_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(mother_rel)
                    div()
                    teen()

            elif ch == 2:
                print(father_name)
                print("Father [Age " + str(age + 32) + "]")
                pbar(father_rel)
                print("[0] Return")
                print("[1] Spend Time")
                print("[2] Disrespect")
                print("[3] Attack")
                try:
                    ch = int(input(">>"))
                except:
                    ch = 0
                div()
                if ch == 0:
                    teen()
                elif ch == 1:
                    div()
                    print("You spent time with your father.")
                    father_rel += 0.25
                    if father_rel > 1:
                        father_rel = 1
                    pbar(father_rel)
                    div()
                    teen()
                elif ch == 2:
                    print("You disrespected your father.")
                    father_rel -= 0.25
                    happiness -= 0.35
                    if father_rel < 0:
                        father_rel = 0
                    if happiness < 0:
                        happiness = 0
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
                    health -= 0.75
                    happiness = 0
                    div()
                    is_depressed = 1
                    print("You are now suffering from DEPRESSION.")
                    div()
                    father_rel -= 0.55
                    happiness -= 0.75
                    if father_rel < 0:
                        father_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(father_rel)
                    teen()

            elif ch == 0:
                teen()
        elif ch == 4:
            teen_activities()
        teen()

    def teen_init():
        div()
        print("You are now a teenager.")
        print("You can now earn money and spend it on certain items.")
        print(
            "You will be able to commit juvenile crimes, but you can't go to prison for them yet. Make the most of it."
        )
        print("Enjoy!")
        div()
        print("TIP: You now have 2 new values: CLOUT and SOCIAL CURRENCY.")
        print("CLOUT is earned through crime and parties")
        print("SOCIAL CURRENCY cannot be earned yet.")
        div()
        print("Press ENTER to continue.")
        wer = input()
        global clout, socialc
        global mother_rel, father_rel
        global stress
        stress = 0.65
        from random import randint

        if mother_rel > 0.8:
            mother_rel = 0.8
        if father_rel > 0.8:
            father_rel = 0.8
        socialc = randint(1, 100)
        socialc /= 100
        clout = 0
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
            ch = int(input("<"))
        except:
            ch = 0
        if ch == 0:
            child()
        elif ch == 1:
            div()
            happiness += 0.35
            health += 0.25
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
            intel += 0.25
            div()
            child()
        elif ch == 3:
            div()
            print("No doctor available.")
            div()
            child()
        elif ch == 4:
            die(0)
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
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                child()
            elif ch == 1:
                father_rel = 1
                mother_rel = 1
            elif ch == 2:
                looks = 1
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
            ch = int(input(">"))
        except:
            ch = 0
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
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                child()
            elif ch == 1:
                div()
                print("You studied until you lost your vision.")
                div()
                grades += 0.25
                intel += 0.15
                child()
            elif ch == 2:
                div()
                print("Insted of going to school, you decided to go bowling instead.")
                div()
                grades -= 0.25
                intel -= 0.35
                happiness -= 0.45
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
            grades = 1
        if grades < 0:
            grades = 0
        if happiness > 1:
            happiness = 1
        if happiness < 0:
            happiness = 0
        if health > 1:
            health = 1
        if health < 0:
            health = 0
        if intel > 1:
            intel = 1
        if looks > 1:
            looks = 1
        if intel < 0:
            intel = 0
        if looks < 0:
            looks = 0
        global forename, surname
        global mother_rel, father_rel
        global money
        print(forename + " " + surname)
        print("Primary School Student")
        print("Age", age)
        print(f"{currency}" + str("{:,}".format((money))))
        div()
        print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "%")
        print("Health:   ", pbar2(health), str(int(health * 100)) + "%")
        print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "%")
        print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "%")
        div()
        print("[1] School")
        print("[2] Assets")
        print("[0] Age Up")
        print("[3] Relationships")
        print("[4] Activities")
        print("[5] Pause Menu")
        try:
            ch = int(input(">"))
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
            print("Mother [Age " + str(age + 32) + "]")
            pbar(mother_rel)
            print("[1] Interact")
            div()
            print(father_name)
            print("Father [Age " + str(age + 37) + "]")
            pbar(father_rel)
            print("[2] Interact")
            div()
            print("[0] Return")
            div()
            try:
                ch = int(input(">>"))
            except:
                child()
            if ch == 1:
                print(mother_name)
                print("Mother [Age " + str(age + 32) + "]")
                pbar(mother_rel)
                print("[0] Return")
                print("[1] Spend Time")
                print("[2] Disrespect")
                print("[3] Attack")
                try:
                    ch = int(input(">>"))
                except:
                    ch = 0
                div()
                if ch == 0:
                    child()
                elif ch == 1:
                    div()
                    print("You spent time with your mother.")
                    mother_rel += 0.25
                    if mother_rel > 1:
                        mother_rel = 1
                    pbar(mother_rel)
                    div()
                    child()
                elif ch == 2:
                    print("You disrespected your mother.")
                    mother_rel -= 0.25
                    happiness -= 0.35
                    if mother_rel < 0:
                        mother_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(mother_rel)
                    div()
                    child()
                elif ch == 3:
                    print("You hit your mother.")
                    print("Damage:")
                    pbar(0.65)
                    div()
                    mother_rel -= 0.55
                    happiness -= 0.75
                    if mother_rel < 0:
                        mother_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(mother_rel)
                    div()
                    child()
            elif ch == 2:
                print(father_name)
                print("father [Age " + str(age + 32) + "]")
                pbar(father_rel)
                print("[0] Return")
                print("[1] Spend Time")
                print("[2] Disrespect")
                print("[3] Attack")
                try:
                    ch = int(input(">>"))
                except:
                    ch = 0
                div()
                if ch == 0:
                    child()
                elif ch == 1:
                    div()
                    print("You spent time with your father.")
                    father_rel += 0.25
                    if father_rel > 1:
                        father_rel = 1
                    pbar(father_rel)
                    div()
                    child()
                elif ch == 2:
                    print("You disrespected your father.")
                    father_rel -= 0.25
                    happiness -= 0.35
                    if father_rel < 0:
                        father_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(father_rel)
                    div()
                    child()
                elif ch == 3:
                    div()
                    print("You hit your father.")
                    print("Damage:")
                    pbar(0.25)
                    father_rel -= 0.55
                    happiness -= 0.75
                    if father_rel < 0:
                        father_rel = 0
                    if happiness < 0:
                        happiness = 0
                    pbar(father_rel)
                    child()

                child()
            elif ch == 0:
                child()
        elif ch == 4:
            child_activities()
        child()

    def child_init():
        global mother_rel, father_rel
        print(
            "You are now a child. You have more activities to do and can also use money."
        )
        print("Once you hit 12, you'll be a teen.")
        print("Hint: Don't die")
        mother_rel -= 0.3
        if mother_rel < 0:
            mother_rel = 0
        father_rel -= 0.3
        if father_rel <= 0:
            father_rel = 0
        div()
        global money
        money = 0
        global grades, intel
        grades = intel
        print("You have now joined Primary School")
        div()
        wer = input("Press ENTER to continue. ")
        child()

    def infant_activities():
        print("[1] Surrender")
        print("[2] Return To Menu")
        print("[0] Exit")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            infant()
        elif ch == 1:
            die(0)
        elif ch == 2:
            mainmenu()

    def infant():
        global mother_name, father_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel, age
        if happiness > 1:
            happiness = 1
        if happiness < 0:
            happiness = 0
        if health > 1:
            health = 1
        if health < 0:
            health = 0
        if intel > 1:
            intel = 1
        if looks > 1:
            looks = 1
        if intel < 0:
            intel = 0
        if looks < 0:
            looks = 0
        if age > 5:
            child()
        else:
            div()
            print(forename + " " + surname)
            print("Age:", age)
            div()
            print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "%")
            print("Health:   ", pbar2(health), str(int(health * 100)) + "%")
            print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "%")
            print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "%")
            div()
            print("[0] Age Up")
            print("[1] Relationships")
            print("[2] Activities")
            try:
                ch = int(input(">"))
            except:
                ch = 999
            if ch == 0:
                age_up()
            elif ch == 1:
                print(mother_name)
                print("Mother [Age", str(age + 32) + "]")
                pbar(mother_rel)
                print("[1] Interact with")
                div()
                print(father_name)
                print("Father [Age", str(age + 37) + "]")
                pbar(father_rel)
                print("[x] Interact with")
                div()
                print("[0] Return to menu")
                div()
                try:
                    ch = int(input(">"))
                except:
                    ch == 0
                if ch == 0:
                    infant()
                elif ch == 1:
                    print(mother_name)
                    print("Mother [Age ", str(age + 32) + "]")
                    pbar(mother_rel)
                    print("[0] Leave")
                    print("[1] Spend Time With")
                    print("[2] Disobey")
                    print("[3] Attack")
                    try:
                        ch = int(input(">"))
                    except:
                        ch = 0
                    if ch == 0:
                        infant()
                    elif ch == 1:
                        mother_rel += 0.25
                        if mother_rel > 1:
                            mother_rel = 1
                        print("You spent time with your mother.")
                        pbar(mother_rel)
                    elif ch == 2:
                        print("You disobeyed your mother.")
                        mother_rel -= 0.35
                        happiness -= 0.35
                        if happiness < 0:
                            happiness = 0
                        if mother_rel < 0:
                            mother_rel = 0
                        pbar(mother_rel)
                    elif ch == 3:
                        print("You hit your mother!")
                        print("Damage:")
                        pbar(0.15)
                        mother_rel -= 0.35
                        if mother_rel < 0:
                            mother_rel = 0
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
        mother_rel = 1
        father_rel = 1
        print("Welcome to", game_name + ".")
        print("You will start a new, randomised life as a toddler.")
        print("Changes you make will affect your stats and change your life.")
        print("Since life is [literally] a game, you should try to win it.")
        print("'Winning' can be defined as reaching your life goal.")
        print("That goal can be anything. Getting your dream job, becoming rich,")
        print("living a fulfilling life, etc.")
        print("\nPress ENTER to continue.")
        global age
        wer = input()
        infant()

    def life_creator():
        global forename_m, forename_f, salary, hours
        salary = 0
        hours = 0
        global edu_lvl
        edu_lvl = 0
        global mother_name, father_name
        from random import choice

        mother_name = choice(forename_f)
        father_name = choice(forename_m)
        global happiness, health, intel, looks, ethics
        from random import randint

        print("[1] Random Life")
        print("[2] Custom Life")
        try:
            ch = int(input(">"))
        except:
            ch = 1
        if ch == 1:
            global forename, surname
            forename = input("Forename >>")
            if forename == "":
                forename = choice(forename_m)

            surname = input("Surname >>")
            if surname == "":
                surname = choice(surnames)
            forename = forename.replace("|", "")
            surname = surname.replace("|", "")
            mother_name += " " + surname
            father_name += " " + surname
            happiness = randint(1, 100)
            happiness /= 100
            health = randint(1, 100)
            health /= 100
            intel = randint(1, 100)
            intel /= 100
            looks = randint(1, 100)
            looks /= 100
            ethics = 1
            global start_age
            try:
                start_age = int(input("Enter START AGE >"))
            except:
                start_age = 0
            choose_start()
            try:
                start_age = int(input("Enter START AGE >"))
                choose_start()
            except:
                start_age = 0
                choose_start()
            choose_start()
        elif ch == 2:
            print("[1] Maxxed-out Values")
            print("[2] 0% Everything")
            print("[3] Custom Values")
            try:
                wer = int(input(">>"))
            except:
                wer = 1
            # name=input("Name >>")
            forename = input("Forename >>")
            if forename == "":
                forename = choice(forename_m)
            surname = input("Surname >>")
            if surname == "":
                surname = choice(surnames)
            try:
                start_age = int(input(">Start Age >"))
            except:
                start_age = 0
            forename = forename.replace("|", "")
            surname = surname.replace("|", "")
            from random import randint

            if wer == 1:
                happiness = randint(1, 1)
                health = randint(1, 1)
                intel = randint(1, 1)
                looks = randint(1, 1)
                ethics = 1
            elif wer == 2:
                happiness = 0
                health = 0
                intel = 0
                looks = 0
                ethics = 0
            elif wer == 3:
                from random import randint

                print("Enter the percent amount of each value.")
                try:
                    happiness = int(input("Happiness $"))
                except:
                    happiness = randint(1, 100)
                happiness /= 100
                try:
                    intel = int(input("Intelligence $"))
                except:
                    intel = randint(1, 100)
                intel /= 100
                try:
                    health = int(input("Health $"))
                except:
                    health = randint(1, 100)
                health /= 100
                try:
                    looks = int(input("Looks  $"))
                except:
                    looks = randit(1, 100)
                looks /= 100
                ethics = 1

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

        startpoint = os.getcwd()
        challenge_site = ""  # change this URL if the location changes / you want to add custom challenges
        if alt_logo == 1:
            logo = [
                " .d88888b.                             888      d8b  .d888         ",
                'd88P" "Y88b                            888      Y8P d88P"          ',
                "888     888                            888          888            ",
                "888     888 88888b.   .d88b.  88888b.  888      888 888888 .d88b.  ",
                '888     888 888 "88b d8P  Y8b 888 "88b 888      888 888   d8P  Y8b ',
                "888     888 888  888 88888888 888  888 888      888 888   88888888 ",
                "Y88b. .d88P 888 d88P Y8b.     888  888 888      888 888   Y8b.     ",
                ' "Y88888P"  88888P"   "Y8888  888  888 88888888 888 888    "Y8888  ',
                "            888                                                    ",
                "            888                                                    ",
                "            888                                                    ",
            ]
        elif alt_logo == 2:
            logo = [
                " #######  ########  ######## ##    ## ##       #### ######## ######## ",
                "##     ## ##     ## ##       ###   ## ##        ##  ##       ##       ",
                "##     ## ##     ## ##       ####  ## ##        ##  ##       ##       ",
                "##     ## ########  ######   ## ## ## ##        ##  ######   ######   ",
                "##     ## ##        ##       ##  #### ##        ##  ##       ##       ",
                "##     ## ##        ##       ##   ### ##        ##  ##       ##       ",
                " #######  ##        ######## ##    ## ######## #### ##       ######## ",
                "%div%",
                "[Throwback Mode]",
            ]
        else:
            logo = [
                "________                           .____     .__   _____         ",
                "\\_____  \\  ______    ____    ____  |    |    |__|_/ ____\\ ____   ",
                " /   |   \\ \\____ \\ _/ __ \\  /    \\ |    |    |  |\\   __\\_/ __ \\  ",
                "/    |    \\|  |_> >\\  ___/ |   |  \\|    |___ |  | |  |  \\  ___/  ",
                "\\_______  /|   __/  \\___  >|___|  /|_______ \\|__| |__|   \\___  > ",
                "        \\/ |__|         \\/      \\/         \\/                \\/  ",
                "                                                                 ",
            ]
        for l in logo:
            if l == "%div%":
                div()
            else:
                print(l)
        div()
        print("[1] New Life")
        print("[2] Load Life")
        print("[3] Credits")
        print(
            "[4] Download Latest Challenge"
        )  # Download location: https://winfan3672.000webhostapp.com/challenge/latest.py
        print("[x] Load Challenge.zip from disk")
        print("[6] Exit")
        print("[7] Changelog")
        print("[x] Download Latest Custom Life")  # Download location: N/A
        print("[x] Options")
        print("[x] Quick Create Life")
        print("[0] About Game")
        div()
        print("Version:", version)
        div()
        try:
            ch = int(input(">>"))
        except:
            ch = 1
        if ch == 1:
            life_creator()
        elif ch == 9:
            div()
            print(
                "Some or all of these options may not change when accessing the menu this way!"
            )
            br()
            div()
            edit_configuration()
            mainmenu()
        elif ch == 6:
            raise ExitError
        elif ch == 0:
            div()
            print(game_name, "is an attempt at a FULL reimplementation of BitLife.")
            print("BitLife is a life simulator released on mobile platforms.")
            print("The app suffers from:")
            print("- lazy development")
            print("- obvious cash grabs")
            print("- updates/achievements/features locked behind a paywall")
            print("- no PC release")
            print("We aim to rectify that.")
            div()
            print("We will make a version of BitLife that:")
            print("- Has more features")
            print("- Is 100% FOSS")
            print("- Has NO paywalls")
            print("- Is multi-platform [since it's in Python]")
            print(
                "- Has no compatibility/performance issues with older devices [since BitLife does not run on Arm32]"
            )

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
            print(
                "Thank you for playing the most ambitious programming project I have taken on."
            )
            div()
            print("And special thanks to fungamer2 for:")
            print("[-] Finding my project")
            print("[-] Allowing me to help out on his one []")
            print("[-] Generally being a nice guy")
            br()
            div()
            mainmenu()
        elif ch == 4:
            import urllib.request

            url = "https://winfan3672.000webhostapp.com/challenge/latest.zip"
            print("Downloading challenge...")
            try:
                urllib.request.urlretrieve(url, "challenge.zip")
            except:
                div()
                print("Failed to download challenge.")
                mainmenu()
            div()
            print("Downloaded challenge.")
            mainmenu()
        elif ch == 7:
            changelog = [
                "Alpha 13- The Childbirth Update",
                "",
                "1 Introduction",
                "1.1 What This Update Is",
                "",
                "Alpha 13 is here! It features a lot of great features that you have been dying to have added, such as:",
                "[-] Spouses",
                "",
                "This update is also the first time that you can change the currency from in-game, by editing the main file!",
                'Simply find the currency variable near the top and set it to whatever you would like, such as "$" or "â™ª"!',
                "",
                "It was originally going to have children, but that was canned due to complexity. Children will [obviously] be added, it's just that it's on the back burner for now.",
                "",
                "1.2 Alpha 14",
                "",
                "Alpha 14 will be the identity update. It will bring things like fame and friends. Be excited.",
                "",
                "1.3 Thoughts",
                "",
                "This update feels kind of half-arsed, compared to Alpha 12. I think this update is a minor let-down, but then again, I am taking the progress of the game for granted here. This update is smaller and took longer to make, but that's fine. I just need to remind myself that.",
                "",
                "2 Spouses",
                "2.1 Spouse",
                "",
                "You can have a spouse and:",
                "[-] Marry them",
                "[-] Break up with them",
                "Sadly, since it's an alpha, it will always be a female spouse and you will always be a male character.",
                "",
                "3 Die()",
                "3.1 What Is It",
                "The die() function is a universal death screen. It has 5 causes at the moment, and not all of them in use [Suicide, heart attack, health issues, cancer and old age].",
                "",
                "3.2 Menu",
                "The menu will be the front page of the OpenLife Times, a newspaper in the OpenLife universe. You will be able to read the article, and once you've read it you can:",
                "[-] Exit the game",
                "[-] Return to the main menu",
                "[-] Respawn",
                "   [-] That's right, escape death! It only works up to 130 years old.",
                "",
                "4 Job Additions",
                "4.1 Teen Jobs",
                "",
                "You can now have a job as a teen!",
                "The jobs are:",
                "[-] Pizza Delivery Person",
                "[-] Newspaper Delivery Person",
                "[-] Lawn Mower",
                "[-] Car Washer",
                "",
                "4.2 Part-Time Jobs",
                "",
                "You can now have a job alongside your job :o",
                "You work 10 hours per week, so 520 hours. ",
                "The jobs are:",
                "[-] Receptionist",
                "[-] Mall Santa",
                "",
                "5 School Gang",
                "5.1 Gang",
                "This is a half-arsed update to school gangs. It adds:",
                "[-] Gang wars",
                "[-] Enemy gangs",
                "",
                "The enemy gang has a placeholder name, sadly.",
                "",
                "6 General Additions",
                "6.1 Currency Changes",
                "The variable `currency` determines what symbol is rendered when you see the `Â£` symbol. You can edit the main file and turn it into dollars if you want.",
                "6.2 Custom Surnames",
                "Yep. Make a file called `surname.dat` and every line is a different valid surname. ",
                "6.3 SGCU",
                "SGCU [Save Game Conversion Utility] can convert an Alpha 12 save file into an Alpha 13 one. One day, it will support the original OLL files.",
                "6.4 Options Menu",
                "The options menu allows you to change themes and enable Auto Deposit for the first time ever. No more editing save files. Ok, technically you still will, since the changes get reset when you relaunch the game/exit to the main menu. But still, it's a step in the right direction.",
                "",
                "7 Bug Fixes",
                "[-] Fixed a bug where 2 `div()` elements are displayed when rendering the `Feature Not In Current Build` message on the main menu.",
                "",
                "8 Known Bugs",
                "[-] Save game breaks a few things",
                "",
                "Next Update: Identity Update",
                "Build Date: 26 Oct 2022",
                "Publish Date: 26 Oct 2022",
            ]
            for l in changelog:
                if l == "===============":
                    div()
                else:
                    print(l)
            br()
            mainmenu()
        else:
            div()
            print("That option is not available in the current build of the game")
            mainmenu()

    mainmenu()
except KeyboardInterrupt:
    try:
        print("The anticheat caught you.")
        wer = input()
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
    if allow_debug == 1 or allow_debug == 3:
        # https://www.geeksforgeeks.org/viewing-all-defined-variables-in-python/
        # This code spits out all variables in memory
        # in a format I can filter using a special program in order to list them by type :) [used when developing save system]
        # Very, very useful and very, very specialised.
        all_variables = dir()

        # Iterate over the whole list where dir()
        # is stored.
        for name in all_variables:

            # Print the item if it doesn't start with '__'
            if not name.startswith("__"):
                myvalue = eval(name)
                base = type(myvalue)
                if allow_debug != 3:
                    print(name, "|", type(myvalue))
                else:
                    print(name, "|", type(myvalue), "|", myvalue)
                # print(name, "is", type(myvalue), "and is equal to ", myvalue)

    # Code from: https://maschituts.com/how-to-clear-variables-in-python-explained/
    if allow_debug != 2:
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
