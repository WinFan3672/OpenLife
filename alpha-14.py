# OpenLife Alpha 14

# OpenLife is a FOSS replacement for BitLife.
# For years, BitLife has become worse and worse, so I decided to step in and
# replace it with this. It's way better. Trust me.
from random import randint as rng
from random import choice
from time import sleep
import os


class FriendRecompile:
    # This class is used by load_game() to take raw save data and rebuild it as a proper friend object
    # The normal Friend class cannot be used as it randomises stats
    def __init__(self, name, age, gender, intel, looks, craziness, end, rel):
        self.name = name
        self.age = age
        self.gender = gender
        self.intel = intel
        self.looks = looks
        self.craziness = craziness
        self.end = end
        self.rel = rel


class Friend:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

        self.intel = rng(1, 100) / 100
        self.looks = rng(1, 100) / 100
        self.craziness = rng(1, 100) / 100

        self.end = self.age + rng(25, 55)
        self.rel = rng(50, 75) / 100


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = 0
        self.relation = 1
        self.end = rng(35, 85)
        self.gender = rng(0, 1)


class Parent:
    def __init__(self, name, age, end, rel, gender):
        self.name = name
        self.age = age
        self.end = end
        self.rel = rel
        self.gender = gender


class Sibling:
    # This class can also be used to rebuild an object
    def __init__(self, name, age, rel):
        self.name = name
        self.age = age
        self.rel = rel


class SpouseRecompile:
    # This is a class that is used in load_game()
    # in order to rebuild the spouse object
    def __init__(
        self, name, rel, lvl, age, end, intel, looks, craziness, gender, fortune
    ):
        self.name = name
        self.age = age
        self.end = end
        self.rel = rel
        self.lvl = lvl

        self.intel = intel
        self.looks = looks
        self.craziness = craziness
        self.gender = gender
        self.fortune = fortune


class Spouse:
    def __init__(self, name, relation, relationship_level, your_age, gender):
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
        self.gender = gender

        # Level 1 = Girlfriend/Boyfriend
        # Level 2 = Married
        self.lvl = relationship_level

        self.intel = (rng(1, 100)) / 100
        self.looks = (rng(1, 100)) / 100
        self.craziness = (rng(1, 100)) / 100
        self.fortune = rng(0, 10000000)


