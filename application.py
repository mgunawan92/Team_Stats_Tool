# Import from constants.py the players' data to be used within your program.
import constants
from copy import deepcopy

# deepcopy function obtained from https://stackoverflow.com/questions/14204326/how-to-copy-a-dictionary-of-lists
# read the existing player data from the PLAYERS constants provided in constants.py
# clean the player data without changing the original data
# save it to a new collection
player_collection = deepcopy(constants.PLAYERS)
teams_collection = constants.TEAMS[:]

# Create a clean_data function
def clean_data():
    
    for player in player_collection:
        
        # obtain height slice from each dictionary in list of PLAYERS
        height = (player["height"][0:2])
        
        # convert height into int per requirements
        int_height = int(height)
        
        # insert converted integer height into each dictionary in player collection
        player["height"] = int_height
        
        # convert experience/inexperienced to bool values per requirements
        if player["experience"] == "YES":
            player["experience"] = True
            
        elif player["experience"] == "NO":
            player["experience"] = False
            
        # store guardians into guardian list
        # when cleaning the data, clean the guardian field as well before adding it into your newly created collection, split up the guardian string into a List
        player['guardians'] = player['guardians'].split(" and ")

# Create a balance_teams function
def balance_teams():

    # create lists for all teams to store values
    panthers = []
    bandits = []
    warriors = []
    
    # create lists for both experienced and inexperienced players to store values
    experienced_players = []
    inexperienced_players = []
    
    # sort by experienced/inexperienced and append to corresponding list
    for player in player_collection:
        
        if player["experience"] == True:
            experienced_players.append(player)
            
        elif player["experience"] == False:
            inexperienced_players.append(player)
    
    # append values from both experienced and inexperienced lists into team lists using pop()
    while experienced_players:
        panthers.append(experienced_players.pop())
        bandits.append(experienced_players.pop())
        warriors.append(experienced_players.pop())
        
    while inexperienced_players:
        panthers.append(inexperienced_players.pop())
        bandits.append(inexperienced_players.pop())
        warriors.append(inexperienced_players.pop())
        
    teams = [panthers, bandits, warriors]
    return teams

if __name__ == "__main__":

    # clean data and balance teams (for both number of players and number of experienced/inexperienced players)
    clean_data()        
    teams = balance_teams()
    
    #start while loop for repeated prompts
    while True:
    
        # function for displaying three teams when Option 1 in first prompt is selected
        def display_teams():
            for index, team in enumerate(constants.TEAMS, start=1):
                print("{}) {}".format(index, team))
            print()
        
        # function for creating list of experienced players based on selected team
        def experienced(teams):
            exp = []
            for player in teams:
                if player["experience"] == True:
                    exp.append(player)
            return exp
        
        # function for creating list of inexperienced players based on selected team
        def inexperienced(teams):
            inexp = []
            for player in teams:
                if player["experience"] == False:
                    inexp.append(player)
            return inexp
        
        # function for calculating average height based on selected team
        def average(teams):
            total_height = 0
            for player in teams:
                total_height += player["height"]
            average_height = round(total_height/len(teams))
            return average_height
        
        # function for displaying team stats within dunder main
        def display_team_info(team_selection):
            team_name = teams_collection[int(team_selection)-1]
            team_selection = teams[int(team_selection) - 1]
            experienced_players = experienced(team_selection)
            inexperienced_players = inexperienced(team_selection)
            average_height = average(team_selection)
            
            # creating list for players on team based on team selection
            names_of_players = []
            for player in team_selection:
                names_of_players.append(player["name"])
            players_list = ', '.join(names_of_players)
            
            # creating list for guardians corresponding to players on team based on team selection
            guardians = []
            for player in team_selection:
                guardians += (player["guardians"])
            guardian_list = ', '.join(guardians)
    
            # print stats
            print("\n\nTeam: {} Stats".format(team_name))
            print("-" * 20)
            print("Total players: {}".format(len(team_selection)))
            print("Total experienced: {}".format(len(experienced_players)))
            print("Total inexperienced: {}".format(len(inexperienced_players)))
            print("Average height: {} inches".format(average_height))
            print("\nPlayers on Team: {}".format(players_list))
            print("\nGuardians: {}\n".format(guardian_list))
        
        print("\nBASKETBALL TEAM STATS TOOL")
        print ("\n---- MENU----\n")
        print("Here are your choices: \n\n1) Display Team Stats. \n2) Quit")
        option = input("\nEnter an option > ")

        if option == "1":
            print("\n")
            display_teams()
            pass
        
        # break out of while loop if user decides to exit
        elif option == "2":
            print("\nGoodbye\n")
            break

        # notify user of invalid response, then repeat loop
        else:
            print("\nInvalid Option. Try again.\n")
            continue

        # start new while loop once user has selected option 1
        while True:
            team_selection = input("Enter an option > ")
            if team_selection == "1" or team_selection == "2" or team_selection == "3":
                display_team_info(team_selection)
                break
            else:
                print("\nThat isn't a valid option, please enter an option corresponding to one of the listed teams.\n  ")
                continue
                
        # start new while loop once user has selected finished viewing stats to see if they want to start again
        while True:
            continue_or_not = input("\nRestart Stats Tool? (Y/N)\n ")
            if continue_or_not == "Y" or continue_or_not == "y":
                exit = "No"
                break
            elif continue_or_not == "N" or continue_or_not == "n":
                exit = "Yes"
                break
            else:
                print("\nNot a valid response. Please try again\n")
                continue
                
        if exit == "Yes":
            print("\nGoodbye\n")
            break
        elif exit == "No":
            continue
        else:
            print("\nInvalid Option\n")
