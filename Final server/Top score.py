#!/usr/bin/python

# Turn on debug mode.
import cgitb
import pymysql
import json

cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")

import cgi
form = cgi.FieldStorage()

# Connect to the database.
conn = pymysql.connect(
    db='highscores',
    user='root',
    passwd='samwillsfal',
    host='localhost')
c = conn.cursor()

def print_highscore():
    c.execute("SELECT players.first_name, players.last_name, scores.score FROM scores INNER JOIN players ON player_id = players.id ORDER BY score DESC LIMIT 1")
    print ("<b>Top score</b><br />")
    scores = ([(r[0], r[1], r[2]) for r in c.fetchall()])
    print (json.dumps(scores))
    
    '''
The main gets request from form then displays appropriate text or error.
'''
def main():
    if 'request' not in form:
        print("Missing request")
    else:
        request = str(form.getvalue('request'))
        if request == 'top_score':
            print_highscore()

if __name__ == "__main__":
    main()
