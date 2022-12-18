def clean_the_data(theList):
    cleaned = []
    for key in theList:
        fixed = {}
        fixed["name"] = key["name"]
        fixed["guardians"] = key["guardians"]
        if key["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        
        fixed["height"] = int(key["height"].split(" ")[0])
        
        cleaned.append(fixed)
    return cleaned


def balance_the_teams(theTeams, dataThatHasBeenCleaned):
    num_players_team = int(len(dataThatHasBeenCleaned) / len(theTeams))
    theTeamsBalanced = []
    for x in theTeams:
        teamRoster = []
        for y in range(num_players_team):
            teamRoster.append(dataThatHasBeenCleaned.pop())
        theTeamsBalanced.append(teamRoster)

    return theTeamsBalanced, num_players_team


def info_stripper_leave_just_name(theTeamsBalanced, num_players_team):
    theTeamsBalancedButJustNames = []
    for x in range(len(theTeamsBalanced)):
        holdingList = []
        for y in range(num_players_team):
           holdingList.append(theTeamsBalanced[x][y].get("name"))

        theTeamsBalancedButJustNames.append(holdingList)

    return theTeamsBalancedButJustNames


def your_first_choice():
    while True:
        try:
            userInput = int(input("Input 1 to display team stats\nInput 2 to quit program\n(or press enter to go straight through): ")or 1)
        except ValueError:
            print("Hey I don't think that's even a number. \nGo ahead and enter the number of userInput again,\nbut make sure it's like a actual number this time:\n\n")
            continue
        if userInput not in (1,2):
            print("\nthat is not a viable option\n")
            continue
        else:
            return userInput


def your_second_choice(theTeams):
    while True:
        try:
            userInput = int(input("Please choose from the above options which team you would like to see: "))
        except ValueError:
            print("Hey I don't think that's even a number. \nGo ahead and enter the number of userInput again,\nbut make sure it's like a actual number this time:\n\n")
            continue
        if userInput not in range(1, (len(theTeams)+1)):
            print("\nthat is not a viable option\n")
            continue
        else:
            return userInput


def main():
    clean_the_data()
    balance_the_teams()
    info_stripper_leave_just_name()
    your_first_choice()
    your_second_choice()

if __name__ == '__main__':
    main()

