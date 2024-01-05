from replit import db

gossip = [
  "Do you think the victim has a lot of pubic hair?",
  "Do you think the victim has sent naked pictures to someone?",
  "Do you think the victim has seen beastiality porn?",
  "Do you think the victim has ever avoided a kiss from someone?",
  "Do you think the vitim has ever fucked someone under the influence of alcohol?",
  "Do you think the victim has ever had car sex?",
  "Do you think the victim has nudes saved on their phone?",
  "Do you think the victim has fucked any of the players?",
  "Do you think the victim has tried eating dog food?",
  "Do you think the victim has given hickeys to more than 10 people?",
  "Do you think the victim has ever pleaded more than once just to have sex with someone?",
  "Do you think the victim has ever ejaculated in less than a minute?",
  "Do you think the victim is multiorgasmic?",
  "Do you think the victim has lost their virginity at the age of 15 or less?",
  "Do you think the victim has ever been handcuffed to bed while having sex?",
  "Do you think the victim has ever done a striptease?",
  "Do you think the victim has doubts about their sexuality?",
  "Do you think the victim has used a dildo during the last week?",
  "Do you think the victim is able to fuck for more than 30 minutes straight?",
  "Do you think the victim enjoys anal sex?",
  "Do you think the victim has ever had semen on their face?",
  "Do you think the victim fakes their orgasms?",
  "Do you think the victim enjoys being insulted while fucking?",
  "Do you think the victim is a sex addict?",
  "Do you think the victim has ever made a sex tape?",
  "Do you think the victim has searched online sexual questions?",
  "Do you think the victim has ever tried to get someone else drunk in order to have sex with them?",
  "Do you think the victim has cheated on any of their partners?",
  "Do you think the victim has masturbated today?",
  "Do you think the victim has ever seen homosexual porn?",
  "Do you think the victim enjoys having fingers up their ass?",
  "Do you think the victim will be the first to get married among the players?",
  "Do you think the victim has stolen something?",
  "Do you think the victim enjoys reading erotic novels?",
  "Do you think the victim has had phone sex?",
  "Do you think the victim has ever felt jealous seeing a friend flirting with someone else?",
  "Do you think the victim has been caught masturbating by a family member?",
  "Do you think the victim has ever rubbed a stuffed animal/pillow to relieve theirself?",
  "Do you think the victim has masturbated in the shower?",
  "Do you think the victim has masturbated thinking of a teacher?",
  "Do you think the victim has flirted with someone who has a partner?",
  "Do you think the victim is a virgin?",
  "Do you think the victim has used oils or lubricants while fucking?"
]

madGab = [
  "Abe Odd Hull Luck Oak",  # A Bottle Of Coke
  "Ace Lip Puff That Hung",  # A Slip of The Tongue
  "Ace Tray Taste Who Dent",  # A Straight A Student
  "Bat Tree Snot Ink Looted",  # Batteries Not Included
  "Delete Elmer Made",  # The Little Mermaid
  "Fur Chin Ollie Foil",  # Virgin Olive Oil
  "Hoe Pin-Up Hits Depot Lease",  # Open Up It's The Police
  "Sue Perm Are Yo Burrow",  # Super Mario Bro
  "Lower Dove There Ings",  # Lord of The Rings
  "Eye Needle Ax Eight If",  # I Need a Laxative
  "Pie Rate Softly Care Hip Been",  # Pirates of the Carribean
  "Calm Heed At Tea",  # Call Me Daddy
  "Mime Elks Ache Brims Saul Dubais Tooth Uh Yod",  # My milkshake brings all the boys to the yard
  "Eggs Plow If Dire Hey Ya",  # Explosive Diarrhea
  "Sum Hag Tad As",  # Smack That Ass
  "Boo Buzz Wet",  # Booba Sweat
  "Is Bunch Pops Queer Pans",  # Spongebob Squarepants
  "Ha Minch Ease",  # Ham and Cheese
  "His Cat Tin Ought Inner Ear",  # It's getting hot in here
  "Stir Range Earth Inks",  # Stranger Things
  "Door Her Tex Pull Horror",  # Dora The Explorer
  "Wand Hides Tanned",  # One Night Stand
  "Nosed Ring Sat Hatched",  # No Strings Attached
  "Hey Reese Tiles",  # Harry Styles
  "Tail Ores Whiff",  # Taylor Swift
  "Are Heehaw Nag Ran Day",  # Ariana Grande
  "Hoop Side Hid Ditto Ken"  # Oops I Did It Again
]

