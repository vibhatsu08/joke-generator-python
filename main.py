import pyjokes
from googletrans import Translator

# creating an instance of the Translator.
translator = Translator ()

# the template used to translate the input code from it's source language which is "English" : "en" to the user's preference language code.
# (translator.translate("", src="en", dest="{}".format(language))).text

# function to start the program, takes user response/permission to get started.
def userResponse () :
    permission = input("Ready for a joke? || \'yes\' or \'no\' : ")
    
    if permission.lower() == "yes" :
        languageForTheJoke ()
    elif permission.lower() == "no" :
        print("See you next time!")
    else :
        print("Please enter a valid response : ")
        userResponse ()  
        
# function to get the language for the joke.
def languageForTheJoke () :
    # for language
    print("What language would you prefer your joke in ?")
    languages = ["1) : English : en", "2) : German : de", "3) : Spanish : es", "4) : Italian : it", "5) : Galician : gl", "6) : Basque : eu", "7) : or \'Default\' : \'df\'"]
    
    for i in range (len(languages)) :
        print(languages[i], end="\n")
        
    language = input("Please enter the language or the language code : ")
    
    match language :
        case "1" :
            language = "en"
            print("Language chosen is \'English\'")
            categoryForTheJoke (language)
        case "2" :
            language = "de"
            test = translator.translate("Language chosen is \'German\'", src="en", dest="{}".format(language))
            print(test.text)
            categoryForTheJoke (language)
        case "3" :
            language = "es"
            test = translator.translate("Language chosen is \'Spanish\'", src="en", dest="{}".format(language))
            print(test.text)
            categoryForTheJoke (language)
        case "4" :
            language = "it"
            test = translator.translate("Language chosen is \'Italian\'", src="en", dest="{}".format(language))
            print(test.text)
            categoryForTheJoke (language)
        case "5" :
            language = "gl"
            test = translator.translate("Language chosen is \'Galician\'", src="en", dest="{}".format(language))
            print(test.text)
            categoryForTheJoke (language)
        case "6" :
            language = "eu"
            test = translator.translate("Language chosen is \'Basque\'", src="en", dest="{}".format(language))
            print(test.text)
            categoryForTheJoke (language)
        case "7" :
            language = "en"
            print("Language chosen is \'default\' which is \'English\'")
            categoryForTheJoke (language)
        
        case other :
            print("Please enter a valid language!")
            languageForTheJoke ()

# function to get the category for the joke in the user's preferred language.
def categoryForTheJoke (language) :
    categories = ["1) : neutral : Neutral geeky jokes", "2) : all : All types of joke"]
    
    for i in range (len(categories)) :
        print((translator.translate(categories[i], src="en", dest="{}".format(language))).text, end="\n")
        
    category = input((translator.translate("Please enter the category number : ", src="en", dest="{}".format(language))).text)
    
    if category == "1" :
        category = "neutral"
        print((translator.translate("Category chosen in \'Neutral\'", src="en", dest="{}".format(language))).text)
        generateJoke (language, category)
        
    # this category isn't working, checked from my side, didn't find any bugs in my code.
    # elif category == "2" :
    #     category = "twister"
    #     print((translator.translate("Category chosen in \'twister\'", src="en", dest="{}".format(language))).text)
    #     generateJoke (language, category)
        
    elif category == "2" :
        category = "all"
        print((translator.translate("Category chosen in \'all\'", src="en", dest="{}".format(language))).text)
        generateJoke (language, category)
    else :
        print("Please enter a valid category : ")
        categoryForTheJoke (language)
        
# function to generate the joke based on the user's chosen language and category.
def generateJoke (language, category) :
    print((translator.translate("The language chosen is \'{}\' and the category chosen is \'{}\'".format(language, category), src="en", dest="{}".format(language))).text)
    getJoke = pyjokes.get_joke(language, category)
    print(getJoke)
    anotherOne (language, category)
        
# function to implement an another one joke. Recursive function works as long as the another has the input == "yes".
def anotherOne (language, category) :
    another = input((translator.translate("Wanna hear another one? ", src="en", dest="{}".format(language))).text)
    if another == (translator.translate("yes", src="en", dest="{}".format(language))).text :
        getJoke = pyjokes.get_joke(language, category)
        print(getJoke)
        anotherOne (language, category)
    elif another == (translator.translate("no", src="en", dest="{}".format(language))).text :
        print((translator.translate("Alright, thanks for playing!", src="en", dest="{}".format(language))).text)
    else :
        print((translator.translate("Please enter a valid value : \'yes\' or \'no\' ", src="en", dest="{}".format(language))).text)
        anotherOne (language, category)

# calls the first function to trigger the program.
userResponse()