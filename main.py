from flask import Flask, render_template, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
import os
from dotenv import load_dotenv

# Check for DATABASE_URL first (Railway's preferred method)
database_url = os.environ.get('DATABASE_URL')
if database_url:
    conn = psycopg2.connect(database_url, sslmode='require')
else:
    # Fall back to individual variables
    conn = psycopg2.connect(**DATABASE_CONFIG_RAILWAY)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/creatematchup/')
def creatematchup():
  return render_template('creatematchup.html')

if __name__ == '__main__':
  app.run(port=5000)
