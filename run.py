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


class Team:

    def __init__(self, team):
        """
        Class constructor
        """

        self.results = []
        self.name = team
        self.num_games = None
        self.momentum = None

    def addData(self):
        """
        Run functions to add relevant data to Team object
        """

        self.addResults()
        self.calcMomentum()

    def addResults(self):
        """
        Add results and number of games to the
        Team object
        """

        count = 0
        for dic in data:
            homeTeam = dic['HomeTeam']
            awayTeam = dic['AwayTeam']
            result = dic['FTR']
            if homeTeam == self.name or awayTeam == self.name:
                count += 1
                if homeTeam == self.name and result == 'H':
                    self.results.append('W')
                elif homeTeam == self.name and result == 'A':
                    self.results.append('L')
                elif awayTeam == self.name and result == 'A':
                    self.results.append('W')
                elif awayTeam == self.name and result == 'H':
                    self.results.append('L')
                else:
                    self.results.append('D')

        self.num_games = count

    def calcMomentum(self):
        """
        Calculate the momentum of the team, assigning
        more weight to recent results
        """
        count = 10
        tempMomentum = 0

        for i in reversed(self.results):

            if i == "W":
                tempMomentum += count
            elif i == "D":
                if not count == 0:
                    tempMomentum += count/3

            # print(i)
            # print(count)
            count -= 1
            if count == 0:
                # print(f"TempMomentum is: {tempMomentum}")
                self.momentum = round(tempMomentum)
                break

    def print(self):
        print(self.results)
        print(self.name)
        print(self.num_games)
        print(self.momentum)


cTeam = Team("Liverpool")
cTeam.addData()
cTeam.print()


def get_available_teams():
    """
    Return a list containing all the teams in the league, in alphabetical order
    """

    av_teams = []
    for dic in data:
        HomeTeam = dic['HomeTeam']
        if HomeTeam not in av_teams:
            av_teams.append(HomeTeam)
    av_teams.sort()
    return av_teams


def print_available_teams():
    """
    Print the available teams to the terminal
    """

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
        if validate_data(teams):
            print("Teams are valid!")
            # break
            break
        elif choice == 't':
            print_available_teams()
            print("")

        else:
            print("Invalid entry - 's' to start or 't' for possible teams")

    return teams


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        if len(values) != 2:
            raise ValueError(
                f"Exactly 2 teams required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def startText():
    """
    Function to print start text to the terminal on running the program
    """

    f = Figlet(font='slant')
    print(f.renderText('EPL MATCH PREDICTOR'))
    print("Welcome to EPL Match Predictor \n")
    print("Delivering profitable football predictions since 2023 \n")
    print("Enter opposing teams to receive a guaranteed* prediction \n")
    # print("Available teams are:\nArsenal, Aston Villa, Bournemouth, Brentford, Brighton,\nChelsea, Crystal Palace, Everton, Fulham, Leeds,\nLeicester, Liverpool, Man City, Man United, Newcastle,\nNottm Forest, Southampton, Tottenham, West Ham, Wolves\n")


def main():
    """
    Calls the required functions to run the program
    """

    startText()
    teams = get_teams()
    # av_teams = get_available_teams()
    print(teams)
    # print(av_teams)


main()

