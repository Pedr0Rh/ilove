from flask import Flask, render_template, request, redirect, url_for
from main import get_password_from_db
import json
from pathlib import Path
import os

app = Flask(__name__)

# ----------------- JSON DE EVENTOS -----------------
EVENTS_FILE = Path("events.json")

def load_events():
    if not EVENTS_FILE.exists():
        return []
    with open(EVENTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_events(events):
    with open(EVENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=4, ensure_ascii=False)

# ----------------- ROTAS -----------------
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/logar", methods=["POST"])
def logar():
    senhadb = get_password_from_db()
    senhacamp = request.form.get("password")
    if senhadb and senhacamp == senhadb:
        return redirect(url_for("home"))
    else:
        return render_template("login.html", error="Senha incorreta")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/menssager")
def menssager():
    events = load_events()
    return render_template("menssager.html", events=events)

@app.route("/add_event", methods=["POST"])
def add_event():
    data = request.form
    new_event = {
        "date": data.get("date"),
        "description": data.get("description"),
        "music": data.get("music")
    }
    events = load_events()
    events.append(new_event)
    save_events(events)
    return redirect(url_for("menssager"))

@app.route("/calendar_page")
def calendar_page():
    # Se as imagens já estão no HTML com links públicos,
    # não é necessário passar nada aqui
    return render_template("calendar_page.html")

@app.route('/gifts')
def gifts():
    base_url = "https://nzglhtlkpdekehjsocps.supabase.co/storage/v1/object/public/imagens/fotos/"
    # Cria URLs de imagem1.jpeg até imagem20.jpeg
    urls = [f"{base_url}imagem{i}.jpeg" for i in range(1, 21)]
    return render_template('gifts.html', urls=urls)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
