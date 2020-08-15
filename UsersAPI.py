import json
import mysql.connector as mysql
from flask import request, jsonify
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "*"}})
#app.config["DEBUG"] = True
CORS(app,support_credentials=True)

HOST = '172.31.31.20'
DATABASE = 'db_first'
USER = "demo2"
PASSWORD = "Password@123"


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome</h1>
<p>API.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/users/all', methods=['GET'])
def api_all():
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    db_connection.row_factory = dict_factory
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM demousers")
    row_headers = [x[0] for x in cursor.description]  # this will extract row headers
    result = cursor.fetchall()
    json_data = []
    for result in result:
        json_data.append(dict(zip(row_headers, result)))
    return json.dumps(json_data)
    #return jsonify(result)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/users', methods=['GET'])
def api_filter():
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    db_connection.row_factory = dict_factory
    cursor = db_connection.cursor()
    query_parameters = request.args

    ids = query_parameters.get('id')
    name = query_parameters.get('name')
    email = query_parameters.get('email')
    mobile = query_parameters.get('mobile')

    query = "SELECT * FROM demousers WHERE"
    to_filter = []

    if ids:
        query += ' id=%s AND'
        to_filter.append(ids)
    if name:
        query += ' name=%s AND'
        to_filter.append(name)
    if email:
        query += ' email=%s AND'
        to_filter.append(email)
    if mobile:
        query += ' mobile=%s AND'
        to_filter.append(mobile)

    if not (ids or mobile or email or name):
        return page_not_found(404)

    query = query[:-4]
    cursor.execute(query, to_filter)
    results = cursor.fetchall()

    return jsonify(results)


@app.route('/users', methods=['POST'])
def update_users():
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()
    #query_parameters = request.args
    query_parameters = request.get_json(force=True)

    name = query_parameters['name']
    email = query_parameters['email']
    mobile = query_parameters['mobile']
    password = query_parameters['password']
    introduction = query_parameters['introduction']

    query = 'INSERT INTO demousers (name, mobile, password, introduction, email) VALUES (%s, %s, %s, %s, %s)'
    to_filter = (name, mobile, password, introduction, email)

    if not (introduction or mobile or email or name or password):
        return page_not_found(404)

    cursor.execute(query, to_filter)
    #results = cursor.fetchall()
    db_connection.commit()
    return json.dumps({'Result': 'Record Insert'})


@app.route('/users', methods=['DELETE'])
def delete_users():
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    db_connection.row_factory = dict_factory
    cursor = db_connection.cursor()
    query_parameters = request.args

    ids = query_parameters.get('id')
    name = query_parameters.get('name')
    email = query_parameters.get('email')
    mobile = query_parameters.get('mobile')

    query = "DELETE FROM demousers WHERE"
    to_filter = []

    if ids:
        query += ' id=%s AND'
        to_filter.append(ids)
    if name:
        query += ' name=%s AND'
        to_filter.append(name)
    if email:
        query += ' email=%s AND'
        to_filter.append(email)
    if mobile:
        query += ' mobile=%s AND'
        to_filter.append(mobile)

    if not (ids or mobile or email or name):
        return page_not_found(404)

    query = query[:-4]
    cursor.execute(query, to_filter)
    db_connection.commit()

    return json.dumps({'Result': 'Record delete'})


@app.route('/users', methods=['PUT'])
def update():
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    db_connection.row_factory = dict_factory
    cursor = db_connection.cursor()
    #query_parameters = request.args
    query_parameters = request.get_json(force=True)

    name = query_parameters['name']
    email = query_parameters['email']
    mobile = query_parameters['mobile']
    password = query_parameters['password']
    introduction = query_parameters['introduction']
    ids = query_parameters['id']

    query = "UPDATE demousers SET"
    to_filter = []

    if introduction:
        query += ' introduction=%s ,'
        to_filter.append(introduction)
    if name:
        query += ' name=%s ,'
        to_filter.append(name)
    if email:
        query += ' email=%s ,'
        to_filter.append(email)
    if mobile:
        query += ' mobile=%s ,'
        to_filter.append(mobile)
    if password:
        query += ' password=%s'
        to_filter.append(password)
    if ids:
        query += ' WHERE id=%s'
        to_filter.append(ids)

    if not (introduction or mobile or email or name or ids):
        return page_not_found(404)

    cursor.execute(query, to_filter)
    db_connection.commit()

    return json.dumps({'Result': 'Record delete'})


#app.run()
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="172.31.31.20", port=5000)
