#!/usr/bin/python

# OpenLife Life Simulator

# OpenLife is a free and open source BitLife clone, with a vast amount of features.
# It has a lot of shared features with BitLife as well some *exclusive* ones.

# For the official GitHub repo, https://github.com/WinFan3672/OpenLife
# For the Wiki, https://openlife.fandom.com/

# The Project is maintained by WinFan3672, who is the current sole dev for the project.
# Some code is taken from the Internet, but it is approximately 95% in-house.

# It is recommended to use pypy for extra performance, especially since some activities are computationally expensive.

# The compliments, insults, and Spend Time With lists were taken from fungamer2's Life-Simulator1 and edited to make it compatible with OpenLife.
import copy
import json
global degrees
degrees = [
    "None",
    "Finance",
    "Journalism",
    "Computer Science",
    "Ecucation",
    "Accounting",
    "Political Science",
    "Nursing",
    "Psychology",
    "Engineering",
    "Art History",
    "Communications",
    "Graphic Design",
    "Data Science",
    "Criminal Justice",
    "Linguistics",
    "Marketing",
    "Anthopology",
    "Archaeology",
    "Biology",
    "Chemistry",
    "Physics",
    "English",
    "Mathematics",
    "History",
    "Information Systems",
    "Music",
    "Economics",
    "Dance",
    "Electrical Engineering",
    "Religious Studies",
    "Dentistry",
    "Law"
]
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
    "the pros and cons of blockchain technology",
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

global job_roles
job_roles = [
    ["Unemployed"],
    ["Amazon Delivery Driver"],
    ["Jr Translator", "Translator", "Sr Translator"],
    ["Jr Accountant", "Accountant", "Sr Accountant"],
    ["Exorcist"],
    [],
    ["Jr Game Developer", "Game Developer", "Sr Game Developer"],
    [],
    ["Jr Lawyer"],
    ["App Developer"],
    ["Jr Banker"],
    ["Monk"],
    ["Wedding Planner", "Sr Wedding Planner"],
    ["Engineer I", "Engineer II", "Engineer III"],
    ["Data Scientist"],
    [],
    [],
    ["Cashier"],
    ["College Lecturer"],
    ["Oohber Driver"],
    ["Jr Editor", "Editor", "Sr Editor"],
    ["Exotic Dancer"],
    ["Flight Attendant"],
    ["Apprentice Hairdresser", "Hairdresser"],
    [],
    ["Librarian"],
    ["Nun"],
    [],
    ["Porn Actor"],
    ["Stockbroker"],
    ["Social Media Manager","Public Relations Assistant","Head of Marketing"],
]

global researches
researches = [
    ## [id,display name,price,years to develop,function (player object passed to (can leave as None))]
    ["researchLab","Research Lab",1000000000,3,None],
    ["ageDown","Age Down 20 Years",15000000000,1,None],
    ["cureCancer","Cure To Cancer",150000000000,5,None],
    ["isImmortal","Immortality",1000000000000,10,None],
    #["deStress","0% Stress",150000000,3,None]
    ]

global racehorses
racehorses = ["Thunderbolt Express", "Gallop for Gold", "Majestic Mane", "Golden Hooves", "Whirlwind Sprint", "Wildfire Gallop", "Sapphire Blaze", "Diamond Dust", "Red Velvet Run", "Electric Stride", "Royal Canter", "Neptune's Fury", "Midnight Mirage", "Silver Speedster", "Emerald Elegance", "Blazing Comet", "Swift Thunder", "Scarlet Sprint", "Phoenix Flame", "Rapid Racer", "Crimson Charge", "Pegasus Flight", "Frosty Frenzy", "Titan's Trot", "Moonlight Gallop", "Thundering Tornado", "Cherry Blossom Burst", "Oceanic Ovation", "Enchanted Equine", "Jade Jumper"]

import os

try:
    os.mkdir("OpenLife Saves")
except:
    pass
os.chdir("OpenLife Saves")

from random import choice
from random import randint as rng
from time import sleep, ctime
from time import strftime as stime
from platform import uname
import os, signal, logging, pickle, codecs, base64
import pickle

import tkinter as tk

class Fuse:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        self.__blown = False

    def blow(self):
        self.__blown = True

    @property
    def blown(self):
        return self.__blown

    @classmethod
    def is_blown(cls, fuse):
        return fuse.blown

    def __str__(self):
        return str(self.blown)
import inspect
import platform
def OllTwoConverter():
    ## OLL2 To OLL3 Conversion Utility

    ## Variables is a map of all of the attributes in OLL2 and their indexes in the format index:attribute.
    ## Some have been removed due to being useless.
    variables = {
        2: 'happiness',
        3: 'health',
        4: 'intel',
        5: 'looks',
        6: 'ethics',
        7: 'money',
        8: 'forename',
        9: 'surname',
        10: 'age',
        11: 'work_e',
        12: 'edu_lvl',
        13: 'work_e_base',
        14: 'promo_base',
        15: 'is_depressed',
        16: 'debt',
        17: 'savings',
        18: 'expenses',
        19: 'pension',
        23: 'year',
        24: 'is_job',
        25: 'stress',
        26: 'mother_name',
        27: 'father_name',
        28: 'mother_age',
        29: 'father_age',
        30: 'mother_end_age',
        31: 'father_end_age',
        32: 'did_tutor',
        33: 'mother_rel',
        34: 'father_rel',
        35: 'is_spouse',
        36: 'spouse',
        45: 'teen_hours',
        46: 'teen_salary',
        50: 'job_id',
        52: 'gender',
        79: 'fame',
        80: 'is_wpp',
        81: 'wpp_name',
        83: 'sentence',
        84: 'prison_years',
        85: 'juvie_years',
        170: 'is_opentube',
        171: 'opentube_year',
        172: 'is_verif',
        173: 'is_monetised',
        174: 'watch_time',
        175: 'channel_name',
        176: 'subscribers',
        177: 'video_count',
        178: 'view_count',
        180: 'pistol_count',
        181: 'knife_count',
        182: 'is_smartphone',
        183: 'pistol_ammo',
        184: 'chainsaw_count',
        185: 'taser_count',
        186: 'is_common_cold',
        187: 'flip_profits'
    }
    ## Initialisation stage
    global x,y
    y = dir(Player())
    x = []
    for item in variables:
        if not variables[item] in y:
            x.append(variables[item])
    x = sorted(x)
    def autoType(string):
        try:
            value = float(string)
            if value.is_integer():
                return int(value)
            else:
                return value
        except ValueError:
            if string.lower() == 'none':
                return None
            elif string.lower() == 'true':
                return True
            elif string.lower() == 'false':
                return False
            else:
                return string    
    def getPlayerDataBase(filename):
        global x,y
        with open(filename,"rb") as f:
            ssave=f.read()
            ssave = codecs.decode(ssave, "base64_codec")
            ssave = ssave.decode("utf-8")
            ssave = ssave.split("|")
            if [ssave[0],ssave[1]] == ["Alpha","16"]:
                print("yes")
                return ssave
            else:
                print("Error: Invalid Version")
    def getPlayerData(filename="/run/media/winfan3672/SM/Libraries/Documents/Python/OpenLife/alpha/openlife_saves/a16.oll2"):
        global x,y
        i = 0
        zx = []
        for item in variables:
            zx.append(item)
        v=getPlayerDataBase(filename)
        xz = {}
        for item in v:
            if i in zx:
                xz[variables[i]] = item
            i += 1
        x += ["spouse"]
        return xz
    def makePlayer(xz):
        ## Automatic Attribute Assigning
        p = Player()
        for item in xz:
            if not item in x:
                setattr(p,item,autoType(xz[item]))
        ## Manual Attribute Assigning
        ### is depressed
        p.disease["depression"] = bool(xz["is_depressed"])
        ### channel
        if autoType(xz["is_opentube"]):
            o = OpenTube(xz["channel_name"])
            o.subscribers = autoType(xz["subscribers"])
            o.viewCount=autoType(xz["view_count"])
            o.watchHours=autoType(xz["watch_time"])
            o.videoCount=autoType(xz["video_count"])
            o.year=autoType(xz["opentube_year"])
            p.opentube.append(o)
        ### parents
        p.parents = []
        m = Parent()
        f = Parent()
        m.create(1,p.surname)
        f.create(0,p.surname)
        m.name = autoType(xz["mother_name"])
        f.name = autoType(xz["father_name"])
        m.age = autoType(xz["mother_age"])
        f.age = autoType(xz["father_age"])
        m.end = autoType(xz["mother_end_age"])
        f.end = autoType(xz["father_end_age"])
        m.relation = autoType(xz["mother_rel"])
        f.relation = autoType(xz["father_rel"])
        p.parents = [m,f]
        return p
    import os
    def main():
        l = []
        for item in os.listdir():
            if item.endswith(".oll2"):
                l.append(item)
        if l == []:
            cls()
            div()
            print("Error: No Alpha 16 save files present.")
            br()
            return None
        cls()
        div()
        print("Select OLL2 Save File")
        div()
        for i in l:
            print(i.replace(".oll2",""))
        div()
        try:
            ch=input("FileName $")
            xz=getPlayerData(ch+".oll2")
            p = makePlayer(xz)
            saveGameBase(p,ch+".oll3")
            cls()
            div()
            print(f"Successfully converted to \"{ch}\".")

            br()
            
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
    main()
def get_function_parameters(func):
    if not callable(func):
        return None
    sig = inspect.signature(func)
    params = []
    for param in sig.parameters.values():
        if param.kind == inspect.Parameter.VAR_POSITIONAL:
            params.append('*' + param.name)
        elif param.kind == inspect.Parameter.VAR_KEYWORD:
            params.append('**' + param.name)
        else:
            params.append(param.name)
    return params
def uiDebugText(text):
    root = tk.Tk()
    root.title("uiDebugText")

    def exit_window():
        root.destroy()
        root.quit()

    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(input_field.get("1.0", "end"))

    # calculate the width and height of the input box based on the specified resolution
    width = int(0.9 * root.winfo_screenwidth() / 2)
    height = int(0.9 * root.winfo_screenheight() / 2)

    # set the size of the window
    root.geometry("{}x{}".format(width, height))

    # calculate the width and height of the input box based on the specified resolution
    input_width = int(0.8 * width)
    input_height = int(0.8 * height)

    input_field = tk.Text(root, width=input_width, height=input_height, wrap="word")

    # Create a menu bar
    menu_bar = tk.Menu(root)

    # Create a File menu cascade
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Copy To Clipboard", command=copy_to_clipboard)
    file_menu.add_command(label="Exit", command=exit_window)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Add the menu bar to the window
    root.config(menu=menu_bar)

    input_field.insert("end", text)
    input_field.pack()

    root.mainloop()
    return None


global version, app_version, subversion, game_name
game_name = "OpenLife"
app_version = [0, 2, 0]
version = f"{app_version[0]}.{app_version[1]}.{app_version[2]} [26 May 2023]"
sub_version = "xyxyx"
global forename_m, forename_f, surnames
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

global prefs
prefs = {
    "version": app_version,
    "prefVersion": [0, 1, 0],
    "allowDebug": False,
    "hideConsole": False,
    "div": "--------------------",
    "doNotClearVar": True,
    "autoDeposit": False,
    "autoPayLab": False,
}
if prefs['allowDebug']:
    prefs["doNotClearVar"] = prefs["allowDebug"]
# Exceptions


class ExitError(Exception):
    ## Called when exiting game
    ## Used to destroy game
    pass


## Base Classes
class Base():
    '''
Base class used by all classes.
This class is used as a base for other classes exclusively, and is not called directly.
Methods:
    __str__():
        Returns the object as a fornatted dict if you use it in print().
    __iter__():
        If you use a Base class object in a for loop, it iterates through every attribute's name instead of their values.
    __len__():
        If you use len() on it, it returns the amount of attributes it has
    
    '''
    __slots__ = ['__weakref__']
    def __str__(self):
        return pprint_dict(obj_to_dict(self))

    def __iter__(self):
        return iter(sorted(self.__dict__.keys()))

    def __len__(self):
        return len(dir(self))
class rangedInt:
    ## A floating point number with a specified range that gets automatically adhered to
    ## Currently unused, but will be used soon
    def __init__(self, value, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self._value = None
        self.set(value)

    def get(self):
        return self._value

    def set(self, value):
        if value < self.min_value:
            self._value = self.min_value
        elif value > self.max_value:
            self._value = self.max_value
        else:
            self._value = int(value)

    def __str__(self):
        return str(self._value)

    def __add__(self, other):
        if isinstance(other, rangedInt):
            return rangedInt(self._value + other.get(), self.min_value, self.max_value)
        elif isinstance(other, (int, float)):
            return rangedInt(self._value + other, self.min_value, self.max_value)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, rangedInt):
            return rangedInt(self._value - other.get(), self.min_value, self.max_value)
        elif isinstance(other, (int, float)):
            return rangedInt(self._value - other, self.min_value, self.max_value)
        else:
            return NotImplemented

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, rangedInt):
            return rangedInt(self._value * other.get(), self.min_value, self.max_value)
        elif isinstance(other, (int, float)):
            return rangedInt(self._value * other, self.min_value, self.max_value)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, rangedInt):
            return rangedInt(self._value / other.get(), self.min_value, self.max_value)
        elif isinstance(other, (int, float)):
            return rangedInt(self._value / other, self.min_value, self.max_value)
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        return self.__truediv__(other)    
class Scenario(Base):
    """
Scenario object.
Creates a scenario that is callable by the game.

Args:
    <str> title: The title of the message box
    <str> message: The message to be displayed by the game
    <list> buttons: Contains a list of lists in the following format:
    [label, function]
        <str> label: The text displayed for the button
        <method> function: The function that gets called when the option is selected. Can be None as well.
Returns:
    A Scenario object.
Methods:
    run(self): Executes the scenario.
    """
    def __init__(self,title,message,buttons=[],default=None):
        super().__init__()
        self.title=title
        self.msg=message
        self.buttons=buttons if isinstance(buttons,list) else []
    def run(self):
        cls()
        div()
        print(self.title)
        div()
        print(self.msg)
        if self.buttons == []:
            br()
            return None
        i = 1
        div()
        for item in self.buttons:
            print(f"[{i}] {item[0]}")
            i += 1
        div()
        try:
            ch=int(input("$"))
            y = self.buttons[ch-1][1]
        except:
            return default
        if callable(y):
            y()
    __call__ = run
class CallScenario(Base):
    """
CallScenario object.
Creates a scenario that is callable by the game.

Args:
    <str> title: The title of the message box
    <str> message: The message to be displayed by the game
    <list> buttons: Contains a list of lists in the following format:
    [label, value]
        <str> label: The text displayed for the button
        value: The value that gets returned
Returns:
    A CallScenario object.
Methods:
    run(self): Executes the scenario. Returns the correlated value
    """
    def __init__(self,title,message,buttons=[]):
        super().__init__()
        self.title=title
        self.msg=message
        self.buttons=buttons if isinstance(buttons,list) else []
    def run(self):
        cls()
        div()
        print(self.title)
        div()
        print(self.msg)
        if self.buttons == []:
            br()
            return None
        i = 1
        div()
        for item in self.buttons:
            print(f"[{i}] {item[0]}")
            i += 1
        div()
        try:
            ch=int(input("$"))
            y = self.buttons[ch-1][1]
            return y
        except:
            return None
    __call__ = run
class Person(Base):
    '''
Person class.
Used for non-player characters.

Args:
    None
Returns:
    A Person object.
    Person objects have randomly-generated:
    - Names
    - Ages
    - Jobs
    - Death ages
    = Etc.
Methods:
    age_up():
        Increments the age and adds money based on one's salary and hours.
        Also calls age_up_() if it exists.
    reduceLifespan(years):
        Args:
            <int> years: Amount to decrement by
        Decreases how long that person has to live by <years> years.
    '''
    def __init__(self):
        self.gender = rng(0,1)
        self.name = choice(forename_m) if self.gender == 0 else choice(forename_f)
        self.name += " " + choice(surnames)
        self.age = rng(18,30)
        self.money = 0
        self.hours = rng(40,50)
        self.salary = rng(30,50)
        self.endAge = rng(65,85)
        self.relation = 0.5

    def age_up(self):
        self.money += self.hours * self.salary * 52
        self.age += 1
        try:
            self.age_up_()
        except:
            pass

    def reduceLifespan(self, years):
        self.endAge -= years
        if self.end < self.age:
            self.end = self.age + 1
class Vehicle(Base):
    """
Vehicle class.
Base for Car, Boat, and Plane classes.

This class is used as a base for other classes exclusively, and is not called directly.
Methods:
    age_up():
        Performs actions to increment the car's age as well as decrease the price and condition.
        Calls age_up_() if it exists.
    """
    def age_up(self):
        self.value = int(self.value * 0.85)
        self.condition = self.condition * 0.85
        self.age += 1
        if not isinstance(self,Vehicle):
            self.age_up_()
global car_models, boat_models, plane_models
car_models = [
    [["BWM Beetle",35000],["WV Chiron",35000],["Mini Smart",20000],["Smart Mini",20000],["OpenMotors Model 3000",75000]],
    [["Chevollet Monte Carlo",1100],["Holder Accorda",45000],["Holder Civil",30000],["Handai Santa Fe",15000],["Merchant C-Class",55000],["Kai Sorrento",16500]],
    [["Totoya GT99",11000],["Chervolle Corvette",12000],["Dodgem Challenger",14000]],
    [["Mars Rover 3000",40000],["Fodr Mustang",67000]],
    [["Nikola Model S",56000],["Nikola Model x",67000],["Nikola Model Y",99000],["Nikola Cybertruck",150000],["BWM Electric Beetle",45000],["OpenMotors Model 3500",25000]],
    [["McLaid Senna",1250000],["McLaid 4500",1000000],["OpenMotors Exotic Mk. III",750000],["Fodr Extra",1750000],["Holder Xartra",1750000],["OpenMotors Electric Mk. II",1650000]],
    [["OpenMotors RubberScreech",2500000],["Ferry LXVI",4500000],["Bourgeoise Lavish",10000000],["Landbo Avenger",135000],["Doppelsieg Motorworks Silver Claw Mk. II",350000]],
    [["F1 Mk. I",250000],["F1 Mk. II",500000],["F1 Mk. III",750000],["F1 Mk. IV",1000000]]
    ]
boat_models = [
    ["Raft",100,200],
    ["Speedboat",10000,45000],
    ["Yacht",45000,556000],
    ["Pirate Ship",10000000,12000000],
    ["Rowing Boat",5000,10000]
    ]
plane_models = [
    [["Boing 737",150000000],["Boing 747",250000000],["Airbuss A320",175000000],["Airbuss A340",275000000]],
    [["Cessna 172 Skyhawk",15000],["Embracer Predator 520",15000000]],
    [["Gumman F-14 Tompatt",77777777]]
    ]
global house_types
house_types = [
    ["Duplex",100000,200000],["Villa",10000000,15000000],["Castle",5000000,15000000],["Farm",500000,1500000],["Geodesic Home",500000,750000],["Log Cabin",100000,200000],["Condomidium",100000,250000],["Trailer",15000,50000],["Futuristic Home",20000000,50000000],["Penthouse",5000000,25000000],["Modern Home",300000,800000],["Studio",25000,50000],["Tiny House",10000,25000]
    ]
class Achievement(Base):
    def __init__(self,title,description):
        super().__init__()
        self.title=title
        self.desc=description
        self.achieved=False
        self.date=None
    def achieve(self,player):
        if self.achieved:
            return None
        if player.cheater.blown:
            return None
        self.achieved = True
        div()
        print("Earned Achievement")
        div()
        print(self.title)
        div()
        print(self.desc)
        br()
        self.date=time.strftime("%x %X")
## Main Classes
class Bond(Base):
    """
Bond class.
Args:
name: Name of bond
maxInvestment: The maximum amount of money that can be invested. $0 = no limit
mult: multiplier used every year. 1.2 = +20% etc.
defChance: % chance of the bond defaulting.
    """
    def __init__(self,name=None,maxInvestment=None,mult=None,defChance=None):
        super().__init__()
        self.name=name
        self.investment = 0
        self.maxInvestment=maxInvestment
        self.mult=mult
        self.defChance=defChance
    def age_up(self,player):
        self.investment = int(self.investment * self.mult)
        if pChance(self.defChance) and self.investment > 0:
            cls()
            div()
            print(f"Your shares in {self.name} have been defaulted and are now worthless!")
            br()
            self.investment = 0
    def interact(self,player):
        cls()
        div()
        print(f"{self.name} [{Format(int((self.mult-1)*100))}% APR]")
        print(f"Money Invested: {player.nation.currency}{Format(self.investment)}/{player.nation.currency}{Format(self.maxInvestment)}")
        print(f"Risk: {pbar(self.defChance/100)} [{self.defChance}%]")
        div()
        print("[1] Invest Money")
        if self.investment > 0:
            print("[2] Sell Stock")
        else:
            print("[ ] Sell Stock")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            try:
                m = int(input("Amount $"))
            except:
                return None
            if m > player.money:
                m = player.money
            if m > self.maxInvestment:
                m = self.maxInvestment
            if self.maxInvestment - (m + self.investment) < 0:
                m = self.maxInvestment - (m + self.investment)
            if m < 0:
                m = 0
            if player.money >= m:
                player.money -= m
                self.investment += m
                cls()
                div()
                print(f"Successfully invested {player.nation.currency}{Format(m)} in {self.name}.")
                br()
                self.interact(player)
            else:
                cls()
                div()
                print(f"You cannot afford to invest {player.nation.currency}{Format(m)} in {self.name}.")
                br()
                self.interact(player)
        elif ch == 2 and self.investment > 0:
            cls()
            div()
            print(f"Investment: {player.nation.currency}{Format(self.investment)}")
            div()
            try:
                ch = int(input("Amount $"))
            except:
                return None
            if ch < 0:
                ch = 0
            if ch > self.investment:
                ch = self.investment
            self.investment -= ch
            player.money += ch
            cls()
            div()
            print(f"Successfully withdrew {player.nation.currency}{Format(ch)}.")
            br()
            self.interact(player)
        else:
            return None
class Crypto(Base):
    def __init__(self,name,symbol):
        super().__init__()
        self.mode = 0
        self.price = rng(1,100)/100
        self.name=name
        self.symbol=symbol
        self.investment=0
        self.lastPrice = self.price
    def age_up(self,player):
        self.lastPrice = self.price
        if self.mode == 0:
            ## Normal mode (-15 to +15 % /Annum)
            mult = rng(85,115)/100
            self.price *= mult
            if pChance(50):
                self.mode = 0
            else:
                if pChance(50):
                    self.mode = 1
                else:
                    self.mode = 0
        elif self.mode == 1:
            ## Explosion mode (+200 to +500 % /Annum)
            mult = rng(2,5)
            self.price *= mult
            if pChance(60):
                self.mode = 1
            else:
                if pChance(5):
                    self.mode = 0
                else:
                    self.mode = 2
        else:
            ## Crash mode (-30 to -50 % /Annum)
            mult = rng(50,70) / 100
            self.price *= mult
            if pChance(65):
                self.mode = 2
            else:
                if pChance(35):
                    self.mode = 0
                else:
                    self.mode = 1
        self.price = int(self.price*100) / 100
        if self.price == 0.0:
            cls()
            div()
            print(f"The crypto, {self.name} [{self.symbol}] has crashed and will be taken off the market.")
            br()
            player.crypto.remove(self)
        if self.investment > 0:
            cls()
            div()
            print(f"{self.name} [{self.symbol}] Summary")
            div()
            print(f"Old Price: {player.nation.currency}{Format(self.lastPrice)}")
            print(f"New Price: {player.nation.currency}{Format(self.price)}")
            print(f"1Y Price Change: {percentChange(self.lastPrice,self.price)}%")
            br()
    def interact(self,player):
        cls()
        div()
        print(f"{self.name} [{self.symbol}]")
        print(f"Price: {player.nation.currency}{Format(self.price)}")
        print(f"1Y Price Change: {percentChange(self.lastPrice,self.price)}%")
        print(f"Holdings: {Format(self.investment)} {self.symbol}")
        print(f"Portfolio Value: {player.nation.currency}{Format(int(self.investment*self.price))}")
        div()
        print(f"[1] Buy {self.symbol}")
        if self.investment > 0:
            print(f"[2] Sell {self.symbol}")
        else:
            print(f"[ ] Sell {self.symbol}")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print(f"Price: {player.nation.currency}{Format(self.price)}")
            print(f"Money: {player.nation.currency}{Format(player.money)}")
            print(f"Can Buy: {Format(int(player.money / self.price))}{self.symbol}")
            div()
            try:
                ch=int(input("Amount $"))
            except:
                return None
            if ch > int(player.money / self.price):
                ch = int(player.money / self.price)
            if ch < 0:
                ch = 0
            cls()
            div()
            print(f"Successfully purchased {Format(ch)}{self.symbol}.")
            br()
            self.investment = ch
            player.money -= int(ch * self.price)
            self.interact(player)
        elif ch == 2 and self.investment > 0:
            cls()
            div()
            print(f"Price: {player.nation.currency}{Format(self.price)}")
            print(f"Holdings: {Format(self.investment)}{self.symbol}")
            div()
            try:
                ch = int(input(f"{self.symbol} To Sell $"))
            except:
                return None
            if ch > self.investment:
                ch = self.investment
            if ch < 0:
                ch = 0
            self.investment -= ch
            player.money += int (ch * self.price)
            cls()
            div()
            print(f"You sold {Format(ch)}{self.symbol} for {player.nation.currency}{Format(int(ch*self.price))}.")
            br()
            self.interact(player)
        else:
            return None
class Metal(Base):
    def __init__(self,name,basePrice,minInc,maxInc,midInc=None):
        super().__init__()
        self.name=name
        self.mid = midInc
        self.price=basePrice
        self.min=minInc
        self.max=maxInc
        self.investment = 0
    def age_up(self,player):
        if self.mid != None:
            mult = 1 + (weightedRNG(self.min,self.mid,self.max)/100)
        else:
            mult = 1 + (rng(self.min,self.max)/100)
        p = self.price
        self.price = self.price * mult
        self.price *= 100
        self.price = int(self.price) / 100
        if self.investment > 0:
            cls()
            div()
            print(f"Investment Summary: {self.name}")
            div()
            print(f"Old Price: {player.nation.currency}{Format(p)}")
            print(f"New Price: {player.nation.currency}{Format(self.price)}")
            print(f"1Y Return: {percentChange(p,self.price)}%")
            print(f"Portfolio Value: {player.nation.currency}{Format(int(self.price * self.investment))}")
            br()
    def interact(self,player):
        cls()
        div()
        print(f"{self.name}")
        print(f"Investment: {Format(self.investment)} lb.")
        print(f"Price per lb.: {player.nation.currency}{format(self.price)}")
        print(f"Portfolio Value: {player.nation.currency}{Format(int(self.price*self.investment))}")
        div()
        print(f"[1] Buy {self.name}")
        if self.investment > 0:
            print(f"[2] Sell {self.name}")
        else:
            print(f"[ ] Sell {self.name}")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print(f"Price: {player.nation.currency}{Format(self.price)}")
            print(f"Can Afford: {Format(int(player.money/self.price))} lb.")
            div()
            try:
                ch=int(input("Amount $"))
            except:
                return None
            if ch > int(player.money/self.price):
                ch = int(player.money/self.price)
            if ch < 0:
                ch = 0
            cls()
            div()
            print(f"Successfully purchased {Format(ch)} {self.name}.")
            br()
            player.money -= int(ch*self.price)
            self.investment += ch
            self.interact(player)
        elif ch == 2 and self.investment > 0:
            cls()
            div()
            print(f"Price: {player.nation.currency}{Format(self.price)}")
            print(f"Holding: {Format(self.investment)} LB")
            div()
            try:
                ch=int(input("Amount $"))
            except:
                return None
            if ch < 0:
                ch = 0
            if ch > self.investment:
                ch = self.investment
            self.investment -= ch
            x = int(ch*self.price)
            self.money += x
            cls()
            div()
            print(f"You sold {Format(ch)} lb. of {self.name} for {player.nation.currency}{Format(x)}.")
            br()
            self.interact(player)
        else:
            return None
class IndexFund(Base):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.investment = 0
    def age_up(self):
        self.investment = int(self.investment * (1 + rng(5,15)/100))
    def interact(self,player):
        cls()
        div()
        print(self.name)
        print(f"Invested: {player.nation.currency}{Format(self.investment)}")
        div()
        print(f"[1] Buy {self.name}")
        print(f"[2] Sell {self.name}")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            try:
                ch=int(input("Amount $"))
            except:
                return None
            if ch > player.money:
                ch = player.money
            if ch < 0:
                ch = 0
            player.money -= ch
            self.investment += ch
            cls()
            div()
            print(f"Invested {player.nation.currency}{Format(ch)} in {self.name}.")
            br()
        elif ch == 2:
            cls()
            div()
            print(f"Invested: {player.nation.currency}{Format(self.investment)}")
            div()
            try:
                ch=int(input("$"))
            except:
                return None
            if ch > self.investment:
                ch = self.investment
            if ch < 0:
                ch = 0
            player.money += ch
            self.investment -= ch
            cls()
            div()
            print(f"Withdrew {player.nation.currency}{Format(ch)} from {self.name}.")
            br()
