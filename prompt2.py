#Python Prompt Generator
#by silasfelinus
#NSFW
#masterpiece, (margot robbie, red sonja), splashing in magical hot spring drawn by stokoe, soaked, dripping, seductive, tattoo choker, color splash, EF 70mm, canon, perfect lighting, rainbow hair, 4k smokey eyes, freckles++, eye contact, curvy


import random

qualifier = ("magnificent", "candid", "gorgeous", "lovely", "sexy", "xxx", "NSFW");

style = ("polaroid", "canon", "CCTV", "DVDRIP", "HD", "POV", "felt", "graffiti", "High Octane Render", "Instagram", "illustrated", "modeling", "porn scene");

intro = ("masterpiece", "sexy");

scope = ("close up", "bj lips");    

location = ("bedroom", "love hotel", "Star Trek Bridge", "Mos Eisley Cantina", "Starbucks", "KFC", "Target", "walmart", "changing room", "playground", "ice cream truck", "gas station bathroom", "glory hole", "dolphin tank", "cat cafe", "animal shelter", "movie theater", "school", "classroom", "beach", "bar", "hotel", "stadium", "river", "international space station", "mars", "moon", "public", "kitchen", "hot spring," "hot tub", "bath", "shower", "cockpit", "car", "drive-in", "theater", "stage", "office", "penthouse", "pool", "zoo", "future", "ER", "cage", "boat", "yacht", "underwater", "playground", "construction site", "casino", "wizard's labratory", "cemetary", "morgue", "mausoleum", "mansion", "ancient victorian", "fairy glen", "haunted house", "haunted castle", "labyrinth", "maze", "lectern", "lecture hall", "photo booth", "mall", "shopping center", "disneyland", "splash mountain", "circus", "river", "hawaii", "kawaii", "paris", "new york", "iceland", "titanic", "jungle", "atlantis", "las vegas", "Xavier's Mansion", "Castle Greyskull", "Magic Kingdom", "a cartoon", "home", "taxi", "hood of a car", "wing of a plane", "on a dragon", "on a bird", "in a fishbowl", "in a snowglobe", "in outer space", "in a void", "at a porn shoot", "at a funeral", "ancient greece", "jurassic park", "space ship", "in an active volcano", "Hogwarts", "The Amazon", "cruise hip", "The Sphinx", "Egypt", "China", "Korea", "Japan", "farm", "bed-and-breakfast", "english countryide", "red light district", "alien planet", "hell", "heaven", "purgatory", "the dmv", "church", "rectory", "confession booth", "kabuki stage", "MMA Ring", "boxing ring", "wrestling mat", "Amsterdam", "Ancient Japan", "Edo period", "The Age of Enlightenment", "Victorian England", "France", "Africa", "savanah", "the outback", "hyrule", "sci-fi setting", "convention", "kegger", "college dorm", "opium den", "tenement" );

time = ("morning", "afternoon", "evening", "dusk", "golden hour", "twilight");

emotion = ("happy", "sad", "angry", "annoyed", "pouty", "coquettish", "flirty", "amorous", "seductive", "loving", "scared", "obedient", "attentive", "enthusiastic", "surprised", "bored", "crying", "unhappy", "sad", "irritated", "lonely", "hungry", "excited");

#ethnicities.txt

age = ("teen", "teenager", "young woman", "young adult woman", "adult woman", "woman");

identity = ("Margot Robbie", "Emma Stone", "Miley Cyrus", "Drew Barrymore", "Milla Jovovich", "Emma Watson", "Bjork", "Red Sonja", "Princess Peach", "she-hulk", "Barbarella", "Crystal Gems", "Charlies Angels", "Christina Ricci", "Zendaya", "Selena Gomez", "Ke$ha", "P!nk", "Debbie Harry", "Holly Wood", "Wednesday Addams", "Belle Delphine",  );

role = ("goth", "punk", "lolita", "schoolgirl", "preppy", "cheerleader", "brainiac", "slut", "good girl", "catholic schoolgirl", "raver", "dancer", "teacher", "lawyer", "doctor", "nurse", "prisoner", "idol", "model", "secretary", "mcdonald's employee", "service worker", "casino dealer", "police officer", "mortician", "warrior", "magician", "healer", "witch", "lover", "princess", "queen", "whore", "prostitute", "mascot", "magician's assistant", "magician", "sorcerer", "teen girl scout", "catgirl", "marble statue", "astronaut", "young innocent", "hot", "emo", "succubus", "clown", "medusa", "orc", "librarian", "prostitute", "elf-eared", "galactic", "knight", "ninja", "mage", "cyborg", "pirate");