class SpouseDatingApp:
    def __init__(self, name, relation, relationship_level, your_age, gender, age):
        # This class is used for creating a spouse.
        # It includes all necessary data.
        # The `your age` parameter refers to the player character's age
        self.name = name
        self.age = age
        if self.age < 19:
            self.age = 19
        self.end = self.age + rng(10, 35)
        if self.end > 123:
            self.end = 123
        self.rel = relation
        self.gender = gender

        # Level 1 = Girlfriend/Boyfriend
        # Level 2 = Married
        self.lvl = relationship_level

        self.intel = (rng(1, 100)) / 100
        self.looks = (rng(1, 100)) / 100
        self.craziness = (rng(1, 100)) / 100
        self.fortune = rng(0, 10000000)


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
    global has_first_run
    has_first_run = 0

    def view_ribbons(reason):
        global money, debt, ethics, intel, age, ethics, looks, age, happiness, health, is_depressed, lottery_wins, fame, is_bandit
        has_ribbon = 0
        if money > 100000000:
            print("Ribbon: Rich")
            has_ribbon = 1
        if debt >= money + savings:
            print("Ribbon: Debt Slave")
            is_ribbon = 1
        if lottery_wins >= 50:
            print("Ribbon: Cheater")
            is_ribbon = 1
        if ethics == 0:
            print("Ribbon: Bad Karma King")
            has_ribbon = 1
        if age >= 123:
            print("Ribbon: Geriatric")
            has_ribbon = 1
        if intel <= 0.15:
            print("Ribbon: Stupid")
            has_ribbon = 1
        if fame > 0:
            print("Ribbon: Famous")
            has_ribbon = 1
        if intel >= 0.75:
            print("Ribbon: Nerd")
            has_ribbon = 1
        if reason == -1:
            has_ribbon = 1
            print("Ribbon: Wasteful")
        if age < 18:
            has_ribbon = 1
            print("Ribbon: Unlucky")
        if is_bandit == 1:
            print("Ribbon: Bandit")
        if looks >= 0.75:
            has_ribbon = 1
            print("Ribbon: Beautiful")
        if looks == 1 and intel == 1 and happiness == 1 and health == 1:
            has_ribbon = 1
            print("Ribbon: Perfectionist")
        if is_depressed == 1:
            has_ribbon = 1
            print("Ribbon: Depressed")

        if has_ribbon == 0:
            print("Ribbon: Mediocre")
        return True

    def first_run():
        global has_first_run
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
        alt_ui = 3

        global alt_logo, game_name, version
        # 0= Original logo [Alphas 1-10]
        # 1= Current logo
        # 2= "Throwback Mode" logo

        # It is set to `1` by default
        alt_logo = 2

        # End of configurable data
        has_first_run = 1

    def game_init():

        global has_first_run
        if has_first_run == 0:
            first_run()
        # Semi-Configurable Data
        global game_name, version
        game_name = "OpenLife"
        version = "Alpha 14 [4 Nov 2022]"

        global app_version, sub_version
        app_version = [0, 0, 14]
        sub_version = 0

        # Set this to 0 to hide the loaded forenames message
        verbose_message = 1

        # Non-configurable data
        global lottery_wins, is_bandit, book_base
        lottery_wins, is_bandit = 0, 0
        book_base = 0  # Decreases every year. Incremented by 3 when you publish a book. Can only publish a book if this value = 0
        global fame, is_wpp, friend_count
        fame = 0
        is_wpp = 0
        friend_count = 0
        global juvie_years, prison_years, sentence
        juvie_years = 0
        prison_years = 0
        sentence = 0
        global is_appeal, behaviour
        is_appeal = 0
        behaviour = 1.5  # If it's 1.5, you have never been to prison :)
        global is_trans
        is_trans = 0
        global is_hbp
        is_hbp = 0  # When you have 75%+ stress, you have a 50% chance of getting high blood pressure.
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
        global forename_m, forename_f, surnames, gang_names, compliments, insults, debates, spend_time, job_roles, birthdays
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
        # The compliments were taken from fungamer2's Life-Simulator1 and edited to make it compatible with OpenLife.
        compliments = [
            "a boss",
            "a bubbly personality",
            "a brilliant mind",
            "a champion",
            "a gem",
            "a genius",
            "a jewel",
            "a legend",
            "a player",
            "a revolutionary",
            "a smart cookie",
            "a treasure",
            "a winner",
            "a wizard",
            "a VIP",
            "a visionary",
            "adorable",
            "admirable",
            "an OG",
            "an eager beaver",
            "brave",
            "bright",
            "brilliant",
            "charming",
            "clever",
            "cool",
            "courageous",
            "cute",
            "dashing",
            "delightful",
            "dope",
            "elite",
            "fascinating",
            "fearless",
            "fine",
            "fresh",
            "gorgeous",
            "golden",
            "groovy",
            "inspiring",
            "intelligent",
            "legendary",
            "lionhearted",
            "magnetic",
            "magnificent",
            "motivating",
            "neat",
            "nifty",
            "one-of-a-kind",
            "a perfect 10",
            "phenomenal",
            "rad",
            "savage",
            "smart",
            "spectatular",
            "stellar",
            "strong",
            "stunning",
            "stylish",
            "swell",
            "the best",
            "the GOAT",
            "the greatest",
            "the life of the party",
            "unparalled",
            "wise",
            "wonderful",
        ]

        # The insults were taken from fungamer2's Life-Simulator1 and edited to make it compatible with OpenLife.
        insults = [
            "a dimwit",
            "a dork",
            "a douchebag",
            "a dummy",
            "a dunce",
            "a fatty",
            "a freak",
            "a goblin",
            "a jerk",
            "a jumpoff",
            "a lamebrain",
            "a loser",
            "a maniac",
            "a mouth-breather",
            "a pig",
            "a pumpkinhead",
            "a punk",
            "a scallywag",
            "a simpleton",
            "a snake",
            "a tool",
            "a tramp",
            "a triple-chin",
            "a twat",
            "a twit",
            "a villain",
            "a vulture",
            "a weasel",
            "an abomination to mankind",
            "an airhead",
            "an idiot",
            "an imbecile",
            "awful",
            "brainless",
            "careless",
            "dumb",
            "evil",
            "foolhardy",
            "mediocre at best",
            "mentally defective",
            "nasty",
            "obtuse",
            "psycho",
            "putrid",
            "skeezy",
            "stupid",
            "trashy",
            "weak",
            "weaksauce",
            "a dickhead",
            "a dickhead",
            "a dickhead",
            "a dickhead",
            "a dickhead",
            "a dickhead",
        ]
        debates = [
            "why cats are better than dogs",
            "why dogs are better than cats",
            "the Russia-Ukraine War",
            "High Fuel Prices",
            "the Metaverse",
            "the Economic crisis of Sri Lanka",
            "Moonlighting",
            "the Pros and Cons of working from home",
            "whether people should invest in cryptocurrency",
            "the Biomedical waste crisis",
            "the impact of 5G on the global economy",
            "how to prevent the next pandemic",
            "the impact of COVID-19 on the global economy",
            "the pros and cons of block chain technology",
            "the role of social media in international politics",
            "how to end the threat of nuclear war",
            "the impact of COVID-19 on the education sector",
            "Taliban rule in Afghanistan",
            "the rise of the gig economy",
            "the harms of passive smoking",
            "the advantages and disadvantages of having a credit card",
            "whether software should be free for everyone",
            "whether gambling should be allowed from the age of 16",
            "problems caused by the economic boycott in Cuba",
            "how international trade barriers work",
            "how the United Nations is based on diplomacy and strengthening relationships",
            "whether or not public schools are safe enough",
            "whether it is necessary to hold value in what you argue",
            "why drink driving is dangerous",
            "how India became such a large milk producer",
            "how to make money with recycling",
            "the decreasing productivity of the Japanese workforce",
            "a business model to help health-conscious customers",
            "what the best technologies are to safeguard the right of free speech on the internet",
            "what the best technologies are to safeguard the right of privacy on the internet",
            "how to check for the signs of burnout",
            "how to overcome the coal crisis in India",
            "the causes of bullying in schools",
            "why we should have a minimum wage",
            "whether universal basic income is a good idea",
            "the leadership changes needed in our country",
            "whether empowering women is the solution to violence against women",
            "the effects of communalism on social cohesion",
            "whether we're becoming too sensitive in society",
            "lessons for the world from the COVID-19 pandemic",
            "whether crime rates increase because of unemployment",
            "causes of poverty around the world",
            "the effects of the Internet of Things on our lives",
            "whether drug abuse is rampant among teenagers",
            "whether anemia effects urban society",
            "gender equality in the workplace",
            "whether the wealthy should be taxed more",
            "whether the poor should be given more assistance",
            "whether it is possible to maintain a work-life balance",
            "whether saying 'women make good managers' is sexist like saying 'asians are good at maths' is racist",
            "whether job creators are needed more than job seekers",
            "whether a borderless world is a myth or a reality",
            "what would happen if Bitcoin crashed to zero and whether it is possible",
            "business ethics in today's market compared with the past and the potential future",
            "whether patience is important in business and management",
            "whether the family-run business is relevant in today's market",
            "whether E-commerce discounts are harmful in the long run and is it the business or customer being harmed",
            "whether globalisation is an opportunity or a threat",
            "how markets are found and not created",
            "whether the world is ready for a cashless society",
            "whether physical infrastructure is the answer to social equality",
            "whether the public sector being a guarantor of job security is a myth",
            "whether a circular economy is key to sustainable development",
            "the contribution of the Indian IT industry to the US and global economy",
            "whether democracy is a hindrance to economic reforms in India",
            "the technology behind Zero Budget Natural Farming",
            "the effects of technological change on jobs",
            "whether pervasive technology is creating a generation of cyber zombies",
            "whether the IT industry will create more or less jobs in the future",
            "whether artificial intelligence can replace human intelligence",
            "the effects of big data on information privacy",
            "whether automation will create more or less jobs",
            "the benefits and challenges of data localisation",
            "whether artifical intelligence will change the future",
            "how technology can be used to tackle financial crimes",
            "whether polythene bags should be completely banned",
            "how to control air pollution levels",
            "whether green jobs are essential for sustainable development",
            "how to manage natural disasters",
            "how to manage financial disasters",
            "methods of disaster recovery",
            "the effects of Coronaviruses on the environment",
            "whether smart farming is the future of agriculture",
            "whether genetic engineering in agriculture is good or bad",
            "the effects of climate on the farming system and food supply",
            "whether automation in farming is good",
            "whether collective farming is a boon or a bane",
            "our views on natural versus factory farming",
            "our views on conventional farming and organic farming",
            "the role of women in agriculture",
            "whether agroforestry destroys the environment",
            "gay marriage and your views on it",
            "whether war is the best option to solve international disputes",
            "whether primary school children should be allowed to own mobile phones",
            "whether using animals for medical research should be allowed",
            "whether men and women will ever be equal, if they already are, and whether equality will last",
            "whether you can have a happy family life and a successful career at the same time",
            "whether marriage is an outdated institution",
            "whether citizens should be allowed to carry guns and other weapons",
            "whether the death penalty is acceptable for any reasons",
            "whether non-citizens and tourists should be allowed to vote in their country of residence",
            "whether sex education should be taught to children under 12",
            "whether or not women are paid the same as men",
            "whether bribery and corruption is acceptable in government",
            "whether bribery and corruption is acceptable in private business",
            "whether music that glorifies violence should be banned",
            "whether condoms should be distributed for free in primary schools",
            "whether nuclear weapons are necessary weapons",
            "whether teachers should be allowed to carry guns",
            "whether professional sports people earn too much money",
            "our views on whether or not beauty contests should be banned",
            "our views on whether or not cosmetic surgery should be outlawed",
            "our views on whether or not abortions are okay",
            "our views on whether or not social deprivation causes crime",
            "our views on whether or not military service should be compulsory",
            "our views on whether or not war is ever an option for solving international disputes",
            "our views on whether or not torture can be acceptable in some cases",
            "our views on whether or not curfews keep teens out of trouble",
            "our views on whether or not we're becoming too dependent on computers",
            "our views on whether or not smoking should be banned worldwide",
            "our views on whether or not it should be illegal to ride a bicycle without a helmet",
            "our views on whether or not single sex schools are bad for childhood development and lead to unhealthy views of the opposite sex",
            "our views on whether or not homework is harmful",
            "our views on whether or not the United Nations is a failed organisation",
            "our views on whether or not intelligence tests should be given before couples can have children",
            "our views on whether or not a woman's place is in the home",
            "our views on whether or not it's a man's world",
            "our views on whether or not money makes you happy",
            "our views on whether or not money can buy you happiness",
            "our views on whether or not the internet must be censored to protect society",
            "our views on whether or not genetically modified foods have no ill health effects",
            "our views on whether a man should have a wife for the family and a paramour for pleasure",
            "our views on whether a woman should have a husband for the family and a paramour for pleasure",
            "our views on whether soft drugs should be legalised",
            "our views on whether or not electric cars help the environment",
            "our views on whether or not staying unmarried leads to a happier life",
            "our views on whether or not software piracy is a real crime",
            "our views on whether or not religion is needed",
            "our views on whether veganism is the key to solving climate change",
            "our views on whether the police force is institutionally racist",
            "our views on whether democracy must be imposed on nations",
            "our views on whether the war in Iraq was justified",
            "our views on whether your race affects your intelligence",
            "our views on whether your race affects your sporting ability",
            "our views on whether the world is over populated and steps must be taken to reduce births",
            "whether or not euthanasia should be illegal",
            "whether or not cloning is a valuable scientific pursuit",
            "whether obesity is a disease and not a lifestyle choice",
            "whether or not video games contribute to youth violence",
            "whether the drinking age should be lowered",
            "whether the drinking age should be raised",
            "whether the smoking age should be lowered",
            "whether the smoking age should be raised",
            "whether the age of consent should be lowered",
            "whether the age of consent should be raised",
            "whether the voting age should be lowered",
            "whether the voting age should be raised",
            "whether the driving age should be lowered",
            "whether the driving age should be raised",
            "whether the gambling age should be lowered",
            "whether the gambling age should be raised",
            "whether the military service age should be lowered",
            "whether the military service age should be raised",
            "whether drugs should be accepted in sports",
            "whether self driving cars are going to make our lives easier",
            "whether climate change exists",
            "whether carbohydrates are more damaging than fats",
            "whether terrorism can be justifed",
            "whether or not street prostitution should be illegal",
            "whether or not prostitution in a brothel should be illegal",
            "whether or not prostituting yourself in your own home should be illegal",
            "whether prisoners should be allowed to vote",
            "whether prenuptual agreements make families stronger",
        ]
        spend_time = [
            "to practice sumo wrestling",
            "to play in the rain",
            "to toilet paper the neighbour's house",
            "to scare random people by jumping out of the bushes at a local park",
            "to make a wish while throwing a coing in a fountain",
            "to watch toy unboxing videos",
            "to a café to play cards",
            "to watch a movie under the stars in the park",
            "to perform in a flash mob at the grocery store",
            "to fly a kite",
            "to a rugby game",
            "to the circus",
            "longboarding",
            "to a Hindu temple",
            "to build a sandcastle in a sandbox at the park",
            "to an escape room",
            "antiquing",
            "to write haikus",
            "to play in the sprinklers at the local park",
            "to play bingo at the community centre",
            "to an arcade",
            "to throw paper aeroplanes off the bleachers at the local high school",
            "to the water park",
            "to the aquarium to look at sharks",
            "to sing P!nk songs at karaoke night",
            "to the movies",
            "axe throwing",
            "to make home made mini pizzas",
            "to a painting class",
            "to have a random dance party in a public plaza",
            "to plant trees in the forest",
            "whale watching",
            "to make and pass out balloon animals at the park",
            "snowboarding",
            "to the park",
            "to graffiti train cars",
            "to learn origami at the community centre",
            "birdwatching",
            "to the shooting range",
            "to do caricature drawings of random people in a public place",
            "yodelling",
            "deep sea fishing",
            "to a carnival",
            "to ding dong ditch the neighbours",
            "to parkour hardcore",
            "to watch a random trial at the municipal court",
            "to a rugby game",
            "to make selfies for Instagram",
            "to the museum",
            "to walk along a scenic vista",
            "to watch toy unboxing videos",
            "to fly a drone",
            "to make a safety evacuation map",
            "horseback riding in the countryside",
            "to dinner",
            "to a puppet-making seminar",
        ]
        job_roles = [
            "Exorcist",
            "Pilot",
            "Lawyer",
            "Monk",
            "Wedding Planner",
            "Soldier",
            "Architect",
            "Cashier",
            "Oohber Driver",
            "Flight Attendant",
            "Hairdresser",
            "Judge",
            "Librarian",
            "Librarian",
            "Nun",
            "Photographer",
            "Translator",
            "Accountant",
            "Teacher",
            "Game Developer",
            "Banker",
            "App Developer",
            "Engineer",
            "College Lecturer",
            "Editor",
            "Exotic Dancer",
            "Stockbroker",
            "P*rnographer",
        ]
        birthdays = [
            "January 1",
            "January 2",
            "January 3",
            "January 4",
            "January 5",
            "January 6",
            "January 7",
            "January 8",
            "January 9",
            "January 10",
            "January 11",
            "January 12",
            "January 13",
            "January 14",
            "January 15",
            "January 16",
            "January 17",
            "January 18",
            "January 19",
            "January 20",
            "January 21",
            "January 22",
            "January 23",
            "January 24",
            "January 25",
            "January 26",
            "January 27",
            "January 28",
            "January 29",
            "January 30",
            "January 31",
            "February 1",
            "February 2",
            "February 3",
            "February 4",
            "February 5",
            "February 6",
            "February 7",
            "February 8",
            "February 9",
            "February 10",
            "February 11",
            "February 12",
            "February 13",
            "February 14",
            "February 15",
            "February 16",
            "February 17",
            "February 18",
            "February 19",
            "February 20",
            "February 21",
            "February 22",
            "February 23",
            "February 24",
            "February 25",
            "February 26",
            "February 27",
            "February 28",
            "March 1",
            "March 2",
            "March 3",
            "March 4",
            "March 5",
            "March 6",
            "March 7",
            "March 8",
            "March 9",
            "March 10",
            "March 11",
            "March 12",
            "March 13",
            "March 14",
            "March 15",
            "March 16",
            "March 17",
            "March 18",
            "March 19",
            "March 20",
            "March 21",
            "March 22",
            "March 23",
            "March 24",
            "March 25",
            "March 26",
            "March 27",
            "March 28",
            "March 29",
            "March 30",
            "March 31",
            "April 1",
            "April 2",
            "April 3",
            "April 4",
            "April 5",
            "April 6",
            "April 7",
            "April 8",
            "April 9",
            "April 10",
            "April 11",
            "April 12",
            "April 13",
            "April 14",
            "April 15",
            "April 16",
            "April 17",
            "April 18",
            "April 19",
            "April 20",
            "April 21",
            "April 22",
            "April 23",
            "April 24",
            "April 25",
            "April 26",
            "April 27",
            "April 28",
            "April 29",
            "April 30",
            "May 1",
            "May 2",
            "May 3",
            "May 4",
            "May 5",
            "May 6",
            "May 7",
            "May 8",
            "May 9",
            "May 10",
            "May 11",
            "May 12",
            "May 13",
            "May 14",
            "May 15",
            "May 16",
            "May 17",
            "May 18",
            "May 19",
            "May 20",
            "May 21",
            "May 22",
            "May 23",
            "May 24",
            "May 25",
            "May 26",
            "May 27",
            "May 28",
            "May 29",
            "May 30",
            "May 31",
            "June 1",
            "June 2",
            "June 3",
            "June 4",
            "June 5",
            "June 6",
            "June 7",
            "June 8",
            "June 9",
            "June 10",
            "June 11",
            "June 12",
            "June 13",
            "June 14",
            "June 15",
            "June 16",
            "June 17",
            "June 18",
            "June 19",
            "June 20",
            "June 21",
            "June 22",
            "June 23",
            "June 24",
            "June 25",
            "June 26",
            "June 27",
            "June 28",
            "June 29",
            "June 30",
            "July 1",
            "July 2",
            "July 3",
            "July 4",
            "July 5",
            "July 6",
            "July 7",
            "July 8",
            "July 9",
            "July 10",
            "July 11",
            "July 12",
            "July 13",
            "July 14",
            "July 15",
            "July 16",
            "July 17",
            "July 18",
            "July 19",
            "July 20",
            "July 21",
            "July 22",
            "July 23",
            "July 24",
            "July 25",
            "July 26",
            "July 27",
            "July 28",
            "July 29",
            "July 30",
            "July 31",
            "August 1",
            "August 2",
            "August 3",
            "August 4",
            "August 5",
            "August 6",
            "August 7",
            "August 8",
            "August 9",
            "August 10",
            "August 11",
            "August 12",
            "August 13",
            "August 14",
            "August 15",
            "August 16",
            "August 17",
            "August 18",
            "August 19",
            "August 20",
            "August 21",
            "August 22",
            "August 23",
            "August 24",
            "August 25",
            "August 26",
            "August 27",
            "August 28",
            "August 29",
            "August 30",
            "August 31",
            "September 1",
            "September 2",
            "September 3",
            "September 4",
            "September 5",
            "September 6",
            "September 7",
            "September 8",
            "September 9",
            "September 10",
            "September 11",
            "September 12",
            "September 13",
            "September 14",
            "September 15",
            "September 16",
            "September 17",
            "September 18",
            "September 19",
            "September 20",
            "September 21",
            "September 22",
            "September 23",
            "September 24",
            "September 25",
            "September 26",
            "September 27",
            "September 28",
            "September 29",
            "September 30",
            "October 1",
            "October 2",
            "October 3",
            "October 4",
            "October 5",
            "October 6",
            "October 7",
            "October 8",
            "October 9",
            "October 10",
            "October 11",
            "October 12",
            "October 13",
            "October 14",
            "October 15",
            "October 16",
            "October 17",
            "October 18",
            "October 19",
            "October 20",
            "October 21",
            "October 22",
            "October 23",
            "October 24",
            "October 25",
            "October 26",
            "October 27",
            "October 28",
            "October 29",
            "October 30",
            "October 31",
            "November 1",
            "November 2",
            "November 3",
            "November 4",
            "November 5",
            "November 6",
            "November 7",
            "November 8",
            "November 9",
            "November 10",
            "November 11",
            "November 12",
            "November 13",
            "November 14",
            "November 15",
            "November 16",
            "November 17",
            "November 18",
            "November 19",
            "November 20",
            "November 21",
            "November 22",
            "November 23",
            "November 24",
            "November 25",
            "November 26",
            "November 27",
            "November 28",
            "November 29",
            "November 30",
            "December 1",
            "December 2",
            "December 3",
            "December 4",
            "December 5",
            "December 6",
            "December 7",
            "December 8",
            "December 9",
            "December 10",
            "December 11",
            "December 12",
            "December 13",
            "December 14",
            "December 15",
            "December 16",
            "December 17",
            "December 18",
            "December 19",
            "December 20",
            "December 21",
            "December 22",
            "December 23",
            "December 24",
            "December 25",
            "December 26",
            "December 27",
            "December 28",
            "December 29",
            "December 30",
            "December 31",
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
        expenses = 800

        global offences
        global is_job
        offences = 0
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

    def fame_menu():
        global fame, currency, book_base, money
        print(f"[1] Book [{currency}25,000]")
        print(f"[2] Commercial [{currency}{(fame*100)*2500}]")
        print(f"[3] Magazine Cover [{currency}{(fame*100)*5500}]")
        print(f"[4] Talk Show [{currency}0]")
        div()
        try:
            ch = int(input(">"))
        except:
            adult()
        div()
        if ch == 1:
            if book_base == 0:
                if fame >= 0.75:
                    print("You published a book.")
                    print("It became a bestseller.")
                    revenue = int(
                        25000 * (rng(4, 6)) + ((rng(4, 6) / 10)) + ((rng(4, 6) / 100))
                    )
                    base = str("{:,}".format((revenue)))
                    print(f"Your book made {currency}{base}.")
                    money += revenue
                    fame += 0.0001 * revenue
                    book_base += 3
                elif fame >= 0.5:
                    print("You published a book.")
                    print("You just about broke even.")
                    revenue = int(25000 * ((rng(12, 14) / 10)))
                    base = str("{:,}".format((revenue)))
                    print(f"Your book made {currency}{base}.")
                    money += revenue
                    fame += 0.00005 * revenue
                    book_base += 3
                else:
                    print("You published a book.")
                    print("it absolutely bombed.")
                    base = str("{:,}".format((revenue)))
                    revenue = int(rng(4000, 10000))
                    fame -= 0.001 * revenue
                    book_base += 3
                    print(f"Your book made {currency}{base}.")
                adult()
            else:
                print("You were unable to find a publisher for your book.")
        elif ch == 2:
            pay = (fame * 100) * 2500
            print("You did a commerical for [COMPANY NAME HERE]")
            print("Response:", pbar2(0.85))
            print(f"You made {currency}{pay}")
            money += pay
            adult()
        elif ch == 3:
            pay = (fame * 100) * 5500
            print("You posed for Wank Magazine.")
            print("Response:", pbar2(0.55))
            print(f"You made {currency}{pay}")
            money += pay
            adult()
        elif ch == 4:
            if fame >= 0.9:
                chance = rng(1, 3)
                if chance == 1:
                    print(
                        f"You went on the Tonight Show by {choice(forename_m)} {choice(surnames)}."
                    )
                    print("Response:", pbar2(0))
                    if fame > 0.25:
                        fame -= 0.25
                    else:
                        fame -= fame / 4
                    adult()
                else:
                    print(
                        f"You went on the Tonight Show by {choice(forename_m)} {choice(surnames)}."
                    )
                    print("Response:", pbar2(1))
                    if fame < 0.25:
                        fame += 0.25
                    else:
                        fame += fame / 4
                    adult()
        else:
            adult()

    def friend_1_interact():
        global friend_count, friend_1, happiness
        if friend_1.rel > 1:
            friend_1.rel = 1
        if friend_1.rel < 0:
            friend_1.rel = 0
        div()
        print(friend_1.name)
        print("Age:", friend_1.age)
        div()
        print("Relationship:", pbar2(friend_1.rel), f"{int(friend_1.rel*100)}%")
        div()
        print("Smarts      :", pbar2(friend_1.intel), f"{int(friend_1.intel*100)}%")
        print("Looks       :", pbar2(friend_1.looks), f"{int(friend_1.looks*100)}%")
        print(
            "Craziness   :",
            pbar2(friend_1.craziness),
            f"{int(friend_1.craziness*100)}%",
        )
        div()
        print("[1] Spend Time With")
        print("[2] Compliment")
        print("[3] Conversation")
        print("[x] Date")
        print("[5] Unfriend")
        print("[6] Insult")
        print("[x] Make Love")
        print("[x] Movies")
        div()
        try:
            ch = int(input(">"))
        except:
            adult()
        if ch == 1:
            print(f"You took {friend_1.name} {choice(spend_time)}.")
            friend_1.rel += 0.25
        elif ch == 2:
            div()
            print(f"You called {friend_1.name} {choice(compliments)}!")
            happiness += 0.25
            friend_1.rel += 0.25
            if friend_1.rel > 0.75:
                print(f"{friend_1.name} called you {choice(compliments)}!")
                happiness += 0.45
        elif ch == 3:
            pass
        elif ch == 5:
            # If there are 3 friends:
            # Friend 3 --> Friend 2
            # Friend 2 --> Friend 1

            # If there are 2 friends:
            # Friend 2 --> Friend 1

            # If there is 1 friend:
            # Delete friend 1
            if friend_count == 1:
                del friend_1
            elif friend_count == 2:
                friend_1 = friend_2
            elif friend_count == 3:
                friend_1 = friend_2
                friend_2 = friend_3
            else:
                print("An error occured.")
                adult()
            friend_count -= 1
            print("You unfriended your friend.")
            adult()
        elif ch == 6:
            print(f"You called {friend_1.name}  {choice(insults)}!")
            friend_1.rel -= 0.25
            happiness -= 0.25
            if friend_1.rel <= 0.25:
                print(f"{friend_1.name} called you {choice(insults)}!")
                happiness -= 0.25
                friend_1.rel -= 0.10
            adult()
        else:
            adult()

    def friend_2_interact():
        global friend_count, friend_2, happiness, spouse, is_spouse
        if friend_2.rel > 1:
            friend_2.rel = 1
        if friend_2.rel < 0:
            friend_2.rel = 0
        div()
        print(friend_2.name)
        print("Age:", friend_2.age)
        div()
        print("Relationship:", pbar2(friend_2.rel), f"{int(friend_2.rel*100)}%")
        div()
        print("Smarts      :", pbar2(friend_2.intel), f"{int(friend_2.intel*100)}%")
        print("Looks       :", pbar2(friend_2.looks), f"{int(friend_2.looks*100)}%")
        print(
            "Craziness   :",
            pbar2(friend_2.craziness),
            f"{int(friend_2.craziness*100)}%",
        )
        div()
        print("[1] Spend Time With")
        print("[2] Compliment")
        print("[3] Conversation")
        print("[x] Date")
        print("[5] Unfriend")
        print("[6] Insult")
        print("[x] Make Love")
        print("[x] Movies")
        div()
        try:
            ch = int(input(">"))
        except:
            adult()
        if ch == 1:
            print(f"You took {friend_2.name} {choice(spend_time)}.")
            friend_2.rel += 0.25
        elif ch == 2:
            div()
            print(f"You called {friend_2.name} {choice(compliments)}!")
            happiness += 0.25
            friend_2.rel += 0.25
            if friend_2.rel > 0.75:
                print(f"{friend_2.name} called you {choice(compliments)}!")
                happiness += 0.45
        elif ch == 3:
            pass
        elif ch == 5:

            # If there are 3 Friends
            # Friend 3 --> Friend 2

            # If there are 2 Friends
            # Delete Friend_2
            if friend_count == 2:
                del friend_2
            elif friend_count == 3:
                friend_2 = friend_3
            else:
                print("An error occured.")
                adult()
            friend_count -= 1
            print("You unfriended your friend.")
            adult()
        elif ch == 6:
            print(f"You called {friend_2.name}  {choice(insults)}!")
            friend_2.rel -= 0.25
            happiness -= 0.25
            if friend_2.rel <= 0.25:
                print(f"{friend_2.name} called you {choice(insults)}!")
                happiness -= 0.25
                friend_2.rel -= 0.10
            adult()
        else:
            adult()

    def friend_3_interact():
        global friend_count, friend_3, happiness, spouse, is_spouse
        if friend_3.rel > 1:
            friend_3.rel = 1
        if friend_3.rel < 0:
            friend_3.rel = 0
        div()
        print(friend_3.name)
        print("Age:", friend_3.age)
        div()
        print("Relationship:", pbar2(friend_3.rel), f"{int(friend_3.rel*100)}%")
        div()
        print("Smarts      :", pbar2(friend_3.intel), f"{int(friend_3.intel*100)}%")
        print("Looks       :", pbar2(friend_3.looks), f"{int(friend_3.looks*100)}%")
        print(
            "Craziness   :",
            pbar2(friend_3.craziness),
            f"{int(friend_3.craziness*100)}%",
        )
        div()
        print("[1] Spend Time With")
        print("[2] Compliment")
        print("[3] Conversation")
        print("[x] Date")
        print("[5] Unfriend")
        print("[6] Insult")
        print("[x] Make Love")
        print("[x] Movies")
        div()
        try:
            ch = int(input(">"))
        except:
            adult()
        if ch == 1:
            print(f"You took {friend_3.name} {choice(spend_time)}.")
            friend_3.rel += 0.25
        elif ch == 2:
            div()
            print(f"You called {friend_3.name} {choice(compliments)}!")
            happiness += 0.25
            friend_3.rel += 0.25
            if friend_3.rel > 0.75:
                print(f"{friend_3.name} called you {choice(compliments)}!")
                happiness += 0.45
        elif ch == 3:
            pass
        elif ch == 5:
            friend_3 = ""
            friend_count -= 1
            print("You unfriended your friend.")
            adult()
        elif ch == 6:
            print(f"You called {friend_3.name}  {choice(insults)}!")
            friend_3.rel -= 0.25
            happiness -= 0.25
            if friend_3.rel <= 0.25:
                print(f"{friend_3.name} called you {choice(insults)}!")
                happiness -= 0.25
                friend_3.rel -= 0.10
            adult()
        else:
            adult()

    def prison_pause():
        div()
        print("[0] Resume")
        print("[x] Save Game")
        print("[x] Load Game")
        print("[5] Exit Game")
        div()
        try:
            ch = int(input(">"))
        except:
            prison()
        if ch == 5:
            print("[0] Return")
            print("[x] Exit And Save")
            print("[2] Exit Without Saving")
            div()
            try:
                ch = int(input(">"))
            except:
                prison()
            if ch == 2:
                mainmenu()
            else:
                prison()
        else:
            prison()

    def prison_menu():
        global health, behaviour, prison_years, sentence, forename, surname, offences, behaviour, is_appeal
        if is_appeal == 0:
            print("[1] Appeal Sentence")
        else:
            print("[x] Appeal Sentence")
        print("[2] Meditate In Cell")
        print("[3] Escape [25% chance]")
        print("[4] Riot [50% chance]")
        print("[5] Surrender")
        print(
            f"[6] Bail Out [{currency}"
            + str("{:,}".format((45000 * prison_years)))
            + "]"
        )
        print("[0] Return")
        div()
        if prison_years < 0:
            print("Years left: Life")
        else:
            print(f"Years left: " + str("{:,}".format((prison_years))))
        print(f"Sentence: " + str("{:,}".format((sentence))), "years")
        print("Behaviour:", pbar2(behaviour))
        div()
        try:
            ch = int(input(">"))
        except:
            prison()
        if ch == 1:
            if is_appeal == 0 and behaviour >= 0.75 and sentence > 2 * prison_years:
                print("Your appeal was approved!")
                prison_years = 1
                prison_age()
            else:
                print("Your appeal was denied.")
                is_appeal = 1  # Only one chance !
                prison()
        elif ch == 2:
            print("You meditated in your cell.")
            behaviour += 0.25
            prison()
        elif ch == 3:
            chance = rng(1, 4)
            if chance == 3:
                print("You escaped.")
                offences += 1
                adult()
            else:
                add_base = rng(2, 5)
                print(
                    f"Your sentence has been extended by {add_base} years for attempted escape."
                )
                prison_years += add_base
                sentence += add_base
                prison()
        elif ch == 4:
            chance = rng(1, 2)
            if chance == 2:
                print("A riot was started.")
                health -= 0.25
                prison()
            else:
                prison()
        elif ch == 5:
            print(f"[1] Surrender {forename} {surname}")
            print("[0] Return")
            div()
            try:
                ch = int(input(">"))
            except:
                prison()
            if ch == 1:
                die(0)
            else:
                prison()
        else:
            prison()

    def prison_age():
        global sentence, age, prison_years, offences, debt, savings
        debt += int((debt / 5))
        savings += int((savings / 10))
        age += 1
        prison_years -= 1

        # You cannot die in prison yet!

        if prison_years == 0:
            sentence = 0
            offences = 0
            print("You have been released from prison.")
            adult()
        else:
            prison()

    def prison():
        div()
        global happiness, health, intel, looks, forename, surname, behaviour
        if behaviour > 1:
            behaviour = 1
        if behaviour < 0:
            behaviour = 0
        if happiness > 1:
            happiness = 1
        if happiness < 0:
            happiness = 0
        if health > 1:
            health = 1
        if health < 0:
            emergency_room(4)
        if intel > 1:
            intel = 1
        if looks > 1:
            looks = 1
        if intel < 0:
            intel = 0
        if looks < 0:
            looks = 0
        print(forename + " " + surname)
        print("Prisoner")
        if is_depressed == 1:
            div()
            print("Suffers from: Depression")
        print("Age", age)
        print(f"{currency}" + str("{:,}".format((money))))
        div()
        print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "%")
        print("Health:   ", pbar2(health), str(int(health * 100)) + "%")
        print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "%")
        print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "%")
        div()
        print("[1] Prison")
        print("[0] Age Up")
        print("[5] Pause Menu")
        div()
        try:
            ch = int(input(">"))
        except:
            prison()
        if ch == 1:
            prison_menu()
        elif ch == 0:
            prison_age()
        else:
            prison()

    def adult_init_juvie():
        div()
        global clout, socialc
        clout, socialc = 4, 20  # Easter egg :)
        global mother_rel, father_rel
        global stress
        stress = 0.65
        from random import randint

        if mother_rel > 0.8:
            mother_rel = 0.8
        if father_rel > 0.8:
            father_rel = 0.8
        return True

    def transfer_to_prison():
        global sentence, juvie_years, prison_years, behaviour
        behaviour = 0.25
        sentence = juvie_years
        juvie_years = 0
        prison_years = sentence
        adult_init_juvie()
        prison()

    def juvie_age():
        global age, juvie_years, offences
        age += 1
        juvie_years -= 1
        if juvie_years == 0:
            div()
            offences = 0
            print("You have been released from juvie.")
            br()
            teen()
        if age == 18:
            div()
            print("You have been transferred to prison.")
            br()
            transfer_to_prison()
        juvie()

    def juvie_menu():
        global health, behaviour, juvie_years, sentence, forename, surname
        div()
        print("[1] Appeal Sentence")
        print("[2] Meditate In Cell")
        print("[3] Escape [25% chance]")
        print("[4] Riot [50% chance]")
        print("[5] Surrender")
        print("[0] Return")
        div()
        print(f"Years left: " + str("{:,}".format((juvie_years))))
        print(f"Sentence: " + str("{:,}".format((sentence))), "years")
        div()
        try:
            ch = int(input(">"))
        except:
            juvie()
        if ch == 1:
            print("Your appeal was denied.")
            juvie()
        elif ch == 2:
            print("You meditated in your cell.")
            juvie()
        elif ch == 3:
            chance = rng(1, 4)
            if chance == 3:
                print("You escaped.")
                teen()
            else:
                add_base = rng(2, 5)
                print(
                    f"Your sentence has been extended by {add_base} years for attempted escape."
                )
                juvie_years += add_base
                sentence += add_base
                juvie()
        elif ch == 4:
            chance = rng(1, 2)
            if chance == 2:
                print("A riot was started.")
                health -= 0.25
                juvie()
            else:
                juvie()
        elif ch == 5:
            print(f"[1] Surrender {forename} {surname}")
            print("[0] Return")
            div()
            try:
                ch = int(input(">"))
            except:
                juvie()
            if ch == 1:
                die(0)
            else:
                juvie()
        else:
            juvie()

    def juvie():
        global mother_name, father_name
        global offences
        global happiness, health, intel, looks, ethics, grades, clout, socialc
        global mother_rel, father_rel, juvie_years
        global money, is_depressed, is_hbp
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
            emergency_room(3)
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
        print("Juvie Prisoner")
        if is_depressed == 1:
            div()
            print("Suffers from: Depression")
            if is_hbp == 0:
                div()
        print("Age", age)
        print(f"{currency}" + str("{:,}".format((money))))
        div()
        print("Happiness:", pbar2(happiness), str(int(happiness * 100)) + "%")
        print("Health:   ", pbar2(health), str(int(health * 100)) + "%")
        print("Smarts:   ", pbar2(intel), str(int(intel * 100)) + "%")
        print("Looks:    ", pbar2(looks), str(int(looks * 100)) + "%")
        div()
        print("[1] Juvie")
        print("[0] Age Up")
        print("[5] Paue Menu")
        try:
            ch = int(input(">"))
        except:
            juvie()
        if ch == 1:
            juvie_menu()
        elif ch == 0:
            juvie_age()
        else:
            juvie()

    def go_to_prison():
        global prison_years, offences, juvie_years, sentence, behaviour
        beghaviour = 0.25
        if sentence == 0:
            sentence = offences * 2
        elif prison_years > 0:
            offences += 1
            sentence = prison_years * 3 * offences
        else:
            sentence = 69420
        div()
        if prison_years == 1:
            print("You have been sent to prison for a year.")
        else:
            print(f"You have been sent to prison for {sentence} years.")
        if sentence == 0:
            sentence = prison_years
        prison_years = sentence
        prison()

    def go_to_juvie():
        global juvie_years, offences, juvie_years, sentence
        if juvie_years > 0:
            offences += 1
            juvie_years *= offences
        else:
            juvie_years = offences
        div()
        if juvie_years == 1:
            print("You have been sent to juvenile detention for a year.")
        else:
            print(f"You have been sent to juvenile detention for {juvie_years} years.")
        sentence = juvie_years
        juvie()

    def teen_calc_stress():
        global edu_lvl, pension, job_lvl, is_spouse, spouse
        global salary, hours
        global allow_debug
        global mother_age, father_age
        global mother_name, father_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel, part_time_salary
        global money, is_depressed, work_e, is_job
        global job_id, job_lvl, club_count
        global money, stress, teen_hours

        stress = 0.55
        stress += teen_hours * 0.05
        stress += club_count * 0.1
        if happiness >= 0.5:
            stress -= happiness / 2
        if happiness < 0.5:
            stress += happiness
        if stress > 1:
            stress = 1
        if stress < 0:
            stress = 0
        return True

    def calc_stress():
        global edu_lvl, pension, job_lvl, is_spouse, spouse
        global salary, hours
        global allow_debug
        global mother_age, father_age
        global mother_name, father_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel, part_time_salary
        global money, is_depressed, work_e, is_job
        global job_id, job_lvl
        global money, stress
        stress = hours * 0.015
        if part_time_salary > 0:
            stress += 0.2
        if is_depressed == 1:
            stress *= 2
        if happiness <= 0.5:
            stress += happiness
        if happiness >= 0.5 and hours < 40:
            stress -= happiness / 2
        if stress > 1:
            stress = 1
        if stress < 0:
            stress = 0
        return True

    def die(reason):
        global age, forename, surname, is_depressed, is_spouse, spouse
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
            view_ribbons(-1)
            div()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if age < 130:
                if juvie_years > 0:
                    print("[2] Respawn [Go To Juvie]")
                else:
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
                    if juvie_years > 0:
                        juvie()
                    else:
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
                    f"They were {age} years old, making them the oldest person in the world at the time."
                )
            print("\nThey lived a long, happy life, surrounded by great people.")
            print("They will be missed by friends and family.")
            div()
            view_ribbons(reason)
            div()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if age < 130:
                if juvie_years > 0:
                    print("[2] Respawn [Go To Juvie]")
                else:
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
                    if juvie_years > 0:
                        juvie()
                    else:
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
                f"Their death was extremely untimely and is a tragic loss that will be felt by the"
            )
            print(f"entire {game_name} community.")
            if is_spouse == 1:
                print(f"\n{spouse.name}, {forename}'s spouse, had this to say:")
                print(
                    f"'I am deeply saddened by this. I remember seeing [{forename}] regularly have mental breakdowns as a result of stress."
                )
                print(f"Stress is no joke. It killed my partner.'")

            print(
                f"\nHopefully such heart attacks are seen less and less in the community and that"
            )
            print(
                f"the players of {game_name} do not overwork themselves like {forename} {surname} did."
            )
            div()
            view_ribbons(reason)
            div()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if age < 130:
                if juvie_years > 0:
                    print("[2] Respawn [Go To Juvie]")
                else:
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
                    if juvie_years > 0:
                        juvie()
                    else:
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
            view_ribbons(reason)
            div()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if juvie_years > 0:
                print("[2] Respawn [Go To Juvie]")
            else:
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
                    if juvie_years > 0:
                        juvie()
                    else:
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
            view_ribbons(reason)
            div()
            print("[0] Exit Game")
            print("[1] Main Menu")
            if juvie_years > 0:
                print("[2] Respawn [Go To Juvie]")
            else:
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
                    if juvie_years > 0:
                        juvie()
                    else:
                        teen()
                else:
                    adult()
            else:
                mainmenu()
        else:
            raise FeatureNotInGameError

    def spouse_interact():
        global spouse, happiness, is_spouse, money, debt, currency, compliments, insults, spend_time, gender, intel
        div()
        print(f"{spouse.name}")
        if spouse.lvl == 1:
            if spouse.gender == 1:
                print("Girlfriend")
            else:
                print("Boyfriend")
        elif spouse.lvl == 2:
            if spouse.gender == 1:
                print("Wife")
            else:
                print("Husband")
        print(f"Age: {spouse.age}")
        div()
        print(
            "Smarts      :", pbar2(spouse.intel), str((int(spouse.intel * 100))) + "%"
        )
        print(
            "Looks       :", pbar2(spouse.looks), str((int(spouse.looks * 100))) + "%"
        )
        print(
            "Craziness   :",
            pbar2(spouse.craziness),
            str(int(spouse.craziness * 100)) + "%",
        )
        div()
        print("Relationship:", pbar2(spouse.rel), f"{int(spouse.rel*100)}%")
        div()
        print("[0] Return")
        print("[1] Spend Time")
        print("[2] Compliment")
        print("[3] Conversation")
        if spouse.lvl == 1:
            print("[4] Break Up")
        else:
            print("[4] Divorce")
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
            print(f"You took {spouse.name} {choice(spend_time)}.")
            spouse.rel += 0.25
            adult()
        elif ch == 2:
            div()
            print(f"You called your spouse {choice(compliments)}!")
            happiness += 0.25
            spouse.rel += 0.25
            if spouse.rel > 0.75:
                print(f"Your spouse called you {choice(compliments)}!")
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
                money += spouse.fortune
                adult()
            else:
                print("Your spouse refused to marry you.")
                if spouse.rel <= 0.25:
                    print(
                        f"On the way out of the room, they called you {choice(insults)}."
                    )
                adult()

        elif ch == 3:
            argument_chance = rng(1, 4)
            if argument_chance == 1:
                div()
                print(f"You had a conversation about {choice(debates)}.")
                print("Agreement: ", pbar2(0))
                spouse.rel -= 0.45
                happiness -= 0.55
                div()
                print("Your conversation soon turns into a shouting match.")
                div()
                print("[1] Agree to disagree")
                print("[2] Ghost your spouse.")
                print("[3] Make a compromise with the agreement.")
                div()
                try:
                    ch = int(input(">"))
                except:
                    ch = 1
                if ch == 1:
                    spouse.rel += 0.2
                    happiness += 0.2
                elif ch == 2:
                    spouse.rel -= 0.45
                    happiness -= 0.55
                elif ch == 3:
                    spouse.rel += 0.4
                    happiness += 0.5
                adult()
            else:
                div()
                print(f"You had a conversation about {choice(debates)}.")
                print("Agreement: ", pbar2(0.75))
                spouse.rel += 0.25
                happiness += 0.45
                intel += 0.25
                adult()
        elif ch == 4:
            if spouse.lvl == 1:
                div()
                print("You broke up with your spouse.")
                is_spouse = 0
                del spouse
                adult()
            elif spouse.lvl == 2:
                div()
                print("You divorced your spouse.")
                money -= int(spouse.fortune / 2)
                is_spouse = 0
                del spouse
                adult()
            else:
                spouse_interact()
        elif ch == 5:
            div()
            print(f"You called your spouse {choice(insults)}!")
            spouse.rel -= 0.55
            if spouse.rel < 0.25:
                print(f"Your spouse called you {choice(insults)}!")
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

    def dating_app(opposite):
        global gender, age, spouse, is_spouse, surnames, money, debt
        if opposite == 1:
            if gender == 0:
                gg = 1
            else:
                gg = 0
        else:
            gg = gender
        if money > 100:
            money -= 100
        else:
            debt += 100
        div()
        print("[1] 18-21")
        print("[2] 22-24")
        print("[3] 25-29")
        print("[4] 30-34")
        print("[5] 35-39")
        print("[6] 40-44")
        print("[7] 45-49")
        print("[8] 50-54")
        print("[9] 55-59")
        print("[10] 60-64")
        print("[11] 65-69")
        print("[12] 70+")
        div()
        try:
            ch = int(input(">"))
        except:
            rang = [(age - 3), (age + 3)]
        if ch == 1:
            rang = [18, 21]
        elif ch == 2:
            rang = [22, 24]
        elif ch == 3:
            rang = [25, 29]
        elif ch == 4:
            rang = [30, 34]
        elif ch == 5:
            rang = [35, 39]
        elif ch == 6:
            rang = [40, 44]
        elif ch == 7:
            rang = [45, 49]
        elif ch == 8:
            rang = [45, 49]
        elif ch == 9:
            rang = [50, 54]
        elif ch == 10:
            rang = [55, 59]
        elif ch == 11:
            rang = [65, 69]
        elif ch == 12:
            rang = [70, 99]
        else:
            rang = [(age - 3), (age + 3)]
        div()
        spouse = SpouseDatingApp(pickname(gg), 0.75, 1, age, gg, rng(rang[0], rang[1]))
        print(f"Name: {spouse.name}")
        print(f"Age: {spouse.age}")
        div()
        print("Smarts   :", pbar2(spouse.intel))
        print("Looks    :", pbar2(spouse.looks))
        print("Craziness:", pbar2(spouse.craziness))
        div()
        print("[1] Ask on date")
        print(f"[2] Find another [{currency}100]")
        print("[0] Ignore")
        div()
        try:
            ch = int(input(">"))
        except:
            return False
        if ch == 1:
            return spouse
        elif ch == 2:
            dating_app(opposite)
        else:
            return False

    def find_love(opposite):
        global age, spouse, surnames, gender
        div()
        # name, age, relation, relationship_level, your_age
        if opposite == 1:
            if gender == 0:
                gg = 1
            else:
                gg = 0
        else:
            gg = gender
        if gg == 1:
            print("While at the gym, a woman asks you out.")
        else:
            print("While at the gym, a man asks you out.")
        spouse = Spouse(pickname(gg), (rng(50, 75) / 100), 1, age, gg)
        print(f"Name: {spouse.name}")
        print(f"Age: {spouse.age}")
        div()
        print("Smarts   :", pbar2(spouse.intel))
        print("Looks    :", pbar2(spouse.looks))
        print("Craziness:", pbar2(spouse.craziness))
        div()
        print("[1] Ask on date")
        print("[2] Find another")
        print("[0] Ignore")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 1:
            return spouse
        elif ch == 2:
            find_love(1)
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
            print("[3] It was shit. I'm glad to go, dickhead")
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
        global allow_debug, spouse, is_spouse, gender, friend_count, friend_1, friend_2, friend_3, is_wpp, wpp_name, fame, sentence, prison_years, juvie_years
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

        tsn = input("Enter File Name >")
        sn = "" + tsn
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
        if is_wpp == 0:
            wpp_name = "N/A"
        if is_spouse == 0:
            spouse = Spouse("N/A", 1, 1, age, 1)
        if friend_count == 0:
            friend_1 = Friend("N/A", 18, 0)
            friend_2 = Friend("N/A", 18, 0)
            friend_3 = Friend("N/A", 18, 0)
        elif friend_count == 1:
            friend_2 = Friend("N/A", 18, 0)
            friend_3 = Friend("N/A", 18, 0)
        elif friend_count == 2:
            friend_3 = Friend("N/A", 18, 0)
        save = (
            "Alpha|14|"
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
            + str(teen_salary)  # 46
            + "|"
            + str(spouse.intel)  # 47
            + "|"
            + str(spouse.looks)  # 48
            + "|"
            + str(spouse.craziness)  # 49
            + "|"
            + str(job_id)  # 50
            + "|"
            + str(spouse.gender)  # 51
            + "|"
            + str(gender)  # 52
            + "|"
            + str(spouse.fortune)  # 53
            + "|"
            + str(friend_count)  # 54
            + "|"
            + str(friend_1.name)  # 55
            + "|"
            + str(friend_1.age)  # 56
            + "|"
            + str(friend_1.gender)  # 57
            + "|"
            + str(friend_1.intel)  # 58
            + "|"
            + str(friend_1.looks)  # 59
            + "|"
            + str(friend_1.craziness)  # 60
            + "|"
            + str(friend_1.end)  # 61
            + "|"
            + str(friend_1.rel)  # 62
            + "|"
            + str(friend_2.name)  # 63
            + "|"
            + str(friend_2.age)  # 64
            + "|"
            + str(friend_2.gender)  # 65
            + "|"
            + str(friend_2.intel)  # 66
            + "|"
            + str(friend_2.looks)  # 67
            + "|"
            + str(friend_2.craziness)  # 68
            + "|"
            + str(friend_2.end)  # 69
            + "|"
            + str(friend_2.rel)  # 70
            + "|"
            + str(friend_3.name)  # 71
            + "|"
            + str(friend_3.age)  # 72
            + "|"
            + str(friend_3.gender)  # 73
            + "|"
            + str(friend_3.intel)  # 74
            + "|"
            + str(friend_3.looks)  # 75
            + "|"
            + str(friend_3.craziness)  # 76
            + "|"
            + str(friend_3.end)  # 77
            + "|"
            + str(friend_3.rel)  # 78
            + "|"
            + str(fame)  # 79
            + "|"
            + str(is_wpp)  # 80
            + "|"
            + str(wpp_name[0])  # 81
            + "|"
            + wpp_name[1]  # 82
            + "|"
            + str(sentence)  # 83
            + "|"
            + str(prison_years)  # 84
            + "|"
            + str(juvie_years)  # 85
            + "|0"
        )
        if allow_debug == 2:
            print(save)
            div()
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
        global allow_debug, did_tutor, degree, is_spouse, spouse, part_time_salary, friend_1, friend_2, friend_3, friend_count, fame, is_wpp, wpp_name, sentence, prison_years, juvie_years
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary, mother_rel, father_rel
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age, salary, hours, job_id, gender
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
            div()
            print("An error occured.")
            mainmenu()
        import codecs

        ssave = f.read()
        f.close()

        check_version = ["Alpha", "14"]

        ssave = codecs.decode(ssave, "base64_codec")
        ssave = ssave.decode("utf-8")
        ssave = ssave.split("|")
        save = ssave
        if allow_debug != 0:
            print(save)
        if save[0] == check_version[0] and save[1] == check_version[1]:
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
            try:
                savings = int(save[22])
            except:
                savings = float(save[22])
                savings = int(savings)
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
                save[36],
                float(save[40]),
                int(save[39]),
                int(save[37]),
                int(save[38]),
                float(save[47]),
                float(save[48]),
                float(save[49]),
                int(save[51]),
                int(save[53]),
            )
            enemy_gang_rel = float(save[41])
            enemy_gang_lead = float(save[42])
            enemy_gang_name = save[43]
            part_time_salary = int(save[44])
            teen_hours = int(save[45])
            teen_salary = int(save[46])
            job_id = int(save[50])
            gender = int(save[52])
            friend_count = int(save[54])
            friend_1 = FriendRecompile(
                save[55],
                int(save[56]),
                int(save[57]),
                float(save[58]),
                float(save[59]),
                float(save[60]),
                int(save[61]),
                float(save[62]),
            )
            friend_2 = FriendRecompile(
                save[63],
                int(save[64]),
                int(save[65]),
                float(save[66]),
                float(save[67]),
                float(save[68]),
                int(save[69]),
                float(save[70]),
            )
            friend_3 = FriendRecompile(
                save[71],
                int(save[72]),
                int(save[73]),
                float(save[74]),
                float(save[75]),
                float(save[76]),
                int(save[77]),
                float(save[78]),
            )
            fame = int(save[79])
            is_wpp = int(save[80])
            wpp_name = [save[81], save[82]]
            sentence = int(save[83])
            prison_years = int(save[84])
            juvie_years = int(save[85])

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
                "Also, you will not be able to play this save on that older version of",
                game_name,
            )
            div()
            print(f"Note: Your save file will be backed up to `{sn[:-5]}.bak`.")
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
        elif save[0] == "Alpha" and save[1] == "13":
            div()
            print("This save file is incompatible with", game_name + ".")
            print("In order to play, you need to convert it to a supported format.")
            print(
                "You can do this automatically, but this will [sadly] require adding default data."
            )
            print(
                "Also, you will not be able to play this save on that older version of",
                game_name,
            )
            div()
            print(f"Note: Your save file will be backed up to `{sn[:-5]}.bak`.")
            div()
            print("[0] Cancel to Main Menu")
            print("[1] Convert")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 1:
                load_game_a13(sn)
            else:
                mainmenu()
        else:
            if allow_debug == 1:
                print(save)
            print(f"This save is incompatible with {game_name}.")
            print(f"Expected Version: {check_version[0]} {check_version[1]}")
            try:
                print("Got version:", save[0], save[1])
            except:
                print("Got version: N/A")
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
            base += ""
        print(base)
        br()

    def load_game_a13(sn):
        global allow_debug, did_tutor
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary, mother_rel, father_rel
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age
        print("Convert Save [A13] --> [A14]")
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
        save[1] = "14"
        base = ""
        for item in save:
            base += item
            base += "|"
        l = len(base)
        base = base[: l - 1]
        print(base)
        base += "|1|1|0|0|1|0|0|0|SGCU Friend #1|18|0|1|1|0|19|1|SGCU Friend #2|18|0|1|1|0|19|1|SGCU Friend #3|18|0|1|1|0|19|1|0|0|SGCU|MAN|0|0|0"
        save = base
        save = save.encode("utf-8")
        save = codecs.encode(save, "base64_codec")
        f = open(sn, "wb")
        f.write(save)
        f.close()
        print("Converted save successfully.")
        div()
        load_game()

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
        load_game_a13(sn)

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
        global mother_age, age, spouse, is_spouse
        global father_age, offences, is_bandit
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
            if is_spouse == 1:
                if spouse.end > spouse.age:
                    print(f"[3] Kill {spouse.name} [{currency}56,000]")
            try:
                ch = int(input(">"))
            except:
                ch = 0
            if ch == 0:
                adult()
            elif ch == 1 and mother_age < mother_end_age:
                if money >= 45000:
                    chance = rng(1, 3)
                    if chance == 1 or chance == 2:
                        print("The hitman was actually an undercover cop!")
                        offences += 25
                        go_to_prison()
                        adult()
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
                    chance = rng(1, 3)
                    if chance == 1 or chance == 2:
                        print("The hitman was actually an undercover cop!")
                        offences += 25
                        go_to_prison()
                        adult()
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
            elif ch == 3:
                if is_spouse == 1:
                    if spouse.end > spouse.age:
                        if money >= 56000:
                            chance = rng(1, 3)
                            if chance == 1 or chance == 2:
                                print("The hitman was actually an undercover cop!")
                                offences += 25
                                go_to_prison()
                                adult()
                            money -= 56000
                            div()
                            print("Your spouse was successfully hit.")
                            spouse.end = spouse.age + 1
                            age -= 1
                            age_up()
                        else:
                            div()
                            print("Cannot afford.")
                            adult()
                    else:
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
                    is_bandit = 1
                    print(f"You stole {currency}" + str(winnings))
                    money += winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 2:
                if base == "07:00":
                    div()
                    is_bandit = 1
                    print(f"You stole {currency}" + str(winnings))
                    money += winnings
                    br()
                    adult()
                else:
                    print("You tried to board the train but was unable to.")
            if ch == 3:
                if base == "12:00":
                    div()
                    is_bandit = 1
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
                    is_bandit = 1
                    print("You tried to board the train but was unable to.")
            if ch == 5:
                if base == "19:00":
                    div()
                    print(f"You stole {currency}" + str(winnings))
                    money += winnings
                    br()
                    adult()
                else:
                    is_bandit = 1
                    print("You tried to board the train but was unable to.")
            if ch == 6:
                div()
                if base == "21:00":
                    is_bandit = 1
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
        if is_spouse == 1:
            if spouse.age <= spouse.end:
                div()
                print("Your spouse died.")
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
                    print("Your spouse was buried.")
                    money -= 8500
                elif ch == 2:
                    money -= 15000
                    print("You cremated your spouse.")
                    print("Choose what to do with the ashes:")
                    print("[1] Sprinkle somewhere special.")
                    print("[2] Put in urn")
                    print("[0] Throw In Trash")
                    ch = input(">")
                elif ch == 3:
                    print("You had your spouse taxidermied.")
                    money -= 15000
                elif ch == 4:
                    print("Your spouse's body was donated to science.")
                else:
                    print("You skipped the funeral.")
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
        calc_stress()
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
                print("Your university applicartion was declined.")
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
        global money, allow_test, currency, lottery_wins
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
                        lottery_wins += 1
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
            print("Lifetime Wins:", str("{:,}".format((int(lottery_wins)))))
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

    def choose_start(verbose):
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
            adult_init(verbose)
        else:
            raise ExitError

    def fame_increase():
        global job_id, job_lvl, fame, promo_base, money
        if job_id == 6 and job_lvl == 3:
            if promo_base >= 3 and work_e_base >= 10:
                fame += 0.25
        elif job_id == 9 and job_lvl == 3:
            if promo_base >= 3 and work_e_base >= 10:
                fame += 0.25
        elif job_id == 13 and job_lvl == 3:
            if promo_base >= 3 and work_e_base >= 10:
                fame += 0.25
        elif job_id == 28:
            if promo_base >= 3 and work_e_base >= 10:
                fame += 0.25
        elif job_id == 21:
            if promo_base >= 3 and work_e_base >= 15:
                fame += 0.25
        elif money >= 1000000:
            fame += int(money / 1000000) / 100
        else:
            fame -= rng(10, 20) / 100

        return True

    def age_up():
        global salary, hours, expenses, happiness, health, intel, looks, teen_salary, teen_hours
        global mother_end_age, father_end_age, money, is_spouse, spouse, book_base
        global is_depressed, is_anxiety, savings, debt, is_hbp, juvie_years
        global year, is_job, work_e_base, pension, promo_base, currency, prison_years
        year += 1
        if book_base > 0:
            book_base -= 1
        if is_spouse == 1:
            spouse.age += 1
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

        if is_hbp == 1:
            if stress <= 0.45:
                chance = rng(1, 2)
                if chance == 1:
                    is_hbp = 0
                    div()
                    print("You are no longer suffering from HIGH BLOOD PRESSURE.")
            chance = rng(1, 4)
            if chance == 3 and stress >= 0.75:
                die(2)
        if age >= 12 and is_hbp == 0:
            if stress >= 0.75:
                chance = rng(1, 2)
                if chance == 1:
                    is_hbp = 1
                    div()
                    print("You are now suffering from HIGH BLOOD PRESSURE")
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
        if age >= 18:
            fame_increase()
        if age >= 18 and is_job == 1:
            base = salary * hours * 52
            money += base
        if age >= 18:
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
        if is_spouse == 1:
            if spouse.age <= spouse.end:
                div()
                is_spouse = 0
                print("Your spouse died.")
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
                    print("Your spouse was buried.")
                    money -= 8500
                elif ch == 2:
                    money -= 15000
                    print("You cremated your spouse.")
                    print("Choose what to do with the ashes:")
                    print("[1] Sprinkle somewhere special.")
                    print("[2] Put in urn")
                    print("[0] Throw In Trash")
                    ch = input(">")
                elif ch == 3:
                    print("You had your spouse taxidermied.")
                    money -= 15000
                elif ch == 4:
                    print("Your spouse's body was donated to science.")
                else:
                    print("You skipped the funeral.")
        if auto_deposit == 1 and age >= 6:
            savings += money
            money = 0
        # redirect
        if age >= 12 and age < 18:
            if juvie_years > 0:
                chance = rng(1, 2)
                if chance == 2:
                    go_to_juvie()
        if age >= 18:
            if prison_years > 0:
                chance = rng(1, 2)
                if chance == 2:
                    go_to_prison()
        if age <= 5:
            happiness += 0.25
            if intel <= 0.75:
                intel += 0.15
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
            teen_calc_stress()
            if age == 12:
                teen_init()
            else:
                if happiness <= 0.1 and is_depressed == 0:
                    is_depressed = 1
                    div()
                    print("You are now suffering from DEPRESSION.")
                if is_depressed == 1:
                    if happiness < 0.65:
                        happiness /= 4
                    else:
                        div()
                        print("You are no longer suffering from DEPRESSION!")
                        is_depressed = 0
                teen()
        elif age >= 18:
            calc_stress()
            if juvie_years > 0:
                prison_years = juvie_years
                juvie_years = 0
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
                adult_init(1)
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
        try:
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
        except:
            raise ExitError

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

    def doctor_adult():
        is_depressed, is_hbp
        print("You went to visit the doctor.")
        div()
        print(
            "There was no consultation fee, courtesy of OpenLife's free healthcare system [The National Healthcare Organisation]."
        )
        br()
        div()
        if is_depressed == 0 and is_hbp == 0:
            print(
                "The doctor has determined that you are not suffering from any conditions."
            )
            br()
            adult()
        else:
            print(
                "After a brief physical and mental examination, the doctor determined that you are suffering from the following conditions:"
            )
            if is_depressed == 1:
                print("Depression")
            if is_hbp == 1:
                print("High Blood Pressure")
            div()
            if is_depressed == 1:
                print("[0] Return")
                print(f"[1] Treat Depression [{currency}0]")
            if is_hbp - -1:
                print(f"[2] Treat High Blood Pressure [{currency}0]")
            div()
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 1 and is_depressed == 1:
                print("You were treated for Depression.")
                print("You continue to suffer from Depression.")
                br()
                adult()
            elif ch == 2 and is_hbp == 1:
                print("You were treated for High Blood Pressure.")
                print("You continue to suffer from High Blood Pressure.")
                br()
                adult()
            else:
                adult()

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
        elif might_die == 3:
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
                juvie()
        elif might_die == 4:
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
                prison()
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
            print("Do you like BitLife?")
            div()
            print("[1] Never heard of it.")
            print("[2] It's pay-to-win garbage.")
            print("[3] Yes!")
            print(f"[4] {game_name} is better.")  # Not to blow my own trumpet.
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
        global forename, surname, money, gender, sexuality, is_trans, spouse, is_trans
        print("[0] Return")
        print(f"[1] Name Change [{currency}150]")
        print(f"[2] Declare Gender")
        print(f"[x] Declare Sexuality")
        try:
            ch = int(input(">"))
        except:
            adult()
        if ch == 1:
            if money >= 150:
                money -= 150
                forename = input("Forename >")
                forename = forename.replace("|", "")
                if len(forename) > 16:
                    while len(forename) > 16:
                        forename = forename[: (len(forename) - 1)]
                surname = input("Surname >")
                if len(surname) > 16:
                    while len(surname) > 16:
                        surname = surname[: (len(forename) - 1)]
                surname = surname.replace("|", "")
                adult()
            else:
                div()
                print("You cannot afford that.")
                adult()
        elif ch == 2:
            print("[1] Male")
            print("[2] Female")
            print("[3] Non-Binary")
            div()
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 1:
                if gender == 0 and is_trans == 0:
                    adult()
                elif gender == 0 and is_trans == 1:
                    is_trans = 0
                    gender = 1
                    adult()
                else:
                    gender = 0
                    is_trans = 1
                    print("You came out of the closet.")
                    if is_spouse == 1:
                        if spouse.gender == 1:
                            print("Your spouse left you.")
                            spouse = 0
                    if mother_end_age > mother_age:
                        print("Your mother said she would support you, no matter what.")
                    if father_end_age > father_age:
                        print("Your father said he would support you, no matter what.")
                    adult()
            if ch == 2:
                if gender == 1 and is_trans == 0:
                    adult()
                elif gender == 1 and is_trans == 1:
                    is_trans = 0
                    gender = 0
                    adult()
                else:
                    gender = 1
                    is_trans = 1
                    print("You came out of the closet.")
                    if is_spouse == 1:
                        if spouse.gender == 0:
                            print("Your spouse left you.")
                            spouse = 0
                    if mother_end_age > mother_age:
                        print("Your mother said she would support you, no matter what.")
                    if father_end_age > father_age:
                        print("Your father said he would support you, no matter what.")
                    adult()
            if ch == 3:
                if gender == 2:
                    adult()
                else:
                    gender = 0
                    is_trans = 1
                    print("You came out of the closet.")
                    if is_spouse == 1:
                        print("Your spouse left you.")
                        spouse = 0
                    if mother_end_age > mother_age:
                        print("Your mother said she would support you, no matter what.")
                    if father_end_age > father_age:
                        print("Your father said he would support you, no matter what.")
                    adult()
        else:
            adult()

    def love():
        global money, happiness, looks, health, intel, debt, spouse, is_spouse
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age, is_spouse, spouse
        print("[0] Return")
        print("[1] Find Love")
        print(f"[2] Dating App [{currency}100]")
        print(f"[3] Gay Dating App [{currency}100]")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 1 or ch == 2 or ch == 3:
            if ch == 1:
                find_love(1)
            elif ch == 2:
                dating_app(1)
            elif ch == 3:
                dating_app(0)
            if False:
                adult()
            else:
                div()
                is_spouse = 1
                happiness += 0.45
                print(f"You are now dating {spouse.name}.")
                if (
                    mother_end_age > mother_age
                    and father_end_age > father_age
                    and mother_rel >= 0.75
                    and father_rel >= 0.75
                ):
                    div()
                    print("Your mother congratulated you on finding a date.")
                    print("Your father did the same.")
                elif mother_age < mother_end_age:
                    if mother_rel >= 0.75 and mother_rel >= 0.75:
                        div()
                        print("Your mother congratulated you on finding a date.")
                elif father_end_age > father_age and father_rel >= 0.75:
                    div()
                    print("Your father congratulated you on finding a date.")
                adult()
        else:
            adult()

    def adult_activities():
        global money, happiness, looks, health, intel, debt, auto_deposit, allow_debug, job_id, prison_years, sentence, is_wpp, gender
        global happiness, health, intel, looks, ethics, money, forename, surname, age, work_e, edu_lvl, work_e_base, promo_base, degree, hours, salary
        global expenses, pension, is_depressed, debt, savings, year, is_job, stress, mother_name, father_name, mother_age, father_age, mother_end_age, father_end_age, fame
        print("[0] Return")
        print(f"[1] Gym [{currency}15]")
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
        if gender == 0:
            print("[19] Fertility")
        if fame > 0:
            print("[20] Fame")
            if is_wpp == 0:
                print("[21] Witness Protection Program")
        print("[22] Make Friends")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 0:
            adult()
        elif ch == 20 and fame > 0:
            fame_menu()
        elif ch == 22:
            gg = rng(0, 1)
            friend = Friend(pickname(gg), rng(18, age), gg)
            print(friend.name)
            print("Age:", friend.age)
            div()
            print("Smarts   :", pbar2(friend.intel))
            print("Looks    :", pbar2(friend.looks))
            print("Craziness:", pbar2(friend.craziness))
            div()
            print("[1] Make Friend")
            print("[0] Return")
            div()
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 1:
                global friend_count, friend_1, friend_2, friend_3
                friend_count += 1
                if friend_count == 1:
                    friend_1 = friend
                elif friend_count == 2:
                    friend_2 = friend
                elif friend_count == 3:
                    friend_3 = friend
                else:
                    print("You can only have 3 friends at a time.")
            else:
                adult()
        elif ch == 21 and is_wpp == 0 and fame >= 1:
            global forename_m, forename_f, surnames, is_spouse, money, savings, is_spouse, name, debt, wpp_name, is_depressed, wpp_year, his_her, he_she, him_her
            if fame == 1 and is_wpp == 0:
                print("[1] Enter WPP")
            print("[0] Return")
            div()
            try:
                ch = int(input(">"))
            except:
                adult()
            if ch == 1 and fame == 1 and is_wpp == 0:
                div()
                wpp_year = year - age
                if gender == 0 or gender == 1:
                    was_were = "was"
                else:
                    was_were = "were"

                if gender == 0:
                    him_her = "him"
                elif gender == 0:
                    him_her = "her"
                else:
                    him_her = "their"

                if gender == 0:
                    he_she = "he"
                elif gender == 1:
                    he_she = "she"
                else:
                    he_she = "they"

                if gender == 0:
                    his_her = "his"
                elif gender == 1:
                    his_her = "her"
                else:
                    his_her = "their"

                print(f"{game_name} Times")
                print("The *best* newspaper since 2022 AD")
                div()
                print(f"{forename} {surname} dies of heart attack aged {age}")
                div()
                print(
                    f"Last night, while lying in bed in {his_her} 12-bedroom hotel room in Vegas,"
                )
                print(
                    f"{forename} {surname} passed away as a result of a heart attack."
                )
                if gender == 0:
                    print(
                        f"He was found by hotel employees when they heard 'a very loud bang sound' and came to investigate."
                    )
                elif gender == 1:
                    print(
                        f"She was found by hotel employees when they heard 'a very loud bang sound' and came to investigate."
                    )
                else:
                    print(
                        f"They were found by hotel employees when they heard 'a very loud bang sound' and came to investigate."
                    )
                print(
                    f"When they found {him_her}, {he_she} {was_were} lying on the floor of the hotel room's master bedroom, and were immediately rushed to hospital."
                )
                print(
                    f"Attempts to revive {him_her} at the Las Vegas {game_name} Hospital were unsuccessful."
                )
                print(
                    f"\nReports have come out that {forename} {surname} was an avid fan of pharmaceuticals,"
                )
                print(
                    f"and a whopping 32 drugs were detected in {his_her} system when {he_she} died."
                )
                print(
                    f"It is obvious that {his_her} heart attack was caused by an overdose on pharmaceutical drugs,"
                )
                print(
                    f"as evident in the fact that over 90x the safe limit of codiene was detected in {his_her} bloodstream."
                )
                print(
                    f"Alongside codeine, various other substances were found in {his_her} blood, such as morphine and demerol, a popular opioid pain medication."
                )
                if is_depressed == 1:
                    print(
                        f"On top of all of the prescription medication in {his_her} blood, Fluoxetine (sold as Prozac), a popular antidepressant, was also found in alarming quantities."
                    )
                    print(
                        f"This suggests that {he_she} {was_were} either depressed or addicted to the substance."
                    )
                print(
                    f"\nMay this be a lesson on the danger of self-medication and not consulting a doctor for medical advice."
                )
                print(
                    f"Speaking of doctors, {forename}'s doctor, Dr. {choice(forename_m)} {choice(surnames)}, is being charged with overprescribing {forename} with dosages of medicines that 'no reasonable doctor would prescribe'."
                )
                print(
                    f"\nMay {he_she} rest in peace, loved by {his_her} millions of adoring fans."
                )
                div()
                print(f"{forename} {surname}")
                print(f"{wpp_year}-{year}")
                br()
                print(
                    "FBI AGENT: You are officially dead. You can now safely retire. We will protect your deceased status, but it is YOUR responsibility to make sure you're not spotted."
                )
                sleep(4)
                print(
                    "FBI AGENT: If you're spotted, we'll do out best to cover it up, but no guarantees."
                )
                sleep(3)
                print(f"{forename.upper()} {surname.upper()}: And if I admit it?")
                sleep(1)
                print("FBI AGENT: We have an NDA. Prepare to get sued.")
                sleep(2)
                print(
                    f"{forename.upper()} {surname.upper()}: And if someone looks at my FBI files?"
                )
                sleep(2)
                print("FBI AGENT: They'll remain classified until you *actually* die.")
                sleep(2)
                print("FBI AGENT: Good luck.")
                sleep(1)
                div()
                print(
                    "You have now entered the Witness Protection Program. You will receive a new name and new life."
                )
                print(
                    "The only people who will be aware of your new identity are your parents."
                )
                print("You will have to leave your spouse.")
                br()
                is_wpp = 1
                fame = 0
                job_id = 0
                sentence = 0
                money -= money / 8
                savings += money
                money = 0
                prison_years = 0
                is_spouse = 0
                friend_count = 0
                debt = 0
                wpp_name = [forename, surname]
                if gender == 0:
                    forename = choice(forename_m)
                else:
                    forename = choice(forename_f)
                surname = choice(surnames)
                is_spouse = 0
                name = forename + " " + surname
                adult()
            else:
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
            doctor_adult()
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
            print("[4] Show Death Ages")
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
                if is_spouse == 1:
                    if spouse.end < spouse.end:
                        print(
                            "Spouse will die at age",
                            spouse.end,
                            "[Current age: " + str(spouse.age) + "]",
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
                    debt += 10000
                    looks += 0.25
                    div()
                    print("The surgery was successful.")
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
        elif ch == 19 and gender == 0:
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
        global offences
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
        global alt_ui, auto_deposit, allow_debug, alt_logo
        print("[1] Auto-Deposit")
        print(
            "[Every year, all of your money gets automatically sent to your savings account]"
        )
        div()
        print("[2] Change Theme")
        print(f"[Change the look of {game_name}.]")
        print(f"[Different logo, progress bar style and line breaks.]")
        if allow_debug != 0:
            div()
            print("[3] Disable Debug Mode")
            print(
                "Debug mode was enabled by editing the main PY file. Choose this to *permanently* disable it."
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
            print("[3] Throwback Mode [Alpha 13] [Default]")
            try:
                ch = int(input(">"))
            except:
                alt_ui = 2
            if ch == 1:
                alt_ui = 0
                alt_logo = 0
            elif ch == 2:
                alt_ui = 2
                alt_logo = 1
            elif ch == 3:
                alt_ui = 3
                alt_logo = 2
            else:
                alt_ui = 3
                alt_logo = 2
            return True
        elif ch == 3 and allow_debug != 0:
            allow_debug = 0
            return True
        else:
            return True

    def adult_pause():
        global is_depressed, money, happiness, looks, intel, ethics, health, salary, hours
        global mother_age, father_age
        global mother_name, father_name
        global offences
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
        print("[6] Check For Updates")
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
        elif ch == 6:
            import urllib.request

            url = "http://winfan3672.000webhostapp.com/version_check/openlife.version"
            print("Checking for updates...")
            try:
                urllib.request.urlretrieve(url, "openlife.version")
            except:
                div()
                print("Failed to check for updates.")
                div()
                print("You could try:")
                print("[-] Checking that you are connected to the Internet.")
                print(
                    "[-] Checking that winfan3672.000webhostapp.com is still up, since that is the server that provides the version check information."
                )
                print(
                    "[-] Checking that http://winfan3672.000webhostapp.com/version_check/openlife.versio exists, since it may have been deleted."
                )
                print(
                    "[-] Checking that your antivirus or firewall is not blocking winfan3672.000webhostapp.com/"
                )
                print("[-] On Windows, deleting your DNS resolver cache.")
                adult_pause()
            div()
            f = open("openlife.version", "r")
            data = f.read()
            data = data.split("|")
            data = [int(data[0]), int(data[1]), int(data[2])]
            try:
                urllib.request.urlretrieve(
                    "http://winfan3672.000webhostapp.com/latest_v_url/openlife",
                    "openlife.urlcheck",
                )
                f = open("openlife.urlcheck", "r")
                url = f.read()
            except:
                url = "[Could not retrieve URL from server]"
            not_update_text = (
                f"An update for {game_name} is available.\nDownload it from:\n{url}"
            )
            if data[0] > app_version[0]:
                print(not_update_text)
            else:
                if data[1] > app_version[1]:
                    div()
                    print(not_update_text)
                else:
                    if data[2] > app_version[2]:
                        div()
                        print(not_update_text)
                    else:
                        print(f"You are on the latest version of {game_name}.")
            adult_pause()
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
        calc_stress()
        global edu_lvl, pension, job_lvl, is_spouse, spouse
        global salary, hours, fame, friend_count, friend_1
        global allow_debug, allow_debug, friend_2, friend_3
        global mother_age, father_age, is_wpp
        global mother_name, father_name, wpp_name
        global happiness, health, intel, looks, ethics
        global mother_rel, father_rel, part_time_salary
        global money, is_depressed, work_e, is_job
        global job_id, job_lvl, fame
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
        if fame > 1:
            fame = 1
        if fame < 0:
            fame = 0
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
        if is_wpp == 1:
            print(f"Under Witness Protection [Formerly {wpp_name[0]} {wpp_name[1]}]")
        if pension > 0 and money < 400000000000:
            print("Pensioner")
        elif money >= 5000000 and is_job == 0 and money < 400000000000:
            print("Independently Wealthy")
        elif is_job == 1:
            if job_id == 1:
                print("Amazon Delivery Driver")
            elif job_id == 2:
                if job_lvl == 1:
                    print("Jr Translator")
                elif job_lvl == 2:
                    print("Translator")
                else:
                    print("Sr. Translator")
            elif job_id == 3:
                if job_lvl == 1:
                    print("Jr Accountant")
                elif job_lvl == 2:
                    print("Accountant")
                else:
                    print("Sr Accountant")
            elif job_id == 4:
                print("Exorcist")
            elif job_id == 5:
                print("Teacher")
            elif job_id == 6:
                if job_lvl == 1:
                    print("Jr Game Developer")
                elif job_lvl == 2:
                    print("Game Developer")
                else:
                    print("Sr Game Developer")
            elif job_id == 8:
                if job_lvl == 1:
                    print("Jr Lawyer")
                elif job_lvl == 2:
                    print("Lawyer")
                else:
                    print("Sr Lawyer")
            elif job_id == 9:
                if job_lvl == 1:
                    print("Jr App Developer")
                elif job_lvl == 2:
                    print("App Developer")
                else:
                    print("Sr App Developer")
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
                if job_lvl == 1:
                    print("Jr Wedding Planner")
                elif job_lvl == 2:
                    print("Wedding Planner")
                else:
                    print("Sr Wedding Planner")
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
                if job_lvl == 1:
                    print("Private [Army]")
                elif job_lvl == 2:
                    print("Lieutenant [Army")
                else:
                    print("Captain [Army]")
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
                    print("Sr Editor")
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
        elif allow_debug == 1:
            print(f"{game_name} Debugger")
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
        if is_hbp == 1:
            if is_depressed == 0:
                div()
            print("Suffers from: High Blood Pressure")

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
        if fame > 0:
            div()
            print("Fame:     ", pbar2(fame), str(int(fame * 100)) + "%")
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
            if is_spouse == 1:
                if spouse.end > spouse.age:
                    print(spouse.name)
                    print(f"[3] Spouse [Age {spouse.age}]")
                    pbar(spouse.rel)
                    div()
            if friend_count >= 1:
                if friend_1.end > friend_1.age:
                    print(friend_1.name)
                    print(f"[4] Friend #1 [Age {friend_1.age}]")
                    pbar(friend_1.rel)
                    div()
            if friend_count >= 2:
                if friend_2.end > friend_2.age:
                    print(friend_2.name)
                    print(f"[5] Friend #2 [Age {friend_1.age}]")
                    pbar(friend_2.rel)
                    div()
            if friend_count >= 3:
                if friend_3.end > friend_3.age:
                    print(friend_3.name)
                    print(f"[6] Friend #3 [Age {friend_1.age}]")
                    pbar(friend_3.rel)
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
            elif ch == 4 and friend_count >= 1 and friend_1.end > friend_1.age:
                friend_1_interact()
            elif ch == 5 and friend_count >= 2 and friend_2.end > friend_2.age:
                friend_2_interact()
            elif ch == 6 and friend_count >= 2 and friend_3.end > friend_3.age:
                friend_3_interact()

            elif ch == 0:
                adult()
        elif ch == 4:
            adult_activities()
        adult()

    def adult_init(verbose):
        if verbose == 1:
            div()
            print("You are now an adult.")
            print(
                "It is like being a teen but you can go to uni, get a job and live a proper life."
            )
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
        if teen_hours > 0:
            print("[6] Edit Job Details")
        print("[x] Special Careers")
        div()
        print("Stress:", pbar2(stress), f"[{int(stress*100)}%]")
        div()
        print("In", club_count, "school clubs")
        if is_sch_gang == 1:
            print("In School Gang")
        div()
        print(f"Salary: {currency}{teen_salary}")
        print(f"Hours: {teen_hours}")
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
            print(f"[5] Laundrette Worker {currency}15/h] [15h]")
            print(f"[6] Drug Dealer [Local Gang] [{currency}45/h] [10h]")
            print(f"[7] None [{currency}0/h] [0h]")
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
                teen_salary = 15
                hours = 15
            elif ch == 6:
                teen_salary = 45
                teen_hours = 10
            elif ch == 7:
                teen_salary = 0
                teen_hours = 0
                teen()
            else:
                teen()
        elif ch == 6:
            if teen_hours > 0:
                print("[1] Adjust Hours")
                print("[0] Exit")
                div()
                print(f"Salary: {currency}{teen_salary}")
                print(f"Hours: {teen_hours}")
                div()
                try:
                    ch = int(input(">"))
                except:
                    teen()
                if ch == 1:
                    try:
                        hours = int(input(">"))
                    except:
                        hours = 10
                    if hours > 20:
                        hours = 20
                    if hours < 10:
                        hours = 10
                    teen_hours = hours
                    teen()
                else:
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
        global offences
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
            print("[6] Go To Juvie")
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
            elif ch == 6:
                global juvie_years, offences
                if offences == 0:
                    offences = 1
                go_to_juvie()
            else:
                teen()
        elif ch == 6:
            print("Welcome to the NEW Crime menu.")
            print("You can perform some crimes >:)")
            if offences > 0:
                div()
                print("You have committed", offences, "offence[s].")
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
                        div()
                        clout += 0.45
                        teen()
                    else:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        offences += 1
                        div()
                        div()
                        clout -= 0.45
                        teen()
                elif ch == 2:
                    if caught == 1:
                        print("You took a Budweiser from the local off-license.")
                        print("Sure does taste better when it's free.")
                        clout += 0.35
                        div()
                        teen()
                    elif caught == 2:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        offences += 1
                        div()
                        clout -= 0.35
                        div()
                        go_to_juvie()
                elif ch == 3:
                    print("Five finger discount, am I right?")
                    div()
                    happiness += 0.15
                    clout += 0.1
                    intel -= 0.2
                    teen()
                elif ch == 4:
                    if caught == 1:
                        money += 150
                        clout += 0.55
                        print(f"You sold the handbag for {currency}150.")
                        div()
                        teen()
                    else:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        offences += 1
                        div()
                        clout -= 0.55
                        br()
                        go_to_juvie()
                elif ch == 5:
                    if caught == 1:
                        print("You got a wallet. Now what?")
                        money += 50
                        clout += 0.15
                        br()
                        teen()
                    else:
                        print("SHOPKEEPER: What are you doing!")
                        print("YOU: Whoops.")
                        print("[SHOPKEEPER chases YOU out of store.]")
                        print("POLICE: We'll look into it.")
                        offences += 1
                        div()
                        clout -= 0.15
                        br()
                        go_to_juvie()
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
                        offences += 1
                        clout -= 0.35
                        br()
                        go_to_juvie()
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
        teen_calc_stress()
        global mother_name, father_name
        global offences
        global happiness, health, intel, looks, ethics, grades, clout, socialc
        global mother_rel, father_rel
        global money, is_depressed, is_hbp
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
            div()
            print("Suffers from: Depression")
            if is_hbp == 0:
                div()
        if is_hbp == 1:
            if is_depressed == 0:
                div()
            print("Suffers from: High Blood Pressure")
            div()
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
        global happiness, health, intel, looks, ethics, game_name, forename, surname, mother_name, father_name, mother_age, father_age, job_roles, birthdays, gender
        div()
        global mother_rel, father_rel
        mother_rel = 1
        father_rel = 1
        if gender == 0:
            print("I was born a male in OpenLife, OpenLife.")
        else:
            print("I was born a female in OpenLife, OpenLife.")
        print(f"My name is {forename} {surname}.")
        print(
            f"My mother is {mother_name}, a {mother_age}-year-old {choice(job_roles)}."
        )
        print(
            f"My father is {father_name}, a {father_age}-year-old {choice(job_roles)}."
        )
        div()
        print(f"My birthday is {choice(birthdays)}.")
        div()
        print(f"Welcome to {game_name}.")
        print("You are now a toddler.")
        print("Changes you make will affect your stats and change your life.")
        print("Since life is [literally] a game, you should try to win it.")
        print("'Winning' can be defined as reaching your life goal.")
        print("That goal can be anything. Getting your dream job, becoming rich,")
        print("living a fulfilling life, etc.")
        global age
        br()
        infant()

    def quick_life():
        global forename_m, forename_f, salary, hours, start_age, happiness, health, looks, intel, ethics, forename, surname, gender
        salary = 0
        hours = 0
        global edu_lvl
        edu_lvl = 0
        global mother_name, father_name
        from random import choice

        global sexuality, is_trans
        sexuality, is_trans = 0, 0

        mother_name = choice(forename_f)
        father_name = choice(forename_m)
        global happiness, health, intel, looks, ethics
        from random import randint

        if allow_debug == 1:
            happiness = 1
            health = 1
            looks = 1
            intel = 1
        else:
            happiness = (rng(1, 100)) / 100
            health = (rng(1, 100)) / 100
            intel = (rng(1, 100)) / 100
            looks = (rng(1, 100)) / 100
        ethics = 1
        start_age = 18
        gender = rng(0, 1)
        if gender == 0:
            forename = choice(forename_m)
        else:
            forename = choice(forename_f)
        surname = choice(surnames)
        mother_name += " " + surname
        father_name += " " + surname
        choose_start(0)

    def life_creator():
        global forename_m, forename_f, salary, hours, gender
        salary = 0
        hours = 0
        global edu_lvl
        edu_lvl = 0
        global mother_name, father_name
        from random import choice

        mother_name = choice(forename_f)
        father_name = choice(forename_m)
        global happiness, health, intel, looks, ethics
        global sexuality, is_trans
        sexuality = 0  # 1= gay, 2=lesbian, 3=NB, 4=asexual
        is_trans = 0
        from random import randint

        print("[1] Male")
        print("[2] Female")
        try:
            ch = int(input(">"))
        except:
            ch = 0
        if ch == 1:
            gender = 0
        elif ch == 2:
            gender = 1
        else:
            gender = rng(0, 1)
        print()
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
                if gender == 0:
                    forename = choice(forename_m)
                else:
                    forename = choice(forename_f)

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
            choose_start(1)
            try:
                start_age = int(input("Enter START AGE >"))
                choose_start(1)
            except:
                start_age = 0
                choose_start(1)
            choose_start(1)
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
            choose_start(1)
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
        )  # Download Location: http://winfan3672.000webhostapp.com/challenge/latest.zip
        print("[5] Load Challenge From Disk")
        print("[6] Exit")
        print("[7] Changelog")
        print("[8] Download Latest Custom Life")  # Download location: N/A
        print("[9] Options")
        print("[10] Quick Create Life")
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
        elif ch == 10:
            quick_life()
        elif ch == 9:
            div()
            edit_configuration()
            mainmenu()
        elif ch == 8:
            import urllib.request

            url = "https://winfan3672.000webhostapp.com/custom_life/customlife.oll2"
            print("Downloading custom life...")
            try:
                urllib.request.urlretrieve(url, "custom_life.oll2")
            except:
                div()
                print("Failed to download custom life.")
                mainmenu()
            div()
            print("Downloaded custom life.")
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
            print(
                "[-] Allowing me to help out on his one [https://github.com/Fungamer2-2/Life-Simulator1/]"
            )
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
        elif ch == 5:
            import sys

            sys.path.insert(0, "challenge.zip")
            try:
                import challenge

                challenge.init(app_version)
            except:
                div()
                print("The challenge failed to load.")
                div()
                print("Possible fixes:")
                print(
                    '[-] Make sure that a file called "challenge.zip" exists in your /openlife_saves folder'
                )
                print("[-] Download the challenge [main menu option 4]")
                print(
                    "[-] Download the latest version of the game, since the code for running the Challenge may be outdated."
                )
                print(
                    "[-] Check the download server [winfan3672.000webhostapp.com] is up. If not, challenges no longer work."
                )
                print(
                    "[-] Make sure that you can open challenge.zip [in /openlife_saves]. If not, give yourself read access."
                )
                print(
                    "[-] Try again later and download the challenge, it may be updated to work :)"
                )
                br()
            mainmenu()
        elif ch == 7:
            changelog = [
                "Alpha 14- The Identity Update",
                "====================",
                "1 Preface",
                "====================",
                "1.1 Alpha 14",
                "This update is a follow-up to the abysmal Alpha 13. It includes a lot of identity-related things, such as genders, and some unrelated ones, such as the Witness Protection Program.",
                "",
                "1.2 Alpha 15",
                "Alpha 15 will be the Homesteader update. It will include:",
                "[-] OLL to OLL2 converter",
                "[-] House-buying",
                "[-] House-selling",
                "[-] House-flipping",
                "[-] OpenLife Times",
                "   [-] A newspaper that changes articles depending on what happens in your life, for instance, if you enter the Witness Protection Program, there will be reported sightings of you, etc.",
                "[-] Children",
                "[-] Siblings",
                "   [-] Up to 2 siblings may generate when you are born",
                "   [-] Quick Life will NOT make any",
                "",
                "1.3 Look to the future",
                "After Alpha 15, there will be a few more Alpha builds, and the game will jump to Beta.",
                "",
                "[-] Alpha 16",
                "   [-] Bug Fix Update",
                "   [-] Squashes as many known bugs as possible",
                "   [-] Quality of Life changes",
                "[-] Alpha 17",
                "   [-] Just An Update",
                "   [-] This update has no theme and focuses on adding as much as possible to the game.",
                "[-] Alpha 18",
                "   [-] Sccenario Update",
                "   [-] Adds scenarios",
                "   [-] Includes job-specific, child, teen, adult etc.",
                "   [-] This will be the LAST Alpha build of OpenLife. ",
                "",
                "This is the schedule, assuming I do not postpone anything.",
                "",
                "====================",
                "2 Spouse",
                "====================",
                "2.1 Changes",
                "",
                "[-] Added insults",
                "   [-] You now call your spouse more than just a dickhead",
                "[-] Added compliments",
                "[-] New hitman choice for spouse",
                "[-] Parents can now congratulate you for finding a date",
                "[-] Now have intelligence/craziness/looks values",
                "[-] Now have a `fortune` value, which is how much money you inherit.",
                "",
                "====================",
                "3 Debug Log",
                "====================",
                "",
                "3.1 What It Is",
                "This is a utility for creating human-readable and detailed logs that provide information about the game and the system playing it.",
                "",
                "3.2 What data is included",
                "[-] Contents of game memory",
                "[-] OS",
                "[-] Screen resolution",
                "[-] Python version",
                "[-] CPU information",
                "[-] Game settings",
                "",
                "3.3 Who sees this data",
                "The log is saved to a `.log` file in your `openlife_saves` directory. You can choose who sees this data by choosing to share it. You can send it to us for bug reporting, send it to your friends because you are weird, or you could even keep it to yourself. It's up to you.",
                "",
                "**No data gets sent to anyone when creating the log. The delay when creating the log is the time it takes for `tkinter` to launch a window then close it in order to work out the screen resolution.**",
                "",
                "====================",
                "4 Ribbons",
                "====================",
                "4.1 What They Are",
                "Ribbons are listed underneath the OpenLife Times article when you die. You can collect ribbons by fulfiling their requirements. Multiple ribbons can be collected, **just like BitLife used to do**.",
                "",
                "4.2 Ribbon List",
                "[-] Rich",
                "[-] Debt Slave",
                "[-] Cheater",
                "[-] Bad Karma King",
                "[-] Geriatric",
                "[-] Stupid",
                "[-] Famous",
                "[-] Nerd",
                "[-] Wasteful",
                "[-] Unlucky",
                "[-] Bandit",
                "[-] Beautiful",
                "[-] Perfectionist",
                "[-] Depressed",
                "[-] Mediocre",
                "",
                "====================",
                "5 Fame",
                "====================",
                "5.1 Fame",
                "A stat you unlock that shows how famous you are.",
                "",
                "5.2 Perks of fame",
                "You unlock the Fame menu, where you can become even more famous while making a lot of money.",
                "",
                "5.3 Witness Protection Program",
                "When you have 100% fame, you can go into Witness Protection. You will lose all your fame and your death will be faked. You will be given a new identity.  When you actually die, the OpenLife Times will reveal that your death was faked the whole time, and that the FBI were hiding it.",
                "",
                "5.4 Losing Fame",
                "When your fame <= 0%, you become Infamous. At the moment, nothing happens, but when OpenTube [OpenLife's answer to YouTube] gets added, being infamous will result in you losing subscribers instead of gaining them.",
                "",
                "5.5 Legendary Status",
                "When you enter the WPP, you will gain Legendary Status. When this happens, you will be a legend, and your legacy will never be forgotten.",
                "",
                "====================",
                "6 Prison",
                "====================",
                "6.1 Juvie",
                "If you commit a crime while underage, you will be sent to Juvie. If you are 18 and in juvie, you will get transferred to Prison [6.2]",
                "",
                "6.2 Prison",
                "When 18+ and commiting a crime, you get sent to prison.",
                "",
                "6.3 Escaping",
                "Once you escape prison, you may get found by the authorities and sent back to finish your sentence. [Your sentence is extended for good measure]",
                "",
                "====================",
                "7 Stress / Teen Jobs",
                "====================",
                "[-] High Blood Pressure",
                "   [-] You can get it from too much stress.",
                "   [-] You have a 25% chance of dying of a heart attack every year.",
                "   [-] Can be cured by de-stressing, such as by increasing happiness or quitting your job",
                "[-] calc_stress()",
                "   [-] Function to calculate the stress level. ",
                "   [-] Factors like happiness, hours and part-time hours are taken into account",
                "[-] Teen job update!",
                "   [-] More part-time jobs",
                "   [-] Adjust hours",
                "   [-] Stress is added when you have a part-time job",
                "====================",
                "8 Identity",
                "====================",
                "[-] Gender",
                "   [-] You now have a gender",
                "   [-] Wow. So original.",
                "[-] Dating App",
                "   [-] Costs Â£100",
                "   [-] Choose age",
                "[-] Gay Dating App",
                "   [-] Same-sex relationships",
                "",
                "====================",
                "10 Friends",
                "====================",
                "10.1 Friends",
                "You can have up to [3] friends. ",
                "",
                "10.2 Interactions",
                "You can interact with your friends.",
                "",
                "10.2.1 Spend Time",
                "Increases relation and happiness by 25%",
                "",
                "10.2.2 Conversation",
                "Has a 25% chance of becoming an argument.",
                "",
                "10.2.3 Unfriend",
                "Removes that friend",
                "",
                "10.2.4 Insult",
                "Reduces happiness and relations by 25%",
                "",
                "10.2.5 Ask Out",
                "Ask them out. If relations 75%+ they will accept.",
                "",
                "====================",
                "11 General Additions",
                "====================",
                "[-] Doctor",
                "   [-] Treats ailments",
                "   [-] Free",
                "[-] Quick Life",
                "   [-] Menu option",
                "   [-] Creates an 18-year-old with a random gender and stats",
                "[-] Challenges",
                "   [-] You were able to download them, now you can play them.",
                "   [-] Choose a save file and, if you are on the latest version, you might get Â£1M.",
                "   [-] Each challenge has a challenge number, and the save file keeps track of which challenge number was last completed, so that you do not complete it an infinite amount of times.",
                "[-] If you cannot afford surgery, you will take out a loan for it",
                "[-] Load Game will no longer report the wrong expected version, due to `check_version` [a list object] being used for both version checks and reports",
                "[-] When doing a name change, the name cannot be longer than 16 characters long. If it exceeds the limit, characters will be removed until it is exactly 16 characters.",
                "[-] You can now Check for Updates.",
                "   [-] If an update is available, you will be shown a URL that you can paste into your browser to download the latest version of OpenLife.",
                "====================",
                "12 Bug Fixes",
                "====================",
                "[-] The game no longer exits when you pick an invalid choice in the Life Creator",
                "[-] The game no longer exits when you choose an invalid save file in the Load Game screen.",
                "[-] A lot of previously unsaved data is now saved when you save the game.",
                "====================",
                "13 Last Words",
                "====================",
                "I feel like I was way too excited to push this update out. In fact, I was so entheusiastic to do so, I pushed back a few features:",
                "[-] An update to the Teen Shop",
                "[-] Children",
                "   [-] I was definitely underestimating my potential when I decided they were too difficult to implement.",
                "[-] I almost pushed back friends, until I decided that I was capable of doing it.",
                "",
                "I realise that Alpha 15 is so ambitious, that I have only 3 ideas scheduled for the long term on my Monday.com board. I am greatly excited about the future of OpenLife, and I hope you are too.",
                "====================",
                "Build Date  : 4 Nov 2022",
                "Publish Date: 5 Nov 2022",
            ]
            for l in changelog:
                l = l.replace("{game_name}", game_name)
                l = l.replace("OpenLife", game_name)
                if l == "====================":
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
