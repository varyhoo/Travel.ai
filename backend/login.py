from flask import Blueprint, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import bcrypt

login = Blueprint('login', __name__)
CORS(login)  # 允许所有来源的请求

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='36.158.228.122',  # 数据库地址改到公网，没有打开群里@jy就好
            port='44581',  
            user='root',  
            password='20040901(jy)',  # 修改为你的MySQL密码
            database='travelai'
        )
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

@login.route('/login', methods=['POST'])
def login_route():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return jsonify({'success': True, 'message': '登录成功'})
        else:
            return jsonify({'success': False, 'message': '登录失败，邮箱或密码错误'})
    except Error as e:
        cursor.close()
        connection.close()
        return jsonify({'success': False, 'message': f"登录失败: {e}"})

@login.route('/register', methods=['POST'])
def register_route():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_password.decode('utf-8')))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({'success': True, 'message': '注册成功'})
    except Error as e:
        cursor.close()
        connection.close()
        return jsonify({'success': False, 'message': f"注册失败: {e}"})

if __name__ == '__main__':
    login.run(debug=True)