nhie = [
  "Peed in a pool", "Drunk-dialed my ex", "Had a one-night stand",
  "Sent a stranger a drink", "Been nude in public as an adult",
  "Kissed a friend", "Wanted to kiss any of the players",
  "Wanted to fuck any of the players",
  "Used a bigger condom than what I really need",
  "Stripped in front of any camera",
  "Went to the toilet and didn't wash my hands",
  "Danced naked in front of a mirror", "Seen a breast",
  "Wore sexy underwear for my partner",
  "Kissed someone without knowing him/her",
  "A fantasy including firefighters of cops",
  "Kissed someone in front of a person that likes me", "Went naked to a pool",
  "Shower with someone of the opposite sex",
  "Shower with someone of the same sex", "Stared at a friend sibling's ass",
  "Had erection problems", "Pretended to have sex with a pillow",
  "Went outside without underwear", "Seen hentai",
  "Had phone sex with someone", "Compared dick sizes with friends",
  "Masturbated in order to get better sleep", "Used someone else's underwear",
  "Masturbated without erotic photos/porn",
  "Signed up in dating apps and sites",
  "Sent a naked photo of myself to someone",
  "Lied about my dick's size just to impress someone",
  "Dreamed of having a larger penis/breasts",
  "Had a crush on one of the players", "Slept naked",
  "Listened to a family member having sex",
  "Fucked someone in less than half an hour", "Asked a friend to touch my ass",
  "Dreamed about fucking more than one person at once",
  "Lost my virginity somewhere else than a bed",
  "Given a nickname for my genitals",
  "Had an erotic dream with any of the players", "Flirted with a friend",
  "Begged my ex to start over again", "Looked at a friend's ass",
  "Thought about becoming a pornstar", "Used a condom like it was a balloon",
  "Lied about my sexual preferences to ward off someone",
  "Sexually compared my ex-partners", "Seen gay porn",
  "Had a crush on the owner of this phone", "Seen anyone of this group naked",
  "Wanted to break a couple to try to fuck one of them",
  "Sexual confessions to my friends", "Kissed someone of my own gender",
  "Woke up wet of a hot dream", "Slept with a friend",
  "Masturbated besides a friend", "Smelled semen",
  "Cancelled plans with my friends to have sex with someone"
]

paranoia = [
  "Who here has had the most sexual partners?", "Who is the worst in bed?",
  "Who would be great at flirting their way out of trouble?",
  "Who’s most likely to sleep with an ex this week?",
  "Who's most likely to feed the homeless",
  "Who's most likely to be a part of a love triangle",
  "Who is most likely to gossip about their friends?",
  "Who is most likely to take their friends out for lunch and cover everyone’s tab?",
  "Who is most likely to repeat the same outfit thrice a week?",
  "Who is most likely to get married in an art gallery if they could?",
  "Who is most likely to game all night?",
  "Who is most likely to be the best photographer?",
  "Who is most likely to watch cartoons still?",
  "Who is most likely to scratch their genitals in public?",
  "Who is most likely to have a friend with benefits?",
  "Who is most likely to be into BDSM?",
  "Who is most likely to receive a compliment about their hot body?",
  "Who is most likely to cry over little things?",
  "Who is most likely to work out daily?",
  "Who is most likely to be the most popular in a new school?",
  "Who is most likely never to get married?",
  "Who is most likely to be a perfect kisser?",
  "Who is most likely to get a tattoo of their partner’s name?",
  "Who is most likely to give a kidney to a loved one with no regrets?",
  "Who is most likely to date an ex’s friend?",
  "Who is most likely to be a heartbreaker?",
  "Who is most likely the biggest flirt?",
  "Who has the best road trip stories?"
]

truth = [
  "Who do you think is the worst dressed person in this room?",
  "Have you ever cheated on someone?",
  "What is your favourite song when it comes to action in the bedroom?",
  "Who in the room would be the worst person to date and why?",
  "What’s the most embarrassing thing that’s happened to you during sex?",
  "Have you ever faked an orgasm?", "Do you have any fetishes?",
  "What’s your biggest turn on?",
  "If you could only ever do one position for the rest of your life, which one would it be and why?",
  "Who is the most surprising person to ever slide into your DMs?",
  "Do you have a hidden talent?",
  "If you could kiss someone right now, who would it be?",
  "What's the most drunk you've ever been?",
  "Of all the people in this room, who do you want to trade lives with?",
  "Have you ever practiced kissing in a mirror?",
  "Have you ever tried to take a sexy picture of yourself?",
  "Who is your secret crush?",
  "Who do you like the least in this room, and why?",
  "Who is the sexiest person in this room?",
  "What don't you like about each person in this room?",
  "Have you ever thought about cheating on your partner?"
]

