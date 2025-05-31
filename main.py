from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/creatematchup')
def creatematchup():
  return render_template('creatematchup.html')
@app.route('/savematchup', methods=['POST'])
def savematchup():
  try:
      # Get form data
      yourTeamName = request.form.get('yourTeamName', '').strip()
      opponentTeamName = request.form.get('opponentTeamName', '').strip()
      matchDate = request.form.get('matchDate', '')

if __name__ == '__main__':
  app.run(port=5000)
