# Houston Music Venue Scraper
A grouping of website scrapers that will scrape the websites of different popular Houston Texas music venues and save event name, event datem, and any specific venue location from that website.

I am new to coding, so the code contained within this repo will probably be inffecient, but I am using this project as an opprtunity to learn, improve, and educate others on coding. I will try my best to over emphasize comments in the code to try to explain what each line of code does. I am mostly using AI to help educate me on how to code this. Any advice is welcomed. 

Long term, I would like this code to:

1. Scrape each website every morning
    1. Fully load page including any JavaScript
    2. Copy the html
    3. If any issues, save an error flag but continue
2. Save the desired data into a database only adding new events that were not already in the database, or updating any that have been changed.
    1. Look through the html and find every instance of an event
    2. Extract the event name, date, and venue for each instance of an event
    3. Save the information into a database
    4. FUTURE UPGRADE: Find a way to compare database and only add or update items, do not duplicate
3. FUTURE UPGRADE: Make some kind of web based user interface to nicely view and sort all of the upcoming events
5. FUTURE UPGRADE: Make a Spotify and/or Apple Musics playlist with a couple of the top songs of each artist coming to a venue.

Venues I would like to scrape:

* 713 Music Hall (https://www.713musichall.com/shows)
* Bayou Music Center (https://www.bayoumusiccenter.com/shows)
* White Oak Music Hall (https://whiteoakmusichall.com/#event-listing)
* House of Blues Houston (https://www.houseofblues.com/houston/concert-events)
* The Continental Club Houston (https://continentalclub.com/houston)
* Shoeshine Charley's Big Top Lounge (https://continentalclub.com/bigtop)
* The Heights Theater (https://www.prekindle.com/theheights/)
* Dan Electro's (https://www.danelectrosheights.com/events)
* McGonigel's Mucky Duck (https://www.mcgonigels.com/#shows)
* The Armadillo Palace (https://thearmadillopalace.com/live-music/)
* Last Concert Cafe (https://lastconcert.com/)