class Stock(Base):
    def __init__(self,name,symb,price,vol=65):
        super().__init__()
        self.name=name
        self.vol=vol
        self.price=price
        self.symb=symb
        self.investment = 0
    def age_up(self,player):
        price = self.price
        def simulate_stock_price(initial_price, volatility):
            random_factor = random.uniform(-1, 1)
            price_change = initial_price * (volatility / 100) * random_factor
            stock_price = initial_price + price_change
            return stock_price
        self.price = simulate_stock_price(self.price,self.vol)
        self.price = int(100*self.price)/100
        if self.investment > 0:
            cls()
            div()
            print(f"{self.symb}: Financial Report")
            div()
            print(f"Old Price: {player.nation.currency}{price}")
            print(f"Old Price: {player.nation.currency}{self.price}")
            print(f"1Y Price Change: {percentChange(price,self.price)}")
            br()
    def interact(self,player):
        cls()
        div()
        print(f"{self.name} [{self.symb}]")
        print(f"Price: {player.nation.currency}{self.price}")
        print(f"Owned: {Format(self.investment)}")
        div()
        print(f"[1] Buy {self.symb}")
        print(f"[2] Sell {self.symb}")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print(f"Can Afford: {Format(int(player.money/self.price))}")
            try:
                ch=int(input("Amount $"))
            except:
                return None
            if ch > int(player.money/self.price):
                ch = int(player.money/self.price)
            if ch < 0:
                ch = 0
            player.money -= int(self.price * ch)
            self.investment += ch
            cls()
            div()
            print(f"Bought {Format(ch)} {self.symb}.")
            br()
        elif ch == 2:
            cls()
            div()
            print(f"Invested: {Format(self.investment)}")
            div()
            try:
                ch=int(input("$"))
            except:
                return None
            if ch > self.investment:
                ch = self.investment
            if ch < 0:
                ch = 0
            player.money += ch
            self.investment -= ch
            cls()
            div()
            print(f"Sold {Format(ch)} {self.symb}.")
            br()
class Friend(Person):
    """
Friend class.
Based on Person class.

Args:
None

Returns:
Friend obhect.

Methods:
    interact(self,player): Takes a Player ogject; interacts with the friend
See also:
    Person class
    """
    def interact(self, player):
        cls()
        div()
        print(self.name)
        print("Age:",self.age)
        print(f"Relation: {pbar(self.relation)} {int(self.relation*100)}%")
        div()
        print("[1] Unfriend")
        print("[2] Compliment")
        print("[3] Conversation")
        print("[4] Spend Time")
        print("[5] Insult")
        print("[6] Ask Out")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print(f"You unfriended your friend, {self.name}.")
            br()
            player.friends.remove(self)
        elif ch == 2:
            cls()
            div()
            print(f"You called your friend {choice(compliments)}.")
            br()
            self.relation += 0.25
            if self.relation >= 0.75:
                cls()
                div()
                print(f"Your friend called you {choice(compliments)}.")
                br()
                player.happiness += 0.25
            self.interact(player)
        elif ch == 3:
            cls()
            div()
            print(f"You and your friend had a debate about {choice(debates)}.")
            br()
            self.relation += 0.25
            player.happiness += 0.25
            self.interact(player)
        elif ch == 4:
            cls()
            div()
            print(f"You and your friend went {choice(spend_time)}.")
            self.relation += 0.25
            player.happiness += 0.45
            self.interact(player)
        elif ch == 5:
            cls()
            div()
            print(f"You called your friend {choice(insults)}.")
            br()
            self.relation -= 0.45
            self.interact(player)
        elif ch == 6:
            if pChance(int(self.relation * 100)) and self.gender != player.gender:
                grantAchievement(player,"damnThatsFine")
                cls()
                div()
                print("Your friend agreed to date you.")
                player.spouse = castObject(self, Spouse)
                player.friends.remove(self)
                br()
            else:
                cls()
                div()
                print("Your friend asked if you were joking.")
        else:
            return None
class Nation(Base):
    """
Nation class.
Creates a nation that can be switched to by the player.
    """
    def __init__(self,name,nationId,canGamble=True,canLottery=True,dropOutAge=16,deathSentence=False,currency="$",gunLicense=False,freeHealthcare=True,uniPrice=25000,incomeTaxMul=1,houseTaxMul=1,openTubeTaxMul=0.85):
        super().__init__()
        self.name=name
        self.id = nationId
        self.canGamble = canGamble
        self.dropOutAge = dropOutAge
        self.deathSentence = deathSentence
        self.currency=currency
        self.canLottery=canLottery
        self.gunLicense = gunLicense
        self.freeHealth=freeHealthcare
        self.uniPrice = uniPrice
        self.incomeTax=incomeTaxMul
        self.houseTax=houseTaxMul
        self.opentube=openTubeTaxMul
class House(Base):
    """
House class.
Creates a house you can buy/sell/interact with.

Args:
    None
Returns:
    House object.
Methods:
    __init__(self):
        Creates a House object.
        Each House object is randomly-generated.
    age_up(self,player):
        Takes a Player class.
        Performs basic tasks for aging up, such as:
            [-] Incrementing year
            [-] Increasing value of house
            [-] Decreasing condition
    interact(self,player):
        Takes a Player class.
        Allows the player to interact with the house, such as by selling the house.
    """
    def __init__(self):
        super().__init__()
        self.type = rng(0,len(house_types)-1)
        x=house_types[self.type]
        self.name=x[0]
        self.price = rng(x[1],x[2])
        self.value = self.price
        self.condition = 1
        self.age=0
        self.address = str(rng(1,2000)) + " " + generate_street_name()
        self.rentPrice = int(self.price/100)
        self.mortgaged = False
        self.mortgageValue = 0
        self.haunted = True if pChance(35) else False
        if self.haunted:
            self.name = "Haunted " + self.name
    def age_up(self,player):
        if not self.mortgaged:
            self.value = int(self.value * 1.15)
        self.age += 1
        self.condition = self.condition * 0.9
    def interact(self,player):
        x = 100 - int(self.condition * 100)
        y = int(self.price * x/100)
        cls()
        div()
        print(self.name)
        print(self.address)
        if self.mortgaged:
            print(f"Mortgaged")
        div()
        print(f"Condition: {pbar(self.condition)} {int(self.condition*100)}%")
        print(f"Age [Years]: {'{:,}'.format(self.age)}")
        print(f"Original Price: {player.nation.currency}{'{:,}'.format(self.price)}")
        print(f"Value: {player.nation.currency}{'{:,}'.format(self.value)}")
        div()
        if not self.mortgaged:
            print("[1] Sell")
        else:
            print("[ ] Sell")
        if self.mortgaged:
            print("[2] Pay Off")
        else:
            print("[2] Mortgage")
        print("[3] Party")
        if self.condition < 1:
            print(f"[4] Renovate [{'{:,}'.format(y)}]")
        else:
            print("[ ] Renovate")
        if self.haunted:
            print("[5] Exorcise")
        else:
            print("[ ] Exorcise")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1 and not self.mortgaged:
            cls()
            div()
            if pChance(int(self.condition * 100)):
                ov=self.value
                self.value = int(self.value * player.nation.houseTax)
                print("You sold your house.")
                print(f"You sold it for {player.nation.currency}{'{:,}'.format(self.value)}.")
                print(f"You made {player.nation.currency}{'{:,}'.format(self.value-self.price)} in profits.")
                print(f"Tax Paid: {player.nation.currency}{Format(ov-self.value)}")
                br()
                player.property.remove(self)
                player.money += self.value
                player.flip_profits += self.value - self.price
            else:
                print("No-one wanted it.")
                br()
        elif ch == 2:
            if not self.mortgaged:
                cls()
                div()
                print("You mortgaged your house for {player.nation.currency}{'{:,}'.format(self.value)}.")
                br()
                player.money += self.value
                self.mortgaged = True
                self.mortgageValue = self.value
            else:
                cls()
                div()
                print("You paid back your mortgage.")
                br()
                player.money -= self.mortgageValue
                self.mortgaged = False
            self.interact(player)
        elif ch == 3:
            cls()
            div()
            x=pChance(10)
            print("You had a party.")
            print(f"{rng(10,250)} people attended.")
            br()
            if x:
                cls()
                div()
                print("One of the guests gave alcohol to a child, causing them to pass out drunk.")
                br()
                cls()
                div()
                print("The police were called.")
                br()
                player.offences.append(Offence("Supplying Alcohol to Minors",3))
                goToPrison(player)
            else:
                cls()
                div()
                print("Everyone had a great time.")
                br()
            self.interact(player)
        elif ch == 4 and self.condition < 1:
            x = 100 - int(self.condition * 100)
            y = int(self.price * x/100)
            cls()
            div()
            print("Renovation Price:")
            print(f"{player.nation.currency}{'{:,}'.format(y)}")
            div()
            print("[1] Renovate")
            print("[0] Cancel")
            div()
            try:
                ch=int(input("$"))
            except:
                return None
            if ch == 1:
                player.money -= y
                self.condition = 1
                cls()
                div()
                print("The house is now in perfect condidion!")
                br()
            self.interact(player)
        elif ch == 5 and self.haunted:
            if pChance(10) or player.job_id == 4:
                cls()
                div()
                print("Your house was successfully exorcised!")
                br()
                self.value *= 2
                self.haunted = False
                self.name = self.name[8:]
            else:
                cls()
                div()
                print("The exorcism failed.")
                br()
            self.interact(player)
        else:
            return None
class Car(Vehicle):
    """
Car class.
Each car is semi-randomly-generated based on baked-in price and name data.

Args:
    <bool> stolen: Whether the car was purchased (False) or stolen (True).
Returns:
    A car object.
    """
    def __init__(self,stolen=False):
        self.age = 0
        self.stolen=stolen
        self.condition = 1
        self.type=rng(1,len(car_models))
        self.x = car_models[self.type-1]
        self.id = rng(0,len(self.x)-1)
        self.y=self.x[self.id]
        self.price = self.y[1]
        self.value = self.price
        self.name=self.y[0]
        self.wash=False
        self.maintenance=False
        del(self.x)
        del(self.y)
    def age_up_(self):
        self.wash=False
        self.maintenance=False
    def interact(self,player):
        cls()
        div()
        print(car_models[self.type-1][self.id][0])
        if self.stolen:
            print("[!] Stolen Vehicle")
        print(f"Condition: {pbar(self.condition)} {int(self.condition * 100)}%")
        print(f"Original Price: {player.nation.currency}{'{:,}'.format(self.price)}")
        print(f"Value: {player.nation.currency}{'{:,}'.format(self.value)}")
        div()
        print("[1] Ride")
        print("[2] Wash")
        print("[3] Maintenance")
        print("[4] Sell")
        print("[5] Scrap")
        print("[x] Gift")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print("You had a ride in your ride.")
            br()
            player.happiness = 1
        elif ch == 2:
            cls()
            div()
            print("You washed your car.")
            br()
            if not self.wash:
                self.condition += 0.1
                self.wash = True
        elif ch == 3:
            cls()
            div()
            print("You had maintenance done on the car.")
            br()
            if not self.maintenance:
                self.condition += 0.25
                self.maintenance = True
        elif ch == 4:
            cls()
            div()
            print("You sold your car.")
            print(f"Value: {player.nation.currency}{'{:,}'.format(self.value)}")
            br()
            player.money += self.value
            player.vehicles[0].remove(self)
        elif ch == 5:
            cls()
            div()
            print("You scrapped your car.")
            player.vehicles[0].remove(self)
        else:
            return None
class Boat(Vehicle):
    def __init__(self):
        self.condition = 1
        self.age=0
        self.model = rng(1,5)
        x = boat_models[self.model-1]
        self.name=None
        self.modelName=x[0]
        self.price=rng(x[1],x[2])
        self.value=self.price
        self.maintenance = False
    def age_up_(self):
        self.maintenance = False
    def setName(self):
        cls()
        div()
        print("Enter Ship Name")
        div()
        name=input("$")
        if name == "":
            name = choice(["HMS Organic","His Master's Boat","B O T E","RMS Magical","RMS OpenLivian","Ol' Besty","WinBoat3672"])
        self.name=name
    def interact(self,player):
        cls()
        div()
        print(self.name)
        print(self.modelName)
        print(f"Condition: {pbar(self.condition)} [{int(self.condition*100)}%]")
        print(f"Original Price: {player.nation.currency}{'{:,}'.format(self.price)}")
        print(f"Value: {player.nation.currency}{'{:,}'.format(self.value)}")
        div()
        print("[1] Ride")
        print("[2] Maintenance")
        print("[3] Sell")
        print("[4] Scrap")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print("You rode the waves with your boat.")
            br()
            player.happiness = 1
        elif ch == 2:
            cls()
            div()
            print("You had maintenance done on your boat.")
            br()
            if not self.maintenance:
                self.condition += 0.25
                self.maintenance = True
        elif ch == 3 or ch == 4:
            cls()
            div()
            print("You had your boat scrapped" if ch == 4 else "You sold your boat.")
            if ch == 3:
                print(f"Value: {player.nation.currency}{'{:,}'.format(self.value)}")
                player.money += self.value
            br()
            player.vehicles[1].remove(self)
        else:
            return None
class Plane(Vehicle):
    def __init__(self):
        self.age=0
        self.condition=1
        self.type=rng(1,3)
        if self.type == 3 and pChance(66):
            self.type -= rng(1,2)
        x = choice(plane_models[self.type-1])
        self.name=x[0]
        self.price=x[1]
        self.value=self.price
        self.maintenance=False
    def age_up_(self):
        self.maintenance=False
    def interact(self,player):
        cls()
        div()
        print(self.name)
        print(f"Condition: {pbar(self.condition)} [{int(self.condition*100)}%]")
        print(f"Original Price: {player.nation.currency}{'{:,}'.format(self.price)}")
        print(f"Value: {player.nation.currency}{'{:,}'.format(self.value)}")
        div()
        print("[1] Fly")
        print("[2] Maintenance")
        print("[3] Sell")
        print("[4] Scrap")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print("You flew in your plane.")
            br()
            player.happiness = 1
        elif ch == 2:
            cls()
            div()
            print("You had maintenance performed on your plane.")
            br()
            if not self.maintenance:
                self.condition += 0.25
                self.maintenance = True
        elif ch == 3 or ch == 4:
            cls()
            div()
            if ch == 3:
                print("You sold your plane.")
                print(f"Value: {player.nation.currency}{'{:,}'.format(self.value)}")
                
            else:
                print("You scrapped your plane.")
            br()
            if ch == 3:
                player.money += self.value
            player.vehicles[2].remove(self)
def Format(num):
    return '{:,}'.format(num)
def percentChange(a, b):
    try:
        change = ((b - a) / a) * 100
    except ZeroDivisionError:
        change = 100
    return change
class OpenTube(Base):
    """
OpenTube channel.

Args:
    <str> name: The name of the new channel.
Returns:
    An OpenTube object, with 0 views/subscribers/etc.
Methods:
    stats():
        Displays channel statistics.
    delete(player):
        Deletes the channel from the player's channel list.
        Args:
            player: a Player object
    age_up(player,skip):
        Ages up the channel.
        Args:
            player: a player object
            <bool> skip: True = display channnel summary, False = don't display.
    main(player):
        Main frontend for channel control, allowing you to upload videos, set a schedule, etc.
        Args:
            player: Player object
    calcMoney(views, cpm):
        Calculates ad revenue for a video.
        Args:
            <int> views: How many views the video has
            <int> cpm: Amount of cents to pay per million views
        Returns:
            An integer, in dollars, which is the ad revenue for the specified video.
    calcSubs(views):
        Calculates how many subscribers one gains based on view count.
        Args:
            <int> views: How many views the video got
        Returns:
            <int> subscribers: The amount of subscribers gained
    def calcViews():
        Calculates how many views a video should get based on subscriber count and other factors.
        Args:
            None
        Returns:
            <int> views: The amount of views the video got.
    upload(player, normal):
        Uploads a video.
        Args:
            player: a player object
            <bool> normal: Whether or not to display GUI or to automatically specify video type
        Returns:
            None.
            Uploads a video to the channel.
    
    """
    def __init__(self,name):
        self.name=name
        self.subscribers=1
        self.videoCount=0
        self.viewCount=0
        self.watchHours=0
        self.channelYear=0
        self.monetised=False
        self.verified=False
        self.schedule=0
        self.year=1
    def stats(self):
        cls()
        div()
        if self.verified:
            print(f"[✔️]",self.name)
        else:
            print(self.name)
        print(f"Year {self.year}")
        div()
        print(f"Subscribers: {'{:,}'.format(self.subscribers)}")
        print(f"Views:       {'{:,}'.format(self.viewCount)}")
        print(f"Videos:      {'{:,}'.format(self.videoCount)}")
        print(f"Watch Time:  {'{:,}'.format(self.watchHours)} Hours")
        br()
    def delete(self, player):
        cls()
        div()
        print(f"Your channel ('{self.name}') has been deleted from the Internet.")
        div()
        print(f"Subscribers: {'{:,}'.format(self.subscribers)}")
        print(f"Views:       {'{:,}'.format(self.viewCount)}")
        print(f"Videos:      {'{:,}'.format(self.videoCount)}")
        print(f"Watch Time:  {'{:,}'.format(self.watchHours)} Hours")
        br()
        player.opentube.remove(self)
        main(player)
    def age_up(self, player,skip=False):
        old = self.subscribers
        self.year += 1
        if self.schedule:
            views, subs, money = 0,0,0
            for i in range(self.schedule):
                xviews,ldr = self.calcViews()
                views += xviews
            subs = self.calcSubs(views,ldr)
            if self.monetised:
                money += self.calcMoney(player,views,17)
            self.videoCount += self.schedule
            self.viewCount += views
            self.subscribers += subs
            if self.subscribers >= 8000000000:
                self.subscribers = 8000000000
            player.money += money
            self.watchHours += int(views/6)
            if not skip:
                cls()
                div()
                print(f"Channel Summary(\"{self.name}\"): Year {self.year}")
                div()
                print("Views Gained:",'{:,}'.format(views))
                print("Subscribers Gained:",'{:,}'.format(self.subscribers-old))
                print("Money Earned:",player.nation.currency+'{:,}'.format(money))
                br(skip)
    def main(self, player):
        cls()
        div()
        if self.verified:
            print(f"[✔️]",self.name)
        else:
            print(self.name)
        print(f"Year {self.year}")
        div()
        print(f"Subscribers: {'{:,}'.format(self.subscribers)}")
        print(f"Views:       {'{:,}'.format(self.viewCount)}")
        print(f"Videos:      {'{:,}'.format(self.videoCount)}")
        print(f"Money:      {player.nation.currency}{'{:,}'.format(player.money)}")
        div()
        print("[1] Upload Video")
        if not self.monetised:
            print("[2] Request Monetisation")
        else:
            print("[ ] Request Monetisation")
        if not self.verified:
            print("[3] Get Verified")
        else:
            print("[ ] Get Verified")
        print("[4] Sell Channel")
        print("[5] Delete Channel")
        print("[6] Stats")
        print("[x] Sponsor...")
        print("[8] Set Upload Schedule")
        print("[0] Exit")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            self.upload(player)
            self.main(player)
        elif ch == 2 and not self.monetised:
            cls()
            div()
            if self.watchHours >= 10000:
                self.monetised = True
                print("Your videos have been approved for monetisation!")
                print("You now earn ad revenue from every video.")
            else:
                print("Your monetisation request was declined.")
            br()
            self.main(player)
        elif ch == 3 and not self.verified:
            cls()
            div()
            if self.subscribers > 100000:
                print("Your account is now verified!")
                self.verified = True
            else:
                print("You need >= 100,000 subscribers to be verified.")
            br()
            self.main(player)
        elif ch == 4:
            cls()
            div()
            if self.subscribers >= 10000:
                print("x")
                price = int(self.subscribers/15)
                print(f"An anonymous buyer is offering {player.nation.currency}{'{:,}'.format(price)} for your channel.")
                print("x")
                div()
                print("[1] Accept Offer")
                print("[0] Decline Offer")
                div()
                try:
                    ch=int(input("$"))
                except:
                    self.main(player)
                if ch == 1:
                    player.money += price
                    cls()
                    div()
                    print("You sold your channel.")
                    br()
                    player.opentube.remove(self)
                    main(player)
            else:
                print("No-one wants a channel with less than 10,000 subscribers.")
                br()
                self.main(player)
        elif ch == 5:
            cls()
            div()
            print("[1] Delete Channel")
            print("[0] Cancel")
            div()
            try:
                ch=int(input("$"))
            except:
                self.main(player)
            if ch == 1:
                self.delete(player)
            else:
                self.main(player)
        elif ch == 6:
            self.stats()
            self.main(player)
        elif ch == 8:
            cls()
            div()
            print("Set Schedule")
            div()
            print("[0] None")
            print("[1] Monthly")
            print("[2] Weekly")
            print("[3] Daily")
            div()
            try:
                ch=int(input("$"))
            except:
                ch=0
            if ch == 1:
                self.schedule=12
            elif ch == 2:
                self.schedule=52
            elif ch == 3:
                self.schedule=365
            else:
                self.schedule=0
            self.main(player)
        else:
            main(player)
    def calcMoney(self, player, views, cpm):
        return views//1000 * cpm * player.nation.opentube
    def calcSubs(self, views,ldr):
        return int(views/3)
    def viralise(self,views,subs):
        if rng(1,1000) != 1:
            return views
        if subs < 10000:
            return rng(1000000,5000000)
        elif views < 1000000:
            return rng(1000000,10000000)
        elif views < 10000000:
            return rng(50000000,150000000)
        else:
            return 0.5 * subs * views
    def calcViews(self):
        ## Formula:
        ## Base Views + (Like Count / 2) + (Dislike Count * -2)
        ## Base Views = Subscribers / 3 OR 1 if Subscribers < 1
        ## Like:Dislike Ratio: rng(10,90) / 100
        ## Like Count = Base Views * Like Ratio
        ## Dislike Count = Base Views * 1 - Like Ratio
        baseViews = int(self.subscribers / 3)
        ldr = rng(10,90)/100
        likeCount = int(baseViews * ldr)
        dislikeCount = int(baseViews * (1-ldr))
        views = int(baseViews + (likeCount/2) + (dislikeCount*-0.75))
        if self.videoCount == 0:
            views = 500
        if views < 10:
            views = 10
        return views,ldr
    def upload(self,player,normal=True):
        if normal:
            cls()
            div()
            print("Select Video Type:")
            print("CPM = Cents/Thousand Views")
            div()
            print("[1] OpenLife [CPM17]")
            print("[2] BitLife [CPM14]")
            print("[3] Gaming [CPM10]")
            print("[4] How-To [CPM11]")
            print("[5] Educational [CPM6]")
            print("[6] Drama [CPM15]")
            #print("[x] Music [CPM0]")
            div()
            try:
                ch=int(input("$"))
                if ch < 1 or ch > 6:
                    raise Exception
            except:
                return None
            cpms = [17,14,10,11,6,15]
            cpm = cpms[ch-1]
        else:
            cpm=17
        views, ldr = self.calcViews()
        subs = self.calcSubs(views,ldr)
        if self.videoCount:
            views = self.viralise(views,subs)
        if normal:
            cls()
            div()
            print("You uploaded your video.")
            br()
            cls()
            div()
            print("View Count:",'{:,}'.format(views))
            #print("Like:Dislike Ratio:",ldr)
            print(f"{Format(int(views*ldr))} Likes {pbar(ldr)} {Format(int(views*(1-ldr)))} Dislikes")
            print("Subscribers Gained:",'{:,}'.format(subs))
            br()
        if self.monetised:
            money = self.calcMoney(player,views, cpm)
            if normal:
                print(f"You made {player.nation.currency}{'{:,}'.format(money)} in ad revenue!")
                br()
            player.money += money
        self.viewCount += views
        self.subscribers += subs
        if self.subscribers > 8000000000:
            self.subscribers = 8000000000
        self.videoCount += 1
        self.watchHours += int(1/6 * views)

class Child(Person):
    def __init__(self, age=0, gender=0, isAdopted=0):
        super().__init__()
        self.isAdopted = isAdopted
        self.age = age
        self.gender = gender
        self.isAbandoned = 0

    def create(self, player):
        self.age = 0
        self.b_year=player.year
        self.endAge = rng(64, 84)
        self.gender = rng(0, 1)
        if self.gender == 0:
            self.name = f"{choice(forename_m)} {player.surname}"
        else:
            self.name = f"{choice(forename_f)} {player.surname}"
        self.isAdopted = 0
        self.relation = 0.5
    def giveName(self):
        self.name =  choice(forename_m if self.gender == 0 else forename_f) + " " + choice(surnames)
    def interact(self, player):
        cls()
        div()
        print(self.name)
        print(f"Age: {self.age}")
        print(f"Relation:")
        print(pbar(self.relation))
        div()
        print("[1] Compliment")
        if self.isAbandoned == 0:
            print("[2] Conversation")
            print("[3] Spend Time With")
        if self.isAbandoned == 0:
            print("[4] Abandon")
        else:
            print("[ ] Abandon")
        if self.isAbandoned == 0:
            print("[5] Adopt Out")
        print("[6] Insult")
        div()
        try:
            ch = int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print(f"You called your child {choice(compliments)}.")
            self.relation += 0.25
            if self.relation >= 0.75:
                print(f"Your child called you {choice(compliments)}.")
                player.happiness += 0.25
            br()
        elif ch == 2 and self.isAbandoned == 0:
            cls()
            div()
            print(f"You had a debate with your child about {choice(spend_time)}.")
            print("Agreement:")
            print(pbar(0.8))
            br()
            self.relation += 0.25
        elif ch == 3 and self.isAbandoned == 0:
            cls()
            div()
            print(f"You took your child {choice(spend_time)}.")
            br()
        elif ch == 4 and self.isAbandoned == 0:
            self.isAbandoned = 1
            self.relation = 0
            cls()
            div()
            print(f"You abandoned your child, {self.name}.")
            br()
        elif ch == 5 and self.isAbandoned == 0:
            cls()
            div()
            print(f"You adopted out your child, {self.name}")
            player.children.remove(self)
            br()
        elif ch == 6:
            cls()
            div()
            print(f"You called your child {choice(insults)}.")
            self.relation -= 0.25
            br()


class Offence(Base):
    def __init__(self, name, years):
        super().__init__()
        self.name = name
        self.years = years
        self.served = False
        self.years_served = 0

    def age_up(self):
        self.years_served += 1
        if self.years_served >= self.years:
            self.served = True

    def sentence(self):
        return self.years - self.years_served if self.years > self.years_served else 0
class CoWorker(Person):
    def __init__(self):
        super().__init__()
        self.relation = rng(0,100) / 100
    def interact(self,player):
        if self.relation > 1:
            self.relation = 1
        if self.relation < 0:
            self.relation = 0
        cls()
        div()
        print(self.name)
        print("Age:",self.age)
        print(f"Relation: {pbar(self.relation)} {int(self.relation * 100)}%")
        print("Gender:","Male" if self.gender == 0 else "Female")
        div()
        print("[1] Compliment")
        print("[2] Conversation")
        print("[3] Have Lunch")
        print("[x] Ask Out")
        print("[x] Flirt")
        print("[6] Insult")
        print("[x] Suck up to")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print(f"You called your co-worker, {self.name}, {choice(compliments)}.")
            br()
            self.relation += 0.25
            if self.relation >= 0.75:
                cls()
                div()
                print(f"Your co-worker, {self.name}, called you {choice(compliments)}.")
                br()
                player.happiness += 0.25
            if self.relation <= 0.25:
                cls()
                div()
                print("You were ignored.")
                br()
                player.happiness -= 0.25
            self.interact(player)
        elif ch == 2:
            cls()
            div()
            if self.relation >= 0.5:
                print(f"You and your co-worker, {self.name}, had a debate about {choice(debates)}.")
            else:
                print(f"Your co-worker, {self.name}, ignored you.")
                player.happiness -= 0.25
            br()
            self.interact(player)
        elif ch == 3:
            cls()
            div()
            print("You invited your co-worker, {self.name}, to lunch.")
            br()
            if self.relation >= 0.5:
                cls()
                div()
                print("You had lunch together.")
                br()
            else:
                cls()
                div()
                print(f"{self.name} politely declined.")
            self.interact(player)
        elif ch == 6:
            cls()
            div()
            print("You called your co-worker, {self.name}, {choice(insults)}!")
            self.relation -= 0.25
            br()
            self.interact(player)
        else:
            return None
