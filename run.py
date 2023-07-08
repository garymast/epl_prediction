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

data = stats.get_all_values()


print(data)


def get_available_teams():
    av_teams = stats.col_values(4)
    # get available teams from spreadsheet

    av_teams = list(dict.fromkeys(av_teams))
    # Remove duplicates from teams list
    return av_teams


def get_teams():
    """
    Get home and away teams input from the user.
    Run a while loop to collect two valid teams from the user
    via the terminal, which must be strings matching the specified teams
    The loop will repeatedly request data, until it is valid.
    """
    
    while True:
        print("Enter the two teams, seperated by a comma:")
        # print("Data should be six numbers, separated by commas.")
        print("Example: Arsenal, Aston Villa\n")

        data_str = input("Enter the teams:\n")
        teams = data_str.split(",")
        # if validate_data(teams):
        #     print("Teams are valid!")
        #     break
        break
    return teams


def startText():
    f = Figlet(font='slant')
    print(f.renderText('EPL MATCH PREDICTOR'))
    print("Welcome to EPL Match Predictor \n")
    print("Delivering profitable football predictions since 2023 \n")
    print("Enter opposing teams to receive a guaranteed* prediction \n")
    print("Available teams are:\nArsenal, Aston Villa, Bournemouth, Brentford, Brighton,\nChelsea, Crystal Palace, Everton, Fulham, Leeds,\nLeicester, Liverpool, Man City, Man United, Newcastle,\nNottm Forest, Southampton, Tottenham, West Ham, Wolves\n")


def main():
    startText()
    teams = get_teams()
    av_teams = get_available_teams()
    print(teams)
    print(av_teams)


main()

