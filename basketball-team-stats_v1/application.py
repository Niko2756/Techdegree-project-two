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
    num_players_team = len(dataThatHasBeenCleaned) / len(theTeams)
    theTeamsBalanced = []
    for x in theTeams:
        teamRoster = {}
        for y in range(num_players_team):
            teamRoster.append(dataThatHasBeenCleaned.pop())
        theTeamsBalanced.append(teamRoster)

    return theTeamsBalanced

def main():
    clean_the_data()
    balance_the_teams()


if __name__ == '__main__':
    main()