dare = [
  "Google the dirtiest thing you can think of and show it to the person next to you.",
  "Serenade the person to your right.",
  "Close your eyes, sit on someone’s lap and guess who it is.",
  "Rate everyone playing from your most to least favourite.",
  "Let another person draw a tattoo on your back with a permanent market.",
  "Pretend to be the person on your left for 10 minutes",
  "Whisper a secret to the person on your left",
  "Pretend to be the person to your right for 10 minutes",
  "Say two honest things about everyone in the group",
  "Seductively eat a banana whilst locking eyes with the person to your left.",
  "Google the dirtiest thing you can think of and show it to the person next to you.",
  "Serenade the person to your right.", "Tell us your cheesiest pick-up line.",
  "Say something dirty to the person on your left",
  "Give a lap dance to someone of your choice",
  "Let someone else tickle you and try not to laugh"
]

wyr = [
  "Know the date of your death or the cause of your death?",
  "Be the person who flips the switch during executions or be the judge who decides who should be executed?",
  "Die before your spouse or after?",
  "Get diarrhea on vacation or the day of a big presentation at work?",
  "Lose all of the money you’ve earned this year or lose all of the memories you’ve gained this year?",
  "Find a dead body or be a witness to a deadly assault?",
  "Give up your favorite food or give up sex?",
  "Be half your height or double your weight?",
  "Be the only person who speaks out of their butt or be the only person who doesn’t speak out of their butt?",
  "Get a tattoo or a lip piercing?",
  "Sniff butts like a dog when you meet someone new or eat dog food every night for dinner?"
]


# Helper Functions
# Gossip
def update_gossip(new_gossip):
  if "gossip" in db.keys():
    gossip = db["gossip"]
    gossip.append(new_gossip)
    db["gossip"] = gossip
  else:
    db["gossip"] = [new_gossip]


def delete_gossip(index):
  gossip = db["gossip"]
  if len(gossip) > index:
    del gossip[index]
    db["gossip"] = gossip


gossipOptions = gossip
if "gossip" in db.keys():
  gossipOptions = gossipOptions + list(db["gossip"])


# Mad Gab
def update_madGab(new_madGab):
  if "madGab" in db.keys():
    madGab = db["madGab"]
    madGab.append(new_madGab)
    db["madGab"] = madGab
  else:
    db["madGab"] = [new_madGab]


def delete_madGab(index):
  madGab = db["madGab"]
  if len(madGab) > index:
    del madGab[index]
    db["madGab"] = madGab


madGabOptions = madGab
if "madGab" in db.keys():
  madGabOptions = madGabOptions + list(db["madGab"])


# Never Have I Ever
def update_nhie(new_nhie):
  if "nhie" in db.keys():
    nhie = db["nhie"]
    nhie.append(new_nhie)
    db["nhie"] = nhie
  else:
    db["nhie"] = [new_nhie]


def delete_nhie(index):
  nhie = db["nhie"]
  if len(nhie) > index:
    del nhie[index]
    db["nhie"] = nhie


nhieOptions = nhie
if "nhie" in db.keys():
  nhieOptions = nhieOptions + list(db["nhie"])


# Paranoia
def update_paranoia(new_paranoia):
  if "paranoia" in db.keys():
    paranoia = db["paranoia"]
    paranoia.append(new_paranoia)
    db["paranoia"] = paranoia
  else:
    db["paranoia"] = [new_paranoia]


def delete_paranoia(index):
  paranoia = db["paranoia"]
  if len(paranoia) > index:
    del paranoia[index]
    db["paranoia"] = paranoia


parOptions = paranoia
if "paranoia" in db.keys():
  parOptions = parOptions + list(db["paranoia"])


# Truth or Dare
def update_truth(new_truth):
  if "truth" in db.keys():
    truth = db["truth"]
    truth.append(new_truth)
    db["truth"] = truth
  else:
    db["truth"] = [new_truth]


def delete_truth(index):
  truth = db["truth"]
  if len(truth) > index:
    del truth[index]
    db["truth"] = truth


truthOptions = truth
if "truth" in db.keys():
  truthOptions = truthOptions + list(db["truth"])


def update_dare(new_dare):
  if "dare" in db.keys():
    dare = db["dare"]
    dare.append(new_dare)
    db["dare"] = dare
  else:
    db["dare"] = [new_dare]


def delete_dare(index):
  dare = db["dare"]
  if len(dare) > index:
    del dare[index]
    db["dare"] = dare


dareOptions = dare
if "dare" in db.keys():
  dareOptions = dareOptions + list(db['dare'])

todRandom = truthOptions + dareOptions


# Would You Rather
def update_wyr(new_wyr):
  if "wyr" in db.keys():
    wyr = db["wyr"]
    wyr.append(new_wyr)
    db["wyr"] = wyr
  else:
    db["wyr"] = [new_wyr]


def delete_wyr(index):
  wyr = db["wyr"]
  if len(wyr) > index:
    del wyr[index]
    db["wyr"] = wyr


wyrOptions = wyr
if "wyr" in db.keys():
  wyrOptions += list(db["wyr"])
