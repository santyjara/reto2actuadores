from flask import Flask,request,render_template
#import cursor

#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/',methods=['POST'])
def add_entry():

    print("p0")
    content = request.get_json()
    valor = content.get('name')
    fecha = content.get('time')
    print(valor)
    print(fecha)

    # return render_template('tabla.html',value1=value1,value2=value2)

app.run(debug=True)

if __name__ == '__name__':
    app.run(debug=True)