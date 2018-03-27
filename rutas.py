from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Wodddddddddddddddddrld!'

@app.route('/nombre/')
@app.route('/nombre/<name>')
def hello_dr(name='default'):
    return 'SU nombre es : {}'.format(name,'ingrese nombre valido')

if __name__ == '__main.py__':
    app.run(debug=True,port=8000)