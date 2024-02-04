from flask import Flask, jsonify, render_template
import simplejson as json
from flask_mysqldb import MySQL
app = Flask(__name__, template_folder='templates')
app.config['MYSQL_HOST'] = '192.168.1.16'
app.config['MYSQL_PORT']=3306
app.config['MYSQL_USER'] = 'kirti'
app.config['MYSQL_PASSWORD'] = 'kirti@1234'
app.config['MYSQL_DB'] = 'kdmdb'
mysql = MySQL(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/emp', methods=['GET'])
def get_employee():
    cur = mysql.connection.cursor()
    cur.execute('select * from emp')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)
    #return 'connnected with data'


@app.route('/department', methods=['GET'])
def department():
    cur = mysql.connection.cursor()
    cur.execute('select * from dept')
    data = cur.fetchall()
    cur.close()
    #return jsonify(data)
    return render_template('department.html',data=json.dumps(data))


if __name__ == '__main__':
    app.run(port=8082, debug=True)
