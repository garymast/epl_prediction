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
        self.wins = 0
        self.draws = 0
        self.losses = 0
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
                    
                    # currentWins = self.wins
                    # self.wins = currentWins + 1
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
                self.wins += 1

            elif i == "D":
                if not count == 0:
                    tempMomentum += count/3
                    self.draws += 1

            else:
                self.losses += 1

            count -= 1
            if count == 0:
                self.momentum = round(tempMomentum)
                break

    def print(self):
        print(self.results)
        print(self.wins)
        print(self.draws)
        print(self.losses)
        print(self.name)
        print(self.num_games)
        print(self.momentum)


cTeam = Team("Liverpool")
cTeam.addData()


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

            print("Enter the two teams, seperated by a comma (no spaces):")
            print("Example: Arsenal,Aston Villa\n")

            data_str = input("Enter the teams:\n")
            teams = data_str.split(",")

            if validate_data(teams):
                print("Teams are valid!")
                teamOne = Team(teams[0])
                teamOne.addData()
            
                teamTwo = Team(teams[1])
                teamTwo.addData()

                break

        elif choice == 't':
            print_available_teams()
            print("")

        else:
            print("Invalid entry - 's' to start or 't' for possible teams")

    return teamOne, teamTwo


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    av_teams = get_available_teams()
    try:
        if len(values) != 2:
            raise ValueError(
                f"Exactly 2 teams required, you provided {len(values)}"
            )

        # print(values)
        # print(av_teams)
        for value in values:
            if value not in av_teams:
                raise ValueError(
                    f"{value} is not a valid team"
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
 

def calcWinner(teamOne, teamTwo):
    """
    Predicts the game winner based on current momentum
    """
    
    if teamOne.momentum > (teamTwo.momentum + 5):
        print(f"{teamOne.name} should win this game,\nhaving won {teamOne.wins} of their past 10 games")

    elif teamTwo.momentum > (teamOne.momentum + 5):
        print(f"{teamTwo.name} should win this game,\nhaving won {teamTwo.wins} of their past 10 games")

    else:
        print(f"{teamOne.name} and {teamTwo.name} are in similar form,\nThis should be a draw")    


def main():
    """
    Calls the required functions to run the program
    """

    startText()
    teamOne, teamTwo = get_teams()
    calcWinner(teamOne, teamTwo)
    # teamOne.print()
    # teamTwo.print()


main()

