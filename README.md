# EPL Match Predictor

 EPL Match Predictor is a terminal program which predicts the outcome of Premier League Matches, using the teams current form to calculate the likelihood of them winning.

[Link To Live Project](https://gm-epl-prediction-dedf30f0a371.herokuapp.com/)

# How it works

The user is prompted to enter two teams from the current season of the English Premier League.

The program then validates the entered teams and calculates a match prediction based on the recent form of both teams.

The user is then given options to enter further team selections.

# Features

- Welcome Message
  - A welcome message is written to the terminal, providing the user with guidelines on the use of the program

![Welcome Message](images/WelcomeMessage.jpg) 

- Accepts user input
- View Possible teams
  - The user can press 't' to view all available teams, sorted alphabetically

![Welcome Message](images/WelcomeMessage.jpg) 

- Input validation and error-checking
  - You cannot enter the same team for both home and away
  - There must be exactly two teams entered
  - The teams entered nmust match exactly, two teams in the available teams list
- Google Sheets and Drive API Connectivity
- Data maintained in class instances

# Future Feaures

- Write each prediction to google sheets and provide a summary of the predictions on user request
- Add additional analysis to improve predictions. For example, "Home Advantage"
- Scrape current weeks fixtures from the web and automatically predict all games
- Improve the programs UI by adding colour and additional styling

### Existing Features

- __Navigation Bar__

  - Featured on all three pages, the fully responsive navigation bar includes links to the Logo, Services/home, Technologies, Contact page and also a functional phone  number. It is identical in each page to allow for easy navigation.
  - This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button. 

![Nav Bar](assets/images/readme_images/navbar.jpg)

- __The landing page image__

  - The landing page includes a striking photograph of a drone which is one of the key pieces of equipment that this company would use.
  - This section also includes cover text with the company slogan.

![Landing Page](assets/images/readme_images/landing-image.jpg)

- __Services Section__

  - The services section provides a brief overview of the companies offerings, along with an interactive list of the geospatial services offered by the company.
  - The user can click on a service and be redirected to a wikipedia page with further information about that service.

![Services Section](assets/images/readme_images/services.jpg)

- __The Footer__ 

  - The footer section includes links to the relevant social media sites for Delta Geospatial. The links will open to a new tab to allow easy navigation for the user. 
  - On hover, the link icons highlight to the relative colour of the social media site.

![Footer](assets/images/readme_images/footer.jpg)

- __Technologies__

  - The technologies page will provide the user with a capability statement and a list of technologies used by the company. These are represented with images and a brief description of the technolgy.
  - This will highlight to the user that only state of the art equipment and software is being utilised.

![Technologies](assets/images/readme_images/technologies.jpg)

- __The Contact Page__

  - This page will allow the user to send a message to the company via a form and also view phone, email and street address.
  - There is a google map on the page which will be of instant value to the user.

![Contact](assets/images/readme_images/contact-page.jpg)

### Features Left to Implement

- Individual pages for each service will be added in future as opposed to the links to wikipedia
- A Projects page will be added to highlight some recent projects which the company has successfully undertaken.

## Testing 

- Testing was carried out on all three pages of the website. The testing was carried out on the following devices:
  - Desktop
  - Tablet
  - Mobile
- Tested using the lightroom dev tool in Google Chrome.

![Lighthouse](assets/images/readme_images/lighthouse.jpg)

### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgarymast.github.io%2Fgeospatial-co%2Findex.html)

![HTML Validate](assets/images/readme_images/html-check.jpg)

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fgarymast.github.io%2Fgeospatial-co%2Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

![CSS Validate](assets/images/readme_images/css-check.jpg)

### Bugs and Issues

Debugging and troubleshooting was done continuously throughout the development process. All known bugs have now been removed.

## Deployment

The site was deployed using Code Institute's mock terminal for Heroku:
- Steps for Deployment:
  - Clone the Code Institute Github Template
  - Create Google Sheet and add relevant historical football data
  - Enable Google Drive and Sheets API's in Google Cloud Services
  - Create a New Heroku App
  - Set the buildbacks to Python and NodeJS in that order
  - Link the Heroku App to the repository
  - Click on Deploy

The live link can be found here - https://garymast.github.io/geospatial-co/index.html

# Credits 

- Code Institute for the Deployment Terminal

# THANK YOU!