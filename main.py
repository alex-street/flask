from flask import Flask, render_template, request, redirect, url_for
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
database_url = os.environ.get('DATABASE_URL')
conn = psycopg2.connect(database_url, sslmode='require')
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
      firstPick = 1 if request.form['firstPick'] == "your-team" else 0

      cursor = conn.cursor()
      print(cursor)
      insert_query = """
                INSERT INTO matchup (date, firstpick, us, them)
                VALUES (%s, %i, %s, %s)
                RETURNING id
            """
      cursor.execute(insert_query, (
                matchDate,
                firstPick,
                yourTeamName,
                opponentTeamName
            ))
            
      matchup_id = cursor.fetchone()[0]
      conn.commit()
            
      return redirect(url_for('add_probs'))

  except:
      return None
  
  finally:
      cursor.close()
      conn.close()

@app.route('/addprobabilities')
def add_probs():
   render_template('addprobabilities.html')

if __name__ == '__main__':
  app.run(port=5000)
