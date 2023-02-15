import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Portfolio_3')

answer_data = []

def get_answers():
    """
    Gets answer inputs from the users.
    Asks 5 questions for the user to answer "yes" or "no". 
    It checks that all the inputs are valid and submits them to the documnet.
    """

    while True:
        print('You will now be asked 5 questions.')
        print('Answer each question with either "yes" or "no" in lowercase only.\n')

        q1_data = input("Q1: Do you exercise? \n")
        answer_data.append(q1_data)
        q2_data = input("Q2: Do you play an instrument? \n")
        answer_data.append(q2_data)
        q3_data = input("Q3: Do you keep a diary? \n")
        answer_data.append(q3_data)
        q4_data = input("Q4: Have you cried in the last week? \n")
        answer_data.append(q4_data)
        q5_data = input("Q5: Do you have a tattoo? \n")
        answer_data.append(q5_data)

        if validate_answers(answer_data) == True:
            break

    return answer_data

def validate_answers(answer_data):
    """
    Validates the inputs of the user by ensuring all inputs are either "yes" or "no"
    Raises a ValueError is an incorrect value is entered and repeats get_answers()
    """

    try:
        [answer for  answer in answer_data]
        if ("yes" or "no") not in answer_data :
            answer_data.clear()
            raise ValueError(
                "Answer entered not yes or no. Please try again.\n"
            )

    except ValueError as e:
        print(f"Invalid data: {e}")
        return False
        
    return True       
