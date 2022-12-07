# wordpress-analyzer-save-to-database
A program that crawls a list of websites and saves themes ,scripts ,plugins, and more on a database


Hi everyone,

The code gets data from Wordpress sites and stores them on a database

The code receives a list of urls from the website_list.txt and checks the following parameters on each of them:
	-it checks if it's a Wordpress website
	-it saves the the wordpress theme
	-it checks if the website uses Google Analytics
	-it creates a list of all the Wordpress plugin that are used
	-it creates a list of all the scripts located in the page

The algorithm prints the data above for each of the websites and saves them on a database.

For non-Wordpress websites it saves the url on table nowp

If it's a Wordpress website it gives the website a unique id, it saves its url, it saves if it has Google Analytics, and the name of its theme on table w_list
Additionally, it saves the list of plugins on table plugins with the id of the url and the name of the plugin.
Same principle applies with the list of scripts saved on table scripts

HOW TO GET STARTED

First create the database in your server by running the query database_creation.sql

Secondly, you need to put the credentials of your server in the main.py file. Place your host address, username, and password in parameters
MY_HOST,MY_USER,MY_PASS

Thirdly, make sure to pip install the libraries in header

Fourthly, place the list of websites in the website_list.txt

Finally, run main.py
	