class Job(Base):
    def __init__(self,name,id,lvl,pay,hours,minEdu,degree=0,l2pay=0,l3pay=0):
        super().__init__()
        self.name = name
        self.id=id
        self.lvl=lvl
        self.pay=pay
        self.hours=hours
        self.minHours=hours
        self.minEdu=minEdu
        self.degree=degree
        self.performance = 0.5
        self.promoBase=3
        self.pay_2 = l2pay
        self.pay_3 = l3pay
        self.work_e = 0
        self.coworkers=[]
        for i in range(rng(7,15)):
            self.coworkers.append(CoWorker())
    def interact(self, player):
        cls()
        div()
        print(job_roles[self.id][self.lvl-1])
        div()
        print(f"Performance: {pbar(self.performance)} {int(self.performance*100)}%")
        print(f"Salary: {player.nation.currency}{self.pay}/Hr.")
        print(f"Hours: {self.hours}/Week [{self.minHours} Minimum]")
        div()
        print("[1] Resign")
        print("[2] Adjust Hours")
        if self.work_e >= 20:
            print("[3] Retire")
        else:
            print(f"[ ] {20-self.work_e} Years To Retirement")
        print("[x] Request Raise")
        print("[x] Request Promotion")
        print("[6] Co-Worker Interaction")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print("You resigned from your position.")
            br()
            player.job=None
            player.job_id, player.job_lvl = 0,0
            adult(player)
        elif ch == 2:
            cls()
            div()
            try:
                h = int(input("New Hours [0-70] $"))
            except:
                self.interact(player)
            if h < 0:
                h = 0
            if h > 70:
                h = 70
            self.hours = h
            self.interact(player)
        elif ch == 3 and self.work_e >= 20:
            cls()
            div()
            print("You retired.")
            player.job = None
            player.pension += int((self.pay * self.hours * 52)/2)
            print(f"Yearly Pension: {player.nation.currency}{'{:,}'.format(player.pension)}")
            br()
        elif ch == 0:
            return None
        elif ch == 6:
            cls()
            div()
            i = 1
            for item in self.coworkers:
                print(f"[{i}] {item.name}\nRelation: {pbar(item.relation)} {int(item.relation*100)}%")
                i += 1
            div()
            try:
                ch=int(input("$"))
                self.coworkers[ch-1].interact(player)
                self.interact(player)
            except:
                return None
        else:
            self.interact(player)
    def promote(self,player):
        cls()
        div()
        print("You got a promotion!")
        div()
        self.lvl += 1
        print("New Role:",job_roles[self.id][self.lvl-1])
        if self.lvl == 2 and self.pay_2 != 0:
            self.pay = self.pay_2
        if self.lvl == 3 and self.pay_3 != 0:
            self.pay = self.pay_3
        print("Salary:",str(self.pay)+"/Hr.")
        self.promoBase = 4 if self.lvl == 2 else 5
        try:
            player.job_lvl += 1
        except Exception as e:
            print(e)
        br()
    def promoteCheck(self):
        try:
            x = job_roles[self.id][self.lvl]
            x = True
        except:
            x = False
        return x
    def check(self,player):
        if player.job_lvl == -1:
            return True
        if self.lvl > 1:
            if player.job_id == self.job_id and player.lvl == self.lvl:
                return True
            else:
                return False
        if self.minEdu == 0 or self.minEdu == 1:
            return True
        elif self.minEdu == 2:
            if not isinstance(self.degree,list):
                self.degree = [self.degree]
            if player.degree in self.degree:
                return True
            else:
                return False
    def age_up(self,player):
        for item in self.coworkers:
            item.age_up()
        self.performance += (self.hours - self.minHours) / 10
        if self.performance > 1:
            self.performance = 1
        if self.performance < 0:
            self.performance = 0
        self.promoBase -= 1
        self.work_e += 1
        player.work_e += 1
        if self.performance == 1:
            self.work_e += 1
        if self.promoBase <= 0 and self.promoteCheck():
            self.promote(player)
        salary = int((self.pay * self.hours * 52) * player.nation.incomeTax)
        player.money += self.pay * self.hours * 52
    def __str__(self):
        return f"{self.name} [£{self.pay}/hr] [{self.hours} Hours/Week]"
class Player(Base):
    ## This is the main player class.
    ## It is instantiated when the game creates a life, and is pickled when the game saves or loads.
    ## Its attrubutes are statistics that are kept by the game, as well as objects pertaining to the player, such as owned vehicles and such.
    def __init__(self):
        self.version = [0, 1, 0]
        self.stressMode = False
        self.backup = []
        self.dic={}
        self.funds = [
            IndexFund("S&P 500"),
            IndexFund("Dow Jones Industrial Average"),
            IndexFund("GTK Technology Fund"),
            IndexFund("GTK Hospitality Fund"),
            IndexFund("GTK Finance Fund"),
            IndexFund("GTK Automotive Fund"),
            IndexFund("GTK Videogame Fund"),
            IndexFund("GTK Aerospace Fund"),
            ]
        self.stocks = [
            Stock("OpenMotors","OPMM",15,45),
            Stock("Airfruit Inc.","AIRF",175),
            Stock("Nanosoft Corp","NSFT",330),
            Stock("Woogle","WOOG",125),
            Stock("Rainforest Industries","RFST",120),
            Stock("Boing Airspace","BNGA",747),
            Stock("Airbuss","ABUS",320),
            Stock("Doppelsieg Motorworks","DPSG",55),
            Stock("OpenLife Studios","OPEN",69,10),
            Stock("Candywriter LLC","CNDY",45,90),
            ]
        self.lotteryWins=0
        self.behaviour = 0.0
        self.pension = 0
        self.hasDonate = False
        self.droppedOut = False
        self.reassigned = False
        self.version = ["0", "1", "pre1x2"]
        self.forename, self.surname = "John", "Smith"
        self.job = None
        self.grades = rng(1,100)/100
        self.metals = [
            Metal("Gold",17000,-20,20),
            Metal("Silver",23,-10,25),
            Metal("Copper",5,-65,455,65),
            Metal("Palladium",2200,-55,10),
            Metal("Platinum",3500,-25,35)
            ]
        if prefs["allowDebug"] == True:
            self.cheater = Fuse()
            self.cheater.blow()
        else:
            self.cheater = Fuse()
        self.gender = 0
        self.age = 0
        self.surgeon = None
        self.freelance = {
            "tutor": False,
        }
        self.money = 0
        self.crypto = [
            Crypto("Xipple","XXP"),
            Crypto("Botcoin","BTC"),
            Crypto("ZephyrToken","ZPH"),
            Crypto("LuminaToken","LMT"),
            Crypto("QuantumBit","QBT"),
            Crypto("SolsticeToken","STK"),
            Crypto("NebulaCash","NBL"),
            Crypto("SecuCoin","VLT"),
            Crypto("OpenToken","OPN"),
            Crypto("Ethereal","ETL"),
            ]
        random.shuffle(self.crypto)
        self.crypto = self.crypto[3:]
        self.pregnant = False
        self.suable = []
        ### Stats values start

        self.happiness = 1.0
        self.health = 1.0
        self.intel = 1.0
        self.looks = 1.0
        self.ethics = 1
        self.casinoWinnings = 0
        self.criminalRecords = {}

        ### The stat values are in a range from 0 to 1, representing a %age.

        ### Stat values end
        self.work_e = 0
        self.edu_lvl = 0
        self.work_e_base = 0
        self.degree = 0
        self.work = {
            "hours": 0,
            "salary": 0,
            "partTimeSalary": 0,
            "pension": 0,
        }
        self.fertile = True
        self.disease = {
            "depression": False,
            "anxiety": False,
            "commonCold": False,
            "HBP": False,
            "Cancer": False,
            "postSSRI": False,
            "loneliness": False,
        }
        self.debt, self.savings = 0, 0
        self.current_research = [0,0]
        self.year = int(stime("%Y"))
        self.b_year = int(stime("%Y"))
        self.stress = 0.0
        self.job_id = 0  # Every job has a job ID, see {} for more info.
        self.job_lvl = 1
        self.parents = []  # Stores the player's parent objects.
        self.vehicles = [[], [], []]  # Cars / Boats / Planes
        self.spouse = None  # Stores spouse object
        self.friends = []
        self.houses = []
        self.exes = []
        self.addictions = {
                "gambling":False,
                "alcohol":False,
                "heroin":False,
                "cannabis":False,
                "morphine":False,
                "LSD":False,
                "cocaine":False,
                "MDMA":False,
            }
        self.years_addicted = 0
        self.children = []
        self.nation = choice(nations)
        self.fame = 0.0
        self.wpp = {
            "enrolled":False,
            "oldNames":[],
            }
        self.sentence = 0
        self.extra = None
        self.offences = []
        self.opentube = []  # All OpenTube channels contained here
        self.property = []
        self.inv = []  # Contains all items
        self.flip_profits = 0  # Total profit from selling houses
        self.lottery_wins = 0  # The amount of times you've won the lottery
        self.bonds = []
        self.licenses = {"car": False, "boat": False, "gun": False, "plane": False}
        self.lab = {}
        for item in researches:
            self.lab[item[0]] = False
        self.pending = [
            0,
            0,
        ]  # Pending Research ID / How many years to go for research : When [1] is 0, self.lab[self.pending[0]] is set to 1
        self.surgeons = []
        self.bandit = 0  # If you've robbed a train, it's set to 1
        self.expenses = 775  # Per month

        # Inheritance
        # The first value [index 0] refers to the inheritance type
        # types: 0 = charity / 1 = equal / 2 = spouse / 3 = child [needs second value]
        # The second is the [optional] person number, such as the child ID.
        self.will = [0, 0]
    def genderStr(self):
        return "male" if self.gender == 0 else "female"
    def doScenario(self):
        return None
        ## Child stage
        if self.age > 5 and self.age < 12:
            if pChance(50) and childScenarios != []:
                x=choice(childScenarios)
                x.run(self)
                childScenarios.remove(x)
    def calcFame(self):
        x=False
        if self.job_id in [6,9,13] and self.job_lvl == 3 or self.job_id in [21,28] and self.job.work_e >= 20:
            self.fame += 0.25
            x=True
        if not self.wpp["enrolled"]:
            self.fame += int(self.money/1000000)/100 if self.money >= 1000000 else 0
        if not x:
            self.fame -= rng(10,25)/100
        if self.fame > 1:
            self.fame = 1.0
        if self.fame < 0:
            self.fame = 0.0
    def calcNetWorth(self):
        nw = 0
        nw += self.money
        nw += self.savings
        nw -= self.debt
        for item in self.crypto:
            nw += int(item.investment * item.price)
        for item in self.bonds:
            nw += item.investment
        for item in self.funds:
            nw += int(item.investment)
        for item in self.metals:
            nw += int(item.investment * item.price)
        for item in self.stocks:
            nw += int(item.investment * item.price)
        
        for item in self.vehicles:
            for i in item:
                nw += i.value
        for item in self.property:
            if not item.mortgaged:
                nw += item.value
        for item in self.bonds:
            nw += item.investment
        return nw
    def prisonAge(self):
        self.backup.append(copy.deepcopy(self))
        while len(self.backup) > 20:
            self.backup.pop()
        self.age += 1
        if self.sentence < 255:
            self.sentence -= 1
        self.happiness -= 0.1
        if self.sentence == 0:
            cls()
            div()
            print("You have been released from prison.")
            br()
            for item in self.offences:
                item.served = True
            finishSentence(self)

    def calcStress(self):
        self.stress = 0
        if self.job:
            self.stress += self.job.hours / 100
        if self.happiness < 0.2:
            self.stress *= 2
        if self.stress > 1:
            self.stress = 1
        if self.stress < 0:
            self.stress = 0
        if self.stress > 0.7 and not self.disease["HBP"] and pChance(100/3):
            cls()
            div()
            print("You are now suffering from High Blood Pressure.")
            br()
            self.disease["HBP"] = True
        if self.stress < 0.4 and self.disease["HBP"] and pChance(100/3):
            cls()
            div()
            print("You are no longer suffering from High Blood Pressure.")
            br()
            self.disease["HBP"] = False
    def debug(self):
        ### Returns a debug log
        ### Debug logs are used for eliminating bugs by printing all values of the player object, as well as platform and config info.
        global version, app_version, sub_version
        log = ""

        log += "--------------------\n"
        log += "OpenLife Debug Log\n"
        log += f"LocalTime: {stime('%A %d %B %Y %H:%M:%S')}\n"
        log += "--------------------\n"
        log += f"LogVersion=7\n"
        log += f"GameVersion={app_version}\n"
        log += "--------------------\n"
        log += f"# Player Class\n"
        log += pprint_dict(obj_to_dict(self))
        log += f"\n\n# Preferences\n"
        log += pprint_dict(prefs)
        log += f"\n\n# SysConfig Information\n"
        try:
            import platform

            base = platform.system()
            base2 = platform.uname()[2]
            base3 = platform.architecture()
            base4 = platform.platform()
            base5 = platform.machine()
        except:
            base = "N/A"
            base2 = "N/A"
            base3 = "N/A"
            base4 = "N/A"
            base5 = "N/A"
        try:
            import tkinter as tk

            root = tk.Tk()
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            root.withdraw()
        except:
            screen_width = "N/A"
            screen_height = "N/A"
        try:
            v = platform.python_version()
            th = platform.architecture()
        except:
            v = "N/A"
            th = "N/A"
        cpu = platform.processor()
        log += f"Platform={base} {base2}\n"
        log += f"ScreenResolution={screen_width}x{screen_height}\n"
        log += f"PyVer={v}\n"
        log += f"Architecture={base3}\n"
        log += f"GeneralInfo={base4}\n"
        log += f"Machine={base5}\n"
        log += f"CPU={cpu}\n"
        log += f"#Achievements\n"
        log += pprint_dict(obj_to_dict(achievements))
        log += "\n\n## This log was generated using the OpenLife Log Creation Tool.\n"
        log += "## Tool (c) 2022-2023 WinFan3672, some rights reserved."
        return log

    def create(
        self,
        gender=0,
        forename="John",
        surname="Smith",
        age=18,
        happiness=1,
        health=1,
        intel=1,
        looks=1,
    ):
        self.backup = []
        self.nation = choice(nations)
        for item in nations:
            self.criminalRecords[item.id] = []
        ### Create parents
        mother = Parent()
        father = Parent()
        mother.create(rng(0, 1), surname)
        father.create(rng(0, 1), surname)
        self.parents = [mother, father]
        ### Create everything else
        self.happiness = happiness
        self.health = health
        self.intel = intel
        self.looks = looks
        self.forename, self.surname = forename, surname
        self.age = age
        from time import strftime

        self.year = strftime("%Y")
        self.b_year = int(self.year)
        self.b_year = int(self.b_year - age)
        self.biologicalGender = self.gender
        for i in range(rng(5,10)):
            x = Bond()
            x.maxInvestment = rng(5,250)*100000
            x.name=getBankName()
            typ = rng(1,3) # 1 = standard, 2 = safe, 3 = risky
            if typ == 1:
                x.mult = rng(110,125)/100
                x.defChance = rng(1,10)
            elif typ == 2:
                x.mult = rng(101,105)/100
                x.defChance = rng(1,10)
            else:
                x.mult = rng(110,150)/100
                x.defChance=rng(10,50)
            self.bonds.append(x)
        grantAchievement(self,"didBirth")
    def print_backup(self):
        print(f"Age:{self.age}|Money:{self.money}|Debt:{self.debt}")

    def age_up(self):
        # time machine
        self.backup.insert(0,copy.deepcopy(self))
        while len(self.backup) > 20:
            self.backup.pop()
        # age up
        self.doScenario()
        if self.sentence != 0:
            if rng(1, 3) == 1:
                cls()
                div()
                print("You were caught on the loose by the authorities!")
                print("You now face court judgement.")
                br(self.stressMode)
                self.offences.append(Offence("Felony Escape", self.sentence))
                goToPrison(self)
        self.calcStress()
        if self.surgeon:
            self.surgeon.age_up(self)
        if self.spouse:
            if rng(1,2) == 2:
                self.spouse.relation -= 0.08
            else:
                self.spouse.relation -= 0.12
            if self.spouse.relation <= 0.1:
                if rng(1,2):
                    cls()
                    div()
                    print(f"Your spouse mentioned how they want to separate with you.")
                    br()
        for item in self.metals:
            item.age_up(self)
        for item in self.stocks:
            item.age_up(self)
        self.money += self.pension
        for item in self.bonds:
            item.age_up(self)
        if self.current_research != Player().current_research:
            self.current_research[1] -= 1
            if self.current_research[1] == 0:
                cls()
                div()
                print("Research Complete.")
                if self.current_research[0] != "researchLab":
                    print("To take advantage of your research, go to Activities > My Lab.")
                else:
                    print("You can now begin performing research.")
                br()
                self.lab[self.current_research[0]] = True
                self.current_research = Player().current_research
        for item in self.property:
            item.age_up(self)
        for item in self.funds:
            item.age_up()
        for item in self.crypto:
            item.age_up(self)
        if self.job:
            self.job.age_up(self)
        if self.addictions != Player().addictions:
            exceptions = ["gambling","caffeine"]
            detc = 7
            mul = 1.05
            self.years_addicted += 1
            for item in self.addictions:
                if item:
                    mul += 0.005
                    if item not in exceptions:
                        detc -= 1
                    if detc < 3:
                        detc = 3
            self.expenses *= mul
            self.expenses=int(self.expenses)
            if rng(1,detc) == detc:
                x,y = self.addictions, Player().addictions
                for item in exceptions:
                    try:
                        del(x[item])
                    except:
                        pass
                    try:
                        del y[item]
                    except:
                        pass
                if x != y:
                    die(self,9)
        try:
            if self.backup[-1].addictions != self.addictions and self.addictions == Player().addictions:
                self.expenses = 775
        except:
            pass
        if self.age >= 18:
            self.money -= 12 * self.expenses
        if self.pregnant:
            cls()
            div()
            self.pregnant = False
            rng(1, 5)
            if rng != 5:
                c = Child()
                x = "boyfriend" if self.spouse.gender == 0 else "girlfriend"
                c.create(self)
                if self.gender == 1:
                    print("You gave birth to a child!")
                else:
                    print(f"Your {x} gave birth to a child!")
                print(f"Name: {c.name}")
                if c.gender == 0:
                    print("Male")
                else:
                    print("Female")
                self.children.append(c)
            else:
                if self.gender == 1:
                    print("You suffered a miscarriage and lost the baby!")
                else:
                    print(f"Your {x} suffered a miscarriage and lost the baby!")
            br(self.stressMode)
        self.freelance = Player().freelance
        for item in self.parents:
            item.age_up(self)
        self.happiness += rng(-10, 10) / 100
        self.health += rng(-10, 10) / 100
        self.intel += rng(-10, 10) / 100
        self.looks += rng(-10, 10) / 100
        if not self.disease["depression"] and self.happiness <= 0.25:
            cls()
            div()
            print("You are now suffering from Depression.")
            br()
            grantAchievement(self,"hasDepression")
            self.disease["depression"] = True
        if self.disease["depression"] and self.happiness >= 0.8:
            cls()
            div()
            print("You are no longer suffering from depression.")
            br(self.stressMode)
            self.disease["depression"] = False
        if self.disease["depression"]:
            self.happiness = (int((self.happiness * 100) / 3)) / 100

        self.hasDonate = False
        for item in self.surgeons:
            item.age_up()
        for item in self.parents:
            item.age_up(self)
        for item in self.vehicles:
            for i in item:
                i.age_up()
        for item in self.children:
            item.age_up()
        if rng(1, 3) == 1:
            if rng(1, 40) == 39:
                if self.disease["commonCold"] == False:
                    self.disease["commonCold"] = True
                    cls()
                    div()
                    print("You are now suffering from the Common Cold.")
                    br(self.stressMode)
            if rng(1,300) == 2:
                if not self.disease["Cancer"]:
                    self.disease["Cancer"] = True
                    self.happiness = 0
                    cls()
                    div()
                    print("You have been diagnosed with cancer!")
                    br()
        if self.spouse is not None:
            self.spouse.age_up()
        for item in self.opentube:
            item.age_up(self,self.stressMode)
        self.tutor = 0
        if rng(1, 400) == 4000:
            print("You were struck by lighting!")
            br(self.stressMode)
            if rng(1, 2) == 1:
                print("You survived.")
                br(self.stressMode)
                self.happiness, self.health, self.looks, self.intel = 1, 1, 1, 1
            else:
                print("You died.")
                br(self.stressMode)
                die(self, 6)
        self.age += 1
        if self.age == 18 and not self.droppedOut:
            self.edu_lvl = 1
        for item in self.vehicles:
            for i in item:
                i.age_up()
        self.year = 1 + int(self.year)
        self.money += self.work["salary"] * self.work["hours"]
        self.savings = int(self.savings * 1.1)
        self.debt = int(self.debt * 1.2)
        self.money -= int(self.debt / 10)
        if prefs["autoDeposit"] == True:
            self.savings += self.money
            self.money = 0
        if self.age >= 123 or self.age >= 100 and pChance(50) or self.age >= 90 and pChance(33) or self.age >=80 and pChance(5):
            die(self,1)
        x=self.fame
        self.calcFame()
        if x == 0.0 and self.fame > 0:
            Scenario("Fame","You are now famous!").run()
        if x > 0 and self.fame == 0.0:
            Scenario("Fame","You are no longer famous.").run()
        if prefs['autoDeposit']:
            self.savings += self.money
            self.money = 0
        if self.savings < 0:
            self.savings = 0
    def hasAdoptedAttr(self):
        m = self.parents[0]
        f = self.parents[1]
        if m.gender != f.gender:
            return True
        else:
            return False

class Ex(Person):
    pass
class Spouse(Person):
    def __init__(self, gender=0):
        super().__init__()
        self.lvl = 0
        self.fortune = weightedRNG(0,10000, 10000000)
        self.gender = gender

    def create(self, name, age, end, salary, hours):
        self.name = name
        self.age = age
        self.endAge = end
        self.salary = salary
        self.hours = hours
        self.relation = 0.5

    def interact(self, player):
        if self.relation > 1:
            self.relation = 1
        if self.relation < 0:
            self.relation = 0
        cls()
        div()
        print(self.name)
        if self.lvl == 1:
            if self.gender == 1:
                x = "wife"
            else:
                x = "husband"
        else:
            if self.gender == 1:
                x = "girlfriend"
            else:
                x = "boyfriend"
        if self.gender == 0:
            g="his"
        else:
            g="her"
        if self.lvl == 0:
            if self.gender == 1:
                print("Girlfriend")
            else:
                print("Boyfriend")
        else:
            if self.gender == 1:
                print("Wife")
            else:
                print("Husband")
        print(f"Age: {self.age}")
        print("Relation:" + pbar(self.relation) + f" {int(self.relation*100)}%")
        div()
        print("[1] Compliment")
        print("[2] Conversation")
        print("[3] Spend Time")
        if self.lvl == 0:
            print("[4] Break Up")
        else:
            print("[4] Divorce")
        print("[5] Insult")
        print("[6] Make Love")
        print("[x] Movies")
        if self.lvl == 0:
            print(f"[8] Marriage [{player.nation.currency}75,000]")
        else:
            print("[ ] Marriage")
        div()
        try:
            ch = int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print(f"You called your {x} {choice(compliments)}.")
            self.relation += 0.25
            if self.relation >= 0.75:
                print(f"Your {x} called you {choice(compliments)}.")
                player.happiness += 0.5
            br()
            self.interact(player)
        elif ch == 2:
            cls()
            div()
            z = rng(1, 4)
            print(f"You had a debate with your {x} about {choice(debates)}.")
            if z != 4:
                print("Agreement:")
                print(pbar(0.9))
                self.relation += 0.25
            else:
                print("Agreement:")
                print(pbar(0.05))
            br()
            if z == 4:
                cls()
                div()
                print("The argument turned into a shouting match.")
                self.relation -= 0.25
                div()
                print("[1] Agree to disagree")
                print(f"[2] Insult your {x}")
                print("[3] Apologise")
                div()
                try:
                    ch = int(input("$"))
                except:
                    return None
                if ch == 1:
                    self.relation += 0.2
                elif ch == 2:
                    self.relation -= 0.45
                elif ch == 3:
                    self.relation += 0.3
                else:
                    self.relation += 0.25
            self.interact(player)
        elif ch == 3:
            cls()
            div()
            print(f"You took your {x} {choice(spend_time)}.")
            br()
            self.interact(player)
        elif ch == 4:
            cls()
            div()
            if self.lvl == 0:
                print(f"You broke up with your {x}.")
            else:
                print(f"You divorced with your {x}.")
            br()
            if self.lvl == 1:
                cls()
                div()
                print(f"Due to your marriage agreement, your money is split 50/50 with your {x}.")
                print(f"You each get {player.nation.currency}{int((player.money+player.savings-player.debt)/2)}.")
                br()
                player.money += player.savings
                player.money -= player.debt
                player.savings = 0
                player.debt = 0
                player.money = int(player.money/2)
            player.spouse = None
        elif ch == 5:
            cls()
            div()
            print(f"You called your {x} {choice(insults)}.")
            self.relation -= 0.35
            br()
            self.interact(player)
        elif ch == 6:
            cls()
            div()
            if self.relation >= 0.5 or self.age > 70:
                print(f"You and your {x} made love.")
                if player.gender != self.gender and player.fertile:
                    player.pregnant = True
                    if self.gender == 1:
                        print(f"Your {x} is now pregnant.")
                    else:
                        print(f"You are now pregnant.")
            else:
                print(f"Your {x} does not want to make love.")
                if prefs["allowDebug"]:
                    print("[Debugging] Reasons:")
                    if self.age > 70:
                        print("Age")
                    if self.relation < 0.5:
                        print("Relations")

            br()
            self.interact(player)
        elif ch == 8 and self.lvl == 0:
            cls()
            div()
            print(f"You asked your {x} to marry you.")
            br()
            cls()
            div()
            if self.relation >= 0.75:
                print(f"Your {x} accepted your proposal!")
                br()
                self.relation += 0.25
            else:
                print(f"Your {x} rejected your proposal!")
                br()
                return None
            player.money -= 75000
            cls()
            div()
            print(f"You married your {x}.")
            if pChance(50):
                print(f"Your {x} chose to keep {g} surname.")
            else:
                n=self.name
                n=n.split(" ")
                n=n.pop(0)
                n=[n]
                n.append(player.surname)
                n=" ".join(n)
                self.name=n
                print(f"Your {x} changed {g} name to {self.name}!")
            br()
            self.lvl = 1
            player.money += self.fortune
            cls()
            div()
            print(f"You are now sharing assets with your {x}.")
            print("Assets:")
            print(f"{player.nation.currency}{'{:,}'.format(self.fortune)}")
            self.fortune=0
            br()
        else:
            return None

class Suable(Person):
    def sue(self, player, damages):
        cls()
        div()
        print(f"You successfully sued {self.name} for {player.nation.currency}{'{:,}'.format(damages)}!")
        br()
        player.money += damages
