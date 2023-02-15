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


def update_worksheet(data,worksheet):
    """
    Takes all inputed answers and uploads them to the linked worksheet
    """
    print("Updating Portfolio worksheet with answers given. Please wait \n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print("Portfolio worksheet updated successfully.\n")

def return_answers():
    """
    Retrieves the data entered by the user by obtaining the last row of the google doc 
    and informs the user of their answer.
    """

    q1_answers_entered = SHEET.worksheet('Answers').col_values(1)[-1]
    q2_answers_entered = SHEET.worksheet('Answers').col_values(2)[-1]
    q3_answers_entered = SHEET.worksheet('Answers').col_values(3)[-1]
    q4_answers_entered = SHEET.worksheet('Answers').col_values(4)[-1]
    q5_answers_entered = SHEET.worksheet('Answers').col_values(5)[-1]

    print("Thank you for your cooperation.")
    print("For your information, the answers you gave were:\n")

    print(f"Q1: {q1_answers_entered}")
    print(f"Q2: {q2_answers_entered}")
    print(f"Q3: {q3_answers_entered}")
    print(f"Q4: {q4_answers_entered}")
    print(f"Q5: {q5_answers_entered}\n")

    print("Goodbye!!!")

def main():
    """
    Runs all main functions
    """

    data = get_answers()
    update_worksheet(data, 'Answers')
    return_answers()


main()