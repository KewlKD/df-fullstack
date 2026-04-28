import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2


load_dotenv()  # Load variables from .env

app = Flask(__name__)
CORS(app)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=os.getenv("PG_DBNAME"),
    user=os.getenv("PG_USER"),
    password=os.getenv("PG_PASS"),
    host=os.getenv("PG_HOST"),
    port=os.getenv("PG_PORT")
)
cursor = conn.cursor()

# Create table (run once)
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
   # id SERIAL PRIMARY KEY,
    #name TEXT,
    #email TEXT
#)
#""")
#conn.commit()


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'message': 'Server is operational'}), 200


@app.route('/users', methods=['GET'])
def get_users():
    try:
        cursor.execute("SELECT name, email FROM users")
        rows = cursor.fetchall()

        users = [{"name": row[0], "email": row[1]} for row in rows]
        return jsonify(users), 200
    except Exception as e:
        print("Error fetching users:", e)
        return jsonify({"error": "Unable to fetch users"}), 500


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data['name']
    email = data['email']
    
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    
    return jsonify({'message': 'Data inserted'}), 201

if __name__ == '__main__':
    app.run(debug=True)
