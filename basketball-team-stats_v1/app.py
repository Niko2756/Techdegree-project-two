import constants
import fuctions

def main():
	data = constants.PLAYERS.copy()
	theTeams = constants.TEAMS.copy()
	dataThatHasBeenCleaned = fuctions.clean_the_data(data)
	theTeamsBalanced, num_players_team = fuctions.balance_the_teams(theTeams, dataThatHasBeenCleaned)
	theTeamsBalancedButJustNames = fuctions.info_stripper_leave_just_name(theTeamsBalanced, num_players_team)
	print("basketball team stat tool")
	while True:
		print("\n\n-----MENU-----\n\n")
		print("Here are your choices:\n")
		userInput = fuctions.your_first_choice()
		if userInput == 1:
			for x, team in enumerate(theTeams):
				print(f'{x+1}) {team}')
			secondUserInput = fuctions.your_second_choice(theTeams)
			print(f"\nTeam: {theTeams[secondUserInput-1]}\n")
			print(', '.join(map(str, theTeamsBalancedButJustNames[secondUserInput-1])))
			print(f"Total players: {len(theTeamsBalancedButJustNames[secondUserInput-1])} \n")
		else:
			print("Thank you so much for using this thing.\nThis app has been coded by Niko.")
			break



if __name__ == '__main__':
	main()