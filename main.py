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

@app.route('/savematchup', methods=['POST'])
def savematchup():
  try:
      # Get form data
      yourTeamName = request.form['yourTeamName']
      opponentTeamName = request.form['opponentTeamName']
      matchDate = request.form['matchDate']
      firstPick = bool(1 if request.form['firstPick'] == "your-team" else 0)
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
                INSERT INTO matchup (date, firstpick, us, them, opponent1, opponent2, opponent3, opponent4, opponent5, opponent6, opponent7, opponent8, home1, home2, home3, home4, home5)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """
      cursor.execute(insert_query, (
                matchDate,
                firstPick,
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

@app.route('/addprobabilities/')
def add_probs():
   render_template('addprobabilities.html')

if __name__ == '__main__':
  app.run(port=5000)
