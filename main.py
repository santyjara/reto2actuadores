from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello_world(name="Santiago"):
    list = []
    for x in range(10):
        num = input("Igrese numero: ")
        list.append(num)
    return render_template('index.html',nombre=name, list=list)

if __name__ == '__main.py__':
    app.run(debug=True,port=8000)