class Surgeon(Base):
    def __init__(self, name="John Smith", age=18, gender=0, rep=1):
        super().__init__()
        self.name = name
        self.age = 0
        self.end = 0
        self.rep = rep
        self.rep_base = self.rep
        self.rep_cap = rep + (rng(25, 75) / 100)
        if self.rep_cap > 1:
            self.rep_cap = 1
        self.gender = 0
        self.price = False
        self.facelift = False
        self.liposuction = False
        self.botox = False
        self.nose = False
        self.eyelid = False
        self.gender_specific = False
        self.reassignment = False
        self.can_sue = False
        self.fortune = 0
        self.years_served = 0
    def sue(self, player, damages):
        cls()
        div()
        print(f"You successfully sued your plastic surgeon, {self.name}!")
        self.fortune -= damages
        player.money += damages
        if self.fortune < 0:
            cls()
            div()
            print("Your plastic surgeon filed for bankruptcy.")
            br()
            cls()
            div()
            print("They can no longer serve you.")
            br()
            player.surgeon = None
    def age_up(self,player):
        player.money -= int(self.price)
        self.fortune += int(0.8*self.price)
        self.facelift = False
        self.liposuction = False
        self.botox = False
        self.nose = False
        self.eyelid = False
        self.gender_specific = False
        self.reassignment = False
        self.can_sue = False
    def list(self, no, will_choose = True):
        global allow_debug
        div()
        print(f"{self.name}")
        print(f"Age: {self.age}")
        div()
        print(f"Reputation:     {pbar(self.rep)}")
        if prefs['allowDebug']:
            print(f"BaseRep:        {pbar(self.rep_base)}")
        print(f"Max Reputation: {pbar(self.rep_cap)}")
        div()
        print(f"Price: {player.nation.currency}{'{:,}'.format(self.price)}/Yr.")
        div()
        if will_choose:
            print(f"[{no}] Hire")
        else:
            print(f"[{no}] Interact")
    def rep_down(self, player, amount):
        player.looks -= amount
        self.rep -= amount
        if self.rep < 0:
            self.rep = 0
    def rep_up(self,player, amount):
        self.rep += amount
        player.looks += amount
        self.rep_base += amount
        if self.rep > self.rep_cap:
            self.rep = self.rep_cap
        if self.rep_base > self.rep_cap:
            self.rep_base = self.rep_cap
        if self.rep > 1:
            self.rep=1
        if self.rep_base == 1:
            self.rep_base=1
    def chance(self):
        return pChance(self.rep_base * 100)
    def interact(self,player):
        cls()
        div()
        print(self.name)
        print("Age:",self.age)
        print(f"Reputation:     {pbar(self.rep)} {int(self.rep*100)}%")
        print(f"Max Reputation: {pbar(self.rep_cap)} {int(self.rep_cap*100)}%")
        div()
        print("[1] Facelift")
        print("[2] Liposuction")
        if not player.reassigned:
            print("[3] Gender Reassignment")
        else:
            print("[ ] Gender Reassignment")
        print("[4] Eyelid Surgery")
        print("[5] Nose Job")
        print("[x] Botox")
        if player.gender == 0:
            print("[7] Penis Enlargement Surgery")
        else:
            print("[7] Breast Augmentation")
        print("[8] Fire")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print("You had a facelift done.")
            br()
            cls()
            div()
            if self.chance():
                print("It was successful.")
                br()
                if not self.facelift:
                    self.rep_up(player, 0.25)
                    player.facelift = True
            else:
                print("It was botched!")
                br()
                self.rep_down(player, 0.25)
                self.can_sue=True
        elif ch == 2:
            cls()
            div()
            print("You had a liposuction done.")
            br()
            cls()
            div()
            if self.chance():
                print("It was successful.")
                br()
                if not self.liposuction:
                    self.rep_up(player, 0.25)
                    self.liposuction = True
            else:
                print("It was botched!")
                br()
                self.rep_down(player, 0.25)
                self.can_sue=True
        elif ch == 3 and not player.reassigned:
            cls()
            div()
            print("You had a gender reassignment surgery done.")
            br()
            cls()
            div()
            if self.chance():
                print("It was successful.")
                br()
                self.rep_up(player, 0.25)
                player.gender = 0 if player.gender == 1 else 1
                player.biologicalGender = 0 if player.biologicalGender == 1 else 1
                player.reassigned = True
            else:
                print("It was botched!")
                br()
                self.rep_down(player, 0.25)
                self.can_sue=True
                player.surgeon=None
                die(player,7)
        elif ch == 4:
            cls()
            div()
            print("You had an eyelid surgery done.")
            br()
            cls()
            div()
            if self.chance():
                print("It was successful.")
                br()
                if not self.eyelid:
                    self.rep_up(player, 0.25)
                    self.eyelid = True
            else:
                print("It was botched!")
                br()
                self.rep_down(player, 0.25)
                self.can_sue=True
        elif ch == 5:
            cls()
            div()
            print("You had a nose job done.")
            br()
            cls()
            div()
            if self.chance():
                print("It was successful.")
                br()
                if not self.nose:
                    self.rep_up(player, 0.25)
                    self.nose = True
            else:
                print("It was botched!")
                br()
                self.rep_down(player, 0.25)
                self.can_sue=True
        elif ch == 7:
            cls()
            div()
            if player.gender == 0:
                print(f"You had a {'penis enlargement' if player.gender == 0 else 'breast augmentation'} surgery done.")
            else:
                print()
            br()
            cls()
            div()
            if self.chance():
                print("It was successful.")
                br()
                if not self.gender_specific:
                    self.rep_up(player, 0.25)
                    self.gender_specific = True
            else:
                print("It was botched!")
                self.rep_down(player,0.25)
                br()
        elif ch == 8:
            cls()
            div()
            print(f"You fired {self.name}.")
            br()
            player.surgeon = None
        else:
            return None
def uniTest(player):
    for item in player.parents:
        if pChance(item.generosity * 100 + item.relation * 100):
            return True
    return False


class Parent(Base):
    # The parent class. Defines data for parents
    def __init__(self):
        self.name = None
        self.age = 0
        self.end = 0
        self.fortune = 0
        self.salary = 0

    def create(self, gender, surname):
        self.salary = rng(25, 55) * 1000
        self.age = rng(25, 45)
        self.end = rng(65, 85)
        self.gender = gender
        self.fortune = rng(0, 256) * rng(0, 100000)
        self.relation = rng(50, 100) / 100
        self.generosity = rng(1, 100) / 100
        if self.gender == 1:
            self.name = choice(forename_m) + " " + surname
        else:
            self.name = choice(forename_f) + " " + surname

    def getLines(self):
        if self.gender == 1:
            return f"My father is {self.name}, a {self.age}-year-old."
        else:
            return f"My mother is {self.name}, a {self.age}-year-old."

    def kill(self, player):
        cls()
        div()
        if self.gender == 1:
            print(f"Your father, {self.name}, died, aged {self.age}.")

        else:
            print(f"Your mother, {self.name}, died.")
        br()
        cls()
        div()
        print(f"You inherited {player.nation.currency}{Format(self.fortune)}.")
        br()
        player.money += self.fortune
        player.happiness = 0
        self.fortune = 0

    def display(self):
        if self.gender == 0:
            g = "Father"
        else:
            g = "Mother"
        return f"{self.name} ({g}) (Age {self.age})\n    {pbar(self.relation)} {int(self.relation*100)}%"

    def age_up(self, player):
        self.age += 1
        self.fortune = int(self.fortune * 1.01)
        self.fortune += self.salary
        if self.age == self.end:
            self.kill(player)

    def interact(self, player):
        if self.relation > 1:
            self.relation = 1
        if self.relation < 0:
            self.relation = 0
        if self.gender == 0:
            g = "father"
        else:
            g = "mother"
        cls()
        div()
        print(self.name)
        print("Age:", self.age)
        print("Relation:", pbar(self.relation), str(int(self.relation * 100)) + "%")
        div()
        print("[1] Compliment")
        print("[2] Conversation")
        print("[3] Ask For Money")
        print("[x] Give Gift...")
        print("[5] Spend Time With")
        print("[x] Give Money...")
        div()
        try:
            ch = int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print(f"You called your {g} {choice(compliments)}.")
            br()
            self.relation += 0.45
            self.interact(player)
        elif ch == 2:
            cls()
            div()
            print(f"You had a conversation with your {g} about {choice(debates)}.")
            br()
            self.relation += 0.45
            self.interact(player)
        elif ch == 3:
            cls()
            div()
            print(f"You asked your {g} for money.")
            br()
            cls()
            div()
            m = rng(0, 100)
            m *= 100*self.relation
            m=int(m)
            print(f"You got {player.nation.currency}{m}")
            br()
            player.money += m
            self.interact(player)
        elif ch == 5:
            cls()
            div()
            print(f"You took your {g} {choice(spend_time)}.")
            br()
            self.relation += 0.45
            self.interact(player)
        else:
            return None


import random
import tkinter as tk
from tkinter import messagebox


global nations
nations = [
    Nation("OpenLife",0,openTubeTaxMul=1,currency="£"),
    Nation("United Kingdom",1,currency="£",incomeTaxMul=0.95,houseTaxMul=0.85),
    Nation("United States of America",2,gunLicense=True,freeHealthcare=False,incomeTaxMul=0.95,houseTaxMul=0.85),
    Nation("China",3,False,False,19,True,freeHealthcare=False,incomeTaxMul=0.5,houseTaxMul=0),
    Nation("France",4,currency="€",freeHealthcare=False,incomeTaxMul=0.95,houseTaxMul=0.85),
    Nation("Germany",5,currency="€",canGamble=False,freeHealthcare=False,incomeTaxMul=0.95,houseTaxMul=0.85),
    Nation("Poland",6,currency="€",freeHealthcare=False,incomeTaxMul=0.9,houseTaxMul=0),
    Nation("Turkey",7,currency="€",freeHealthcare=False,canLottery=False),
    Nation("India",8,canGamble=False,incomeTaxMul=0.8,houseTaxMul=0.75),
    Nation("Sweden",9,currency="€",canGamble=False,incomeTaxMul=0.95,houseTaxMul=0.95),
    Nation("Norway",10,currency="€",incomeTaxMul=0.95,houseTaxMul=0.95),
    Nation("Denmark",11,currency="€",incomeTaxMul=0.95,houseTaxMul=0.95),
    Nation("UAE",12,incomeTaxMul=1,houseTaxMul=1,canGamble=False,canLottery=False),
    ]

def pChance(percent):
    if rng(1, 100) <= percent:
        return True
    else:
        return False


def pChanceTest(amount, percent):
    true = 0
    false = 0
    for i in range(amount):
        if pChance(percent):
            true += 1
        else:
            false += 1
    return true, false


import random
import time


def play_blackjack():
    # initialize deck
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4
    random.shuffle(deck)

    while True:
        # initialize player and dealer hands
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # keep track of player's score
        player_score = score_hand(player_hand)

        # player's turn
        while player_score < 21:
            print(f"Your hand: {player_hand}, Score: {player_score}")
            action = input("Do you want to hit (1) or stand (2)? ")
            if action == "1":
                new_card = deck.pop()
                print(f"You drew a {new_card}")
                player_hand.append(new_card)
                player_score = score_hand(player_hand)
                time.sleep(1)
            elif action == "2":
                break

        # determine outcome of player's turn
        if player_score > 21:
            print(f"Bust! Your score is {player_score}")
            return False
        else:
            # dealer's turn
            dealer_score = score_hand(dealer_hand)
            print(f"Dealer's hand: {dealer_hand}, Score: {dealer_score}")
            time.sleep(1)
            while dealer_score < 17:
                new_card = deck.pop()
                print(f"Dealer drew a {new_card}")
                dealer_hand.append(new_card)
                dealer_score = score_hand(dealer_hand)
                time.sleep(1)

            # determine outcome of game
            if dealer_score > 21:
                print(f"Dealer bust! Dealer's score is {dealer_score}")
                return True
            elif player_score > dealer_score:
                print(
                    f"You win! Your score is {player_score}, dealer's score is {dealer_score}"
                )
                return True
            elif player_score == dealer_score:
                print(
                    f"Draw! Your score is {player_score}, dealer's score is {dealer_score}"
                )
                continue  # restart the game
            else:
                print(
                    f"You lose! Your score is {player_score}, dealer's score is {dealer_score}"
                )
                return False


def score_hand(hand):
    score = 0
    aces = 0
    for card in hand:
        if card == "A":
            aces += 1
            score += 11
        elif card in ["K", "Q", "J"]:
            score += 10
        else:
            score += int(card)
    while aces > 0 and score > 21:
        score -= 10
        aces -= 1
    return score


def timeTravelMenu(player):
    cls()
    div()
    if len(player.backup) == 0:
        print("There are no snapshots to time travel to.")
        br()
        return None
    index = 1
    for item in player.backup:
        print(f"[{index}] Age: {item.age} | Money: {'{:,}'.format(item.money)}")
        index += 1
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    try:
        p = player.backup[ch - 1]
        player.backup = player.backup [ch:]
        while len(player.backup) > ch - 1:
            player.backup.pop()
        p.backup = player.backup
        main(upgradePlayer(p, False))
    except Exception as e:
        pass
global achievements, ACHIEVEMENTS
achievements = {
    "didBirth":Achievement("Fresh Meat","Greetings, OpenLivian!"),
    "cheater":Achievement("Cheater!","You cheated!"),
    "swiftLife":Achievement("Swift","Speedrun creating a life."),
    "doDeath":Achievement("RIP","Your family will miss you."),
##    "coldHearted":Achievement("Cold-Hearted","Kill someone."),
##    "hireHitman":Achievement("No Payne, No Gayne","Hire a hitman."),
##    "caughtHitman":Achievement("Wait, I was joking!","Get caught hiring a hitman."),
    "bff":Achievement("BFF","Make a friend."),
##    "bffl":Achievement("BFFL","Take your friendship to the next level."),
    "damnThatsFine":Achievement("Damn, That's Fine","Take your friendship to the NEXT level."),
    "freeEdu":Achievement("Free Education","Thanks, Mum!"),
    "hasDepression":Achievement("Stomach Upset","Not exactly at your happiest, are you?"),
    "unShackled":Achievement("Unshackled...","The secret to happiness is happiness..."),
    "notDisease":Achievement("Not A Disease","Get denied donating blood due to \"poor health\""),
    }
ACHIEVEMENTS = achievements
def mergeList(base, lst):
    set_lst = set(lst)
    merged_list = []
    for item in base:
        if item not in set_lst:
            merged_list.append(item)
    return merged_list
def mergeDict(a, b):
    result = a.copy()  # Create a copy of dictionary a
    
    for key, value in b.items():
        if key not in a:
            result[key] = value  # Add entries from b to result if key is not present in a
    
    return result
def saveAchievements(ach):
    with open("achievements.dat","wb") as f:
        pickle.dump(ach,f)
def loadAchievements():
    global achievements
    try:
        with open("achievements.dat","rb") as f:
            return mergeDict(pickle.load(f),ACHIEVEMENTS)
    except Exception as e:
        return e
def grantAchievement(player=Player(),achID=None):
    try:
        x=achievements[achID]
    except Exception as e:
        return e
    if player.cheater.blown or x.achieved:
        return None
    cls()
    div()
    print("Achievement earned!")
    x.achieve(player)
    achievements[achID]=x
    saveAchievements(achievements)
def achEarned(ach=achievements):
    z = 0
    for i in ach:
        if i != "version":
            if ach[i].achieved:
                z += 1
    return z
def listAchievements(ach=achievements):
    cls()
    div()
    x = []
    z = 0
    for item in ach.items():
        if item[0] != "version":
            x.append(item[1])
    for i in x:
        if i.achieved:
            z += 1
    saveAchievements(ach)
    print(f"{z}/{len(x)}")
    if z == 0:
        div()
        print("No achievements earned.")
        print("To earn achievements, play through the game.")
    for i in x:
        if i.achieved:
            div()
            print(i.title)
            div()
            print(i.desc)
            print(f"Earned: {i.date}")
    br()
    return z
def viewRibbons(player,reason):
    r = []
    if player.money >= 100000000:
        r.append("Rich")
    if player.debt > player.money + player.savings:
        r.append("Debt Slave")
    if player.lotteryWins >= 50:
        r.append("Cheater")
    if player.ethics == 0:
        r.append("Bad Karma King")
    if player.age >= 123:
        r.append("Geriatric")
    if player.intel <= 0.15:
        r.append("Stupid")
    if player.flip_profits >= 2000000:
        r.append("Flipper")
    if player.fame > 0:
        r.append("Famous")
    if player.intel >= 0.75:
        r.append("Nerd")
    if reason == 0:
        r.append("Wasteful")
    if player.age < 18:
        r.append("Unlucky")
    if player.bandit == 1:
        r.append("Bandit")
    if player.looks >= 0.75:
        r.append("Beautiful")
    if player.looks == 1 and player.intel == 1 and player.happiness == 1 and player.health == 1:
        r.append("Perfectionist")
    s=0
    for item in player.opentube:
        s += item.subscribers
    if s >= 1000000:
        r.append("Influencer")
    if player.disease["depression"]:
        r.append("Depressed")
    if player.disease["Cancer"]:
        r.append("Carcinogenic")
    aax = 0
    for item in player.addictions:
        if item == True:
            aax += 1
    if aax >= 3:
        r.append("Addicted")
    if reason == 9:
        r.append("Overdosed")
    if r == []:
        r.append("Mediocre")
    cls()
    div()
    for item in r:
        print(f"Ribbon: {item}")
    br()
def die(player, reason,subreason=-1):
    grantAchievement(player,"doDeath")
    if player.lab['isImmortal'] and not reason in [0]:
        cls()
        div()
        print("You felt a jolt as your vision shot up.")
        br()
        cls()
        div()
        print("You saw your limp body lie on the floor.")
        br()
        cls()
        div()
        print("As soon as you begin panicking, you are back inside your body.")
        print("You realise you'd nearly died.")
        print("Thankfully, you are immortal.")
        br()
        main(player)
    if player.stressMode:
        div()
        print(f"Death {reason}")
        div()
        return None
    if player.wpp["enrolled"] and reason != 10 and subreason == -1:
        die(player,10,reason)
    if reason == 10:
        nn=f"{player.wpp['oldNames'][0]} {player.wpp['oldNames'][1]}"
    n = f"{player.forename} {player.surname}"
    cls()
    div()
    print("OpenLife Times")
    print("The *best* newspaper since 2022 AD")
    div()
    if reason == 0:
        print(f"{player.forename} {player.surname} surrenders, aged {player.age}")
        div()
        print(
            f"{player.forename} {player.surname} surrendered themselves last night by throwing themselves off a bridge."
        )
        print(f"Their body was found floating in a nearby river last night.")
        print(
            f"Autopsies suggest that this was deliberate, as their neck has rope marks, suggesting an attempted hanging."
        )
        print(
            f"This has caused shock in their local community as friends and family refuse to believe that {player.surname} did this."
        )
        print(f"They will be missed.")
        div()
        print(
            "Game dev notice: If you are thinking of ending your life, please don't. Your situation *will* get better. I would know, having been in a similar position before. Don't give up."
        )
    elif reason == 1:
        print(f"{player.forename} {player.surname} dies of old age, aged {player.age}")
        div()
        print(
            f"{player.forename} {player.surname} has passed away in their sleep, of old age."
        )
        print(
            f"They lived a long and happy life surrounded by loved ones and will be dearly missed."
        )
    elif reason == 2:
        print(
            f"{player.forename} {player.surname} dies of heart attack, aged {player.age}"
        )
        div()
        print(
            f"Last night, {player.forename} {player.surname} collapsed onto the floor, suffering a massive heart attack."
        )
        print(f"They were rushed to a hospital, and were unable to be revived.")
        print(
            f"Family members and close friends noted that they were undergoing extreme stress."
        )
        print(
            f"Medical records show a disgnosis of High Blood Pressure a few years ago."
        )
        print(
            f"If you have high blood pressure, or heart disease, or anything similar, we implore you not to stress your cardiovascular system too much."
        )
    elif reason == 3:
        print(f"{player.forename} {player.surname} dies of cancer, aged {player.age}")
        div()
        print(f"{player.forename} {player.surname} has died of Stage IV cancer.")
        print(f"They battled with it for several years, until their body gave in.")
    elif reason == 4:
        print(
            f"{player.forename} {player.surname}, age {player.age}, collapses onto floor and dies"
        )
        div()
        print(
            f"Last night, {player.forename} {player.surname} reportedly collapsed onto the floor and fell down the stairs of their home."
        )
        print(
            f"They were rushed to the local hospital, where they died of multiple organ failure."
        )
        print(
            f'An autopsy suggests that their health was extremely poor and that their fate was "inevitable".'
        )
    elif reason == 5:
        pass
    elif reason == 6:
        print(
            f"{player.forename} {player.surname} killed by burns and shock lightning strike"
        )
        div()
        print(
            f"Last night, at 11:47PM, a lightning bolt struck {player.forename}'s body, causing them to immediately pass out."
        )
        print(
            f"The heavy rain as well as the shock from the fourth-degree burns received caused them to die soon after."
        )
        print(f"Their burned remains were unsuitable for autopsy.")
    elif reason == 7:
        print(f"{player.forename} {player.surname} killed by botched plastic surgery")
        div()
        print(f"Last night, {player.surgeon.name} attempted to perform a gender reassignment surgery.")
        print(f"Unfortunately, it did not go to plan. His customer, {player.forename} {player.surname}, died due to")
        print(f"Multiple Organ Failure [MOF]. {player.surgeon.name}'s actions were unprofessional, and it is unlikely that {'he' if player.surgeon.gender == 0 else 'she'} will find new clients ever again.")
    elif reason == 8:
        print(f"{player.forename} {player.surname} dies at hands of witch-doctor")
        div()
        print(f"The local witch-doctor has allegedly poisoned a local civilian.")
        print(
            f"The civilian in question, {player.forename} {player.surname}, aged {player.age}, was given an ointment to treat an ailment."
        )
        print(f"This treatment immediately killed them.")
        print(
            f"The witch-doctor in question pled not guilty to 1st-degree murder and was charged for 1st-degree manslaughter, and was sentenced to 35 years in prison."
        )
        print(f"This is a punishment more severe than 1st-degree murder.")
    elif reason == 9:
        print(f"{n} dies of drug overdose")
        div()
        print(
            f"{n} was found lying dead on the pavement with a needle in their hand last night."
        )
        print(
            f"The drug has not been identified because it was consumed in its entirety."
        )
        print(f"They will be buried next week.")
    elif reason == 10:
        print(f"{nn} Faked Death As {n}, Dies Aged {player.age}")
        div()
        print(f"Some years back, fans mourned the death of {nn}.")
        print(f"Last night, the FBI revealed through a press release that they had entered the Witness Protection Program,")
        print(f"and had died last week.")
        print(f"Their alias identity, {n}, was revealed as well.")
        print(f"The FBI did not state the reason for this decision.")
        print(f"A cause of death was also not provided, but will be soon.")
        div()
        print(f"The funeral procession will start next week.")
        print(f"Conspiracy theories around the world rejoice as they are proven right for the first time ever,")
        print(f"Rumours and reported sightings have been floating around for years, but no concrete proof had been released until now.")
        br()
        die(player,subreason,0)
    div()
    print("[1] Main Menu")
    if player.age < 130:
        if player.cheater.blown:
            print("[2] Respawn")
        else:
            print("[2] Respawn [Disables Achievements]")
    print("[3] Time Travel")
    print("[4] View Ribbons")
    div()
    try:
        ch = int(input("$"))
    except:
        die(player, reason)
    if ch == 1:
        cls()
        div()
        print("Are you sure?")
        print("This will remove all unsaved progress.")
        div()
        print("[1] Confirm")
        print("[0] Go Back")
        div()
        try:
            ch=int(input("$"))
        except:
            ch=0
        if ch == 1:
            mainMenu()
        else:
            die(player,reason)
    elif ch == 2:
        if not player.cheater.blown:
            cls()
            div()
            print("Are you sure?")
            print("This will disable achievements!")
            div()
            print("[1] Confirm")
            print("[0] Go Back")
            div()
            try:
                ch=int(input("$"))
            except:
                ch=0
        if ch == 1 or player.cheater.blown:
            cls()
            div()
            print("You found yourself lying on a hard, metal bed in the middle of an operating theatre.")
            print("The confused doctors let you go, saying you had apparently just risen from the dead.")
            br()
            player.cheater.blow()
            main(player)
        else:
            die(player, reason)
    elif ch == 3:
        timeTravelMenu(player)
        die(player, reason)
    elif ch == 4:
        viewRibbons(player,reason)
        die(player,reason)
    else:
        die(player, reason)


def play_minesweeper(num_rows=10, num_cols=10, num_mines=10):
    if prefs["allowDebug"] == True:
        return True

    # Define a callback function to close the window and set the result
    def end_game(win):
        global result
        result = None
        result = win
        root.destroy()

    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root, num_rows=num_rows, num_cols=num_cols, num_mines=num_mines)
    root.protocol("WM_DELETE_WINDOW", lambda: end_game(None))
    root.mainloop()

    # check if all non-mine cells are uncovered
    for i in range(game.num_rows):
        for j in range(game.num_cols):
            if not game.uncovered[i][j] and game.board[i][j] != "X":
                # player has not uncovered all non-mine cells
                return False

    # player has uncovered all non-mine cells
    return True


class Minesweeper:
    def __init__(self, master, num_rows=10, num_cols=10, num_mines=10):
        self.master = master
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.num_mines = num_mines
        self.board = self.generate_board()
        self.uncovered = [
            [False for _ in range(self.num_cols)] for _ in range(self.num_rows)
        ]

        # create buttons for each cell
        self.buttons = []
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                button = tk.Button(
                    master,
                    text="-",
                    width=2,
                    fg="black",
                    command=lambda i=i, j=j: self.handle_click(i, j),
                )
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def generate_board(self):
        """
        Generates a Minesweeper board with the specified number of rows, columns,
        and mines.
        """
        # create empty board
        board = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]

        # place mines randomly
        mine_locations = random.sample(
            range(self.num_rows * self.num_cols), self.num_mines
        )
        for loc in mine_locations:
            row = loc // self.num_cols
            col = loc % self.num_cols
            board[row][col] = "X"

        # fill in the numbers
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if board[i][j] != "X":
                    # count the number of adjacent mines
                    count = 0
                    for x in range(max(0, i - 1), min(self.num_rows, i + 2)):
                        for y in range(max(0, j - 1), min(self.num_cols, j + 2)):
                            if board[x][y] == "X":
                                count += 1
                    board[i][j] = count

        return board

    def handle_click(self, row, col):
        """
        Handles a button click.
        """
        if self.board[row][col] == "X":
            # player loses
            self.buttons[row][col].config(text="X", state="disabled")
            messagebox.showinfo("Game Over", "You clicked on a mine. Game over!")
            self.master.after(1000, lambda: self.master.destroy())
        else:
            # reveal the square
            self.uncovered[row][col] = True
            self.buttons[row][col].config(text=self.board[row][col], state="disabled")
            if self.board[row][col] == 0:
                # recursively uncover adjacent squares if this square is blank
                for i in range(max(0, row - 1), min(self.num_rows, row + 2)):
                    for j in range(max(0, col - 1), min(self.num_cols, col + 2)):
                        if not self.uncovered[i][j]:
                            self.handle_click(i, j)

global childScenarios
childScenarios = [
            Scenario("Vaccination","Your parents took you to get vaccinated.\nWhat do you do?",[["Stay Calm",None],["Bite The Doctor",None]]),
    ]
def clear_variables():
    exceptions = [
        "Player",
        "stime",
        "obj_to_dict",
        "list2Dict",
        "pprint_dict",
        "remove_functions",
        "get_user_classes",
        "inspect",
        "rng",
        "cls",
        "div",
        "br",
        "uname",
        "sys",
        "os",
        "Parent",
        "Blank",
        "Minesweeper",
        "play_minesweeper",
        "tk",
        "random",
        "messagebox",
        "prefs",
    ]
    if prefs["allowDebug"] == False:
        exceptions = ["div"]
    ## Deletes all variables in game
    ## Essentially nuking it :o
    user_vars = [var for var in globals() if not var.startswith("__")]
    for var in user_vars:
        if var not in exceptions:
            del globals()[var]


def pprint_dict(dic):
    ## Takes a dictionary and returns it as a string with indentation
    import json

    return json.dumps(dic, indent=4)


def list2Dict(lst):
    ## Takes a 2D list and converts it into a dictionary.
    ## Example Usage:

    ## lst = [["hello", "world"]]
    ## dictionary = list2Dict(lst)
    ## print(dictionary)  # Output: {"hello":"world"}

    dictionary = {}
    for sublst in lst:
        if len(sublst) == 2:
            key, value = sublst[0], sublst[1]
            dictionary[key] = value
    return dictionary


def remove_functions(dictionary):
    ## Takes a dict
    ## Removes all pairs in the dict where the value is callable
    return {k: v for k, v in dictionary.items() if not callable(v)}


def get_user_classes():
    import inspect, sys

    ## Returns a list of all user-defined classes in the current module.
    classes = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and obj.__module__ == __name__:
            classes.append(obj)
    return classes


import inspect
def representValue(string,value,modifier=0):
    x = f"{string}: "
    for i in range(modifier):
        x += " "
    x += f"{pbar(value)} {int(value*100)}%"
    return x
def obj_to_dict(obj,addItemType=True):
    """
    Recursively convert an object and all its attributes to a dictionary.
    """
    if isinstance(obj, (int, float, bool, str)):
        return obj
    if isinstance(obj,Fuse):
        return obj.blown
    if inspect.isclass(obj):
        return {"__class__": obj.__name__}

    if isinstance(obj, (tuple, list)):
        return [obj_to_dict(x) for x in obj]

    if isinstance(obj, dict):
        if addItemType:
            obj2 = {"@itemType":type({}).__name__}
        obj2.update(obj)
        obj = obj2
        return {key: obj_to_dict(value) for key, value in obj.items()}
    obj_dict = {}
    if addItemType:
        obj_dict["@itemType"] = type(obj).__name__
    for attr in dir(obj):
        if attr.startswith("__") and attr.endswith("__"):
            continue
        if attr == "dic":
            continue
        if attr == "extra" and getattr(obj,attr) != None:
            value = getattr(obj, attr)
            obj_dict["extra"] = f"<attribute value hidden: length={len(value)}>"
        if attr == "backup" and isinstance(obj, Player):
            value = getattr(obj, attr)
            obj_dict["backup"] = f"<attribute value hidden: length={len(value)}>"
            continue
        if getattr(obj, attr) is None:
            obj_dict[attr] = "<class 'none'>"
            continue
        if callable(getattr(obj, attr)):
            obj_dict[attr] = f"<function '{attr}'>"
            continue
        value = getattr(obj, attr)
        obj_dict[attr] = obj_to_dict(value)
    return obj_dict


def div():
    print(prefs['div'])
def br(skip=False):
    if not skip:
        div()
        input("Press ENTER to continue.")
    cls()


def pbar(percent):
    global alt_ui
    if percent > 1:
        percent = 1
    if percent < 0:
        percent = 0
    percent *= 100
    bar = "["
    hash = percent / 5
    global alt_ui
    hash = int(hash)
    dot = 20 - hash
    for i in range(hash):
        bar += "#"
    for i in range(dot):
        bar += " "
    bar += "]"
    return bar

