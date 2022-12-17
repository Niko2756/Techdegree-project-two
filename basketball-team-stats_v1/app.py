import constants
import application

def main():
	data = constants.PLAYERS.copy()
	theTeams = constants.TEAMS.copy()
	dataThatHasBeenCleaned = application.clean_the_data(data)
	#print(dataThatHasBeenCleaned)
	theTeamsBalanced = application.balance_the_teams(theTeams, dataThatHasBeenCleaned)




if __name__ == '__main__':
	main()