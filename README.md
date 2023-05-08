#matala3

Assignment 3 – Web services 
General Instructions:
The assignment should be performed independently – no collaborations are allowed.
Late submission will lead to a reduction in your grade – 5 points per day. 
Assignment will written in a Jupyter Notebook (.IPYNB file), which will be uploaded to GitHub. 
In the course’s Moodle you should go to the assignment activity and upload a text file, named:
hw-<id>.txt, where <id> is your ID number. The file should contain the URL of your repository, for example: https://github.com/israel_israeli/DS_Intro_HW_3  

Tasks
A.	Attached is a text file (dests.txt) that includes a list of destinations (cities in the world). You must write a Python code that goes over the destinations in the file and for each destination contact the Googleapis distancematrix service and retrieve:
•	The distance between the city of Tel Aviv and the destination in kilometers
•	The time it takes to reach the destination in minutes.
In addition, you must contact the Google geocode service and retrieve:
•	The longitude and latitude of the target

The information should be stored in a dataframe of the following structure:
Target	Distance_km	Duration (hour+minutes)	Longitude	latitude
				
				

On a separate cell, print the dataframe content.

On a separate cell, for the dataframe you created above: Find the 3 cities furthest from Tel Aviv.

Good luck!