def xPbar(min,max):
    print("\033[F",end="")
    print(f"{pbar(min/max)} [{min}/{max}]")
def saveGameBase(player, fn):
    import base64

    ## Backend of the save game mechanic
    with open(fn, "wb") as f:
        pickle.dump(player, f)
def subtractLists(a, b):
    return [elem for elem in a if elem not in b]
def rang(x, y):
    """
    Returns a range object from x to y
    Args:
    x: the minimum value
    y: the maximum value
    Returns:
    range object
    """
    return range(x, y+1)

def upgradePlayer(player, verbose=True):
    z = Player()
    z.create()
    diff = subtractLists(Player(), player)
    for item in player:
        try:
            x = getattr(player, item)
            y = getattr(z,item)
            if type(x) != type(y) and type(x) != type(None):
                diff.append(item)
        except Exception as e:
            pass
    for item in diff:
        d = getattr(z, item)
        setattr(player, item, d)
    if verbose:
        cls()
        div()
        print("Your save file has been upgraded to a newer format.")
        print("It should still work, however corruption may have occured.")
        print("Back up your old save, just in case.")
        br()
    return player


def loadGameBase(fn):
    import base64

    try:
        with open(fn, "rb") as f:
            d = pickle.load(f)
        try:
            if subtractLists(Player(), d) != []:
                return upgradePlayer(d)
            else:
                return d
        except Exception as e:
            return "Error: " + str(e)
    except Exception as e:
        return f"Error: {str(e)}"


def saveGame(player):
    l = []
    d = os.listdir(os.getcwd())
    for item in d:
        if item.endswith(".oll3"):
            l.append(item.replace(".oll3", ""))
        else:
            d.remove(item)
    div()
    print("Saves Taken")
    div()
    for item in l:
        print(item)
    div()
    fn = input("File Name $") + ".oll3"
    saveGameBase(player, fn)
    print("Saved to", fn.replace(".oll3", ""))
    return None


def godMenu(player):
    cls()
    div()
    print("God Menu")
    div()
    print("[x] Person Editor")
    print("Allows you to edit the attributes of a person")
    print("[x] Player Editor")
    print("Edit your own attributes.")
    print("[3] Event Forcer")
    print("Forces in-game events to occur.")
    print("[x] Scenario Creator")
    print(f"Create a custom scenario and call it.")
    print("[x] Path Forcer")
    print("Deletes all previous time travel locations.")
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    if ch == 1:
        return None
    elif ch == 3:
        cls()
        div()
        print("[1] Childhood Scenario")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            i = 1
            for item in childScenarios:
                print(f"[{i}] {item.title}")
                i += 1
            div()
            try:
                ch=int(input("$"))
                x=childScenarios[ch-1]
            except:
                return None
            x.run()
    else:
        return None
def statDict(player):
    return {
        "age":player.age,
        "happiness": player.happiness,
        "health": player.health,
        "ethics": player.ethics,
        "looks": player.looks,
        "intel": player.intel,
        "money": player.money,
        "debt":player.debt,
        "savings":player.savings,
        "expenses":player.expenses,
        "year":player.year,
        "birthYear":player.b_year,
        }
def stressTest(player,count=255,verbose=True):
    player.stressMode = True
    x = []
    s = len(pickle.dumps(player))
    t = time.time()
    o = statDict(player)
    y = {"0": {"size":s,"time":t,"stat":o}}
    for item in player.parents:
        item.age = item.end
        x.append(item)
    player.parents = x
    print("Begin stress test...")
    for i in rang(1,count):
        player.age_up()
        player = cleanTT(player)
        player.age -= 1
        player.year -= 1
        if verbose:
            xPbar(i,count)
        import sys, os, io
        if verbose:
            print("\033[F",end="")
        y[f"{i+1}"] = {"size":len(pickle.dumps(player)),"time":time.time(),"stat":statDict(player)}
    print("Stress test ended.")
    print("Check your OpenLife Saves folder for a file called \"stressTest.json\".")
    br()
    cls()
    s2 = len(pickle.dumps(player))
    t2 = time.time()
    y["reportFinal"] = {
        "preTime": t,
        "postTime": t2,
        "preSize": s,
        "postSize": s2,
        "diffSize": s2 - s,
        "diffTime": t2 - t,
    }
    import json
    with open("stressTest.json", "w") as f:
       json.dump(y,f)
    with open("stressTest.json","r") as f:
        x=json.load(f)
        x=pprint_dict(x)
    with open("stressTest.json", "w") as f:
        f.write(x)
    player.stressMode = False
def diff_dict(dict1, dict2):
    """
    Returns a dictionary containing the keys that are in one dictionary but not the other, along with their corresponding
    values.
    
    Parameters:
    dict1 (dict): The first dictionary to compare.
    dict2 (dict): The second dictionary to compare.
    
    Returns:
    dict: A dictionary containing the keys that are in one dictionary but not the other, along with their corresponding
    values.
    """
    result = {}
    for key in set(dict1.keys()) ^ set(dict2.keys()):
        if key in dict1:
            result[key] = dict1[key]
        else:
            result[key] = dict2[key]
    return result
def console(player, elev=0):
    if elev == 1:
        text = input("elev-console $")
    else:
        text = input("console $")
    if text == "exit":
        return None
    else:
        consoleBase(player,elev,text)
def consoleBase(player, elev, text):
    import json
    ch = text
    if text == "":
        console(player,elev)
    elif text == "elevate" or text == "elev":
        grantAchievement(player,"cheater")
        player.cheater.blow()
        elev=1
        console(player,elev)
    elif text == "help":
        div()
        print("help - this menu")
        print("echo <text> - prints <text> to the terminal")
        print("pref - shows saved preferences")
        print("dlog - Prints a debug log")
        print("save - Saves current life")
        print("load - loads a life (exits terminal)")
        print("cls - Clears console")
        print("stat - prints out all stats as a dictionary")
        print("nation - prints information about all nations")
        div()
        print("size - prints estimated size of save, in bytes")
        print("dump - dumps player object to JSON file")
        print("healthc - reports potentially broken attrubutes")
        print("compare - shows default state of missing attributes")
        print("healthd - shows default state of potentially broken attributes")
        print("pyclock - shows the \"clock speed\" of Python's operatin in hz")
        print("pybm - generates a JSON file that shows Python's \"clock speed\"(Takes 60s)")
        if elev == 1:
            print("balloon - inflates the save file size by filling it with junk data [USE AT OWN RISK]")
        div()
        print(
            "sv_cheats <0/1> - enables/disables cheats (warning: this disables achievements!)"
        )
        if elev == 1:
            div()
            print("god - enter the god menu")
            print("cdebt - clears debt")
            print("rich <int> - sets your money to <int>")
            print("max lab - maxxes out lab")
            print("max license - gives you all licenses")
            print("max stat - 100% for all stats")
            print("max addict - You gain all addictions")
            print("max job - allows you to get any job")
            print("forgive - Forgive prison sentence")
            print("sentence <int> - sets you to prison for <int> years")
            print("killp - forces your parents to die when you age up")
            print("age <age> - sets your age to <age>")
            print("sweep - opens a game of Minesweeper")
            if prefs["allowDebug"] == True:
                print("dgboff - disables debug mode")
            div()
            print("edu - lists all edu levels")
            print("edu <int> - set edu level to <int>")
            print("degree - lists all degrees")
            print("degree <int> - sets degree to <int>")
            print("makep - adds a freshly-generated parent")
            print("makes - adds a freshly-generated spouse")
            print("witch - gives you all diseases")
            print("unwitch - cures all diseases")
            div()
            print("depress - make your player depressed")
            print("faux - age up, then decrement your age")
            print("stress - perform a stress test (also creates a report file)")
            div()
        print("version - prints app/console version")
        print("exit - return to main screen")
        div()
        console(player, elev)
    elif text == "nation":
        pprint(nations)
        console(player,elev)
    elif text == "opentube":
        z=256
        o=OpenTube("")
        v = 0
        s = 0
        d = {}
        print("Calculating...")
        for i in range(z):
            xv,l=o.calcViews()
            o.subscribers = s
            v += xv
            s += o.calcSubs(xv,l)
            if s > 8000000000:
                s = 8000000000
            d[i] = {"viewsGained":xv,"totalViews":v,"subs":s}
            o.videoCount += 1
            if i % 10 == 0:
                xPbar(i,z)
        with open("openTube.json","w") as f:
            import json
            json.dump(d,f)
        div()
        print("Dumped to \"openTube.json\".")
        div()
        console(player,elev)
    elif text == "fund":
        fund=IndexFund("Console Fund")
        fund.investment = 1000
        z={}
        for i in range(256):
            z[i] = fund.investment
            fund.age_up()
        with open("fund.json","w") as f:
            json.dump(z,f)
        div()
        print("Dumped to \"fund.json\".")
        div()
        console(player,elev)
    elif text == "achid":
        for item in achievements:
            if item != "version":
                print([item,achievements[item].title,achievements[item].desc])
        console(player,elev)
    elif text.startswith("degree "):
        text = text[7:]
        try:
            text = int(text)
            if not text in range(len(degrees)):
                raise Exception
        except:
            print(f"Error: cannot set degree #{text}")
        player.edu_lvl = 2 if text != 0 else 1 
        player.degree = text
        console(player,elev)
    elif text == "degree":
        i = 0
        for item in degrees:
            print(f"{i} {item}")
            i += 1
        console(player,elev)
    elif text == "unichance":
        x = 0
        for item in player.parents:
            x += item.generosity * item.relation
        print(f"P: {x}")
        console(player,elev)
    elif text == "cargen":
        x = []
        for i in range(100000):
            x.append(Car())
        console(player,elev)
    elif text == "speedTest" and elev == 1:
        d={}
        l = [
            ["initPlayer",Player],["initChild",Child],["initParent",Parent],
            ["makePbar",lambda:pbar(1)],["cleanTT",lambda:cleanTT(player)]
            ]
        import time
        for item in l:
            x=time.time()
            y=item[1]()
            z=time.time()
            d[item[0]]=z-x
        pprint(d)
        console(player,elev)
    elif text == "max lab" and elev == 1:
        player.lab = invertDict(player.lab)
        console(player,elev)
    elif text == "inflate" and elev == 1:
        ascii_chars = "".join([chr(i) for i in range(128)])
        for i in range(2**16-1):
            c=""
            c2=""
            for x in rang(1,64):
                c+=choice(list(ascii_chars))
                c2+=choice(list(ascii_chars))
            player.dic[c] = c2
            if i % 1000 == 0 or i >= 2**16:
                xPbar(i,2**16-1)
        console(player,elev)
    elif text == "clean":
        player = cleanTT(player)
        player.extra=None
        console(player,elev)
    elif text == "max job" and elev == 1:
        player.job_lvl = -1
        console(player,elev)
    elif text == "witch" and elev == 1:
        player.disease = invertDict(Player().disease)
        console(player,elev)
    elif text == "unwitch" and elev == 1:
        player.disease = Player().disease
        console(player,elev)
    elif text == "pybm":
        z = {}
        z2 = []
        print("Starting Benchmark...")
        cls()
        for i in range(60):
            print("\033[F",end="")
            print(f"-->{i+1}/60<--")
            import time
            x = time.time()
            y = 0
            while time.time() - x < 1:
                y += 1
            z[i]=y
            z2.append(y)
        z3 = 0
        for item in z2:
            z3 += i
        z["average"] = z3 // 60
        print("Benchmark Finished.")
        import json
        with open("benchMark.json","w") as f:
            json.dump(z,f)
        console(player,elev)
    elif text == "balloon" and elev == 1:
        print("Begin operation...")
        try:
            del(player.extra.extra)
        except:
            pass
        if player.extra != None:
            print("Error: Already run operation.")
            console(player, elev)
        for i in range(256):
            print("\033[F",end="")
            print("-->"+str(i+1)+"/256<--")
            try:
                player.extra=obj_to_dict(player)
                try:
                    del(player.extra.extra)
                except:
                    pass
            except:
                pass
        print("Finished operation.")
        console(player,elev)
    elif text == "pyclock":
        import time
        x = time.time()
        y = 0
        while time.time() - x < 1:
            y += 1
        print("{:,}".format(y))
        console(player,elev)
    elif text == "makesue" and elev == 1:
        player.suable.append([Suable(),""])
        console(player, elev)
    elif text == "stress" and elev == 1:
        stressTest(player)
        console(player, elev)
    elif text == "forgive" and elev == 1:
        player.sentence = 0
        player.offences = []
        console(player,elev)
    elif text == "healthc":
        print(get_invalid_attributes(player))
        console(player,elev)
    elif text == "compare":
        x = obj_to_dict(player)
        y = obj_to_dict(Player())
        z = diff_dict(x,y)
        pprint(z)
        console(player,elev)
    elif text == "makech" and elev == 1:
        o=OpenTube("Console Test")
        o.monetised=True
        o.verified=True
        o.videoCount=1
        o.schedule=365
        player.opentube.append(o)
        console(player, elev)
    elif text == "healthd":
        x = obj_to_dict(player)
        y = get_invalid_attributes(player)
        z = {}
        for item in x:
            if item in y:
                z[item] = obj_to_dict(Player())[item]
        pprint(z)
        console(player,elev)
    elif text == "max license" and elev == 1:
        player.licenses = invertDict(Player().licenses)
        console(player,elev)
    elif text == "max addict" and elev == 1:
        player.addictions = invertDict(Player().addictions)
        console(player,elev)
    elif ch.startswith("stress ") and elev == 1:
        try:
            ch=int(ch[7:])
            stressTest(player,ch)
        except:
            pass
        console(player,elev)
    elif text == "size":
        print('{:,}'.format(len(pickle.dumps(player))))
        console(player, elev)
    elif text.startswith("sentence ") and elev == 1:
        player.offences.append(Offence("Game Cheating", int(ch[9:])))
        goToPrison(player)
        console(elev)
    elif text == "dump":
        import json
        x=obj_to_dict(player)
        x["platfomInformation"]=get_platform_info()
        with open("player.json","w") as f:
            json.dump(x,f)
        print("Dump successful.")
        print("To view, access the 'player.json' file in your save directory.")
        console(player,elev)
    elif text == "makec" and elev == 1:
        ch = Child()
        ch.create(player)
        player.children.append(ch)
        console(player, elev)
    elif text == "faux" and elev == 1:
        b = player.backup
        player.age_up()
        player.age -= 1
        player.backup = b
        console(player, elev)
    elif text == "makes" and elev == 1:
        sp = Spouse(1 if player.gender == 0 else 0)
        if player.gender == 0:
            sp.create(
                f"{choice(forename_f)} {choice(surnames)}",
                player.age,
                rng(65, 85),
                0,
                0,
            )
            sp.gender = 1
        else:
            sp.create(
                f"{choice(forename_m)} {choice(surnames)}",
                player.age,
                rng(65, 85),
                0,
                0,
            )
            sp.gender = 0
        player.spouse = sp
        console(player, elev)
    elif text == "god" and elev == 1:
        godMenu(player)
        console(player, elev)
    elif text == "makep" and elev == 1:
        pa = Parent()
        pa.create(rng(0, 1), player.surname)
        player.parents.append(pa)
        console(player, elev)
    elif text == "stat":
        pprint(statDict(player))
        console(player, elev)
    elif text == "depress" and elev == 1:
        player.disease["depression"] = True
        console(player, elev)
    elif text.startswith("jid "):
        ch = text[4:]
        try:
            player.job_id = int(ch)
        except:
            print("InvalidSyntax")
        console(player, elev)
    elif text.startswith("jlvl "):
        try:
            player.job_lvl = int(text[5:])
        except:
            print("InvalidSyntax")
        console(player, elev)
    elif text == "edu":
        print("0 - none")
        print("1 - high school")
        print("2 - degree")
        console(player, elev)
    elif text.startswith("edu "):
        try:
            text = int(text[4:])
            player.edu_lvl = text
        except:
            print("InvalidLVL")
        console(player, elev)
    elif text == "pref":
        print(pprint_dict(prefs))
        console(player, elev)
    elif text == "dbgoff":
        prefs["allowDebug"] = False
        console(player, elev)
    elif text == "sweep":
        print(play_minesweeper())
        console(player, elev)
    elif text == "killp" and elev == 1:
        m = player.parents[0]
        f = player.parents[1]
        m.end = m.age + 1
        f.end = f.age + 1
        player.parents = [m, f]
        console(player, elev)
    elif text == "dlog":
        print(player.debug())
        console(player, elev)
    elif ch == "max stat" and elev == 1:
        player.intel, player.looks, player.health, player.happiness, player.ethics = (
            1,
            1,
            1,
            1,
            0,
        )
        console(player, elev)
    elif text == "cdebt" and elev == 1:
        player.debt = 0
        console(player, elev)
    elif text.startswith("rich ") and elev == 1:
        ch = text[5:]
        try:
            player.money = int(ch)
        except:
            print("[ERROR] Invalid Val")
        console(player, elev)
    elif ch == "load":
        loadGame()
    elif text.startswith("echo "):
        print(text[5:])
        console(player, elev)
    elif text == "save":
        saveGame(player)
        console(player, elev)
    elif text == "cls":
        cls()
        console(player, elev)
    elif ch == "version":
        div()
        print(f"game {app_version[0]}.{app_version[1]}.{app_version[2]}")
        print("console 2.0.0")
        div()
        console(player, elev)
    elif ch == "sv_cheats 1":
        print("Warning! This will enable cheats.")
        print("Enabling cheats will disable achievements for the player.")
        print(
            'If you accept the consequences, type "I know what I am doing" into the terminal.'
        )
        ch = input("Confirm? $")
        if ch == "I know what I am doing":
            grantAchievement(player,"cheater")
            player.cheater.blow()
            console(player, 1)
        else:
            console(player)
    elif ch == "sv_cheats 0":
        print("[WARNING] Achievements will not be re-enabled.")
        console(player)
    elif ch.startswith("age ") and elev == 1:
        try:
            player.age = int(ch[4:])
        except Exception as e:
            print(str(e))
        console(player, elev)
    elif ch == "exit":
        return None
    else:
        print("InvalidConsoleCommandError: the Console Command is not valid.")
        console(player, elev)


def loadGame():
    cls()
    div()
    l = []
    d = os.listdir(os.getcwd())
    for item in d:
        if item.endswith(".oll3"):
            l.append(item.replace(".oll3", ""))
        else:
            d.remove(item)
    print("Saves:")
    for item in l:
        print(item)
    div()
    try:
        l = loadGameBase(input("Input $") + ".oll3")
    except Exception as e:
        cls()
        div()
        print(f"Error: {e}")
        br()

    if type(l) == str:
        print(l)
        br()
    else:
        main(l)

import random
def weightedRNG(a,b,c):
    """
    Has a 2/3 Chance of returning rng(a,b) and a 1/3 chance of rng(a,c)
    """
    if rng(1,3) != 3:
        return rng(a,b)
    else:
        return rng(a,c)
def generateFunctionTable(function, times, *args, **kwargs):
    """
Calls a function times times and returns a dict showing the values it returned and how many times
    """
    x = {"total":0}
    for i in range(times):
        y = function(*args, **kwargs)
        if y in x:
            x[y] += 1
        else:
            x[y] = 1
        x["total"] += 1
    return x
def generate_street_name():
    adjectives = ['Sunny', 'Cozy', 'Breezy', 'Green', 'Rustic', 'Charming', 'Vibrant', 'Peaceful', 'Tranquil', 'Quaint','Clearwater','Pinewood','Henderson',"Serene",
    "Vibrant",
    "Historic",
    "Charming",
    "Picturesque",
    "Quaint",
    "Bustling",
    "Majestic",
    "Lively",
    "Eclectic",
    "Tranquil",
    "Enchanting",
    "Colorful",
    "Elegant",
    "Scenic",
    "Captivating",
    "Cozy",
    "Artistic",
    "Romantic",
    "Whimsical"
]
    nouns = ['Grove', 'Hill', 'Lane', 'Avenue', 'Court', 'Boulevard', 'Way', 'Street', 'Road', 'Drive']
    return random.choice(adjectives) + ' ' + random.choice(nouns)
def adultPause(player):
    cls()
    div()
    print("[0] Resume")
    print("[1] Save Life")
    print("[2] Load Life")
    print("[3] Exit To Main Menu")
    div()
    print("[4] Download Challenge From Web")
    print("[5] Load Challenge From File")
    print("[6] Check For Updates")
    div()
    print("[7] Console")
    print("[8] Options")
    print("[9] Print Debug Log")
    print("[10] Create Debug Log")
    div()
    print(f"[14] Achievements [Earned: {achEarned(loadAchievements())}/{len(loadAchievements())}]")
    div()
    try:
        ch = int(input("$"))
    except:
        adult(player)
    if ch == 0:
        adult(player)
    elif ch == 1:
        saveGame(player)
        adultPause(player)
    elif ch == 2:
        loadGame()
    elif ch == 3:
        cls()
        div()
        print("[0] Return")
        print("[1] Exit & Save")
        print("[2] Exit Without Saving")
        div()
        try:
            ch = int(input("$"))
        except:
            adultPause(player)
        if ch == 1:
            saveGame(player)
            mainMenu()
        elif ch == 2:
            mainMenu()
        else:
            adultPause(player)
    elif ch == 4:
        cls()
        import urllib.request

        url = "https://winfan3672.000webhostapp.com/challenge/latest.zip"
        print("Downloading challenge...")
        try:
            urllib.request.urlretrieve(url, "challenge.zip")
        except:
            print("Failed to download challenge.")
            br()
            adultPause(player)
        print("Downloaded challenge.")
        br()
        adultPause(player)
    elif ch == 5:
        cls()
        div()
        print("Not Implemented Yet.")
        br()
        adultPause(player)
        pb = player  # backup of player
        player = doChallenge(player)
        if isinstance(player, Player):
            adultPause(pb)
        else:
            adultPause(player)
    elif ch == 6:
        cls()
        import urllib.request

        url = "http://winfan3672.000webhostapp.com/version_check/openlife.version"
        print("Checking for updates...")
        print(
            f"Current Version: {app_version[0]}.{app_version[1]}.{app_version[2]} [sub-version {sub_version}]"
        )
        try:
            urllib.request.urlretrieve(url, "openlife.version")
        except Exception as e:
            div()
            print("Failed to check for updates.")
            div()
            print("You could try:")
            print("[-] Checking that you are connected to the Internet.")
            print(
                "[-] Checking that winfan3672.000webhostapp.com is still up, since that is the server that provides the version check information."
            )
            print(f"[-] Checking that {url} exists, since it may have been deleted.")
            print(
                "[-] Checking that your antivirus or firewall is not blocking winfan3672.000webhostapp.com/"
            )
            print("[-] On Windows, deleting your DNS resolver cache.")
            div()
            print("Error for advanced users:", e)
            br()
            mainMenu()
        div()
        f = open("openlife.version", "r")
        data = f.read()
        data = data.split("|")
        data = [int(data[0]), int(data[1]), int(data[2])]
        d = [data[0],data[1]]
        av = [app_version[0], app_version[1]]
        not_update_text = f"An update for {game_name} [{data[0]}.{data[1]}.{data[2]}] is available.\nDownload it from:\nhttps://github.com/WinFan3672/OpenLife/releases/"
        if av <= d:
            print(not_update_text)
        else:
            print(f"You are on the latest version of {game_name}.")
        br()
        adultPause(player)
    elif ch == 7:
        cls()
        if prefs["allowDebug"] == False:
            console(player)
        else:
            console(player, 1)
        adultPause(player)
    elif ch == 8:
        savePrefs(editPrefs(prefs))
        adultPause(player)
    elif ch == 9:
        cls()
        print(player.debug())
        br()
        adultPause(player)
    elif ch == 10:
        d = player.debug()
        sn = ctime() + ".log"
        sn = sn.replace(":", "-")
        sn = sn.replace(" ", "_")
        with open(sn, "w") as f:
            f.write(d)
        div()
        print("Created log", sn)
        adultPause(player)
    elif ch == 11:
        listAchievements(achievements)
        adultPause(player)
    else:
        adult(player)

import json

def from_json_string(json_str):
    return json.loads(json_str)
def dict_to_obj(d, cls):
    obj = cls()
    for key, value in d.items():
        setattr(obj, key, value)
    return obj

def exportPlayer(player,filename):
    import marshal
    with open(filename,"wb") as f:
        marshal.dump(obj_to_dict(player),f)
def lifetimeStats(player):
    nw = player.calcNetWorth()
    print("Years Played:", player.age)
    div()
    print("Money Accrued")
    div()
    print("Money: $" + '{:,}'.format(player.money))
    print("Net Worth: $"+'{:,}'.format(nw))
    print("Total Debt: $" + '{:,}'.format(player.debt))
    print("Total Savings: $" + '{:,}'.format(player.savings))
    try:
        x = player.debt+1 / player.savings+1
    except:
        x = 0.0
    x *= 100
    x = int(x)
    x /= 100
    print(f"Debt:Savings Ratio: {x}")
    div()
    print("Money Outflow")
    div()
    print("Income: $" + (str(player.job.pay) if isinstance(player.job,Job) else "0")+"/Hr")
    print("Expenses: $" + str(player.expenses)+"/Month")
    if player.pension > 0:
        print(f"Yearly Pension: {player.nation.currency}{'{:,}'.format(player.pension)}")
    print("Yearly Wage: $"+('{:,}'.format(player.job.pay * player.job.hours * 52 + player.pension) if isinstance(player.job,Job) else "0"))
    if isinstance(player.job,Job):
        itax = player.job.pay * player.job.hours * 52
        itax *= 1 - player.nation.incomeTax
    else:
        itax = 0
    print(f"Income Tax: ${Format(itax)}")
    print("Yearly Expenses: $"+'{:,}'.format(player.expenses * 12))
    if isinstance(player.job,Job):
        x = player.job.pay * player.job.hours * 52
    else:
        x=player.pension
    print("Yearly Net Income: $"+'{:,}'.format(x-player.expenses*12))
    div()
    print("Tax Rates")
    div()
    print(f"Income Tax:           {int((1-player.nation.incomeTax) * 100)}%")
    print(f"House Sell Tax:       {int((1-player.nation.houseTax) * 100)}%")
    print(f"OpenTube Revenue Tax: {int((1-player.nation.opentube) * 100)}%")
def carDealership(player):
    cls()
    div()
    x = []
    for i in range(20):
        x.append(Car())
    i = 1
    for item in x:
        print(f"[{i}] {item.name} [{player.nation.currency}{'{:,}'.format(item.price)}]")
        i += 1
    div()
    try:
        ch=int(input("$"))
        y = x[ch-1]
    except:
        return None
    if player.money >= y.price:
        player.money -= y.price
    else:
        player.debt += y.price
    cls()
    div()
    print(f"You purchased a {y.name} for {player.nation.currency}{'{:,}'.format(y.price)}.")
    br()
    player.vehicles[0].append(y)
def boatDock(player):
    cls()
    div()
    x = []
    for i in range(10):
        x.append(Boat())
    i = 1
    for item in x:
        print(f"[{i}] {item.modelName} [{player.nation.currency}{'{:,}'.format(item.price)}]")
        i += 1
    div()
    try:
        ch=int(input("$"))
        y = x[ch-1]
    except:
        return None
    if player.money >= y.price:
        player.money -= y.price
    else:
        player.debt += y.price
    y.setName()
    cls()
    div()
    print(f"You are now the proud owner of {y.name}!")
    br()
    player.vehicles[1].append(y)
def planeHangar(player):
    cls()
    div()
    x=[]
    for i in range(15):
        x.append(Plane())
    i = 1
    for item in x:
        print(f"[{i}] {item.name} [{player.nation.currency}{'{:,}'.format(item.price)}]")
        i += 1
    div()
    try:
        ch=int(input("$"))
        y=x[ch-1]
    except:
        return None
    if player.money >= y.price:
        player.money -= y.price
    else:
        player.debt += y.price
    cls()
    div()
    print(f"You successfully purchased a {y.name}!")
    br()
    player.vehicles[2].append(y)
def carInteract(player):
    if player.vehicles[0] == []:
        return None
    cls()
    div()
    i = 1
    for item in player.vehicles[0]:
        print(f"[{i}] {item.name}")
        i += 1
    div()
    try:
        ch=int(input("$"))
        player.vehicles[0][ch-1].interact(player)
    except:
        return None
def boatInteract(player):
    if player.vehicles[1] == []:
        return None
    cls()
    div()
    i = 1
    for item in player.vehicles[1]:
        print(f"[{i}] {item.name}")
        i += 1
    div()
    try:
        ch=int(input("$"))
        player.vehicles[1][ch-1].interact(player)
    except:
        return None
def planeInteract(player):
    if player.vehicles[2] == []:
        return None
    cls()
    div()
    i = 1
    for item in player.vehicles[2]:
        print(f"[{i}] {item.name}")
        i += 1
    div()
    try:
        ch = int(input("$"))
        player.vehicles[2][ch-1].interact(player)
    except:
        return None
