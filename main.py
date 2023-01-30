import pyjokes

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
        case "English" | "en" | "english" :
            language = "en"
            print("Language chosen in \'English\'")
            categoryForTheJoke (language)
            
        # case "German" | "de" | "german" :
        #     language = "de"
        #     print("Gewählte Sprache Deutsch")
            
        # case "Spanish" | "es" | "spanish" :
        #     language = "es"
        #     print("Idioma elegido en español")
            
        # case "Italian" | "it" | "italian" :
        #     language = "it"
        #     print("Lingua scelta in italiano")
            
        # case "Galician" | "gl" | "galician" :
        #     language = "gl"
        #     print("Lingua escollida en galego")
            
        # case "Basque" | "eu" | "basque" :
        #     language = "eu"
        #     print("Euskaraz aukeratutako hizkuntza")
            
        # case "default" | "df" :
        #     language = "en"
        #     print("Default language chosen is English")
            
        
        case other :
            print("Other languages are unavailable at the moment...Sorry for the inconvenience.")
            print("Default language chosen is English")
            language = "en"
            categoryForTheJoke (language)
            # print("Please enter a valid language!")
            # languageForTheJoke ()
    
def categoryForTheJoke (language) :
    categories = ["neutral : Neutral geeky jokes", "twister : Tongue-twister", "all : All types of joke"]
    for i in range (len(categories)) :
        print(categories[i], end="\n")
    category = input("Please enter the category or the category or the category value : ")
    match category :
        case "neutral" | "Neutral geeky jokes" :
            category = "neutral"
            print("Category chosen in \'Neutral\'")
            generateJoke (language, category)
            
        case "twister" | "Tongue-twister" :
            category = "twister"
            print("Category chosen in \'Twister\'")
            generateJoke (language, category)
            
        case "all" | "All types of joke" :
            category = "all"
            print("Category chosen in \'All\'")
            generateJoke (language, category)
        
        case other :
            print("Please enter a valid category : ")
            categoryForTheJoke (language)
            
def generateJoke (language, category) :
    print("The language chosen is \'{}\' and the category chosen is \'{}\'".format(language, category))
    getJoke = pyjokes.get_joke(language, category)
    print(getJoke)
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
languageForTheJoke ()