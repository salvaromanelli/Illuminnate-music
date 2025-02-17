from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'salvabmx@gmail.com'
app.config['MAIL_PASSWORD'] = '*********'
app.config['MAIL_DEFAULT_SENDER'] = 'salvabmx@gmail.com'

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
    app.run(debug=True)
