from flask import Flask, render_template, request

app = Flask(__name__)

users = [{'username': 'test', 'password': 'test'}]


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/python")
def python():
    return render_template("python.html")


@app.route("/flask")
def flask():
    return render_template("flask.html")


@app.route("/sql")
def sql():
    return render_template("sql.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    if users and users[0]['username'] == username and users[0]['password'] == password:
        return render_template('register.html', success='Login Successful.')
    else:
        return render_template('register.html', error='Invalid username or password.')


# if __name__ == '__main__':
#     app.run(debug=True)