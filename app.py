from flask import Flask, request, jsonify
import argparse
from flask_mail import Mail, Message
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv('credentials.env')

app = Flask(__name__)
CORS(app)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
<<<<<<< HEAD
app.config['MAIL_USERNAME'] = 'salvabmx@gmail.com'
app.config['MAIL_PASSWORD'] = '*********'
app.config['MAIL_DEFAULT_SENDER'] = 'salvabmx@gmail.com'
=======
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')
>>>>>>> 2fb9b1f (Enhance Flask backend with environment variable support; improve video playback attributes and add social media links in Contact component)

mail = Mail(app)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({'error': 'Faltan datos'}), 400

    msg = Message('Nuevo mensaje de contacto',
                  recipients=['salvabmx@gmail.com'])
    msg.body = f"Nombre: {name}\nEmail: {email}\nMensaje: {message}"
    mail.send(msg)

    return jsonify({'success': 'Mensaje enviado'}), 200

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True)
=======
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000, help='Port to run the server on (default: 5000)')
    args = parser.parse_args()
    
    app.run(debug=True, port=8080)
>>>>>>> 2fb9b1f (Enhance Flask backend with environment variable support; improve video playback attributes and add social media links in Contact component)
