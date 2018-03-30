from flask import Flask,request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST'])
def add_entry():
    print("p0")
    request_json = request.get_json(force=True)
    value1 = request_json.get('name')

    if value1 is not None:
        print("p3")
        cursor.execute("INSERT INTO person (first_name,last_name) VALUES (%s,%s)", (value1, value2))
        data = conn.commit()
        return jsonify(data)

    return render_template('hello.html')