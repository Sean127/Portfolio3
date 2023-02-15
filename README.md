# Portfolio 3 project
Welcome to my third portfolio project. For this assignment, I created a simple 5 question quiz within python. It is a simple programme that asks the user for five inputs to easy questions. It then uploads them to a linked Google Doc and reads the users answers back to them before finishing. you can find a web viewable version of the programme [here](https://seanportfolio3.herokuapp.com/) 

## Features
### Existing Features
- Clear instruction given at the beginnng of the programme
- Updates given as inputs are uploaded to google doc
- Answers read back to the user following the conclusion of the data upload

### Future Feature
- Showing the user how there votes compared to others with average comparisons

## Testing 
i have tested the programme in the following ways
- Passing it throught a PEP8 linter and passing without any major issues
- Giving invalid inputs and ensuring the errors are picked up
- Tested both in a python terminal and on Heroku

### Bugs 
#### Solved Bugs 

- During development, I encountered an amount of difficulty grabing the last entered data into the google doc. I was able to solve this by adding [-1] to the end of the following code (q1_answers_entered = SHEET.worksheet('Answers').col_values(1)[-1])

#### Unsolved Bugs 

- There is currently an error entering "no" for all five questions will raise a ValueError. As of deployment, I was unable to solve this issue

## Deployment

I used the Code Institute provided mock terminal for deployment via Heroku
- Steps for deployment
    - Create a Heroku app
    - Setup two _Config Var_ elemnts. One called CREDS with the contents of the creds.json file
    - The second called PORT and set to 8000
    - Link the Heroku app to my GitHub repository
    - Deploy the app
## Credits 
- Code Institute for the web based deployment terminal
- The Love Sandwiches project for elements of the code regarding uploading data to Google Docs