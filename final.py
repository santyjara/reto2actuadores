from flask import Flask,request,render_template
import sqlite3


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/data', methods=['GET','POST'])
def add_entry():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    if request.method == 'POST':
        print("p0")
        content = request.get_json()
        valor = content.get('name')
        fecha = content.get('time')
        print(valor)
        print(fecha)

        if valor < 15 :
            clasificacion='FRIO'
        elif valor >= 15 and valor < 25:
            clasificacion = 'TEMPLADO'
        else:
            clasificacion = 'CALIDO'

        c.execute("INSERT INTO reto (fecha,valor,clasificacion) VALUES ( ?, ?, ?)",(fecha,valor,clasificacion))
        conn.commit()
        c.close()
        conn.close()

        return render_template('tabla.html', value1=valor, value2=fecha)

    else:

        c.execute("SELECT * FROM reto ORDER BY fecha DESC LIMIT 20")
        list = []

        for row in c.fetchall():
            print(row)
            list.append([row[0], row[1], row[2]])

        return render_template('data.html',list=list)

def borrar():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM reto")


app.run(debug=True)

if __name__ == '__name__':
    app.run(debug=True)