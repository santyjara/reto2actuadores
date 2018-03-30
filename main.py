from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    name = 'Santiago'
    return render_template('index2.html', name=name)

@app.route('/client')
def client():
    list_name = ['nambre1','nombre2']
    return render_template('client.html', list=list_name)

if __name__ == '__main__':
    app.run(debug=True,port=8000)