import sqlite3
from flask import Flask, render_template, request, redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy

import sys

sys.path.append("model")
from Model import getModelScore

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(64), index=True, nullable=False)
    age = db.Column(db.Integer, default=18)



@app.route('/')
def index():
    return render_template('index.html', message=getModelScore())


@app.route('/names/')
def page_names():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS name (
	id integer PRIMARY KEY,
	value text NOT NULL,
	age integer)''')
    c.execute('''SELECT * FROM name''')
    names = Name.query.order_by(Name.id).all()
    return render_template('names.html', names=names)


@app.route('/names/add/', methods=['POST'])
def page_names_add():
    if request.method == 'POST':
        form = request.form
        value = form.get('value')
        age = form.get('age')
        if value:
            name = Name(value=value, age=age)
            db.session.add(name)
            db.session.commit()
            return redirect('/names/')
    return redirect('/')


@app.route('/names/delete/<int:id>')
def action_names_delete(id):
    if not id or id != 0:
        name = Name.query.get(id)
        if name:
            db.session.delete(name)
            db.session.commit()
        return redirect('/names/')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
