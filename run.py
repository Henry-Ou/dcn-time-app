from flask import Flask
from datetime import datetime
from pytz import timezone
app = Flask(__name__)


@app.route('/')
def intro():
    return 'Please visit /time to see the current date and time'


@app.route('/time')
def get_current_time():
    now = datetime.now(timezone('US/Eastern'))
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    return 'New York now date and time is: ' + date_time


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
