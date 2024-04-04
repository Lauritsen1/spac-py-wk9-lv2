from flask import Flask, jsonify, request

from db import Connection

app = Flask(__name__)

connection = Connection("data/db/Cereal.db")


@app.route('/cereal', methods=['GET'])
def get():
    cur = connection.cursor()
    data = cur.execute('SELECT * FROM cereals').fetchall()
    return jsonify(data)


@app.route('/cereal/<int:id>', methods=['GET'])
def get_all(id):
    cur = connection.cursor()
    data = cur.execute(f'SELECT * FROM cereals WHERE id = {id}').fetchall()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
