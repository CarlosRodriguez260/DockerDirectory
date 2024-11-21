from selenium import webdriver
from bs4 import BeautifulSoup
import time
def get_ranks(epicName, verifiedName):
    epicName.replace(" ", "%20")
    url = "https://rocketleague.tracker.network/rocket-league/profile/epic/" + epicName + "/overview"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")
    time.sleep(6)
    # Test if player name is invalid
    if verifiedName == 0:
        error404 = soup.find("div", class_="content content--error")
        try:
            test = error404.text
            print("Invalid player name...")
            return " "
        except AttributeError:
            print("Valid player name. Searching for rank information...")
            verifiedName = 1
    
    # Finds information of 1v1 rank
    try:
        test = soup.find("table", class_="trn-table")
        p = test.text
    except AttributeError:
        driver.quit()
        return get_ranks(epicName, verifiedName)
    
    mmr = soup.find("table", class_="trn-table")
    duelIndex = mmr.text.find("Duel")
    duelInformation = ""
    for character in mmr.text[duelIndex::]:
        if character != "#":
            duelInformation = duelInformation + character
        else:
            break
    
    # Finds information of 2v2 rank
    doublesIndex = mmr.text.find("Doubles")
    doublesInformation = ""
    for character in mmr.text[doublesIndex::]:
        if character != "#":
            doublesInformation = doublesInformation + character
        else:
            break

    # Finds information of 3v3 rank
    standardIndex = mmr.text.find("Standard")
    standardInformation = ""
    for character in mmr.text[standardIndex::]:
        if character != "#":
            standardInformation = standardInformation + character
        else:
            break
    infoArray = [duelInformation, doublesInformation, standardInformation]
    driver.quit()
    return infoArray

proceed = 1
while proceed == 1:
    name = input("Type the epic username of the player: ")
    infoArray = get_ranks(name, 0)
    if infoArray == " ":
        continue
    print("1v1 Rank:" + " " + infoArray[0][9::])
    print("2v2 Rank:" + " " + infoArray[1][12::])
    print("3v3 Rank:" + " " + infoArray[2][13::])
    again = input("Would you like to look up another player's rank? (Y for yes; N for no): ")
    if again == "Y":
        print()
    else:
        proceed = 0