# URL shortener


## Requirements
- Users are able to enter a url into an input box on your website's front page
- This website generate a shortened path at which a User can access their url
- Store this shortened path and it's longer counterpart in a database
- If User tries to access your website with a path you have stored in your database, they should get rerouted to the URL it relates to
- If User tries to access your website with a path you do not have stored in your database, they will get rerouted to the homepage where they can create a new short URL

## Usage and installation

- Use ```pipenv install``` to install dependencies
- Use ```pipenv shell``` 
- cd to repo folder
- ```cd url_shortener```
- run ```python manage.py runserver```
- You need to add http/https at the begining of your url 


## Bugs

- Wasn't able deploy the website to heroku

## Wins 

- All the project requirments were met
- A short url would be generated 
- Clicking on the url will redirect to desired website
- The shortened link can be used as many time as required


## challenges
- Getting the shortend url generated
- Redirect to desired website by clicking on shortend url
- Attempt to deploy on heroku 

## Future features
- Remove the need to add http/https for urls 
- More styling

