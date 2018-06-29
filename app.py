import datetime
from flask import Flask, render_template
import os
year = datetime.date.today().year

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
	return render_template('index.html',year = year)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    print("Starting app on port %d" % port)
app.run(debug=False, port=port, host='0.0.0.0')