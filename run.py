import gspread
from google.oauth2.service_account import Credentials
from pyfiglet import Figlet

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('EPL_prediction')

stats = SHEET.worksheet('stats')

data = stats.get_all_records(head=1)
# change to get all records (head=1)
# Then use the data dictionaries to search for data"

# print(data)


def get_available_teams():
    av_teams = []
    for dic in data:
        HomeTeam = dic['HomeTeam']
        if HomeTeam not in av_teams:
            av_teams.append(HomeTeam)
    return av_teams


def print_available_teams():
    av_teams = get_available_teams()
    # Add validate function here if valid...
    print("The available teams are:\n")
    for team in av_teams:
        print(team)


def get_teams():
    """
    Get home and away teams input from the user.
    Run a while loop to collect two valid teams from the user
    via the terminal, which must be strings matching the specified teams
    The loop will repeatedly request data, until it is valid.
    """
    
    while True:
        choice = input("Press 's' to start or 't' to view possible teams:\n")
        if choice == 's':

            print("Enter the two teams, seperated by a comma:")
            print("Example: Arsenal, Aston Villa\n")

            data_str = input("Enter the teams:\n")
            teams = data_str.split(",")
        # if validate_data(teams):
        #     print("Teams are valid!")
        #     break
            break
        elif choice == 't':
            print_available_teams()
            print("")

        else:
            print("Invalid entry - 's' to start or 't' for possible teams")

    return teams


def startText():
    f = Figlet(font='slant')
    print(f.renderText('EPL MATCH PREDICTOR'))
    print("Welcome to EPL Match Predictor \n")
    print("Delivering profitable football predictions since 2023 \n")
    print("Enter opposing teams to receive a guaranteed* prediction \n")
    # print("Available teams are:\nArsenal, Aston Villa, Bournemouth, Brentford, Brighton,\nChelsea, Crystal Palace, Everton, Fulham, Leeds,\nLeicester, Liverpool, Man City, Man United, Newcastle,\nNottm Forest, Southampton, Tottenham, West Ham, Wolves\n")


def main():
    startText()
    teams = get_teams()
    # av_teams = get_available_teams()
    print(teams)
    # print(av_teams)


main()

