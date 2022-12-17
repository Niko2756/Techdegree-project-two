import constants
import fuctions

def main():
	data = constants.PLAYERS.copy()
	theTeams = constants.TEAMS.copy()
	dataThatHasBeenCleaned = fuctions.clean_the_data(data)
	#print(dataThatHasBeenCleaned)
	theTeamsBalanced, num_players_team = fuctions.balance_the_teams(theTeams, dataThatHasBeenCleaned)
	theTeamsBalancedButJustNames = fuctions.info_stripper_leave_just_name(theTeamsBalanced, num_players_team)
	print()




if __name__ == '__main__':
	main()