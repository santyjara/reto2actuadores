from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def add_entry():

    if request.method == 'POST':
        print("p0")
        content = request.get_json()
        valor = content.get('name')
        fecha = content.get('time')
        # Guardar valor y fehca en la base de datos sqlite
        print(valor)
        print(fecha)
        return render_template('tabla.html', value1=valor, value2=fecha)

    else:
        print("p3")
        valor=0
        fecha=0
        # que los valores de fecha y valor no sean 0 cero sino los que vengan de la base de datos
        print("NONE", valor, fecha)
        return render_template('tabla.html', value1=valor, value2=fecha)


app.run(debug=True)

if __name__ == '__name__':
    app.run(debug=True)