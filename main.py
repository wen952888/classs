from flask import Flask, jsonify
from modules import admin, translate

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask App!"})

@app.route('/admin')
def admin_route():
    return admin.get_admin_info()

@app.route('/translate/<text>/<target_lang>')
def translate_route(text, target_lang):
    return translate.translate_text(text, target_lang)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)