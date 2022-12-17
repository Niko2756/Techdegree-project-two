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

#print(theTeamsBalanced[0][5].get("name"))


def info_stripper_leave_just_name(theTeamsBalanced, num_players_team):
    theTeamsBalancedButJustNames = []
    for x in range(len(theTeamsBalanced)):
        holdingList = []
        for y in range(num_players_team):
           holdingList.append(theTeamsBalanced[x][y].get("name"))

        theTeamsBalancedButJustNames.append(holdingList)

    return theTeamsBalancedButJustNames


def main():
    clean_the_data()
    balance_the_teams()
    info_stripper_leave_just_name()


if __name__ == '__main__':
    main()