def buyHouse(player):
    x = []
    for i in range(15):
        x.append(House())
    i = 1
    div()
    for item in x:
        print(f"[{i}] {item.name} [{player.nation.currency}{'{:,}'.format(item.price)}]")
        i += 1
    div()
    try:
        ch=int(input("$"))
        y = x[ch-1]
    except:
        return None
    cls()
    div()
    if player.money >= y.price:
        player.money -= y.price
        print(f"You bought a {y.name}!")
    else:
        y.mortgaged = True
        y.mortgageValue = y.price
        print(f"You took out a mortgage for a {y.name}.")
    br()
    player.property.append(y)
def houseInteract(player):
    if player.property == []:
        return None
    cls()
    div()
    i = 1
    for item in player.property:
        print(f"[{i}] {item.name}{' [Mortgaged]' if item.mortgaged else ''}")
        i += 1
    div()
    try:
        ch=int(input("$"))
        player.property[ch-1].interact(player)
    except:
        return None
def bondInvest(player):
    cls()
    i = 1
    for item in player.bonds:
        div()
        print(f"[{i}] {item.name}")
        if item.investment > 0:
            print(f"Invested: {player.nation.currency}{Format(item.investment)}")
        print(f"Maximum Investment: {player.nation.currency}{'{:,}'.format(int(item.maxInvestment))}")
        print(f"Return: {int((item.mult-1)*100)}%")
        print(f"Risk: {pbar(item.defChance/100)} {item.defChance}%")
        i += 1
    div()
    try:
        ch=int(input("$"))
        x = player.bonds[ch-1]
    except:
        return None
    x.interact(player)
def cryptoMenu(player):
    cls()
    i = 1
    for item in player.crypto:
        div()
        print(f"[{i}] {item.name} [{item.symbol}]")
        print(f"Price: {player.nation.currency}{Format(item.price)}")
        print(f"1Y Price Change: {percentChange(item.lastPrice,item.price)}%")
        print(f"Holdings: {Format(item.investment)}{item.symbol}")
        print(f"Portfolio Value: {player.nation.currency}{Format(int(item.investment*item.price))}")
        i += 1
    div()
    try:
        ch=int(input("$"))
        player.crypto[ch-1].interact(player)
    except:
        return None
def metalMenu(player):
    cls()
    i = 1
    for item in player.metals:
        div()
        print(f"[{i}] {item.name}")
        print(f"Price: {player.nation.currency}{Format(item.price)}")
        if item.investment > 0:
            print(f"Holdings: {Format(self.investment)}")
        i += 1
    div()
    try:
        ch=int(input("$"))
        player.metals[ch-1].interact(player)
    except Exception as e:
        pass
def indexMenu(player):
    cls()
    i = 1
    for item in player.funds:
        div()
        print(f"[{i}] {item.name}")
        print(f"Invested: {player.nation.currency}{Format(item.investment)}")
        i += 1
    div()
    try:
        ch=int(input("$"))
        player.funds[ch-1].interact(player)
    except:
        pass
def stockMenu(player):
    cls()
    i = 1
    for item in player.stocks:
        div()
        print(f"[{i}] {item.name} [{item.symb}]")
        print(f"Price: {player.nation.currency}{Format(item.price)}")
        print(f"Owned: {Format(item.investment)}")
        i += 1
    div()
    try:
        ch=int(input("$"))
        player.stocks[ch-1].interact(player)
    except:
        pass
def investMenu(player):
    cls()
    div()
    print("[1] Stocks")
    print("[2] Bonds")
    print("[3] Crypto")
    print("[4] Metals")
    print("[5] Index Funds")
    print("[ ] Art")
    div()
    try:
        ch=int(input("$"))
    except:
        return None
    if ch == 1:
        stockMenu(player)
    elif ch == 2:
        bondInvest(player)
    elif ch == 3:
        cryptoMenu(player)
    elif ch == 4:
        metalMenu(player)
    elif ch == 5:
        indexMenu(player)
    else:
        return None
def adultAssets(player):
    cls()
    div()
    print(
        f"Money:           {player.nation.currency}" + str("{:,}".format((int(player.money))))
    )
    print(f"Debt:            {player.nation.currency}" + str("{:,}".format((int(player.debt)))))
    print(
        f"Savings:         {player.nation.currency}" + str("{:,}".format((int(player.savings))))
    )
    print(
        f"Flip Profits:    {player.nation.currency}"
        + str("{:,}".format((int(player.flip_profits))))
    )
    print(
        f"Casino Winnings: {player.nation.currency}{'{:,}'.format(player.casinoWinnings)}"
    )
    div()
    print("[0] Return")
    print("[1] Lifetime Stats")
##    print("[x] Shop")
    print("[3] Loan")
    print("[4] Savings")
##    div()
##    print("[x] Items")
    div()
    print("[6] Buy Houses")
    if len(player.property) > 0:
        print("[7] Owned Houses")
    else:
        print("[ ] Owned Houses")
    print("[8] Cars")
    if len(player.vehicles[0]) > 0:
        print("[9] Owned Cars")
    else:
        print("[ ] Owned Cars")
    print("[10] Planes")
    if len(player.vehicles[2]) > 0:
        print("[11] Owned Planes")
    else:
        print("[  ] Owned Planes")
    print("[12] Boats")
    if len(player.vehicles[1]) > 0:
        print("[13] Owned Boats")
    else:
        print("[  ] Owned Boats")
    print("[14] Investments")
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    if ch == 1:
        cls()
        div()
        lifetimeStats(player)
        br()
        adultAssets(player)
    elif ch == 3:
        cls()
        div()
        print(f"Debt: {player.nation.currency}" + str("{:,}".format((int(player.debt)))))
        print("20% interest, 10% autopaid per year")
        div()
        print("[1] Loan")
        print("[2] Pay Off")
        print("[0] Return")
        div()
        try:
            ch = int(input("$"))
        except:
            adult(player)
        if ch == 0:
            adult(player)
        elif ch == 1:
            cls()
            try:
                loan = int(input("Loan Amount $"))
            except:
                adult(player)
            if loan < 0:
                loan = 0
            player.debt += loan
            player.debt *= 1.2  # Adds interest on loan when you take it out.
            player.money += loan
            adult(player)
        elif ch == 2:
            if player.money < player.debt:
                player.debt -= player.money
                player.money = 0
                adult(player)
            else:
                player.money -= player.debt
                player.debt = 0
                adult(player)
        else:
            adult(player)
    elif ch == 4:
        cls()
        div()
        print(f"Money: {player.nation.currency}{'{:,}'.format(player.money)}")
        print(f"Savings: {player.nation.currency}{'{:,}'.format(player.savings)}")
        div()
        print("[1] Deposit")
        print("[2] Withdraw")
        print("[0] Back")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print(f"Money: {player.nation.currency}{'{:,}'.format(player.money)}")
            div()
            try:
                am = int(input("Deposit Amount $"))
            except:
                am=player.money
            if am > player.money or am > player.money:
                am = player.money
            if am < 0:
                am = 0
            player.savings += am
            player.money -= am
        elif ch == 2:
            cls()
            div()
            print(f"Savings: {player.nation.currency}{'{:,}'.format(player.savings)}")
            div()
            try:
                am=int(input("Withdraw Amount $"))
            except:
                am = player.savings
            if am > player.savings:
                am = player.savings
            if am < 0:
                am = 0
            player.savings -= am
            player.money += am
        else:
            return None
    elif ch == 6:
        buyHouse(player)
    elif ch == 7 and len(player.property) > 0:
        houseInteract(player)
    elif ch == 8:
        if not player.licenses["car"]:
            cls()
            div()
            print("The salesman refused to let you in when you failed to show a valid license.")
            br()
            return None
        carDealership(player)
    elif ch == 9 and len(player.vehicles[0]) > 0:
        carInteract(player)
    elif ch == 10:
        if not player.licenses["plane"]:
            cls()
            div()
            print("The salesman refused to let you in when you failed to show a valid license.")
            br()
            return None
        planeHangar(player)
    elif ch == 11 and len(player.vehicles[2]) > 0:
        planeInteract(player)
    elif ch == 12:
        if not player.licenses["boat"]:
            cls()
            div()
            print("The salesman refused to let you in when you failed to show a valid license.")
            br()
            return None
        boatDock(player)
    elif ch == 13 and len(player.vehicles[1]) > 0:
        boatInteract(player)
    elif ch == 14:
        investMenu(player)
    else:
        adult(player)


def lottery(player):
    cls()
    div()
    print("Lifetime Winning Tickets:",player.lotteryWins)
    div()
    print("How Many Tickets To Buy?")
    print("Can Afford:", str("{:,}".format(int(player.money / 100)) if player.money/100 >= 0 else 0))
    div()
    losses, wins, win_amount = 0, 0, 0
    try:
        ticket_count = int(input("$"))
    except:
        return None
    cls()
    price = ticket_count * 100
    try:
        for i in range(ticket_count):
            if player.money >= 100:
                player.money -= 100
            else:
                player.debt += 100
            chance = rng(1, 10000000)
            if chance == 2345:
                wins += 1
                base = wins + losses
                base /= ticket_count
                base *= 100
                print("\033[F",end="")
                print(f"You won! {pbar(losses/ticket_count)} [{str(int(base))}%]")
                wins += 1
                base = rng(250, 1000)
                base *= 1000000
                player.money += base
                win_amount += base
            else:
                losses += 1
        cls()
        div()
        print("Wins:", wins)
        print("Losses:", losses)
        print("Total Jackpot:", str("{:,}".format(win_amount)))
        player.lotteryWins += wins
        br()
    except Exception as e:
        print(str(e))
    except KeyboardInterrupt:
        pass


def robBank(player):
    success_table = [
        [0, 0, 0, 0, 0, 0],
        [50, 75, 95, 60, 70],
        [45, 85, 100, 70, 70],
        [50, 100, 100, 100, 80, 100],
        [100, 100, 100, 100, 100, 100],
        [75, 85, 85, 85, 85, 85],
        [25, 75, 75, 75, 75, 75],
    ]
    payout = rng(45000, 60000)
    cls()
    div()
    print("Select a disguise")
    div()
    print("[1] None")
    print("[2] Ski Mask")
    print("[3] Coloured Contact Lenses")
    print("[4] SCUBA Helmet")
    print("[5] Scream Mask")
    print("[6] Guy Fawkes Mask")
    print("[7] Mummy")
    print("[8] Policeman Outfit")
    print("[9] Darth Vader Costume")
    div()
    try:
        x = int(input("$"))
    except:
        return None
    cls()
    div()
    print("Select an escape method")
    div()
    print("[1] Foot")
    print("[2] Roller blades")
    print("[3] Car")
    print("[4] Subway")
    print("[5] Shopping Trolley")
    print("[6] E-Scooter")
    div()
    try:
        y = int(input("$"))
    except:
        return None
    if pChance(success_table[x - 1][y - 1]):
        cls()
        div()
        print("You successfully robbed the bank!")
        x = player.nation.currency
        y = "{:,}".format(payout)
        print(f"You got {x}{y}!")
        player.money += payout
        br()
    else:
        cls()
        div()
        print("You were caught robbing a bank!")
        print("You have been arrested by the authorities!")
        br()
        player.offences.append(Offence("Attempted Robbery", 5))
        goToPrison(player)


def adultCrime(player, ch=""):
    if ch == "":
        cls()
        div()
        print("[0] Return")
        print("[1] Bank Robbery")
        print("[x] Burglary")
        print("[3] Grand Theft Auto")
        print("[x] Hire Hitman")
        print("[x] Murder")
        print("[6] Pickpocket")
        print("[7] Shoplift")
        print("[8] Rob Train")
        div()
        try:
            ch = int(input("$"))
        except:
            return None
    if ch == 1:
        robBank(player)
    elif ch == 3:
        cls()
        div()
        x=[]
        for i in range(10):
            y=Car()
            y.stolen=True
            x.append(y)
        i = 1
        for item in x:
            print(f"[{i}] {item.name} [{player.nation.currency}{'{:,}'.format(item.price)}]")
            i += 1
        div()
        try:
            ch=int(input("$"))
            if pChance(50):
                cls()
                div()
                print(f"You stole the {x[ch-1].name} successfully!")
                br()
                player.vehicles[0].append(x[ch-1])
            else:
                cls()
                div()
                print(f"You were unable to steal the {x[ch-1].name}.")
                br()
                if pChance(20):
                    cls()
                    div()
                    print(f"A nearby policeman saw you attempt to rob a vehicle, and arrested you!")
                    br()
                    player.offences.append(Offence("Grand Theft Auto",7))
                    goToPrison(player)
        except:
            return None
    elif ch == 6:
        div()
        if rng(1, 5) != 5:
            amount = rng(10, 50)
            print(f"You stole ${amount}.")
            br()
            player.money += amount
        else:
            print("You stole nothing.")
            br()
        return None
    elif ch == 7:
        cls()
        div()
        if rng(1, 2) == 1:
            po = rng(45000, 100000)
            print(f"You went on a 'shopping spree' and stole {rng(45,55)} items!")
            br()
            print(f"You got a payout of {'{:,}'.format(po)}!")
            player.money += po
            br()
        else:
            print("You got caught trying to shoplift!")
            print("You will be sent to prison.")
            br()
            player.offences.append(Offence("Attempted Robbery", 5))
            player.offences.append(Offence("Attempted Shoplifting", 5))
            player.offences.append(Offence("Possession of an armed weapon", 7))
            goToPrison(player)
    elif ch == 8:
        cls()
        div()
        print("[1] Midnight")
        print("[2] 6AM")
        print("[3] Midday")
        print("[4] 6PM")
        div()
        try:
            ch = int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print("You tried boarding the midnight train.")
            br()
            x = time.strftime("%H%M")
            y = rng(10000000, 15000000)
            if x == "0000":
                cls()
                div()
                print("You robbed the train successfully!")
                print(f"You got {player.nation.currency}{'{:,}'.format(y)}")
                br()
                player.money += y
            else:
                cls()
                div()
                print("The train didn't show up.")
                br()
        elif ch == 2:
            cls()
            div()
            print("You tried boarding the 6AM train.")
            br()
            x = time.strftime("%H%M")
            y = rng(10000000, 15000000)
            if x == "0600":
                cls()
                div()
                print("You robbed the train successfully!")
                print(f"You got {player.nation.currency}{'{:,}'.format(y)}")
                br()
                player.money += y
            else:
                cls()
                div()
                print("The train didn't show up.")
                br()
        elif ch == 3:
            cls()
            div()
            print("You tried boarding the midday train.")
            br()
            x = time.strftime("%H%M")
            y = rng(10000000, 15000000)
            if x == "1200":
                cls()
                div()
                print("You robbed the train successfully!")
                print(f"You got {player.nation.currency}{'{:,}'.format(y)}")
                br()
                player.money += y
            else:
                cls()
                div()
                print("The train didn't show up.")
                br()
        elif ch == 4:
            cls()
            div()
            print("You tried boarding the 6PM train.")
            br()
            x = time.strftime("%H%M")
            y = rng(10000000, 15000000)
            if x == "1800":
                cls()
                div()
                print("You robbed the train successfully!")
                print(f"You got {player.nation.currency}{'{:,}'.format(y)}")
                br()
                player.money += y
            else:
                cls()
                div()
                print("The train didn't show up.")
                br()
        else:
            return None
    else:
        return None


def adultWill(player):
    div()
    print("[0] No Inheritance")
    print("[1] Child")
    print("[2] Spouse")
    print("[3] Divide Equally")
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    return None
def adoption(player):
    children = []
    for i in range(rng(5,9)):
        ch = Child(rng(0,12),rng(0,1),1)
        ch.giveName()
        children.append(ch)
    cls()
    div()
    print(f"Price: {player.nation.currency}5,000")
    div()
    i = 1
    for item in children:
        print(f"[{i}] {item.name}\n    Age: {item.age}\n    Gender: {'Male' if item.gender == 0 else 'Female'}")
        i += 1
        div()
    try:
        ch=int(input("$"))
        x = children[ch-1]
    except:
        return None
    player.money -= 5000
    player.children.append(x)
    cls()
    div()
    print(f"You are now the proud owner of {x.name}.")
    br()
def hireSurgeon(player):
    cls()
    l = []
    for i in range(3):
        g=rng(0,1)
        s = Surgeon()
        s.age=rng(45,55)
        s.rep=rng(1,100)/100
        s.rep_base = s.rep
        s.rep_cap = s.rep + 0.45 if s.rep + 0.45 < 1 else 1
        s.gender=g
        s.end=rng(65,85)
        s.price = s.rep * 1000000
        if g == 0:
            s.name = "Dr " + choice(forename_m) + " " + choice(surnames)
        else:
            s.name = "Dr " + choice(forename_f) + " " + choice(surnames)
        l.append(s)
    index = 1
    for item in l:
        item.list(index)
        index += 1
    div()
    try:
        ch=int(input("$"))
    except:
        return None
    try:
        player.surgeon = l[ch-1]
        cls()
        div()
        print(f"You hired {player.surgeon.name} as your surgeon.")
        br()
    except:
        pass
def hiredServices(player):
    div()
    print("[1] Plastic Surgeon")
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    if ch == 1:
        if player.surgeon == None:
            hireSurgeon(player)
        else:
            player.surgeon.interact(player)
    else:
        return None


def doctorMenu(player):
    cls()
    div()
    print("[x] Doctor")
    print("[2] Psychiatrist")
    print("[x] Alternate Medicine")
    print("[4] Donate Blood")
    print("[5] Donate Plasma")
    print("[6] Witch Doctor")
    if player.addictions != Player().addictions:
        print("[7] Rehab")
    else:
        print("[ ] Rehab")
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    if ch == 1:
        return None
    elif ch == 2:
        cls()
        div()
        print("You went to have your mental health analysed.")
        br()
        cls()
        div()
        if player.disease["depression"]:
            print("You were diagnosed with depression.")
        if player.disease["anxiety"]:
            print("You were diagnosed with anxiety.")
        if not player.disease["depression"] and not player.disease["anxiety"]:
            print("You were not diagnosed with anything and were let go.")
            br()
            return None
        div()
        if player.disease["depression"]:
            print("[1] Treat Depression")
        if player.disease["anxiety"]:
            print("[2] Treat Anxiety")
        div()
        try:
            ch = int(input("$"))
        except:
            return None
        if ch == 1 and player.disease["depression"]:
            cls()
            div()
            print("You were put on a course of antidepressants (SSRIs) for 2 weeks.")
            br()
            cls()
            div()
            chance = rng(1, 10)
            if chance == 1:
                print("You were cured of depression.")
                br()
                cls()
                div()
                if rng(1, 2) == 1:
                    player.disease["postSSRI"] = True
                if player.disease["anxiety"] and rng(1, 2) == 2:
                    print("You were also cured of anxiety.")
                    br()
                    cls()
                    div()
                    player.disease["anxiety"] = 0
                    player.happiness += 0.5
                player.disease["depression"] = False
                player.happiness += 0.5
            else:
                print("You continue to suffer from depression.")
                br()
                cls()
                div()
                if rng(1, 2) == 2 and not player.disease["anxiety"]:
                    player.disease["anxiety"] = True
                    print("You are now suffering from anxiety.")
                    br()
                    cls()
                    div()
        elif ch == 2 and player.disease["anxiety"]:
            cls()
            div()
            print(
                "You were assigned to a Cognitive Behavioural Therapy (CBT) specialist for 2 weeks."
            )
            br()
            cls()
            div()
            if rng(1, 3) != 1:
                print("You are no longer suffering from anxiety.")
                br()
                cls()
                div()
                player.disease["anxiety"] = False
                player.happiness += 0.5
            else:
                print("You continue to suffer from anxiety.")
                br()
                cls()
                div()
    elif ch == 4:
        cls()
        div()
        print("You went to donate blood.")
        print("The doctor performed a brief physical and mental examination.")
        br()
        div()
        if player.disease == Player().disease and player.hasDonate == False:
            pay = rng(75, 100)
            print("You donated blood.")
            print(f"You earned {player.nation.currency}{pay}")
            player.money += pay
            player.hasDonate = True
        elif player.hasDonate:
            print(
                "The doctor refused to take your blood because you had already donated recently."
            )
        else:
            print("The doctor does not want your blood due to your poor health.")
            br()
            if player.disease["depression"] or player.disease["anxiety"]:
                grantAchievement(player,"notDisease")
            return None
        br()
    elif ch == 5:
        div()
        print("You went to donate plasma.")
        print("The doctor performed a brief physical and mental examination.")
        if player.disease == Player().disease and player.hasDonate == False:
            pay = rng(25, 250)
            print("You donated plasma.")
            print(f"You earned {player.nation.currency}{pay}")
            player.money += pay
            player.hasDonate = True
        elif player.hasDonate:
            print(
                "The doctor refused to take your plasma because you had already donated recently."
            )
        else:
            print("The doctor does not want your plasma due to your poor health.")
    elif ch == 6:
        cls()
        div()
        print("You went to visit the witch doctor.")
        br()
        if rng(1, 10) == 10:
            die(player, 8)
    elif ch == 7 and player.addictions != Player().addictions:
        rehab(player)
    else:
        return None


def specialJobs(player):
    cls()
    div()
    print("[0] Return")
    print("[x] Musician")
    print("[x] Mafia")
    print("[x] Politics")
    print("[x] Local Gangs")
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    if ch == 1:
        return None
    else:
        return None


def freelanceWork(player):
    cls()
    div()
    print(f"[1] Tutor [{player.nation.currency}17/hr]")
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    if ch == 1:
        cls()
        div()
        if player.freelance["tutor"]:
            print("No-one accepted your offer.")
        else:
            print(f"You earned {player.nation.currency}{17*30} doing tutoring for 30 hours.")
            player.money += 17 * 30
            player.freelance["tutor"] = True
        br()
    else:
        return None
def giveJob(player,job):
    cls()
    div()
    print("You got the job!")
    div()
    print("Job:",job_roles[job.id][job.lvl-1])
    print(f"Pay: {player.nation.currency}{job.pay}/hr")
    print(f"Hours: {job.hours} Per Week")
    br()
    player.job = job
    player.job_id = job.id
    player.job_lvl = job.lvl
def uniMenu(player):
    cls()
    div()
    print("[1] Drop Out")
    print("[x] Faculty")
    print("[x] Students")
    print("[x] Extracurricular Activities")
    print("[x] Fraternities")
    div()
    try:
        ch=int(input("$"))
    except:
        return None
    if ch == 1:
        cls()
        div()
        player.degree = 0
        print("You dropped out of University.")
        br()
        main(player)
def university(player):
    cls()
    div()
    print(player.forename + " " + player.surname)
    print("Age:", player.age)
    print("Years To Go:",player.uniYears)
    div()
    print("Happiness:", pbar(player.happiness), str(int(player.happiness * 100)) + "%")
    print("Health:   ", pbar(player.health), str(int(player.health * 100)) + "%")
    print("Smarts:   ", pbar(player.intel), str(int(player.intel * 100)) + "%")
    print("Looks:    ", pbar(player.looks), str(int(player.looks * 100)) + "%")
    div()
    print("[1] University")
    print("[2] Assets and Stats")
    print("[3] Relationships")
    print("[0] Age Up")
    print("[ ] Activities")
    print("[ ] Pause Game")
    div()
    try:
        ch=int(input("$"))
    except:
        return None
    if ch == 1:
        uniMenu(player)
    elif ch == 2:
        adultAssets(player)
    elif ch == 3:
        adultRelations(player)
    elif ch == 0:
        player.age_up()
        player.uniYears -= 1
        if player.uniYears == 0:
            cls()
            div()
            print("You graduated from University.")
            br()
            player.edu_lvl = 2
            adult(player)
    university(player)
def goToUni(player,degree):
    player.degree=degree
    player.uniYears=3
    cls()
    div()
    university(player)
def payForUni(player,degree,canMoney=True,canParents=True):
    cls()
    div()
    print("How Will You Pay?")
    print(f"Price: {player.nation.currency}25,000")
    div()
    print("[0] Cancel")
    if canMoney:
        print("[1] Cash")
    if canParents:
        print("[2] Ask Parents To Pay")
    print("[3] Student Loan")
    div()
    try:
        ch=int(input("$"))
    except:
        return None
    if ch == 1 and canMoney:
        if player.money < 25000:
            cls()
            div()
            print("You cannot afford to pay the fee.")
            br()
            payForUni(player,degree,False,canParents)
        else:
            player.money -= 25000
            cls()
            div()
            print("You were accepted!")
            br()
            goToUni(player,degree)
    elif ch == 2 and canParents:
        i = 0
        for item in player.parents:
            if pChance(item.generosity * item.relation * 100) and item.fortune >= 25000:
                cls()
                div()
                print("Your parents agreed to pay!")
                br()
                player.parents[i].fortune -= 25000
                goToUni(player,degree)
            i += 1
        cls()
        div()
        print("Your parents refused to pay.")
        br()
        payForUni(player,degree,canMoney,False)
    elif ch == 3:
        cls()
        div()
        print("You took out a student loan.")
        br()
        player.debt += 25000
        goToUni(player,degree)
    elif ch == 0:
        return None
    else:
        payForUni(player.degree,canMoney,canParents)
def uniApplication(player):
    cls()
    div()
    i = 0
    for item in degrees:
        print(f"[{i}] {item}")
        i += 1
    div()
    try:
        ch=int(input("$"))
        if ch <= 0 or ch > len(degrees):
            raise Exception
    except:
        return None
    if pChance(player.intel*100):
        cls()
        div()
        print("You were accepted into University!")
        br()
        payForUni(player,ch)
    else:
        cls()
        div()
        print("You were not accepted into University.")
        br()
def jobInterview():
    interviews = [
        ["Which Harry Potter character do you relate to most?","Harry Potter","Dobby","Hagrid","Draco Malfoy",[2,3]],
        ["Tea or coffee?","Tea","Coffee","Both","Neither",[1,2]],
        ["Team Edward or Team Jacob?","Team Edward","Team Jacob","I don't care","What is that?",[1,2]],
        ["Do you prefer to call or text?","Call","Text","Either one's fine","I prefer to talk in person",[1,2]],
        ["What are your weaknesses?","Where do I start?","I'm a perfectionist","I feel horny at work","I don't have any",[2]],
        ["Any more questions?","When do I start?","What is the company culture like?","What is the pay?","How inclusive is the company?",[2,4]],
        ["What do you want to see in a workplace?","Collaboration","Cute female employees","Good Pay","Diversity",[1,4]]
        ]
    q = choice(interviews)
    cls()
    div()
    print("Job Interview")
    div()
    print(q[0])
    div()
    print("[1] "+q[1])
    print("[2] "+q[2])
    print("[3] "+q[3])
    print("[4] "+q[4])
    div()
    try:
        ch=int(input("$"))
    except:
        return False
    if ch in q[5]:
        return True
    else:
        return False
def getJob(player):
    jobs = [
        Job("Amazon Delivery Driver",1,1,5,40,0),
        Job("Jr Translator",2,1,10,40,2,15,40,60),
        Job("Jr Accountant",3,1,30,40,2,5),
        Job("Exorcist",4,1,10,40,0),
        Job("Jr Game Dev",6,1,40,40,2,3,45,50),
        Job("Jr Lawyer",8,1,60,40,2,32),
        Job("App Developer",9,1,45,40,2,3),
        Job("Jr Banker",10,1,45,40,2,[5,1,23]),
        Job("Monk",11,1,15,50,0),
        Job("Wedding Planner",12,1,25,40,0,0,35),
        Job("Engineer I",13,1,55,40,2,9,75,95),
        Job("Data Scientist",14,1,75,40,2,13),
        Job("Cashier",17,1,10,50,0),
        Job("College Lecturer",18,1,45,40,2,[22,23,19,20,21]),
        Job("Jr. Editor",20,1,25,50,2,[11,2],35,65),
        Job("Flight Attendant",22,1,25,40,0),
        Job("Apprentice Hairdresser",23,1,25,40,0,0,35),
        Job("Librarian",25,1,25,40,0),
        Job("Nun",26,1,10,40,0),
        Job("Stockbroker",29,1,45,40,2,[1,16,5]),
        Job("Social Media Manager",30,1,35,50,2,16,55,70)
        ]
    j = []
    j = sorted(j, key=lambda e: e.pay, reverse=True)
    for item in jobs:
        if item.check(player):
            j.append(item)
    cls()
    div()
    i = 1
    for item in j:
        print(f"[{i}] {item.__str__().replace('£',player.nation.currency)}")
        i += 1
    div()
    try:
        ch=int(input("$"))
    except:
        return None
    try:
        j = j[ch-1]
    except:
        return None
    if jobInterview():
        giveJob(player,j)
    else:
        cls()
        div()
        print("You were unable to secure the job.")
        br()
def eduMenu(player):
    cls()
    div()
    if player.edu_lvl == 0:
        print(f"[1] GED[{player.nation.currency}1,000]")
    elif player.edu_lvl == 1:
        print(f"[1] University [{player.nation.currency}25,000]")
    else:
        return None
    div()
    try:
        ch=int(input("$"))
    except:
        return None
    if ch == 1 and player.edu_lvl == 0:
        cls()
        div()
        print("You did your GED and now have secondary school qualifications.")
        br()
        player.money -= 1000
        player.edu_lvl = 1
    elif ch == 1 and player.edu_lvl == 1:
        uniApplication(player)
    else:
        return None
