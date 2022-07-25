from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Endpoint served from Apache"
@app.route('/v2')
def indexV2():
    return "Endpoint served from Apache-V2"
#app.run()

