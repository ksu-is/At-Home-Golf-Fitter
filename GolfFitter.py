def get_golfer_info():
    #create intro
    print("Welcome to this At Home Golf Fitter program!")
    print("This program will ask some questions to gain info about you and your swing.")
    print("Then it will determine a good set of irons for you and give you info about them.")
    input("Press enter to start!")

    budget = int(float((input("What is the most you want to spend on a set of clubs? (Please enter an integer or dollar amount)")).strip("$")))
    
    if budget <= 500 == True:
        print("What category of experience do you fall into?")
        print("Beginner = Just starting to a few months, Light Intermediate = a few months to a year,")
        print("Experienced Intermediate = a year to 3 years, Advanced = 3+ years")
        experience = (input("Please enter here:")).lower()
        
        if experience == "Beginner":
            print("test")
        
        elif experience == "Light Intermediate":
            print("Test2")
        
        elif experience == "Experienced Intermediate":
            print("Test3")
        
        elif experience == "Advanced":
            print("Test4")
    
    elif budget > 500 and budget <= 1000:
        print("What category of experience do you fall into?")
        print("Beginner = Just starting to a few months, Light Intermediate = a few months to a year,")
        print("Experienced Intermediate = a year to 3 years, Advanced = 3+ years")
        experience = input("Please enter here:").lower()

        if experience == "Beginner":
            print("test")
        
        elif experience == "Light Intermediate":
            print("Test2")
        
        elif experience == "Experienced Intermediate":
            print("Test3")
        
        elif experience == "Advanced":
            print("Test4")

    
    
    elif budget > 1000:
        print("What category of experience do you fall into?")
        print("Beginner = Just starting to a few months, Light Intermediate = a few months to a year,")
        print("Experienced Intermediate = a year to 3 years, Advanced = 3+ years")
        experience = input("Please enter here:").lower()

        if experience == "Beginner":
            print("test")
        
        elif experience == "Light Intermediate":
            print("Test2")
        
        elif experience == "Experienced Intermediate":
            print("Test3")
        
        elif experience == "Advanced":
            print("Test4")

        


    return

get_golfer_info()