def adultOccupation(player):
    cls()
    div()
    print(f"Stress: {pbar(player.stress)} {int(player.stress*100)}%")
    div()
    print("[0] Return")
    print("[1] Education")
    if player.job:
        print("[2] Current Job")
    else:
        print("[ ] Current Job")
    print("[x] Part-Time Work")
    print("[4] Freelance Work")
    print("[5] Get Job...")
    print("[6] Special Careers")
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    if ch == 1:
        eduMenu(player)
    elif ch == 2 and player.job:
        player.job.interact(player)
    elif ch == 4:
        freelanceWork(player)
    elif ch == 5:
        getJob(player)
    elif ch == 6:
        specialJobs(player)
    else:
        return None

def finishSentence(player):
    for item in player.offences:
        item.served = True
    adult(player)
def prisonMenu(player):
    if player.behaviour > 1:
        player.behaviour = 1
    if player.behaviour < 0:
        player.behaviour = 0
    cls()
    div()
    if player.sentence > 255:
        print("Sentence: Life")
    else:
        print("Sentence:", player.sentence, "Years")
    print(f"Behaviour: {pbar(player.behaviour)} {int(player.behaviour*100)}%")
    div()
    if not player.hasAppeal:
        print("[1] Appeal Sentence")
    else:
        print("[ ] Appeal Sentence")
    print("[2] Meditate")
    print("[3] Escape [25% chance]")
    print("[4] Start Riot [50% chance]")
    print("[5] Surrender")
    if player.sentence > 255:
        x = 2500000
    else:
        x = 45000*player.sentence
    print(f"[6] Bail Out [{player.nation.currency}{'{:,}'.format(x)}]")
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    if ch == 1:
        cls()
        div()
        print("You appealed your sentence.")
        br()
        if pChance(int(player.behaviour/2*100)) and not player.hasAppeal:
            cls()
            div()
            print("You won the appeal!")
            print("You are a free individual!")
            br()
            player.sentence = 0
            finishSentence(player)
        cls()
        div()
        print("You lost the appeal.")
        br()
        player.hasAppeal = True
    elif ch == 2:
        cls()
        div()
        print("You meditated in your cell.")
        player.behaviour += 0.05
        br()
    elif ch == 3:
        cls()
        div()
        if rng(1, 4) == 4:
            cls()
            print("You escaped!")
            br()
            main(player)
        else:
            print("You did not escape.")
            print("Your sentence was extended by 3 years.")
            player.behaviour -= 0.5
            player.sentence += 3
        br()
    elif ch == 4:
        cls()
        div()
        if rng(1, 2) == 2:
            print("A riot was started!")
        else:
            print("A riot was not started.")
        print("Your sentence was extended by 3 years.")
        player.sentence += 3
        player.behaviour -= 0.5
        br()
    elif ch == 5:
        cls()
        div()
        print("[1] Surrender")
        print("[0] Cancel")
        div()
        try:
            ch = int(input("$"))
        except:
            return None
        if ch == 1:
            die(player, 0)
    elif ch == 6:
        cls()
        div()
        player.money -= x
        player.sentence = 0
        print(f"You bailed yourself out.")
        br()
        finishSentence(player)
def prison(player):
    cls()
    div()
    print(player.forename + " " + player.surname)
    print("Age:", player.age)
    div()
    print("Happiness:", pbar(player.happiness), str(int(player.happiness * 100)) + "%")
    print("Health:   ", pbar(player.health), str(int(player.health * 100)) + "%")
    print("Smarts:   ", pbar(player.intel), str(int(player.intel * 100)) + "%")
    print("Looks:    ", pbar(player.looks), str(int(player.looks * 100)) + "%")
    div()
    print("[1] Prison")
    print("[x] Yard")
    print("[0] Age Up")
    print("[x] Market")
    print("[x] Gangs")
    div()
    try:
        ch = int(input("$"))
    except:
        prison(player)
    if ch == 1:
        prisonMenu(player)
    elif ch == 0:
        player.prisonAge()
        player=cleanTT(player)
    prison(player)


def goToPrison(player):
    cls()
    div()
    years = 0
    offences = []
    player.behaviour=0.0
    player.hasAppeal = False
    for item in player.offences:
        if item.served == False:
            years += item.years
            offences.append(item.name)
        mul = int((player.sentence + 1) / 5)
        if mul < 1:
            mul = 1
        years *= mul
    print("You have been charged with the following crimes:")
    div()
    for item in offences:
        print(item)
    div()
    if years >= 255:
        print("And will be sentenced to life in prison.")
    elif years == 1:
        print("And will be sentenced to a year in prison.")
    else:
        print(f"And will be sentenced to [{years}] years in prison.")
    div()
    if years < 255:
        print(f"[1] Hire Lawyers {player.nation.currency}{25000*years}")
    else:
        print(f"[1] Hire Lawyers {player.nation.currency}{150000*len(offences)}")
    print("[0] Do Not Hire")
    div()
    try:
        ch = int(input("$"))
    except:
        ch = 0
    if ch == 1:
        law = 1
    else:
        law = 0
    cls()
    div()
    if law == 1:
        if years < 255:
            player.money -= 45000 * years
        else:
            player.money -= 150000 * len(offences)
        years = int(years / 2)
    print(f"Crimes: {offences}")
    if years > 255:
        print("Sentence: Life")
    else:
        print(f"Sentence: {years} yr.")
    div()
    print("[1] Plead Guilty")
    print("[2] Not Guilty")
    div()
    try:
        ch = int(input("$"))
    except:
        ch = 1
    cls()
    div()
    if ch == 1:
        if years < 255:
            if law == 1:
                years = int((2 / 3) * years)
        if years < 255:
            print(f"You have been sent to prison for {years} years.")
        else:
            print("You have been sent to prison for life.")
        br()
        player.sentence = years
        prison(player)
    else:
        if law == 1:
            rng(1, 3)
            if rng == 3:
                print("You have been found not guilty!")
                br()
            else:
                player.sentence = years
                prison(player)
        else:
            print("You have been found guilty!")
            br()
            player.sentence = years
            prison(player)


def casino(player):
    cls()
    div()
    print(f"{player.nation.currency}{'{:,}'.format(player.money)}")
    print(
        f"Lifetime Winnings: {player.nation.currency}{'{:,}'.format(player.casinoWinnings)}"
    )
    div()
    print("Enter Bet:")
    try:
        bet = int(input("$"))
    except:
        bet = player.money
    if bet > player.money:
        bet = player.money
    if bet < 1000:
        bet = 1000
    if bet > 10000000:
        bet = 10000000
    cls()
    print(f"Your Bet: {player.nation.currency}{'{:,}'.format(bet)}")
    if play_blackjack():
        player.money += bet
        player.casinoWinnings += bet
    else:
        player.money -= bet
        player.casinoWinnings -= bet
    br()
    cls()
    div()
    print("Go Again?")
    print("[1] Yes")
    print("[0] No")
    div()
    try:
        ch = int(input("$"))
    except:
        casino(player)
    try:
        if ch == 0:
            return None
    except:
        return None
    casino(player)


def fertilityCenter(player):
    cls()
    div()
    if player.gender == 0:
        print("[1] Donate Sperm")
    else:
        print("[x] Receive Sperm")
    print("[x] Surrogacy")
    if player.fertile:
        print(f"[3] Vasectomy [{player.nation.currency}2500]")
    else:
        print("[ ] Vasectomy")
    if player.gender == 1:
        print("[x] IVF")
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    if ch == 1 and player.gender == 0:
        cls()
        div()
        print("You donated sperm.")
        player.money += rng(15, 150)
        br()
    elif ch == 3 and player.fertile:
        cls()
        div()
        print(f"You paid {player.nation.currency}2500 for a vasectomy.")
        player.money -= 2500
        player.fertile = False
        print("You are now infertile.")
        br()
    else:
        return None


def identityMenu(player):
    cls()
    div()
    print(f"[1] Name Change [{player.nation.currency}150]")
    print("[x] Declare Gender")
    print("[x] Declare Sexuality")
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    if ch == 1:
        fn = input("Forename $")
        sn = input("Surname $")
        player.money -= 150
        player.forename, player.surname = fn, sn
    else:
        return None


def nightlifeMenu(player):
    cls()
    div()
    print(f"[1] Club [{player.nation.currency}450]")
    print(f"[2] Drugs")
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    if ch == 1:
        cls()
        div()
        print("You went clubbing.")
        print("Enjoyment:")
        print(pbar(0.65))
        br()
        player.happiness += 0.35
        player.money -= 450
    elif ch == 2:
        cls()
        div()
        print(f"[1] Cocaine [{player.nation.currency}50]")
        print(f"[2] Cannabis [{player.nation.currency}80]")
        print(f"[3] Heroin [{player.nation.currency}250]")
        print(f"[4] MDMA [{player.nation.currency}115]")
        print(f"[5] Morphine [{player.nation.currency}75]")
        # LSD $675
        # PCP $ 125
        # Magic Mushrooms $ 65
        # Cough Syrup $ 10
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            cls()
            div()
            print("You tried cocaine at a nightclub.")
            br()
            if pChance(67) and not player.addictions["cocaine"]:
                cls()
                div()
                print("You are now addicted to cocaine.")
                br()
                player.addictions["cocaine"]=True
            player.money -= 50
        elif ch == 2:
            cls()
            div()
            print("You tried cannabis at a nightclub.")
            br()
            if pChance(10) and not player.addictions["cannabis"]:
                cls()
                div()
                print("You are now addicted to cannabis.")
                br()
                player.addictions["cannabis"]=True
            player.money -= 80
        elif ch == 3:
            cls()
            div()
            print("You tried heroin at a nightclub.")
            br()
            if pChance(95) and not player.addictions["heroin"]:
                cls()
                div()
                print("You are now addicted to heroin.")
                br()
                player.addictions["heroin"]=True
            player.money -= 250
        elif ch == 4:
            cls()
            div()
            print("You tried MDMA at a nightclub.")
            br()
            if pChance(50) and not player.addictions["MDMA"]:
                cls()
                div()
                print("You are now addicted to MDMA.")
                br()
                player.addictions["MDMA"]=True
            player.money -= 50
        elif ch == 5:
            cls()
            div()
            print("You tried morphine at a nightclub.")
            br()
            if pChance(190) and not player.addictions["morphine"]:
                cls()
                div()
                print("You are now addicted to morphine.")
                br()
                player.addictions["morphine"]=True
            player.money -= 50
        else:
            return None
    else:
        return None


def vacationMenu(player):
    cls()
    div()
    print(f"[1] 1st Class [{player.nation.currency}25000]")
    print(f"[2] Business Class [{player.nation.currency}2500]")
    print(f"[3] Economy Class [{player.nation.currency}50]")
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    print("You went on vacation.")
    print("Enjoyment:")
    if ch == 1:
        print(pbar(0.35))
        player.money -= 25000
    elif ch == 2:
        print(pbar(0.75))
        player.money -= 2500
    elif ch == 3:
        print(pbar(1))
        player.money -= 50
    player.happiness += 1 if ch != 3 else 0.45
    br()


def generateSpouse(player):
    if player.gender == 1:
        g = 0
    else:
        g = 1
    sp = Spouse(g)
    if player.gender == 0:
        n = choice(forename_f)
    else:
        n = choice(forename_m)
    s = choice(surnames)
    ag = player.age + rng(-5, 5)
    if ag < 18:
        ag = 18
    sp.create(f"{n} {s}", ag, rng(65, 85), rng(25, 50), rng(40, 50))
    return sp

import types
def castObject(obj, new_type):
    """
Create a new object of a specified type or use an existing object, copying all attributes (excluding methods) of the original object to the new one.

Args:
    obj: The original object to cast
    cast_type: The type or object to cast the original object to. If `cast_type` is a type, a new object of that type is created. If `cast_type` is an object, the original object is copied to that object.

Returns:
    A new object of the specified type, with all attributes (excluding methods) of the original object copied over. If `cast_type` is an object, the original object is copied to that object and returned.
    """
    # Create a new instance of the specified type
    if isinstance(new_type, type):
        new_obj = new_type()
    else:
        new_obj = new_type

    # Copy over all non-callable attributes from the original object
    for key, value in obj.__dict__.items():
        if not callable(value):
            setattr(new_obj, key, value)

    return new_obj
import inspect

def viewMethod(method):
    """
    Prints the source code of the given method.

    Args:
    method: A method object.

    Returns:
    None
    """
    module = inspect.getmodule(method)
    if module:
        print(inspect.getsource(module))
    else:
        print(f"Could not find source code for {method.__name__}")

def breakUp(player):
    if player.spouse:
        x=castObject(player.spouse,Ex)
        player.exes.append(x)
        player.spouse=None
def hashData(bytes,bitSize=2048):
    ## High accuracy checksum algorithm, default 2048 bits
    checksum = 0
    prime = 31  # Prime number used for hashing

    for byte in bytes:
        checksum = (checksum * prime + byte) % (2**bitSize)

    return checksum
def loveMenu(player,ch=""):
    if ch == "":
        cls()
        div()
        print("[1] Date")
        print("[x] Dating App")
        print("[x] Gay Dating App")
        print("[x] Hook Up")
        div()
        try:
            ch = int(input("$"))
        except:
            return None
    if ch == 1:
        sp = generateSpouse(player)
        cls()
        div()
        print(sp.name)
        if sp.gender == 0:
            print("Male")
        else:
            print("Female")
        print(f"Age: {sp.age}")
        print(f"Money: {player.nation.currency}{'{:,}'.format(sp.fortune)}")
        div()
        print("[1] Accept")
        print("[2] Try Again")
        print("[0] Decline")
        div()
        try:
            ch = int(input("$"))
        except:
            return None
        if ch == 1:
            player.spouse = sp
            cls()
            div()
            print(f"You are now dating {sp.name}.")
            br()
        elif ch == 2:
            loveMenu(player,1)
    else:
        return None
def lawsuit(player):
    suable = []
    try:
        if player.surgeon.can_sue:
            suable.append([player.surgeon,"surgeon"])
    except:
        pass
    suable += player.suable
    if suable == []:
        cls()
        div()
        print("You can't think of anyone to sue.")
        br()
        return None
    else:
        cls()
        div()
        index = 1
        for item in suable:
            print(f"[{index}] {item[0].name}")
            index += 1
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        ch -= 1
        try:
            suable[ch][0]
            suable[ch][1]
        except Exception as e:
            print(e)
        damages = [rng(100000,250000),rng(250000,500000),rng(1000000,10000000)]
        cls()
        div()
        print("Select Damages:")
        div()
        index = 1
        for item in damages:
            print(f"[{index}] {player.nation.currency}{'{:,}'.format(item)}")
            index += 1
        div()
        try:
            xh=int(input("$"))
        except:
            return None
        xh -= 1
        try:
            if xh == 0:
                chance = True
            elif xh == 1:
                chance = True if rng(1,5) != 5 else False
            elif xh == 2:
                chance = True if rng(1,5) not in [1,2] else False
            else:
                chance = False
            if chance:
                try:
                    suable[ch][0].sue(player, damages[xh])
                except Exception as e:
                    print(e)
            else:
                cls()
                div()
                print(f"You were unable to sue {suable[ch][0].name}.")
                br()
            if suable[ch] in player.suable:
                player.suable.pop(ch)
            else:
                setattr(player,suable[ch][1],None)
        except Exception as e:
            print(e)
def createChannel(player):
    cls()
    div()
    name = input("Channel Name $")
    if name == "":
        name = f"{player.forename} {player.surname}"
    o = OpenTube(name)
    player.opentube.append(o)
    openTube(player)
def openTube(player):
    if player.opentube == []:
        createChannel(player)
    else:
        index = 1
        cls()
        div()
        print("Select Channel")
        div()
        for item in player.opentube:
            print(f"[{index}] {item.name}")
            index += 1
        print(f"[0] Create New Channel")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 0:
            createChannel(player)
        else:
            try:
                player.opentube[ch-1].main(player)
            except:
                return None
def rehab(player):
    cls()
    div()
    print("You went for a 14-day rehab program.")
    br()
    if pChance(70):
        cls()
        div()
        print("You are no longer suffering from any addictions.")
        br()
        player.addictions = Player().addictions
    else:
        cls()
        div()
        print("You continue to be addicted.")
def licenseCentre(player):
    cls()
    lic = [["Driving License","car",50],["Boating License","boat",100],["Pilot's License","plane",2500],["Gun License","gun",0]]
    lic2=[]
    for item in lic:
        if not player.licenses[item[1]]:
            lic2.append(item)
    lic=lic2
    if lic == []:
        cls()
        div()
        print("There are no licenses left for you to unlock.")
        br()
        return None
    div()
    i = 1
    for item in lic:
        print(f"[{i}] {item[0]} [{player.nation.currency}{item[2]}]")
        i += 1
    div()
    try:
        ch=int(input("$"))
        x = lic[ch-1]
        if player.licenses[x[1]]:
            raise Exception
        if pChance(player.intel*100):
            cls()
            div()
            print(f"You now have a {x[0]}!")
            br()
            player.money -= x[2]
            player.licenses[x[1]] = True
        else:
            cls()
            div()
            print("You failed your test.")
            br()
    except Exception as e:
        return None
def makeFriend(player,f=None):
    cls()
    div()
    if f is None:
        f=Friend()
        f.age = player.age + rng(-5,5)
        if f.age < 18:
            f.age = 18
    print(f.name)
    print("Female" if f.gender == 1 else "Male")
    print("Age:",f.age)
    print(f"Salary: {player.nation.currency}{'{:,}'.format(int(f.salary*f.hours*52))}")
    div()
    print("[1] Make Friend")
    print("[0] Decline")
    div()
    try:
        ch=int(input("$"))
    except:
        return None
    if ch == 1:
        grantAchievement(player,"makeFriend")
        cls()
        div()
        print(f"You are now friends with {f.name}.")
        br()
        player.friends.append(f)
def goWitnessProtection(player):
    cls()
    div()
    print("You applied for Witness Protection.")
    br()
    cls()
    div()
    print("Your record was processed successfully.")
    br()
    price = int(player.money/64)
    cls()
    div()
    print(f"In order to enroll, you'll need to pay {player.nation.currency}{'{:,}'.format(price)}.")
    div()
    print("[1] Enroll")
    print("[0] Cancel")
    div()
    try:
        ch=int(input("$"))
    except:
        return None
    if ch == 1:
        cls()
        div()
        x=surnames
        try:
            x.remove(player.surname)
        except:
            pass
        f,s=choice(forename_m if player.gender == 0 else forename_f),choice(x)
        print(f"You are now {f} {s}.")
        br()
        player.wpp["enrolled"] = True
        player.wpp["oldNames"] = [player.forename,player.surname]
        player.forename, player.surname = f,s
        player.fame = 0
        player.openlife = []
        cls()
        div()
        print("All of your ties to your previous identity have been removed.")
        print("Your OpenLife channels have been deactivated.")
        print("Your homes were sold.")
        br()
        for item in player.property:
            player.money += item.value
        player.property = []
def researchLab(player):
    cls()
    div()
    if player.current_research != Player().current_research:
        print("Research ongoing.")
        print(f"Years To Go: {player.current_research[1]}")
        br()
        return None
    i=1
    x=researches
    if player.lab == Player().lab:
        x=[x[0]]
    else:
        for item in x:
            if player.lab[item[0]]:
                x.remove(item)
    if x == []:
        cls()
        div()
        print("No researches to research.")
        br()
        cls()
        div()
        print("To take advantage of your lab, go to Activities [4] > My Researches [27]")
        br()
        return None
    for item in x:
       print(f"[{i}] {item[1]} [{player.nation.currency}{'{:,}'.format(item[2])}] [Time: {item[3]} Years]")
       i += 1
    div()
    try:
        ch=int(input("$"))
        x=x[ch-1]
    except:
        return None
    player.current_research = [x[0],x[3]]
    player.money -= x[2]
    cls()
    div()
    print(f"You are now researching {x[1]}.")
    print(f"It will take {x[3]} years to finish.")
    br()
def myLab(player):
    cls()
    div()
    if player.lab["ageDown"] and player.age > 37:
        print(f"[1] Age-Down")
    elif player.age < 37 and player.lab["ageDown"]:
        print("[ ] Age-Down [TOO YOUNG: MUST BE 38]")
    else:
        print("[ ] Age-Down")
    if player.lab["cureCancer"] and player.disease["Cancer"]:
        print(f"[2] Cure Cancer [{player.nation.currency}1,000,000,000]")
    elif player.lab["cureCancer"] and  not player.disease["Cancer"]:
        print("[ ] Cure Cancer [ERROR: DO NOT HAVE CANCER]")
    else:
        print("[ ] Cure Cancer")
    div()
    try:
        ch=int(input("$"))
    except:
        return None
    if ch == 1 and player.age > 37 and player.lab["ageDown"]:
        cls()
        div()
        print("You are now 20 years younger!")
        br()
        player.age -= 20
    elif ch == 2 and player.lab['cureCancer'] and player.disease['Cancer']:
        cls()
        div()
        print("You paid {player.nation.currency}1,000,000,000 to cure your cancer.")
        br()
        player.disease['cancer'] = False
        player.money -= 1000000000
def emigrate(player):
    cls()
    div()
    for item in nations + player.criminalRecords[player.nation.id]:
        print(f"[{item.id}] {item.name}")
    div()
    try:
        ch=int(input("$"))
        if ch == player.nation.id:
            raise Exception
        x=nations[ch]
    except:
        return None
    div()
    z=[]
    for item in player.offences:
        if not item.served:
            z.append(item)
    if not z:
        print(f"Your emigration request to {x.name} was approved.")
        print(f"Emigrate to {x.name}?")
    else:
        print(f"Your emigration to {x.name} was declined.")
        print(f"Illegaly emigrate to {x.name}?")
    print(f"Price: {player.nation.currency}25,000")
    div()
    print("[1] Yes")
    print("[0] No")
    div()
    try:
        ch=int(input("$"))
        if not ch == 1:
            raise Exception
    except:
        return None
    player.money -= 25000
    if not z and not pChance(player.ethics*100):
        cls()
        div()
        print("You were caught trying to emigrate illegaly into {x.name}!")
        br()
        player.offences.append(Offence("Illegal Immigration",5))
        goToPrison(player)
    player.criminalRecords[player.nation.id] = player.offences
    player.nation = x
    player.offences = player.criminalRecords[player.nation.id]
def adultActivities(player, ch=""):
    cls()
    div()
    print("[0] Return")
    print("[1] Gym [$15]")
    print("[2] Library")
    print("[3] Doctor")
    print("[4] Surrender")
    if len(player.backup):
        print("[5] Time Travel")
    else:
        print("[ ] Time Travel")
    print("[6] Crime")
    print("[7] Adoption")
    print("[8] Hired Services")
    print("[9] Casino")
    print("[10] Identity")
    print("[11] Licenses")
    print("[12] Lawsuit")
    print("[13] Lottery")
    print("[14] Love")
    print("[15] Movies")
    print("[16] Nightlife")
    print("[17] Vacation")
    print("[x] Last Will And Testament")
    print("[19] Fertility")
    if not player.wpp["enrolled"] and player.fame == 1:
        print("[21] Witness Protection Program")
    else:
        print("[  ] Witness Protection Program")
    print("[22] Make Friends")
    if player.debt > ((player.money + player.savings) * 2):
        print("[23] Personal Bankruptcy")
    else:
        print("[  ] Personal Bankruptcy")
    print("[24] Research Lab")
    print("[26] Social Media")
    zz=Player().lab
    zz["researchLab"] = True
    if player.lab != Player().lab and player.lab != zz:
        print("[27] My Lab")
    else:
        print("[  ] My Lab")
    print("[28] Emigrate")
    div()
    if ch == "":
        try:
            ch = int(input("$"))
        except:
            return None
    if ch == 1:
        if player.money >= 15:
            player.money -= 15
        else:
            player.debt += 15
        player.happiness += 0.45
        player.health += 0.45
        player.looks += 0.1
        cls()
        div()
        print("You went to the gym.")
        print("Your Enjoyment:")
        print(pbar(1))
        br()
    elif ch == 2:
        cls()
        div()
        print("You visited the library.")
        print("Enjoyment:")
        print(pbar(0.35))
        br()
        player.intel += 0.25
        player.happiness += 0.45
        adult(player)
    elif ch == 3:
        doctorMenu(player)
    elif ch == 4:
        cls()
        div()
        print("[0] Cancel")
        print("[1] Surrender")
        div()
        if input("$") == "1":
            ## die
            die(player, 0)
        else:
            adultActivities(player)
    elif ch == 5 and len(player.backup):
        timeTravelMenu(player)
    elif ch == 6:
        adultCrime(player)
    elif ch == 7:
        adoption(player)
    elif ch == 8:
        cls()
        hiredServices(player)
    elif ch == 9:
        casino(player)
        if player.casinoWinnings != 0 and not player.addictions["gambling"] and pChance(20):
            cls()
            div()
            print("You are now addicted to gambling.")
            br()
            player.addictions["gambling"] = True
    elif ch == 10:
        identityMenu(player)
    elif ch == 11:
        licenseCentre(player)
    elif ch == 12:
        lawsuit(player)
    elif ch == 13:
        lottery(player)
    elif ch == 14:
        loveMenu(player)
    elif ch == 15:
        cls()
        div()
        print("You went to the movies.")
        div()
        print(f"Happiness: {pbar(1)}")
        br()
        player.happiness += 0.45
        adultActivities(player)
    elif ch == 16:
        nightlifeMenu(player)
    elif ch == 17:
        vacationMenu(player)
    elif ch == 19:
        fertilityCenter(player)
    elif ch == 21 and player.fame == 1 and not player.wpp["enrolled"]:
        goWitnessProtection(player)
    elif ch == 22:
        makeFriend(player)
    elif ch == 23 and player.debt > ((player.money + player.savings) * 2):
        cls()
        div()
        print("Are you sure you want to do this?")
        div()
        print("[-] Your debt will be cleared.")
        print("[-] You will lose all of your money and savings.")
        print("[-] Your vehicles and properties will be repossessed.")
        print("[-] You will lose your job.")
        print("[-] Your OpenTube channels will be deleted.")
        div()
        print("[1] Yes")
        print("[0] No")
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            player.money = 0
            player.debt = 0
            player.savings = 0
            player.property=[]
            player.opentube=[]
            player.vehicles=[[],[],[]]
            player.job,job_id=None,0
            cls()
            div()
            print("You are now worthless and debt-free!")
            br()
    elif ch == 24:
        researchLab(player)
    elif ch == 26:
        cls()
        div()
        print("[1] OpenTube")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            openTube(player)
        else:
            return None
    elif ch == 27 and player.lab != Player().lab and player.lab != zz:
        myLab(player)
    elif ch == 28:
        emigrate(player)
    else:
        return None


def parentInteract(player):
    cls()
    div()
    index = 1
    for item in player.parents:
        if item.age < item.end:
            print(f"[{index}]", item.display())
        index += 1
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    ch = ch - 1
    try:
        if player.parents[ch].end > player.parents[ch].age:
            player.parents[ch].interact(player)
    except Exception as e:
        print(e)


def childrenInteract(player):
    cls()
    div()
    index = 1
    for item in player.children:
        print(f"[{index}] {item.name}")
        index += 1
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    try:
        player.children[ch - 1].interact(player)
    except Exception as e:
        print(e)

def friendInteract(player):
    cls()
    div()
    i = 1
    for item in player.friends:
        if item.endAge <= item.age:
            player.friends.remove(item)
    for item in player.friends:
        print(f"[{i}] {item.name}")
        i += 1
    div()
    try:
        ch=int(input("$"))
        y=player.friends[ch-1]
    except:
        return None
    player.friends[ch-1].interact(player)
def adultRelations(player):
    cls()
    div()
    pl = 0
    for item in player.parents:
        if item.age < item.end:
            pl += 1
    if pl > 0:
        print("[1] Parents")
    else:
        print("[ ] Parents")
    if len(player.friends) > 0:
        print("[2] Friends")
    else:
        print("[ ] Friends")
    if player.spouse:
        print("[3] Spouse")
    else:
        print("[ ] Spouse")
    if len(player.children) > 0:
        print("[4] Children")
    else:
        print("[ ] Children")
    div()
    try:
        ch = int(input("$"))
    except:
        return None
    if ch == 1 and pl > 0:
        parentInteract(player)
    elif ch == 2 and len(player.friends) > 0:
        friendInteract(player)
    elif ch == 3 and player.spouse:
        player.spouse.interact(player)
    elif ch == 4 and player.children != []:
        childrenInteract(player)
    else:
        return None


