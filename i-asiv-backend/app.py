# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return "Hello World!"

# from flask import Flask
# from flask_mysqldb import MySQL
#
# app = Flask(__name__)
# mysql = MySQL(app)
#
#
# @app.route('/')
# def users():
#     cur = mysql.connection.cursor()
#     cur.execute('''SELECT user, host FROM mysql.user''')
#     rv = cur.fetchall()
#     return str(rv)
#
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask
from flaskext.mysql import MySQL
app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)
