import pyjokes

# for a single joke

def userResponse () :
    permission = input("Ready for a joke? || \'yes\' or \'no\' : ")
    if permission.lower() == "yes" :
        languageForTheJoke ()
    if permission.lower() == "no" :
        print("See you next time!")
    else :
        print("Please enter a valid response : ")
        userResponse ()
        
def languageForTheJoke () :
    # for language
    print("What language would you prefer your joke in ?")
    languages = ["English : en", "German : de", "Spanish : es", "Italian : it", "Galician : gl", "Basque : eu", "or \'Default\' : \'df\'"]
    for i in range (len(languages)) :
        print(languages[i], end="\n")
    language = input("Please enter the language or the language code : ")
    match language :
        case  "English" | "en" :
            language = "en"
            print("Language chosen in English")
        case  "German" | "de" :
            language = "de"
            print("Gewählte Sprache Deutsch")
        case  "Spanish" | "es" :
            language = "es"
            print("Idioma elegido en español")
        case  "Italian" | "it" :
            language = "it"
            print("Lingua scelta in italiano")
        case  "Galician" | "gl" :
            language = "gl"
            print("Lingua escollida en galego")
        case  "Basque" | "eu" :
            language = "eu"
            print("Euskaraz aukeratutako hizkuntza")
        
        case "default" | "df" :
            language = "en"
            print("Language chosen in English")
    # for category
    # print("What category would you prefer your joke in ?")
    # categories = ["neutral : Neutral geeky jokes", "twister : Tongue-twister", "all : All types of joke"]
    # for i in range (len(categories)) :
    #     print(categories[i], end="\n")
    # category = input("Please enter the category or the category or the category value : ")
    # match category :
    #     case "neutral" | "Neutral geeky jokes" :
    #         category = "neutral"
    #         print("Category chosen is Neutral")