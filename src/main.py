import uuid

from flask import Flask, jsonify, request

from db import Connection

app = Flask(__name__)

connection = Connection("data/db/Cereal.db")


@app.route('/cereal', methods=['GET'])
def get_all():
    cur = connection.cursor()
    url_params = list(request.args.items())
    query = "SELECT * FROM cereals WHERE "
    params = []
    for k, v in url_params:
        query += f"{k} = ? AND "
        params.append(v)
    query = query[:-5]
    data = cur.execute(query, params).fetchall()
    return jsonify(data)


@app.route('/cereal/<int:id>', methods=['GET'])
def get(id):
    cur = connection.cursor()
    data = cur.execute(f'SELECT * FROM cereals WHERE id = {id}').fetchall()
    return jsonify(data)


@app.route('/cereal', methods=['POST'])
def create():
    cur = connection.cursor()
    query = f'INSERT INTO cereals (id, name, mfr, type, calories, protein, fat, sodium, fiber, carbo, sugars, potass, vitamins, shelf, weight, cups, rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    params = (
        str(uuid.uuid4()),
        request.args.get('name'),
        request.args.get('mfr'),
        request.args.get('type'),
        request.args.get('calories'),
        request.args.get('protein'),
        request.args.get('fat'),
        request.args.get('sodium'),
        request.args.get('fiber'),
        request.args.get('carbo'),
        request.args.get('sugars'),
        request.args.get('potass'),
        request.args.get('vitamins'),
        request.args.get('shelf'),
        request.args.get('weight'),
        request.args.get('cups'),
        request.args.get('rating'),
    )
    cur.execute(query, params)
    connection.connection.commit()
    return '', 201


@app.route('/cereal/delete/<int:id>', methods=['DELETE'])
def delete(id):
    cur = connection.cursor()
    data = cur.execute(f'DELETE FROM cereals WHERE id = ?', (id,)).fetchall()
    connection.connection.commit()
    return jsonify(data), 204


if __name__ == '__main__':
    app.run(debug=True)
