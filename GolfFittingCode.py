import webbrowser
import time

print("Welcome to this At Home Golf Fitter program!")
print("This program will ask some questions to gain info about you and your swing.")
print("Then it will determine a good set of irons and take you to the a")
print("webpage to buy that set of irons.")
input("Press enter to start!")

budget = int(float((input("What is your budget for a set of irons? (Please enter an integer or dollar amount)")).strip("$")))

#Create function to gain info about the golfer to determine a set of clubs
def get_info():
    if budget <= 500:
        print("What is your golf experience level? (Beginner, Intermediate, Advanced)")
        experience = input('Please Enter Here:').lower()
    
        if experience == "beginner":
            return "cheap beginner"
        elif experience == "intermediate":
            return "cheap intermediate"
        elif experience == "advanced":
            return "cheap advanced"

    if budget > 500 and budget <= 1000:
        print("What is your golf experience level? (Beginner, Intermediate, Advanced)")
        experience = input('Please Enter Here:').lower()

        if experience == "beginner":
            return "mid_spender beginner"
        elif experience == "intermediate":
            return "mid_spender intermediate"
        elif experience == "advanced":
            return "mid-spender advanced"

    if budget > 1000:
        print("What is your golf experience level? (Beginner, Intermediate, Advanced)")
        experience = input('Please Enter Here:').lower()

        if experience == "beginner":
            return "expensive beginner"
        elif experience == "intermediate":
            return "expensive intermediate"
        elif experience == "advanced":
            return "expensive advanced"

golfer_info = get_info()


#Section of if statements to open webpages based on golfer_info data
#Cheap Section
if golfer_info == "cheap beginner":
    print("Ok, I think I have a set of clubs for you. Opening webpage....")
    time.sleep(3)
    webbrowser.open("https://www.carlsgolfland.com/wilson-d300-irons?product=80622")

if golfer_info == "cheap intermediate":
    print("Ok, I think I have a set of clubs for you. Opening webpage....")
    time.sleep(3)
    webbrowser.open("https://stix.golf/products/stix-golf-iron-set-5-pw?variant=39287801643074&currency=USD&nbt=nb%3Aadwords%3Ax%3A17528803185%3A%3A&nb_adtype=pla&nb_kwd=&nb_ti=&nb_mi=299733814&nb_pc=online&nb_pi=shopify_US_6554966589506_39287801643074&nb_ppi=&nb_placement=&nb_si={sourceid}&nb_li_ms=&nb_lp_ms=&nb_fii=&nb_ap=&nb_mt=&gclid=CjwKCAiAv9ucBhBXEiwA6N8nYBI2d6J-u5nFOY-GpkIPF90ZlZQcbtUp3Q-nId1OsBG9gBhZn8kSxRoCOVYQAvD_BwE")

if golfer_info == "cheap advanced":
    print("Ok, I think I have a set of clubs for you. Opening webpage....")
    time.sleep(3)
    webbrowser.open("https://stix.golf/products/stix-golf-iron-set-5-pw?variant=39287801643074&currency=USD&nbt=nb%3Aadwords%3Ax%3A17528803185%3A%3A&nb_adtype=pla&nb_kwd=&nb_ti=&nb_mi=299733814&nb_pc=online&nb_pi=shopify_US_6554966589506_39287801643074&nb_ppi=&nb_placement=&nb_si={sourceid}&nb_li_ms=&nb_lp_ms=&nb_fii=&nb_ap=&nb_mt=&gclid=CjwKCAiAv9ucBhBXEiwA6N8nYBI2d6J-u5nFOY-GpkIPF90ZlZQcbtUp3Q-nId1OsBG9gBhZn8kSxRoCOVYQAvD_BwE")


#Mid-Spender Section
if golfer_info == "mid-spender beginner":
    print("Ok, I think I have a set of clubs for you. Opening webpage....")
    time.sleep(3)
    webbrowser.open("https://www.amazon.com/TaylorMade-Graphite-Fujikura-Ventus-Regular/dp/B082PPVJJR/ref=asc_df_B082PPVJJR/?tag=hyprod-20&linkCode=df0&hvadid=416978016675&hvpos=&hvnetw=g&hvrand=17591862160217294192&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1015399&hvtargid=pla-936004434167&psc=1&tag=&ref=&adgrpid=99610405088&hvpone=&hvptwo=&hvadid=416978016675&hvpos=&hvnetw=g&hvrand=17591862160217294192&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1015399&hvtargid=pla-936004434167")

if golfer_info == "mid-spender intermediate":
    print("Ok, I think I have a set of clubs for you. Opening webpage....")
    time.sleep(3)
    webbrowser.open("https://ping.com/en-us/clubs/irons/g410")

if golfer_info == "mid-spender advanced":
    print("Ok, I think I have a set of clubs for you. Opening webpage....")
    time.sleep(3)
    webbrowser.open("https://mizunogolf.com/us/golf-clubs/jpx921-series/jpx921-hot-metal/")


#Expensive Section
if golfer_info == "expensive advanced":
    print("Ok, I think I have a set of clubs for you. Opening webpage....")
    time.sleep(3)
    webbrowser.open("https://www.titleist.com/product/t400/544C.html")

if golfer_info == "expensive advanced":
    print("Ok, I think I have a set of clubs for you. Opening webpage....")
    time.sleep(3)
    webbrowser.open("https://www.titleist.com/product/t200/550C.html")

if golfer_info == "expensive advanced":
    print("Ok, I think I have a set of clubs for you. Opening webpage....")
    time.sleep(3)
    webbrowser.open("titleist.com/product/t100/548C.html")