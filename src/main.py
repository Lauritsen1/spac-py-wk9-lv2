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


@app.route('/cereal/delete/<int:id>', methods=['DELETE'])
def delete(id):
    cur = connection.cursor()
    data = cur.execute(f'DELETE FROM cereals WHERE id = ?', (id,)).fetchall()
    connection.connection.commit()
    return jsonify(data), 204


if __name__ == '__main__':
    app.run(debug=True)
