Purpose of this database
=========================
Answer following three questions that are given from event data of the music app.
1. Give me the artist, song title and song's length in the music app history that was heard during  sessionId = 338, and itemInSession  = 4
2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

How to use this programs
========================
1.Preparing data in event_data directory
2.Run the code "create_new_event_datafile.py" on terminal for creating a csv file that include all data.
3.Run Project_1B.ipynb for answering 3 questions. Creating cassandra tables and run queries.

About files in repositry
=========================
1.event_data
Include all dataset used by analysis 

2.images
Images of datasets

3.create_new_event_datafile.py
Code for creating new csv that includes all data in the event_data directory.

4.event_data_file_new.csv
CSV file that include all data taht is used for creating NoSQL tables.

5.Project_1B.ipynb
jupyter notebook for creating cassandra database and doing queries.

6.Project_1B_Project_template.ipynb
jupyter notebook for prototype of ETL and creating casandra database and queries.

Screenshots of tables
=====================
In directory that is root/Pic_create_tables
![songplay table]:songplay_table.png
![Users table]:users_table.png
![Song Table]:songs_table.png
![Artist Table]artists_table.png
![Time table]:time_table.png