bSize = ("large breasts", "medium breasts", "small breasts");

physique = ("thin", "curvy", "petite", "curvaceous", "zaftig", "plump", "rubenesque", "statuesque", "model", "bodybuilder")

adjective = ("expressive", "beautiful", "cute", "kawaii", "sexy", "alluring", "innocent", "sweet", "enchanting", "captivating", "ravishing", "beauty", "nubile", "flashy", "seductive", "snazzy", "playful", "fun", "photogenic", "telegenic");
    
action = ("cuddling", "sleeping with", "stroking", "licking", "fucking", "sucking", "seducing", "coveting", "praying to", "worshipping", "petting", "holding", "being held by", "missionary", "doggy-style", "blowjob", "vaginal", "pov", "deepthroat", "bukakke", "group sex");
        
props = ("book", "glasses", "lolipop", "dildo", "vibrator", "hitachi", "magic wand", "candy", "popsicle", "banana", "cock", "pussy", "toy", "nothing", "stockings", "pony tail", "freckles", "cybernetic augments", "choker and eyeshadow", "bodysuit", "swimsuit", "mecha suit", "pulled up tshirt", "kimono", "skirt", "body stocking", "rope dress", "cocktail dress", "raver gear", "goggles", "armor", "loincloth", "furs", "long scarf")

hairLength = ("long", "medium", "short");

hairColor = ("white hair", "black hair", "purple hair", "pink hair",
             "red hair", "blonde hair", "green hair," "silver hair", "golden hair", "rainbow hair");

hairstyles = ("punk", "goth", "lolita", "trendy", "queer", "modern", "creative", "gorgeous", "wavy", "bangs", "shaved", "shaved side", "buzzed");


eyeColor = ("hazel", "green", "brown", "black", "grey", "purple", "pink",
            "red", "silver", "yellow", "Sapphire", "turquoise", "amethyst", "aquamarine", "ruby", "coral",
            "peach", "gold", "dark brown", "jade", "teal", "ice blue", "light blue", "blue", "grey-blue",
            "amber");
    
accessories = ("choker", "nipple piercing", "tattoos", "tongue piercing", "earrings", "necklace", "ball gag", "handcuffs", "raver toys", "laser toy", "poi", "sushi");
    
partner = ("friend", "girlfriend", "friends", "animal", "alien", "pet", "slave", "lover", "master", "monster", "ghost", "dream", "memory", "desire", "tentacle monster", "water elemental", "fairy", "genderqueer lover", "man", "alone", "herself", "dragon", "giant", "troll", "ogre", "sprite", "nymph", "satyr", "vampire", "werewolf", "zombie", "a gang of aliens", "lilliputians", "midgets", "miniature people", "robot", "Crystal Gem", "cheerleader", "lesbian");

outro = "color splash, EF 70mm, canon, perfect lighting, rainbow hair, 4k smokey eyes, freckles++, eye contact";
negatives = "[bad anatomy, extra legs, extra arms, extra fingers, poorly drawn hands, poorly drawn feet, disfigured, out of frame, tiling, bad art, deformed, mutated]";


def createPrompts(promptCount):
    prompts = ""

    f = open("prompts.txt", "w")

    for i in range(promptCount):
        lower_bound = 0.9
        upper_bound = 1.4
        multiplier = random.uniform(lower_bound, upper_bound)



        prompts = prompts + "(" \
                  + getRandomStringFromList(intro) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(scope) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(location) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(time) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(emotion) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(age) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(identity) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(identity) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(role) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(bSize) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(physique) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(adjective) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(action) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(props) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(hairLength) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(hairColor) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(hairstyles) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(eyeColor) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + getRandomStringFromList(accessories) \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + "(" \
                  + outro \
                  + ":" \
                  + "{:.2f}".format(random.uniform(lower_bound, multiplier)) \
                  + ") " \
                  + negatives \
                  + "\n"

    f.write(prompts)



def getRandomStringFromList(list):
    i = random.randint(0, len(list) - 1)
    return list[i]

def random_line(afile):
    f = open(afile, "r")
    line = next(f)
    for num, aline in enumerate(f, 2):
        if random.randrange(num):
            continue
        line = aline
    return line

if __name__ == '__main__':
    createPrompts(10)
    
