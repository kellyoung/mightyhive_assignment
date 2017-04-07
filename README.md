# mightyhive_assignment
Mini Flask App for MightyHive's Coding Assignment

### Explanation
**1. Shows a user an image of either a red or blue ball upon visiting the page. This should be random, with a 50/50 split of users.**
I tried to keep this part client-side. The function chooseColor will choose a random number between 0 and 1 to determine if the user will be shown red or blue. The function is called if there is no key "color" in the document's cookie, taken to mean this is the first time the user visits the page. I created a server to host my page because Google Chrome ignores cookies coming from local files.

**2.  Determine whether the user saw a red or a blue ball, and the next time a user visits the page shows them the same color ball of what they saw previously.**
In the function showInfo, if the key "color" is not in the cookie, it will store the color as well as a count of 1 in the cookie. If there is already the key "color" in the cookie, this is taken to mean that the user has been on the site before. Therefore, the cookie's "count" key is incremented by 1. The function will also edit the display, and provide text output of what color ball the user is seeing and how many times they have seen it. All of this information is stored client-side.

**3.  This cookie should also record how many times a user has seen each color of ball. You should be able to provide a report on users and number of times they saw each color ball.**
As mentioned earlier, I have provided text output to update the user for how many times they have seen the ball of their initial color.
In order to keep a report of all users and the number of times they saw their ball, I created a Flask App, and utilized Flask's session capabilities. I also utilized a psql database and SQLAlchemy in order to keep track of the session information such as color the user of the session saw, the number of times the user saw the ball, a unique id, and the date and time they first visited. Each session is unique to the browser by default and a session ends if the browser is closed. When a user visits the route, it will always check if the user is in session or not. If the user is not in session, a new user is created and the database is updated. If there is a user in session, then the app queries the databases for the id stored in the session in order to update the count.
When visiting, the "/stats" route, a table is shown with the information stored in the database. Creating a database allowed me to gather information from all users/browsers opening my page, so I could have all my information in one place.

### Installation