def adult(player):
    player.stressMode = False
    if player.happiness > 1:
        player.happiness = 1
    if player.happiness < 0:
        player.happiness = 0

    if player.health > 1:
        player.health = 1
    if player.health < 0:
        player.health = 0

    if player.intel > 1:
        player.intel = 1
    if player.intel < 0:
        player.intel = 0

    if player.looks > 1:
        player.looks = 1
    if player.looks < 0:
        player.looks = 0

    if player.ethics > 1:
        player.ethics = 1
    if player.ethics < 0:
        player.ethics = 0

    cls()
    div()
    if player.gender == 0:
        x = "Male"
    else:
        x = "Female"
    print(player.forename + " " + player.surname + " [" + x + "]")
    try:
        print(job_roles[player.job_id][player.job_lvl - 1])
    except:
        print(f"InvalidJob: [{player.job_id}][{player.job_lvl}]")
    print("Nation:",player.nation.name)
    if player.disease != Player().disease:
        div()
        print("Diseases:")
        for item in player.disease:
            if player.disease[item]:
                if item == "depression":
                    print("Depression")
                elif item == "anxiety":
                    print("Anxiety")
                elif item == "commonCold":
                    print("Common Cold")
                elif item == "HBP":
                    print("High Blood Pressure")
                elif item == "Cancer":
                    print("Cancer")
                elif item == "postSSRI":
                    print("Post-SSRI Side Effects")
                elif item == "loneliness":
                    print("Terminal Loneliness Disorder")
                else:
                    print("ID://" + item)
    if player.addictions != Player().addictions:
        div()
        print("Addictions:")
        for item in player.addictions:
            if player.addictions[item]:
                if item == "gambling":
                    print("Gambling")
                elif item == "alcohol":
                    print("Alcohol")
                elif item == "heroin":
                    print("Heroin")
                elif item == "cannabis":
                    print("Cannabis")
                elif item == "morphine":
                    print("Morphine")
                elif item == "LSD":
                    print(item)
                elif item == "cocaine":
                    print("Cocaine")
                elif item == "MDMA":
                    print("MDMA")
                else:
                    print("ID:",item)
    div()
    print("Age:", player.age)
    print(player.nation.currency + str("{:,}".format((player.money))))
    if prefs['autoDeposit']:
        print("Savings:",player.nation.currency + str("{:,}".format((player.savings))))
    div()
    if player.edu_lvl == 1:
        print("Education: High School")
    elif player.edu_lvl == 2:
        print(f"Education: University [{degrees[player.degree]}]")
    else:
        print("Education: N/A")
    print(f"Work Experience: {player.work_e} Years")
    div()
    print("Happiness:", pbar(player.happiness), str(int(player.happiness * 100)) + "%")
    print("Health:   ", pbar(player.health), str(int(player.health * 100)) + "%")
    print("Smarts:   ", pbar(player.intel), str(int(player.intel * 100)) + "%")
    print("Looks:    ", pbar(player.looks), str(int(player.looks * 100)) + "%")
    if player.fame > 0:
        print("Fame:     ", pbar(player.fame), str(int(player.fame * 100)) + "%")    
    div()
    print("[1] Occupation")
    print("[2] Assets & Stats")
    print("[0] Age Up")
    print("[3] Relationships")
    print("[4] Activities")
    print("[5] Pause Menu")
    div()
    try:
        ch = int(input("$"))
    except:
        adult(player)
    if ch == 0:
        player.age_up()
        main(player)
    elif ch == 1:
        adultOccupation(player)
        adult(player)
    elif ch == 2:
        adultAssets(player)
        adult(player)
    elif ch == 3:
        adultRelations(player)
        adult(player)
    elif ch == 4:
        adultActivities(player)
        adult(player)
    elif ch == 5:
        adultPause(player)
    else:
        adult(player)


def teen(player):
    cls()
    div()
    print(player.forename + " " + player.surname)
    print("Age:", player.age)
    print("Nation:",player.nation.name)
    print(player.nation.currency + str("{:,}".format((player.money))))
    div()
    print("Happiness:", pbar(player.happiness), str(int(player.happiness * 100)) + "%")
    print("Health:   ", pbar(player.health), str(int(player.health * 100)) + "%")
    print("Smarts:   ", pbar(player.intel), str(int(player.intel * 100)) + "%")
    print("Looks:    ", pbar(player.looks), str(int(player.looks * 100)) + "%")
    div()
    if not player.droppedOut:
        print("[1] School")
    else:
        print("[ ] School")
    print("[x] Assets")
    print("[0] Age Up")
    print("[3] Relationships")
    print("[x] Activities")
    print("[5] Pause Menu")
    div()
    try:
        ch = int(input("$"))
    except:
        teen(player)
    if ch == 0:
        player.age_up()
        if player.age == 18:
            cls()
            div()
            print("You are now an adult.")
            br()
        main(player)
    elif ch == 1 and not player.droppedOut:
        secondarySchool(player)
        teen(player)
    elif ch == 3:
        adultRelations(player)
        teen(player)
    elif ch == 5:
        childPause()
        teen(player)
    else:
        teen(player)

def invertDict(dic):
    dic2={}
    for item in dic:
        if dic[item]:
            dic2[item] = False
        else:
            dic2[item]=True
    return dic2
def cleanTT(player):
    ## This function stops the game from slowing to a crawl by deleting the backup attribute from backups, massively reducing file size.
    ## This is the first thing called by the main() function
    ## Without this function, the file size gets exponentially larger (~8MB by age ~40)
    ## This function is integral to the game's performance.
    x = []
    for item in player.backup:
        try:
            del item.backup
        except:
            pass
        x.append(item)
    player.backup = x
    return player

def allCombos(a,b):
    z=[]
    for item in a:
        for i in b:
            z.append([item,i])
    return z
def getBankName(r=False):
    adjectives = ['First', 'National', 'Global', 'City', 'United', 'Capital', 'Elite', 'Secure', 'Prime', 'Royal']
    nouns = ['Bank', 'Trust', 'Financial', 'Group', 'Savings', 'Institution', 'Union', 'Corp', 'Investments', 'Holdings']
    if r:
        return adjectives, nouns
    bank_name = random.choice(adjectives) + ' ' + random.choice(nouns)
    return bank_name
def main(player):
    # The main() function is meant to be called after player.age_up().
    # It redirects the program to the correct stage function.
    player = cleanTT(player)
    if player.happiness > 1:
        player.happiness = 1
    if player.happiness < 0:
        player.happiness = 0

    if player.health > 1:
        player.health = 1
    if player.health < 0:
        player.health = 0

    if player.intel > 1:
        player.intel = 1
    if player.intel < 0:
        player.intel = 0

    if player.looks > 1:
        player.looks = 1
    if player.looks < 0:
        player.looks = 0

    if player.ethics > 1:
        player.ethics = 1
    if player.ethics < 0:
        player.ethics = 0
    if player.age < 6:
        infant(player)
    elif player.age < 12:
        child(player)
    elif player.age < 18:
        teen(player)
    else:
        adult(player)


def infant(player):
    cls()
    div()
    print(player.forename + " " + player.surname)
    print("Age:", player.age)
    div()
    print("Happiness:", pbar(player.happiness), str(int(player.happiness * 100)) + "%")
    print("Health:   ", pbar(player.health), str(int(player.health * 100)) + "%")
    print("Smarts:   ", pbar(player.intel), str(int(player.intel * 100)) + "%")
    print("Looks:    ", pbar(player.looks), str(int(player.looks * 100)) + "%")
    div()
    print("[0] Age Up")
    print("[1] Relationships")
    print("[2] Activities")
    div()
    try:
        ch = int(input("$"))
    except:
        infant(player)
    if ch == 0:
        player.age_up()
        if player.age == 6:
            cls()
            div()
            print(
                "You are now a child. You can now access school as well as proper activities."
            )
            br()
        main(player)
    elif ch == 1:
        adultRelations(player)
        infant(player)
    elif ch == 2:
        cls()
        div()
        print("[0] Return")
        print("[1] Exit To Main Menu")
        div()
        ch = input("$")
        if ch == "1":
            mainMenu()
        else:
            infant(player)
    else:
        infant(player)


def childPause():
    cls()
    div()
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
        ch = int(input("$"))
    except:
        return None
    if ch == 0:
        return None
    elif ch == 3:
        mainMenu()
    else:
        return None

def primarySchool(player):
    if player.grades > 1:
        player.grades = 1
    if player.grades < 0:
        player.grades = 0
    cls()
    div()
    print(f"Grades: {pbar(player.grades)} {int(player.grades * 100)}%")
    div()
    print("[x] Class...")
    print("[ ] Drop Out")
    print("[x] faculty...")
    print("[x] Nurse")
    print("[5] Study Harder")
    div()
    try:
        ch=int(input("$"))
    except:
        return None
    if ch == 1:
        return None
    elif ch == 5:
        cls()
        div()
        print(choice(["You studied until you fell asleep.","You studied until you went cross-eyed.",f"You studied for {rng(5,11)} hours straight."]))
        br()
        player.grades += 0.25
def dropOut(player):
    if player.nation.dropOutAge <= player.age:
        cls()
        div()
        print("Do you want to drop out?")
        div()
        print("[1] Drop Out")
        print("[0] Cancel")
        div()
        try:
            ch=int(input("$"))
        except:
            return None
        if ch == 1:
            player.droppedOut = True
    else:
        if player.nation.dropOutAge < 18:
            cls()
            div()
            print(f"You need to be {player.nation.dropOutAge} to drop out in {player.nation.name}.")
            br()
        else:
            cls()
            div()
            print(f"You cannot drop out in {player.nation.name}.")
            br()
def secondarySchool(player):
    cls()
    div()
    if player.grades > 1:
        player.grades = 1
    if player.grades < 0:
        player.grades = 0
    print(f"Grades: {pbar(player.grades)} {int(player.grades * 100)}%")
    div()
    print("[x] Activities...")
    print("[x] Class...")
    print("[x] Cliques...")
    print("[4] Drop Out")
    print("[x] Faculty")
    print("[x] Nurse")
    print("[7] Skip School")
    print("[8] Study Harder")
    div()
    try:
        ch=int(input("$"))
    except:
        return None
    if ch == 1:
        return None
    elif ch == 7:
        cls()
        div()
        print(choice(["You studied until you fell asleep.","You studied until you went cross-eyed.",f"You studied for {rng(5,11)} hours straight."]))
        br()
        player.grades += 0.25
    elif ch == 4:
        dropOut(player)
    elif ch == 8:
        cls()
        div()
        activities = ["went bowling","went roller-blading","loitered about","soliticed some people"]
        print(f"You and a friend skipped school and {choice(activities)} instead.")
        br()
        player.grades -= 0.35
        player.happiness += 0.35
        if pChance(100/3):
            player.happiness -= 0.45
            cls()
            div()
            print("You were caught skipping school by a teacher!")
            br()
            sc = CallScenario("Trouble","You were sent to the principal.",[["Insult him",1],["Apologise",2],["Make an excuse",3]])()
            if sc == 1:
                CallScenario("Trouble",f"You called your principal {choice(insults)}!")()
                CallScenario("Trouble",f"You were suspended from school for a week.")()
                z=CallScenario("Trouble",f"Your parents are angry that you were suspended from school",[["Apologise",1],["Insult Them",2]])()
                if z == 1:
                    CallScenario("Apology","You apologised to your parents.")()
                else:
                    CallScenario("Insult","You screamed at your parents.")()
            elif sc == 3:
                CallScenario("Trouble","You tried to make up an excuse for your behaviour.")()
                CallScenario("Trouble","You were suspended from school for a week.")()
                z=CallScenario("Trouble",f"Your parents are angry that you were suspended from school",[["Apologise",1],["Insult Them",2]])()
                if z == 1:
                    CallScenario("Apology","You apologised to your parents.")()
                else:
                    CallScenario("Insult","You screamed at your parents.")()
            else:
                CallScenario("Trouble","You apologised for your actions.\nYou were let go.")()
def child(player):
    cls()
    div()
    print(player.forename + " " + player.surname)
    print("Age:", player.age)
    print("$" + str("{:,}".format((player.money))))
    div()
    print("Happiness:", pbar(player.happiness), str(int(player.happiness * 100)) + "%")
    print("Health:   ", pbar(player.health), str(int(player.health * 100)) + "%")
    print("Smarts:   ", pbar(player.intel), str(int(player.intel * 100)) + "%")
    print("Looks:    ", pbar(player.looks), str(int(player.looks * 100)) + "%")
    div()
    print("[1] School")
    print("[x] Assets")
    print("[3] Relationships")
    print("[0] Age Up")
    print("[x] Activities")
    print("[5] Pause Menu")
    div()
    try:
        ch = int(input("$"))
    except:
        child(player)
    if ch == 0:
        player.age_up()
        if player.age == 12:
            cls()
            div()
            print("You are now a teenager.")
            br()
        main(player)
    elif ch == 1:
        primarySchool(player)
        child(player)
    elif ch == 3:
        adultRelations(player)
        child(player)
    elif ch == 5:
        childPause()
        child(player)
    else:
        child(player)


def cls():
    res = uname()
    os.system("cls" if res[0] == "Windows" else "clear")


def createLife():
    player = Player()
    print("[1] Male")
    print("[2] Female")
    ch = input("$")
    if ch == "1":
        player.gender = 1
    elif ch == "":
        player.gender = rng(1, 2)
    else:
        player.gender = 2
    if player.gender == 1:
        f = choice(forename_m)
    else:
        f = choice(forename_f)
    print("[1] Randomised Life")
    print("[x] Customised Life")
    ch = input("$")
    player.create(
        player.gender,
        f,
        choice(surnames),
        0,
        rng(1, 100) / 100,
        rng(1, 100) / 100,
        rng(1, 100) / 100,
        rng(1, 100) / 100,
    )
    if player.age == 0:
        cls()
        div()
        print("My name is", player.forename, player.surname + ".")
        if player.gender == 1:
            print("I was born a male in OpenLife, OpenLife.")
        else:
            print("I was born a female in OpenLife, OpenLife.")
        div()
        for item in player.parents:
            print(item.getLines())
        div()
        xm = player.hasAdoptedAttr()
        if xm == True:
            print("I was a planned pregnancy.")
        else:
            print("I was adopted. My real parents are unknown.")
        br()
        cls()
    main(player)

def createLife():
##    self,
##        gender=0,
##        forename="John",
##        surname="Smith",
##        age=18,
##        happiness=1,
##        health=1,
##        intel=1,
##        looks=1,
    cls()
    div()
    print("[1] Randomised Life")
    print("[2] Customised Life")
    div()
    try:
        ch=int(input("$"))
    except:
        return None
    if ch == 1:
        p=Player()
        x=rng(0,1)
        p.create(x,choice(forename_m if x == 0 else forename_f),choice(surnames),0,rng(1,100)/100,rng(1,100)/100,rng(1,100)/100,rng(1,100)/100)
        main(p)
    elif ch == 2:
        cls()
        div()
        print("[1] Male")
        print("[2] Female")
        div()
        try:
            ch=int(input("$")) - 1
        except:
            ch=rng(0,1)
        cls()
        fn = input("Forename $")
        if fn == "":
            fn = choice(forename_m if ch == 0 else forename_f)
        cls()
        sn = input("Surname $")
        if sn == "":
            sn = choice(surnames)
        cls()
        try:
            h = int(input("Happiness %"))/100
            if h > 1:
                h = 1
            if h < 0:
                h = 0
        except:
            h = rng(1,100)/100
        cls()
        try:
            hl = int(input("Health %"))/100
            if hl > 1:
                hl = 1
            if hl < 0:
                hl = 0
        except:
            hl = rng(1,100)/100
        cls()
        try:
            i = int(input("Intelligence %"))/100
            if i > 1:
                i = 1
            if i < 0:
                i = 0
        except:
            i = rng(1,100)/100
        cls()
        try:
            l = int(input("Looks %"))/100
            if l > 1:
                l = 1
            if l < 0:
                l = 0
        except:
            l = rng(1,100)/100
        try:
            ag = int(input("Age $"))
        except:
            ag = 0
        cls()
        p = Player()
        p.create(ch,fn,sn,ag,h,hl,i,l)
        main(p)
    else:
        return None
def pprint(obj):
    print(pprint_dict(obj_to_dict(obj)))


def savePrefs(prefs):
    with open("preferences.oldata", "wb") as f:
        pickle.dump(prefs, f)


def loadPrefs():
    try:
        with open("preferences.oldata", "rb") as f:
            d = pickle.load(f)
        return d
    except:
        return prefs


def doChallenge(player):
    try:
        div()
        print("Not implemented yet.")
        br()
    except Exception as e:
        div()
        print("An error occured.")
        print("You can try the following things:")
        print("[-] Trying again")
        print("[-] Trying again later")
        print("[-] Re-Downloading the challenge")
        print("[-] Trying on a new character")
        div()
        print(f"ErrorCode: {e}")
        br()
    return player


def editPrefs(prefs):
    cls()
    div()
    if prefs["autoDeposit"] == True:
        print("[1] Auto-Deposit [ENABLED]")
    else:
        print("[1] Auto-Deposit [DISABLED]")
    print("Automatically deposits all money into savings every age-up.")
    if prefs["allowDebug"] == True:
        print("[3] Disable Debug Mode")
    div()
    try:
        ch = int(input("$"))
    except:
        return prefs
    if ch == 1:
        if prefs["autoDeposit"] == True:
            prefs["autoDeposit"] = False
        else:
            prefs["autoDeposit"] = True
    elif ch == 3 and prefs["allowDebug"]:
        prefs["allowDebug"]=False
        editPrefs(prefs)
    return prefs
def filter_dict(dic):
    """
Deletes all items in a dict that aren't str, int, float, bool, list, dict, or None
Returns the filtered instance of the dict
    """
    for key in list(dic.keys()):
        if not isinstance(dic[key], (str, int, float, bool, list,dict, type(None))):
            del dic[key]
    return dic
def fixPlayer(player,verbose=True):
    if isinstance(player,Player) == False:
        return player
    fixes = 0
    x=Player()
    for item in dir(player):
        try:
            if type(getattr(player,item)) != type(getattr(x,item)):
                if verbose:
                    print("Broken:",item)
                fixes += 1
                setattr(player,item,getattr(x,item))
        except Exception as e:
            print("Warning:",e)
    if verbose:
        print("Fixes:",fixes)
    return player, fixes
def get_invalid_attributes(obj):
    """
    Returns a list of the attributes of the given object that have a different type from the corresponding attributes
    of its base class.
    
    Parameters:
    obj (object): The object to check.
    
    Returns:
    list: A list of the invalid attributes. If no invalid attributes are found, returns an empty list.
    """
    base_class = obj.__class__
    invalid_attrs = []
    for attr_name in base_class.__dict__:
        if not attr_name.startswith("__"):
            if not isinstance(getattr(obj, attr_name), getattr(base_class, attr_name).__class__):
                invalid_attrs.append(attr_name)
    return invalid_attrs
def impexFile():
    import json
    cls()
    div()
    print("[1] Export Save To JSON")
    print("[2] Import Save From JSON")
    print("[3] Import Alpha 16 File")
    print("[4] Reset Achievements File")
    div()
    try:
        ch=int(input("$"))
    except:
        return None
    if ch == 1:
        cls()
        fn = input("FileName $")
        x=fn
        fn += ".oll3"
        try:
            with open(fn,"rb") as f:
                p=pickle.load(f)
            with open(x+".json","w") as f:
                json.dump(filter_dict(obj_to_dict(p,False)),f)
        except Exception as e:
            cls()
            div()
            print("Error:",e)
            cls()
    elif ch == 2:
        cls()
        fn = input("FileName $")
        x=fn + ".oll3"
        fn += ".json"
        try:
            with open(fn,"r") as f:
                p=dict_to_obj(filter_dict(json.load(f)),Player)
            p=obj_to_dict(p)
            p=filter_dict(p)
            p=dict_to_obj(p,Player)
            p.cheater=Fuse()
            p.cheater.blow()
            p=upgradePlayer(p,False)
            p,fx=fixPlayer(p,False)
            with open(x,"wb") as f:
                pickle.dump(p,f)
                cls()
                div()
                print("Successfully imported player from JSON.")
                print(f"{fx} items were reset due to corruption.")
                print(f"To load it, use the Load Game menu.")
                print(f"For security, the anticheat has been triggered.")
                div()
                print("[!] Save files imported from JSON are NOT supported and WILL break the game.")
                br()
        except Exception as e:
            print("Error:",e)
    elif ch == 3:
        OllTwoConverter()
    elif ch == 4:
        saveAchievements(ACHIEVEMENTS)
    else:
        return None
import platform
def get_platform_info():
    """
    Returns a dictionary containing information about the currently running platform.
    """
    platform_info = {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version()
    }
    return platform_info
def changeLog():
    cls()
    div()
    print("OpenLife  0.2 Changes")
    div()
    print("0.2 is the Stock Ticker Update, allowing you to invest your money and either win big or lose it all!")
    print("It also adds nations and achievements.")
    div()
    print("[-] Added Nation-States")
    print("   [-] You are born into a random one and can emigrate to new ones.")
    print("   [-] Each nation has different policies and tax rates")
    print("   [-] Added tax")
    print("      [-] Added Income Tax, OpenTube Revenue Tax, and House Sell Tax.")
    print("      [-] The tax rate you receive is viewable in the Lifetime Stats menu.")
    print("[-] Investments")
    print("   [-] You can now invest in stocks, crypto, index funds, bonds, and metals")
    print("   [-] Each has its own properties and varying risk levels")
    print("[-] Added achievements")
    print("   [-] Earned through performing certain activities")
    print("[-] OpenTube tweaks")
    print("   [-] View formula tweaked to be less broken")
    print("      [-] As a result, the progress is a bit more flat.")
    print("   [-] Updates to OpenTube coming soon.")
    print("[-] Console Tweaks")
    print("   [-] More commands added")
    print("[-] Misc. Changes")
    print("   [-] Added Alpha 16 Save Converter")
    print("      [-] Converts Alpha 16 saves to the latest version")
    print("      [-] Some features, such as property, do not get ported over.")
    print("      [-] These features will be ported over *soon*")
    print("   [-] Main Menu now shows proper game version [AKA 0.2.0]")
    print("   [-] Tweaked parent death menu to display formatted inheritance amount")
    print("   [-] Lottery odds now 1/10,000,000")
    print("      [-] This is to reflect OpenLife's new direction of avoiding exploits like the lottery exploit")
    print("      [-] The lottery is still potentially profitable, but it is no longer an instant money maker")
    print("   [-] Fuse class now uses Singleton design pattern")
    print("      [-] This means you can't replace the player.cheater value directly anymore :)")
    br()
def mainMenu(ch=0):
    global achievements
    achievements = loadAchievements()
    prefs = loadPrefs()
    cls()
    div()
    logo = [
        " #######  ########  ######## ##    ## ##       #### ######## ######## ",
        "##     ## ##     ## ##       ###   ## ##        ##  ##       ##       ",
        "##     ## ##     ## ##       ####  ## ##        ##  ##       ##       ",
        "##     ## ########  ######   ## ## ## ##        ##  ######   ######   ",
        "##     ## ##        ##       ##  #### ##        ##  ##       ##       ",
        "##     ## ##        ##       ##   ### ##        ##  ##       ##       ",
        " #######  ##        ######## ##    ## ######## #### ##       ######## ",
    ]
    for l in logo:
        print(l)
    div()
    print("[1] New Life")
    print("[2] Load Life")
    print("[3] Credits")
    print(
        "[4] Download Latest Challenge"
    )  # Download Location: http://winfan3672.000webhostapp.com/challenge/latest.zip
    #print("[ ] [To open a challenge, load the game first]")
    print("[6] Exit")
    print("[7] Changelog")
    #print("[ ] Download Latest Custom Life")  # Download location: N/A
    print("[9] Options")
    print("[10] Quick Create Life")
    print("[11] Check for Updates")
    #print("[  ] Download OpenLife Times Article")
    print("[13] Tools")
    print(f"[14] Achievements [Earned: {achEarned(loadAchievements())}/{len(loadAchievements())}]")
    print("[0] About Game")
    div()
    print("Version:", version)
    div()
    if ch == 0:
        try:
            x = input("$")
            if x == "hidden test":
                prefs["allowDebug"] = True
                savePrefs(prefs)
                mainMenu()
            ch=int(x)
        except:
            mainMenu()
    if ch == 1:
        createLife()
    elif ch == 2:
        loadGame()
    elif ch == 3:
        cls()
        div()
        print("Game developed by WinFan3672.")
        div()
        print("https://github.com/WinFan3672/")
        print("https://winfan3672.neocities.org/")
        print("i.am@mildlysuspicio.us")
        br()
        cls()
        div()
        print("Some resources taken from fungamer2's LifeSimulator1 game.")
        print("https://github.com/fungamer2-2/Life-Simulator1/")
        br()
    elif ch == 4:
        import urllib.request

        url = "https://winfan3672.000webhostapp.com/challenge/latest.zip"
        print("Downloading challenge...")
        try:
            urllib.request.urlretrieve(url, "challenge.zip")
        except:
            div()
            print("Failed to download challenge.")
            mainMenu()
        div()
        print("Downloaded challenge.")
        mainMenu()
    elif ch == 6:
        raise ExitError
    elif ch == 7:
        changeLog()
        mainMenu()
    elif ch == 9:
        savePrefs(editPrefs(prefs))
        print(prefs)
        prefs = loadPrefs()
        print(prefs)
        mainMenu()
    elif ch == 10:
        grantAchievement(achID="swiftLife")
        player = Player()
        player.edu_lvl = 1
        player.gender = rng(0, 1)
        if player.gender == 0:
            f = choice(forename_m)
        else:
            f = choice(forename_f)
        player.create(
            player.gender,
            f,
            choice(surnames),
            18,
            rng(1, 100) / 100,
            rng(1, 100) / 100,
            rng(1, 100) / 100,
            rng(1, 100) / 100,
        )
        player.nation=nations[0]
        player.parents[0].age += 18
        player.parents[1].age += 18
        adult(player)
        mainMenu()
    elif ch == 11:
        cls()
        import urllib.request

        url = "http://winfan3672.000webhostapp.com/version_check/openlife.version"
        print("Checking for updates...")
        print(
            f"Current Version: {app_version[0]}.{app_version[1]}.{app_version[2]} [sub-version {sub_version}]"
        )
        try:
            urllib.request.urlretrieve(url, "openlife.version")
        except Exception as e:
            div()
            print("Failed to check for updates.")
            div()
            print("You could try:")
            print("[-] Checking that you are connected to the Internet.")
            print(
                "[-] Checking that winfan3672.000webhostapp.com is still up, since that is the server that provides the version check information."
            )
            print(f"[-] Checking that {url} exists, since it may have been deleted.")
            print(
                "[-] Checking that your antivirus or firewall is not blocking winfan3672.000webhostapp.com/"
            )
            print("[-] On Windows, deleting your DNS resolver cache.")
            div()
            print("Error for advanced users:", e)
            br()
            mainMenu()
        div()
        f = open("openlife.version", "r")
        data = f.read()
        data = data.split("|")
        data = [int(data[0]), int(data[1]), int(data[2])]
        d = [data[0],data[1]]
        av = [app_version[0], app_version[1]]
        not_update_text = f"An update for {game_name} [{data[0]}.{data[1]}.{data[2]}] is available.\nDownload it from:\nhttps://github.com/WinFan3672/OpenLife/releases/"
        if av <= d:
            print(not_update_text)
        else:
            print(f"You are on the latest version of {game_name}.")
        br()
        mainMenu()
    elif ch == 13:
        impexFile()
    elif ch == 14:
        listAchievements(loadAchievements())
    elif ch == 0:
        cls()
        div()
        print(game_name, "is a clone of BitLife written in Python.")
        print(
            "For years, BitLife: Life Simulator has suffered from a lot of issues, including:"
        )
        div()
        print("[-] Lazy Development")
        print("[-] Cash Grabs")
        print("[-] In-App Purchases")
        print("[-] Paywalls for achievements/features/updates/challenges")
        print("[-] No PC Release")
        print("[-] A lack of updates")
        print("[-] A game focused too much on RNG")
        br()
        cls()
        div()
        print(f"{game_name} will be a version of BitLife with:")
        div()
        print("[-] More features")
        print("[-] 100% free-and-open-source code")
        print("[-] No paywalls")
        print("[-] A multi-platform, multi-architecture system")
        print("[-] No lag")
        div()
        print(
            f"On top of this, {game_name} promises to only use the Python standard library, so you do not need to install anything."
        )
        print(
            f"{game_name} will be better than BitLife by the time the 1.0 is released."
        )
        br()
        cls()
        div()
        print(f"I hope you enjoy {game_name}.")
        br()
        mainMenu()
    else:
        mainMenu()
    mainMenu()


try:
    mainMenu()
except ExitError:
    if prefs["doNotClearVar"] == False:
        clear_variables()
        div()
        print("Game Exit")
        div()
        print("Game memory has been cleared.")
        print("In order to restart the game, close it and open it again.")
        div()
    else:
        div()
        print("Game Exit")
        div()
        prefs = loadPrefs()
        p = Player()
        p.create()
        c=Crypto("xRipple","XRP")
        p.money = 10000
        m=p.metals[0]
        m.investment = 1
