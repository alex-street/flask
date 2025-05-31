from flask import Flask, render_template, request
import os
import psycopg2
from psycopg2.extras import RealDictCursor

database_url = os.environ.get('DATABASE_URL')
conn = psycopg2.connect(database_url, sslmode='require')

app = Flask(__name__)

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
      yourTeamName = request.form.get('yourTeamName', '').strip()
      opponentTeamName = request.form.get('opponentTeamName', '').strip()
      matchDate = request.form.get('matchDate', '')

  except:
      return None

if __name__ == '__main__':
  app.run(port=5000)
