from flask import Flask, render_template, request, redirect, url_for
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
database_url = os.environ.get('DATABASE_URL')
conn = psycopg2.connect(database_url, sslmode='require')
cursor = conn.cursor()
print(cursor)
print(conn)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/creatematchup/')
def creatematchup():
  return render_template('creatematchup.html')

@app.route('/addprobabilities/')
def add_probs():
   cursor.execute("SELECT home1, home2, home3, home4, home5, opponent1, opponent2, opponent3, opponent4, opponent5, opponent6, opponent7, opponent8 FROM matchup ORDER BY id DESC LIMIT 1")
   last_matchup = cursor.fetchone()
   print(last_matchup)
   your1 = last_matchup[0]
   your2 = last_matchup[1]
   opp1 = last_matchup[5]
   opp2 = last_matchup[6]
   opp3 = last_matchup[7]
   opp4 = last_matchup[8]
   opp5 = last_matchup[9]
   opp6 = last_matchup[10]
   opp7 = last_matchup[11]
   opp8 = last_matchup[12]
   return render_template('addprobabilities.html', Player1Name=your1, Player2Name=your2, Opp1Name=opp1, Opp2Name=opp2, Opp3Name=opp3, Opp4Name=opp4)

@app.route('/savematchup', methods=['POST'])
def savematchup():
  try:
      # Get form data
      yourTeamName = request.form['yourTeamName']
      opponentTeamName = request.form['opponentTeamName']
      matchDate = request.form['matchDate']
      type = request.form['typePool']
      y1 = request.form['yourPlayer1Name']
      y2 = request.form['yourPlayer2Name']
      y3 = request.form['yourPlayer3Name']
      y4 = request.form['yourPlayer4Name']
      y5 = request.form['yourPlayer5Name']
      o1 = request.form['oppPlayer1Name']
      o2 = request.form['oppPlayer2Name']
      o3 = request.form['oppPlayer3Name']
      o4 = request.form['oppPlayer4Name']
      o5 = request.form['oppPlayer5Name']
      o6 = request.form['oppPlayer6Name']
      o7 = request.form['oppPlayer7Name']
      o8 = request.form['oppPlayer8Name']

      insert_query = """
                INSERT INTO matchup (date, type, us, them, opponent1, opponent2, opponent3, opponent4, opponent5, opponent6, opponent7, opponent8, home1, home2, home3, home4, home5)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """
      cursor.execute(insert_query, (
                matchDate,
                type,
                yourTeamName,
                opponentTeamName,
                o1,
                o2,
                o3,
                o4,
                o5,
                o6,
                o7,
                o8,
                y1,
                y2,
                y3,
                y4,
                y5
            ))
            
      matchup_id = cursor.fetchone()[0]
      conn.commit()
            
      return redirect(url_for('add_probs'))

  except Exception as e:
      print(f"Error fetching matchups: {e}")
      return None

if __name__ == '__main__':
  app.run(port=5000)
