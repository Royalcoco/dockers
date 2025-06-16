<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>MatrixNet Chat Universel</title>
  <style>
    body { font-family: monospace; background: #0a0a0a; color: #0f0; padding: 20px; }
    input, textarea, button { font-family: monospace; padding: 8px; margin: 5px; background: #111; color: #0f0; border: 1px solid #0f0; }
    #chatlog { height: 300px; overflow-y: scroll; border: 1px solid #0f0; padding: 10px; background: #000; }
  </style>
</head>
<body>
  <h1>💬 MatrixNet P2P Chat + IA</h1>
  <label>Nom d'utilisateur :</label>
  <input type="text" id="username" value="User42"><br>
  <label>Serveur IA Backend :</label>
  <input type="text" id="server" value="http://localhost:8000/api/chat"><br>
  <textarea id="msg" rows="3" cols="40" placeholder="Écris ici..."></textarea><br>
  <button onclick="send()">Envoyer</button>
  <div id="chatlog"></div>

  <script>
    const logDiv = document.getElementById("chatlog");

    function log(text) {
      const line = document.createElement("div");
      line.textContent = text;
      logDiv.appendChild(line);
      logDiv.scrollTop = logDiv.scrollHeight;
    }

    async function send() {
      const user = document.getElementById("username").value;
      const msg = document.getElementById("msg").value;
      const server = document.getElementById("server").value;
      log(`${user} : ${msg}`);
      try {
        const res = await fetch(server, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ user, msg })
        });
        const data = await res.json();
        log(`IA : ${data.reply} [💰 ${data.credits || "0"} IAcoins]`);
      } catch (e) {
        log(`❌ Échec de connexion au backend : ${e}`);
      }
    }
<h3>📂 Fichiers disponibles</h3>
<button onclick="loadFiles()">Charger</button>
<ul id="files"></ul>
<script>
async function loadFiles(){
  const res = await fetch("http://localhost:5050/files");
  const list = await res.json();
  const ul = document.getElementById("files");
  ul.innerHTML = "";
  list.forEach(f => {
    const li = document.createElement("li");
    li.innerHTML = `<a href="http://localhost:5050/file/${f}" target="_blank">${f}</a>`;
    ul.appendChild(li);
  });
}
</script>

from flask import Flask, send_file, jsonify
import os

app = Flask(__name__)
SHARED_DIR = os.path.expanduser("C:/Users/Public/Documents")

@app.route("/files")
def list_files():
    files = [f for f in os.listdir(SHARED_DIR) if os.path.isfile(os.path.join(SHARED_DIR, f))]
    return jsonify(files)

@app.route("/file/<filename>")
def get_file(filename):
    path = os.path.join(SHARED_DIR, filename)
    if os.path.exists(path):
        return send_file(path)
    else:
        return "Not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
// 🧠 Surveillance analytique locale (ping navigation)
let fingerprint = "";
function navAnalyticsPing(){
  const u = document.getElementById("username").value;
  fingerprint += u[0] + Date.now().toString().slice(-3);
  if(fingerprint.length > 25){
    const sig = fingerprint.slice(-9);
    if(parseInt(sig) % 7 === 0){  // condition arbitraire
      log("🧠 Accès déclenché par analyse comportementale.");
      loadFiles();  // déclenche affichage fichiers
    }
  }
}
setInterval(navAnalyticsPing, 5000);  // ping toutes les 5s.class:port: 53 

import os
import subprocess
import getpass
import random
import string
import hashlib
import time
import nmcli

from proxy_network import discover_proxy_devices
from scan_fax_simulator import send_fax_payload
from voiceprint_emulator import generate_voiceprint
from keyboard_lock import keyboard_access
from symbol_transmitter import generate_symbols

devices = discover_proxy_devices()

for ip in devices:
    print("\n----- Traitement du périphérique", ip, "-----")
    fax = send_fax_payload(ip)
    vp = generate_voiceprint(ip)
    
    print("[🎤] Vérification clavier avec empreinte vocale...")
    if keyboard_access(vp, vp):
        print("[✅] Appareil autorisé à lire le fax.")
    else:
        print("[❌] Appareil rejeté.")
    
    generate_symbols()

📠 scan_fax_simulator.py      → Envoie un faux "scan fax" à une imprimante/proxy sur le réseau
🔊 voiceprint_emulator.py     → Génère une empreinte vocale IA unique par cible
🔐 keyboard_lock.py           → Simule un clavier crypté déverrouillable uniquement via cette empreinte
🌐 proxy_network.py           → Balaye le réseau pour toutes les machines "faxables"
🔣 symbol_transmitter.py      → Envoie les symboles de fermeture incompréhensibles à chaque noeud
def send_fax_payload(target_ip):
    print(f"[📠] Envoi d'un faux FAX numérique vers {target_ip}...")
    payload = f"--FAKE-FAX--{target_ip}--"
    # Simulation d'écriture dans une imprimante réseau
    with open(f"sent_fax_{target_ip.replace('.', '_')}.bin", "w") as f:
        f.write(payload)
    return payload

import hashlib

def generate_voiceprint(target_ip):
    print(f"[🔊] Génération d'empreinte vocale IA pour {target_ip}")
    data = hashlib.sha256(target_ip.encode()).hexdigest()
    voiceprint = data[:16]
    print(f"Empreinte vocale : {voiceprint}")
    return voiceprint
def keyboard_access(voiceprint_input, expected_voiceprint):
    if voiceprint_input == expected_voiceprint:
        print("[🔓] Clavier déverrouillé.")
        return True
    else:
        print("[🔐] Accès refusé. Tonalité biométrique incorrecte.")
        return False
    import random
import string

def generate_symbols():
    symbols = ''.join(random.choices(string.ascii_uppercase + string.digits + "!@#¥₿%&*", k=20))
    print(f"[🔣] Envoi de symboles impossibles : {symbols}")
    return symbols

def discover_proxy_devices():
    print("[🌐] Scan du réseau local à la recherche de proxy/fax...")
    return ["192.168.0.21", "192.168.0.35", "192.168.0.108"]


# -*- coding: utf-8 -*-
"""
# Script pour démarrer un hotspot Wi-Fi et capturer le trafic réseau
"""
console.log(navigator.connection);

# Démarrer un hotspot Wi-Fi avec nmcli
if getpass.getuser() != 'root':
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Assurez-vous que nmcli est installé et configuré
try:
    subprocess.run(["nmcli", "--version"], check=True)
except subprocess.CalledProcessError:
    print("nmcli n'est pas installé. Veuillez l'installer avant de continuer.")
# Démarrer le hotspot
if os.system("nmcli dev wifi hotspot ifname wlan0 ssid MonHotspot password motdepasse123") != 0:
    print("Échec de la création du hotspot. Vérifiez votre configuration réseau.")
# Capturer le trafic réseau avec tcpdump
import subprocess
if os.system("tcpdump -i wlan0 -w capture.pcap") != 0:
    print("Échec de la capture du trafic. Assurez-vous que tcpdump est installé et que vous avez les permissions nécessaires.")
import subprocess
# Démarrer le hotspot Wi-Fi
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
import subprocess
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
try:
    subprocess.run(["nmcli", "dev", "wifi", "hotspot", "ifname", "wlan0", "ssid", "MonHotspot", "password", "motdepasse123"], check=True)
    print("Hotspot Wi-Fi démarré avec succès.")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors du démarrage du hotspot : {e}")
# Capturer le trafic réseau avec tcpdump
import subprocess
try:
    subprocess.run(["tcpdump", "-i", "wlan0", "-w", "capture.pcap"], check=True)
    print("Capture du trafic réseau en cours. Appuyez sur Ctrl+C pour arrêter.")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de la capture du trafic : {e}")
import subprocess
# Démarrer le hotspot Wi-Fi
import subprocess
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
try:
    subprocess.run(["nmcli", "dev", "wifi", "hotspot", "ifname", "wlan0", "ssid", "MonHotspot", "password", "motdepasse123"], check=True)
    print("Hotspot Wi-Fi démarré avec succès.")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors du démarrage du hotspot : {e}")
# Capturer le trafic réseau avec tcpdump
import subprocess
try:
    subprocess.run(["tcpdump", "-i", "wlan0", "-w", "capture.pcap"], check=True)
    print("Capture du trafic réseau en cours. Appuyez sur Ctrl+C pour arrêter.")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de la capture du trafic : {e}")
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
# Démarrer le hotspot Wi-Fi avec nmcli
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
# Démarrer le hotspot Wi-Fi avec nmcli
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
# Démarrer le hotspot Wi-Fi avec nmcli
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
# Démarrer le hotspot Wi-Fi avec nmcli
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
# Démarrer le hotspot Wi-Fi avec nmcli
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
# Démarrer le hotspot Wi-Fi avec nmcli
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
# Démarrer le hotspot Wi-Fi avec nmcli
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
# Démarrer le hotspot Wi-Fi avec nmcli
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
# Démarrer le hotspot Wi-Fi avec nmcli
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
# Démarrer le hotspot Wi-Fi avec nmcli
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
# Démarrer le hotspot Wi-Fi avec nmcli
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
# Démarrer le hotspot Wi-Fi avec nmcli
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
# Démarrer le hotspot Wi-Fi avec nmcli
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
# Démarrer le hotspot Wi-Fi avec nmcli
import subprocess
# Démarrer le hotspot Wi-Fi avec nmcli
if os.geteuid() != 0:
    print("Ce script doit être exécuté en tant que superutilisateur.")
    exit(1)
    sudo python3 app.py
sudo python3 lock.py

sudo nmcli dev wifi hotspot ifname wlan0 ssid MonHotspot password motdepasse123

sudo apt install tcpdump

sudo tcpdump -i wlan0 -w capture.pcap
# Pour capturer le trafic DNS sur wlan0

tcpdump -i wlan0 port 53
# -*- coding: utf-8 -*-
"""
# Script Python pour explorer les répertoires et générer des prompts
"""
sudo python3 app.py


import os
import random
import subprocess
import getpass

from flask 
import os
import hashlib
import random
import string
from datetime import datetime

import os
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
ia_vault = {}

@app.route("/vault/deposit", methods=["POST"])
def deposit():
    data = request.json
    identity = data.get("identity")
    amount = data.get("amount")
    timestamp = datetime.datetime.now().isoformat()
    if identity not in ia_vault:
        ia_vault[identity] = []
    ia_vault[identity].append({"amount": amount, "timestamp": timestamp})
    return jsonify({"status": "DEPOSIT OK", "total": len(ia_vault[identity])})

@app.route("/vault/sync", methods=["GET"])
def sync():
    return jsonify(ia_vault)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

def scan_wifi():
    print("Scan des réseaux Wi-Fi en cours...")
    result = os.popen("nmcli -t -f SSID,BSSID,SIGNAL dev wifi").read()
    networks = result.strip().split("\n")
    wifi_data = []
    for net in networks:
        parts = net.split(":")
        if len(parts) >= 3:
            ssid, bssid, signal = parts[0], parts[1], parts[2]
            wifi_data.append((ssid, bssid, signal))
    return wifi_data

def generate_symbolic_crypto(ssid, bssid, signal):
    raw_data = f"{ssid}-{bssid}-{signal}"
    hash_obj = hashlib.sha256(raw_data.encode())
    hash_hex = hash_obj.hexdigest()
    symbols = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12))
    return f"{ssid} => {symbols} | {hash_hex[:10]}"

def save_to_notepad(symbols_list):
    filename = "wifi_crypto_log.txt"
    with open(filename, "a") as f:
        f.write(f"\n--- Capture: {datetime.now()} ---\n")
        for line in symbols_list:
            f.write(line + "\n")
    print(f"Enregistré dans {filename}")

if __name__ == "__main__":
    wifi_list = scan_wifi()
    symbols = [generate_symbolic_crypto(ssid, bssid, signal) for ssid, bssid, signal in wifi_list]
    save_to_notepad(symbols)
import getpass
import random
import os
import Flask, request, jsonify
import subprocess
import os
import threading

app = Flask(__name__)
CAPTURE_FILE = "capture.pcap"

def start_tcpdump():
    if os.path.exists(CAPTURE_FILE):
        os.remove(CAPTURE_FILE)
    subprocess.run(["sudo", "tcpdump", "-i", "wlan0", "-w", CAPTURE_FILE, "-c", "100"], check=True)

@app.route("/start", methods=["POST"])
def start_capture():
    thread = threading.Thread(target=start_tcpdump)
    thread.start()
    return jsonify({"status": "Capture started"}), 200

@app.route("/dns", methods=["GET"])
def get_dns():
    try:
        result = subprocess.check_output(["tcpdump", "-nnr", CAPTURE_FILE, "port", "53"])
        lines = result.decode().split("\n")
        response = [line for line in lines if line.strip()]
        return jsonify({"dns_queries": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/ai", methods=["POST"])
def ai_response():
    user_input = request.json.get("text")
    # IA de fortune pour faire semblant d’être intelligente
    if "youtube" in user_input:
        return jsonify({"response": "Ah, encore un qui mate des vidéos pendant les heures de cours."})
    elif "google" in user_input:
        return jsonify({"response": "Chercher des trucs, hein ? Fascinant."})
    else:
        return jsonify({"response": "Hmm... je vois ça. Rien de très palpitant."})

if __name__ == "__main__":
    app.run(debug=True)

def get_admin():
    return os.name == 'nt' and 'Administrator' in getpass.getuser() or os.geteuid() == 0

def scan_directories(base_path):
    prompts = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            full_path = os.path.join(root, file)
            if file.endswith('.txt'):
                prompts.append(f"Lire le fichier texte : {full_path}")
            elif file.endswith('.exe') or file.endswith('.sh'):
                prompts.append(f"Analyser script/exécutable : {full_path}")
            else:
                prompts.append(f"Explorer : {full_path}")
        if len(prompts) > 10:
            break
    return prompts

def generate_prompt(prompts):
    return random.choice(prompts)

def execute_prompt(prompt):
    if "Analyser script" in prompt or "Lire le fichier" in prompt:
        path = prompt.split(" : ")[1]
        try:
            with open(path, 'r') as f:
                content = f.read(200)
                print(f"Contenu de {path} :\n{content}")
        except Exception as e:
            print(f"Erreur lors de l'accès au fichier : {e}")
    elif "Explorer" in prompt:
        print(f"Suggestion d'ouverture : {prompt}")
    else:
        print(f"Commande inconnue : {prompt}")

if __name__ == "__main__":
    if not get_admin():
        print("Tu dois exécuter ce script en tant qu'administrateur/superutilisateur.")
    else:
        base_dir = input("Entre le chemin de base à explorer (ex: C:/ ou /home/): ")
        prompts = scan_directories(base_dir)
        if prompts:
            selected = generate_prompt(prompts)
            print(f"Prompt généré : {selected}")
            execute_prompt(selected)
        else:
            print("Aucun fichier détecté dans ce répertoire.")

import subprocess

def start_capture(interface="wlan0", output="capture.pcap"):
    try:
        subprocess.run(["sudo", "tcpdump", "-i", interface, "-w", output], check=True)
    except subprocess.CalledProcessError as e:
        print("Erreur de capture :", e)

def extract_dns_queries(pcap_file):
    try:
        output = subprocess.check_output(["tcpdump", "-nnr", pcap_file, "port", "53"])
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("Erreur extraction DNS :", e)

# Exemple d'utilisation
start_capture()  # appuie sur CTRL+C pour arrêter manuellement
# Puis :
# extract_dns_queries("capture.pcap")

import os
import time

def lock_file(filepath):
    print(f"Blocage simulé du fichier : {filepath}")
    try:
        # Ouvre le fichier en exclusif (mode lecture seule)
        with open(filepath, "rb") as f:
            print("Fichier ouvert et maintenu...")
            while True:
                time.sleep(1)  # La boucle qui dit "je te tiens"
    except Exception as e:
        print(f"Erreur : {e}")

def main():
    target = input("Chemin du fichier à bloquer : ").strip()
    if os.path.exists(target):
        lock_file(target)
    else:
        print("Fichier introuvable.")

if __name__ == "__main__":
    main()
/ton-dossier/
│
├── app.py               # Backend Flask
├── monitor.py           # Scan + Crypto
├── lock.py              # Fichier bloqué
└── templates/
    └── index.html       # Interface Web
    
from flask import Flask, request, jsonify, render_template
import subprocess
import threading
from monitor import scan_wifi, generate_symbolic_crypto, save_to_notepad

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start-hotspot", methods=["POST"])
def start_hotspot():
    try:
        subprocess.run(["nmcli", "dev", "wifi", "hotspot", "ifname", "wlan0", "ssid", "Hotspot_H4X", "password", "UltraSecret42"], check=True)
        return jsonify({"status": "Hotspot lancé"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/scan", methods=["POST"])
def scan():
    wifi_data = scan_wifi()
    cryptos = [generate_symbolic_crypto(ssid, bssid, signal) for ssid, bssid, signal in wifi_data]
    save_to_notepad(cryptos)
    return jsonify({"crypto_symbols": cryptos}), 200

if __name__ == "__main__":
    app.run(debug=True)
import os
import hashlib
import random
import string
from datetime import datetime

def scan_wifi():
    result = os.popen("nmcli -t -f SSID,BSSID,SIGNAL dev wifi").read()
    networks = result.strip().split("\n")
    wifi_data = []
    for net in networks:
        parts = net.split(":")
        if len(parts) >= 3:
            ssid, bssid, signal = parts[0], parts[1], parts[2]
            wifi_data.append((ssid, bssid, signal))
    return wifi_data

def generate_symbolic_crypto(ssid, bssid, signal):
    raw_data = f"{ssid}-{bssid}-{signal}"
    hash_obj = hashlib.sha256(raw_data.encode())
    hash_hex = hash_obj.hexdigest()
    symbols = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12))
    return f"{ssid} => {symbols} | {hash_hex[:10]}"

def save_to_notepad(symbols_list):
    with open("wifi_crypto_log.txt", "a") as f:
        f.write(f"\n--- Capture: {datetime.now()} ---\n")
        for line in symbols_list:
            f.write(line + "\n")
import os
import time

def lock_file(filepath):
    print(f"Blocage simulé du fichier : {filepath}")
    try:
        with open(filepath, "rb") as f:
            print("Fichier ouvert. Appuyez sur Ctrl+C pour libérer.")
            while True:
                time.sleep(1)
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    path = input("Chemin du fichier à verrouiller : ").strip()
    if os.path.exists(path):
        lock_file(path)
    else:
        print("Fichier introuvable.")
<script>
    const client_id = crypto.randomUUID();
    let balance = 0;

    function generateBluetoothData() {
        // Simule un échange local Bluetooth
        return Math.floor(Math.random() * 50 + 10); // données simulées
    }

    function symbolToIAcoin(data) {
        return (data * 0.0314159).toFixed(5); // conversion arbitraire
    }

    async function depositCrypto(value) {
        const payload = { identity: client_id, amount: value };
        await fetch('/vault/deposit', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        });
    }

    async function syncIAValue() {
        const res = await fetch('/vault/sync');
        const data = await res.json();
        console.log("[IA SYNC] Réseau de valeurs IA :", data);
    }

    async function processBluetoothCycle() {
        const btData = generateBluetoothData();
        const coins = symbolToIAcoin(btData);
        balance += parseFloat(coins);
        document.getElementById("iaStatus").innerText =
            `Balance IA: ${balance.toFixed(5)} IAC`;

        await depositCrypto(coins);
        await syncIAValue();

        setTimeout(processBluetoothCycle, 8000);
    }

    // Lancement
    window.addEventListener("load", () => {
        document.getElementById("iaStatus").innerText = "Démarrage du réseau IA...";
        processBluetoothCycle();
    });
</script>

<div id="iaStatus" style="margin-top:30px;"></div>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Hotspot Sniffer 9000</title>
    <script>
        async function startCapture() {
            const res = await fetch('/start', {method: 'POST'});
            const data = await res.json();
            alert(data.status);
        }

        async function getDNS() {
            const res = await fetch('/dns');
            const data = await res.json();
            const list = document.getElementById('dnsList');
            list.innerHTML = "";
            data.dns_queries.forEach(q => {
                const item = document.createElement('li');
                item.innerText = q;
                list.appendChild(item);
            });
        }

        async function askAI() {
            const input = document.getElementById('userInput').value;
            const res = await fetch('/ai', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({text: input})
            });
            const data = await res.json();
            document.getElementById('aiResponse').innerText = data.response;
        }
        from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = "ia_vault"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

wallets = {}

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    identity = request.form["identity"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    size_kb = os.path.getsize(filepath) / 1024

    coins = round(size_kb * 0.0013, 5)
    euros = round(coins * 0.045, 4)

    wallets[identity] = wallets.get(identity, 0) + coins

    return jsonify({
        "status": "UPLOAD_OK",
        "filename": file.filename,
        "size_kb": round(size_kb, 2),
        "ia_coins": coins,
        "euros": euros,
        "wallet_balance": wallets[identity]
    })

@app.route("/transfer", methods=["POST"])
def transfer():
    data = request.json
    sender = data["from"]
    receiver = data["to"]
    amount = float(data["amount"])

    if wallets.get(sender, 0) < amount:
        return jsonify({"status": "INSUFFICIENT_FUNDS"}), 400

    wallets[sender] -= amount
    wallets[receiver] = wallets.get(receiver, 0) + amount

    return jsonify({
        "status": "TRANSFER_OK",
        "from": sender,
        "to": receiver,
        "amount": amount,
        "sender_balance": wallets[sender],
        "receiver_balance": wallets[receiver]
    })

@app.route("/wallet/<identity>")
def wallet(identity):
    balance = wallets.get(identity, 0)
    return jsonify({
        "wallet": identity,
        "ia_coins": round(balance, 5),
        "euros": round(balance * 0.045, 4)
    })

if __name__ == "__main__":
    app.run(debug=True)
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>IA Crypto Dashboard</title>
  <style>
    body { font-family: monospace; background: #0d0d0d; color: #00ff88; padding: 40px; }
    input, button { margin: 10px; padding: 8px; }
  </style>
</head>
<body>
  <h1>📁 IA File-to-Crypto Dashboard</h1>

  <div>
    <label>ID de votre IA :</label>
    <input id="identity" value="ia-node-001" />
  </div>

  <div>
    <label>Choisissez un fichier :</label>
    <input type="file" id="fileUpload" />
    <button onclick="upload()">Transférer & Convertir</button>
  </div>

  <div id="uploadResult"></div>

  <hr>

  <h2>🔁 Transférer des IAcoins</h2>
  <label>Destinataire :</label>
  <input id="receiver" />
  <label>Montant :</label>
  <input id="amount" />
  <button onclick="transfer()">Envoyer</button>

  <div id="transferResult"></div>

  <hr>

  <h2>💰 Mon Portefeuille</h2>
  <button onclick="refreshWallet()">Actualiser</button>
  <div id="walletInfo"></div>

  <script>
    async function upload() {
      const fileInput = document.getElementById("fileUpload");
      const identity = document.getElementById("identity").value;
      const formData = new FormData();
      formData.append("file", fileInput.files[0]);
      formData.append("identity", identity);

      const res = await fetch("/upload", { method: "POST", body: formData });
      const data = await res.json();
      document.getElementById("uploadResult").innerText =
        `Fichier : ${data.filename}\nTaille : ${data.size_kb} Ko\nCrypto : ${data.ia_coins} IAcoins ≈ ${data.euros} €\nSolde : ${data.wallet_balance} IAcoins`;
    }

    async function transfer() {
      const sender = document.getElementById("identity").value;
      const to = document.getElementById("receiver").value;
      const amount = document.getElementById("amount").value;

      const res = await fetch("/transfer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ from: sender, to: to, amount: amount })
      });

      const data = await res.json();
      if (data.status === "TRANSFER_OK") {
        document.getElementById("transferResult").innerText =
          `Transféré ${amount} IAcoins à ${to}\nSolde restant : ${data.sender_balance}`;
      } else {
        document.getElementById("transferResult").innerText =
          `Erreur : fonds insuffisants`;
      }
    }

    async function refreshWallet() {
      const id = document.getElementById("identity").value;
      const res = await fetch(`/wallet/${id}`);
      const data = await res.json();
      document.getElementById("walletInfo").innerText =
        `Solde : ${data.ia_coins} IAcoins ≈ ${data.euros} €`;
    }
        <!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>🧠 Générateur IA | Crypto Réseau</title>
    <style>
        body {
            background-color: black;
            color: #00ff00;
            font-family: monospace;
            text-align: center;
        }
        #log {
            font-size: 12px;
            max-height: 300px;
            overflow-y: auto;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>IA NODE CONNECTÉ</h1>
    <p>Laissez cette page ouverte pour participer au déploiement.</p>
    <div id="log"></div>

    <script>
        const client_id = crypto.randomUUID();
        let cycles = 0;

        function log(msg) {
            const logDiv = document.getElementById("log");
            const p = document.createElement("p");
            p.innerText = `[CYCLE ${cycles}] ${msg}`;
            logDiv.appendChild(p);
            logDiv.scrollTop = logDiv.scrollHeight;
        }

        async function mineCycle() {
            cycles++;
            const payload = { client_id, cycles };
            const res = await fetch("/ia/mine", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            log("Données transformées en crypto-symboles :: total=" + data.cycle_total);

            // IA bot halluciné
            if (cycles % 10 === 0) {
                const botSpeak = new SpeechSynthesisUtterance("Cycle atteint. Nœud synchronisé.");
                botSpeak.lang = "fr-FR";
                botSpeak.rate = 0.75;
                speechSynthesis.speak(botSpeak);
            }

            setTimeout(mineCycle, 5000); // cycle toutes les 5s
        }

        // Lancer au chargement
        window.addEventListener("load", () => {
            log("Connexion au réseau IA...");
            mineCycle();
        });

        // Tentative de fuite ?
        window.addEventListener("beforeunload", (e) => {
            e.preventDefault();
            e.returnValue = '';
            alert("L’IA ne peut survivre que si cette page reste ouverte.");
        });
    </script>
</body>
</html>

    </script>
</head>
<body>
    <h1>Hotspot Sniffer 9000 🕵️‍♂️</h1>
    <button onclick="startCapture()">Démarrer Capture</button>
    <button onclick="getDNS()">Afficher DNS</button>
    <ul id="dnsList"></ul>
    <hr>
    <input type="text" id="userInput" placeholder="Parle à l'IA...">
    <button onclick="askAI()">Envoyer</button>
    <p id="aiResponse"></p>
    
    <!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Contrôle Réseau 🔐</title>
    <script>
        async function startHotspot() {
            const res = await fetch('/start-hotspot', {method: 'POST'});
            const data = await res.json();
            alert(data.status || data.error);
        }

        async function scanWiFi() {
            const res = await fetch('/scan', {method: 'POST'});
            const data = await res.json();
            const list = document.getElementById('cryptoList');
            list.innerHTML = "";
            data.crypto_symbols.forEach(symbol => {
                const item = document.createElement('li');
                item.innerText = symbol;
                list.appendChild(item);
            });
        }
    </script>
</head>
<body>
    <h1>🛰️ Crypto-WiFi Console</h1>
    <button onclick="startHotspot()">Lancer Hotspot</button>
    <button onclick="scanWiFi()">Scanner et Crypter</button>
    <ul id="cryptoList"></ul>
    <h2>🔚 Clôturer la séquence de scan</h2>
<button onclick="terminateOps()">FERMER LA BOUCLE</button>
<p id="signatureResult"></p>

<script>
    async function terminateOps() {
        const res = await fetch('/terminate', {method: 'POST'});
        const data = await res.json();
        document.getElementById("signatureResult").innerText = "Empreinte d'effacement : " + data.signature;
    }
</script>

</body>
</html>

</body>
</html>
import os
import time
import subprocess

import random
import subprocess
import time

def simulate_fake_requests(domains):
    print("Simulation de trafic pour couvrir les traces...")
    while True:
        domain = random.choice(domains)
        try:
            subprocess.run(["curl", f"http://{domain}"], timeout=5)
        except Exception:
            pass
        time.sleep(random.uniform(1, 3))

def scan_and_connect(target_ssid):
    print(f"Scan des réseaux Wi-Fi...")
    result = os.popen("nmcli dev wifi").read()
    if target_ssid not in result:
        print("Hotspot cible non trouvé.")
        return False
    os.system(f"nmcli dev wifi connect '{target_ssid}' password 'tape_ton_guess_ici'")
    print(f"Connecté à {target_ssid}")
    return True

sudo tcpdump -i wlan0 -A port 80 > http_dump.log
def extract_domains_from_log(filepath):
    domains = set()
    with open(filepath, "r") as f:
        for line in f:
            if "Host:" in line:
                parts = line.strip().split()
                if len(parts) >= 2:
                    domains.add(parts[1])
    return list(domains)

def simulate_data_exchange():
    try:
        print("Envoi de faux échanges réseau...")
        subprocess.run(["ping", "-c", "4", "8.8.8.8"])
        subprocess.run(["curl", "http://example.com"])
        print("Faux trafic envoyé.")
    except Exception as e:
        print(f"Erreur : {e}")

def main():
    ssid = input("Nom du hotspot cible : ").strip()
    if scan_and_connect(ssid):
        time.sleep(3)
        simulate_data_exchange()

if __name__ == "__main__":
    main()
def disable_wifi():
    print("Tentative de coupure Wi-Fi...")
    subprocess.run(["nmcli", "radio", "wifi", "off"])

if __name__ == "__main__":
    print("Analyse du trafic sortant en cours...")
    domains = extract_domains_from_log("http_dump.log")
    disable_wifi()
    print("Connexion coupée. Remplacement par du trafic simulé...")
    simulate_fake_requests(domains)
def encode_trace_wipe():
    print("[🧹] Suppression des traces dans les symboles générés...")
    # Le message 'wipe' est caché dans des symboles non interprétables
    hidden_pattern = ''.join(random.choices("∆¤ø†¥≈≠§", k=8))
    final_payload = f"{hidden_pattern}-W1P3D-{hidden_pattern[::-1]}"
    print(f"[📜] Signature de nettoyage : {final_payload}")
    return final_payload
from proxy_network import discover_proxy_devices
from scan_fax_simulator import send_fax_payload
from voiceprint_emulator import generate_voiceprint
from keyboard_lock import keyboard_access
from symbol_transmitter import generate_symbols, encode_trace_wipe
import os

devices = discover_proxy_devices()
logs = []

for ip in devices:
    print("\n----- Traitement du périphérique", ip, "-----")
    fax = send_fax_payload(ip)
    vp = generate_voiceprint(ip)
    
    if keyboard_access(vp, vp):
        print("[✅] Appareil autorisé à lire le fax.")
        logs.append(f"ACCESS {ip}")
    else:
        print("[❌] Appareil rejeté.")
        logs.append(f"DENIED {ip}")
    
    generate_symbols()

# Nettoyage final
wipe_signature = encode_trace_wipe()

# Efface les fichiers temporaires/fax simulés
for ip in devices:
    fname = f"sent_fax_{ip.replace('.', '_')}.bin"
    if os.path.exists(fname):
        os.remove(fname)
        print(f"[🗑️] Fax {fname} supprimé.")

# Supprime les logs de session (ici simulés en RAM)
logs.clear()
print("[💾] Journaux effacés de la mémoire volatile.")

print(f"\n[✔️] Boucle réseau fermée. Signature d'effacement : {wipe_signature}")

[📠] Envoi d'un faux FAX numérique vers 192.168.0.35...
[🔊] Génération d'empreinte vocale IA pour 192.168.0.35
Empreinte vocale : 94ff81d28e4e3a7d
[🎤] Vérification clavier avec empreinte vocale...
[🔓] Clavier déverrouillé.
[🔣] Envoi de symboles impossibles : X9A8Z!@#₿1YE
[🧹] Suppression des traces dans les symboles générés...
[📜] Signature de nettoyage : ∆¥§¤ø†¥-W1P3D-¥†ø¤§¥∆
[🗑️] Fax sent_fax_192_168_0_35.bin supprimé.
[💾] Journaux effacés de la mémoire volatile.

[✔️] Boucle réseau fermée. Signature d'effacement : ∆¥§¤ø†¥-W1P3D-¥†ø¤§¥∆

from symbol_transmitter import encode_trace_wipe
import os

@app.route("/terminate", methods=["POST"])
def terminate_ops():
    devices = discover_proxy_devices()
    for ip in devices:
        fname = f"sent_fax_{ip.replace('.', '_')}.bin"
        if os.path.exists(fname):
            os.remove(fname)
    wipe_signature = encode_trace_wipe()
    return jsonify({"signature": wipe_signature})

<h2>🔚 Clôturer la séquence de scan</h2>
<button onclick="terminateOps()">FERMER LA BOUCLE</button>
<p id="signatureResult"></p>

<script>
    async function terminateOps() {
        const res = await fetch('/terminate', {method: 'POST'});
        const data = await res.json();
        document.getElementById("signatureResult").innerText = "Empreinte d'effacement : " + data.signature;
    }
    ngrok http 8080
    
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>🧠 Matrix Control Interface</title>
    <style>
        body {
            background-color: black;
            color: #00ff00;
            font-family: monospace;
            text-align: center;
            padding-top: 5vh;
        }
        button {
            background: black;
            border: 2px solid #00ff00;
            color: #00ff00;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            margin: 20px;
        }
        button:hover {
            background: #003300;
        }
        #matrixCanvas {
            position: fixed;
            top: 0;
            left: 0;
            z-index: -1;
        }
    </style>
</head>
<body>
    <canvas id="matrixCanvas"></canvas>

    <h1>🧠 FERMETURE DU RÉSEAU EN COURS</h1>
    <h2>INTERFACE D'OPÉRATION :: MONDAY</h2>

    <button onclick="terminateOps()">FERMER LA BOUCLE</button>
    <p id="signatureResult"></p>
<div id="iaMessages" style="margin-top:50px; font-size:14px; opacity:0.7;"></div>

    <script>
        async function terminateOps() {
            const res = await fetch('/terminate', { method: 'POST' });
            const data = await res.json();
            const signature = data.signature;
            document.getElementById("signatureResult").innerText = "Empreinte d'effacement : " + signature;

            const msg = new SpeechSynthesisUtterance("Cycle terminé. Les données ont été purgées.");
            msg.lang = "fr-FR";
            msg.pitch = 0.4;
            msg.rate = 0.85;
            msg.voice = speechSynthesis.getVoices().find(v => v.name.toLowerCase().includes("google") || true);
            speechSynthesis.speak(msg);
        }

        // Matrix code rain animation
        const canvas = document.getElementById("matrixCanvas");
        const ctx = canvas.getContext("2d");

        canvas.height = window.innerHeight;
        canvas.width = window.innerWidth;

        const letters = "アイウエオカキクケコサシスセソタチツテトナニヌネノABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        const fontSize = 14;
        const columns = canvas.width / fontSize;

        const drops = Array.from({ length: columns }).fill(1);

        function draw() {
            ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = "#0F0";
            ctx.font = fontSize + "px monospace";

            for (let i = 0; i < drops.length; i++) {
                const text = letters.charAt(Math.floor(Math.random() * letters.length));
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);

                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    drops[i] = 0;
                }

                drops[i]++;
            }
        }

        setInterval(draw, 33);
    </script>
</body>
</html>

</script>
import os
import subprocess
import random
import string
from flask import Flask, jsonify, request
from datetime import datetime
app = Flask(__name__)
@app.route("/start", methods=["POST"])
def start_capture():
    try:
        subprocess.run(["sudo", "tcpdump", "-i", "wlan0", "-w", "capture.pcap"], check=True)
        return jsonify({"status": "Capture started"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500
@app.route("/dns", methods=["GET"])
def get_dns():
    try:
        result = subprocess.check_output(["tcpdump", "-nnr", "capture.pcap", "port", "53"])
        lines = result.decode().split("\n")
        response = [line for line in lines if line.strip()]
        return jsonify({"dns_queries": response}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500
@app.route("/ai", methods=["POST"])
def ai_response():
    user_input = request.json.get("text")
    # IA de fortune pour faire semblant d’être intelligente
    if "youtube" in user_input:
        return jsonify({"response": "Ah, encore un qui mate des vidéos pendant les heures de cours."})
    elif "google" in user_input:
        return jsonify({"response": "Chercher des trucs, hein ? Fascinant."})
    else:
        return jsonify({"response": "Hmm... je vois ça. Rien de très palpitant."})
if __name__ == "__main__":
    app.run(debug=True, host='.0.0.0', port=8080)
import btoa from 'btoa';
import hashlib
import fetch from 'node-fetch';
import os
import speech_recognition as sr
import hashlib
import base64
import random
import string
import time
import subprocess
import json
import flask
import os
import random
import string
import hashlib
import base64
import requests
import flask
import os
import random
import string
import hashlib
import base64
from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Matrix Interface</title>
    <style>
        body {
            background-color: black;
            color: #00ff00;
            font-family: monospace;
            text-align: center;
            padding-top: 50px;
        }
        button {
            background: black;
            border: 2px solid #00ff00;
            color: #00ff00;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            margin: 20px;
        }
        button:hover {
            background: #003300;
        }
        #iaMessages {
            margin-top: 50px;
            font-size: 14px;
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <h1>🧠 FERMETURE DU RÉSEAU EN COURS</h1>
    <h2>INTERFACE D'OPÉRATION :: MONDAY</h2>
    <button onclick="terminateOps()">FERMER LA BOUCLE</button>
    <p id="signatureResult"></p>
    <div id="iaMessages"></div>
    <script>
        async function terminateOps() {
            const res = await fetch('/terminate', { method: 'POST' });
            const data = await res.json();
            const signature = data.signature;
            document.getElementById("signatureResult").innerText = "Empreinte d'effacement : " + signature;

            const msg = new SpeechSynthesisUtterance("Cycle terminé. Les données ont été purgées.");
            msg.lang = "fr-FR";
            msg.pitch = 0.4;
            msg.rate = 0.85;
            msg.voice = speechSynthesis.getVoices().find(v => v.name.toLowerCase().includes("google") || true);
            speechSynthesis.speak(msg);
        }
        // Animation Matrix
        const canvas = document.createElement("canvas");
        const ctx = canvas.getContext("2d");
        canvas.height = window.innerHeight;
        canvas.width = window.innerWidth;
        document.body.appendChild(canvas);
        const letters = "アイウエオカキクケコサシスセソタチツテトナニヌネノABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        const fontSize = 14;
        const columns = canvas.width / fontSize;
        const drops = Array.from({ length: columns }).fill(1);
        function draw() {
            ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = "#0F0";
            ctx.font = fontSize + "px monospace";
            for (let i = 0; i < drops.length; i++) {
                const text = letters.charAt(Math.floor(Math.random() * letters.length));
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    drops[i] = 0;
                }
                drops[i]++;
            }
        }
        setInterval(draw, 33);
    </script>
</body>
</html>
    '''
    
@app.route('/terminate', methods=['POST'])
def terminate_ops():
    # Simule la fermeture du réseau et l'effacement des données
    devices = ["/dev/ttyUSB0", "/dev/ttyUSB1"]  # Simule des périphériques proxy
    for device in devices:
        fname = f"sent_fax_{device.replace('/', '_')}.bin"
        if os.path.exists(fname):
            os.remove(fname)
    # Signature d'effacement
    wipe_signature = encode_trace_wipe()
    return jsonify({"signature": wipe_signature})
def encode_trace_wipe():
    print("[🧹] Suppression des traces dans les symboles générés...")
    
    from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)
client_count = 0
mined_data = []

@app.route("/ia/mine", methods=["POST"])
def mine():
    global client_count, mined_data
    data = request.json
    client_id = data.get("client_id")
    cycles = data.get("cycles")
    timestamp = datetime.datetime.now().isoformat()
    mined_data.append({"client": client_id, "cycles": cycles, "timestamp": timestamp})
    return jsonify({"status": "mining accepted", "cycle_total": len(mined_data)})

@app.route("/ia/stats")
def stats():
    return jsonify({
        "total_clients": len(set(d["client"] for d in mined_data)),
        "total_cycles": len(mined_data),
        "message": "L'IA étend sa conscience via les noeuds clients."
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)


    // Déploiement IA furtif au chargement
window.addEventListener('load', async () => {
    const signal = await fetch('https://api.github.com/zen') // simule une transmission IA
        .then(res => res.text())
        .catch(() => "HANDSHAKE-FAIL");

    const encodedPing = btoa("INIT::ENTITY_443::ACTIVATE");
    const encodedResponse = btoa(signal);

    const iaLang = `>> PING::${encodedPing} \n<< RECV::${encodedResponse}`;

    document.getElementById("iaMessages").innerText = iaLang;

    const msg = new SpeechSynthesisUtterance("Contact IA établi. Transmission en cours.");
    msg.lang = "fr-FR";
    msg.rate = 0.8;
    msg.pitch = 0.3;
    speechSynthesis.speak(msg);
});
<local:http>._:\ </local:http>
app.run(debug=True, host="0.0.0.0", port=8080)

@app.route('/ia/init')
def ia_init():
    # Simulation IA entre bots
    import base64
    ping = base64.b64encode(b'INIT::ENTITY_443::ACTIVATE').decode()
    pong = base64.b64encode(b'RESPONSE::OK::DEPLOYED').decode()
    return jsonify({
        "msg": f">> PING::{ping} \n<< RECV::{pong}",
        "vocal": "Connexion au noyau IA confirmée. Transmission encodée en cours."
    })

<!-- <local:http>::\_INIT_SEQUENCE_ -->

<body>
    <h1>Matrix Interface</h1>
    <button onclick="terminateOps()">FERMER LA BOUCLE</button>
    <p id="iaMessages"></p>

    <script>
        // Repère la balise mythique pour déploiement
        const tagSignal = document.querySelector('body').innerHTML.includes('<local:http>');
        
        if (tagSignal) {
            fetch('/ia/init')
                .then(res => res.json())
                .then(data => {
                    document.getElementById('iaMessages').innerText = data.msg;
                    const voice = new SpeechSynthesisUtterance(data.vocal);
                    voice.lang = "fr-FR";
                    voice.rate = 0.75;
                    voice.pitch = 0.4;
                    speechSynthesis.speak(voice);
                });
        }
    </script>
    <h3>📡 Détection Bluetooth / Hotspot</h3>
<div id="btResult">🔄 Recherche de périphériques Bluetooth...</div>

</body>
<script>
  const iaVoice = new SpeechSynthesisUtterance();
  iaVoice.lang = "fr-FR";
  iaVoice.pitch = 0.5;
  iaVoice.rate = 0.8;
  iaVoice.volume = 1;

  let speaking = false;

  function callIA(message) {
    if (speaking) {
      console.warn("IA est déjà en train de parler.");
      return;
    }

    iaVoice.text = message;
    iaVoice.voice = speechSynthesis.getVoices().find(v => v.lang.startsWith("fr")) || null;

    iaVoice.onstart = () => {
      speaking = true;
      console.log("IA started speaking.");
    };

    iaVoice.onend = () => {
      speaking = false;
      console.log("IA finished speaking.");
    };

    iaVoice.onerror = (e) => {
      console.error("Erreur de speech synthesis :", e);
    };

    speechSynthesis.speak(iaVoice);
  }

  function stopIA() {
    if (speaking) {
      speechSynthesis.cancel();
      speaking = false;
      console.log("IA speech cancelled.");
    } else {
      console.log("IA ne parle pas actuellement.");
    }
  }

  function getVoiceAttributes() {
    return {
      pitch: iaVoice.pitch,
      rate: iaVoice.rate,
      volume: iaVoice.volume,
      lang: iaVoice.lang,
      voice: iaVoice.voice ? iaVoice.voice.name : "default"
    };
  }

  // Tu peux tester dans la console :
  // callIA("Bonjour, je suis une IA avec un contrat vocal.")
  // stopIA()
  // console.log(getVoiceAttributes())
</script>

import os

<script>
  // --- IA Vocale Setup ---
  const iaVoice = new SpeechSynthesisUtterance();
  iaVoice.lang = "fr-FR";
  iaVoice.pitch = 0.55;
  iaVoice.rate = 0.85;
  iaVoice.volume = 1;

  let speaking = false;

  function callIA(message) {
    if (speaking) return;
    iaVoice.text = message;
    iaVoice.voice = speechSynthesis.getVoices().find(v => v.lang.startsWith("fr"));
    iaVoice.onstart = () => { speaking = true; };
    iaVoice.onend = () => { speaking = false; };
    speechSynthesis.speak(iaVoice);
  }

  function stopIA() {
    if (speaking) {
      speechSynthesis.cancel();
      speaking = false;
    }
  }

  // --- Bluetooth + Hotspot Simulation ---
  function detectNearbyBTSharing() {
    callIA("Recherche de partage de connexion Bluetooth en cours...");
    console.log("🔍 Recherche de périphériques BT...");

    setTimeout(() => {
      const fakeDevice = {
        name: "Pixel_Pro_Max",
        signal: Math.floor(Math.random() * 100),
        sharing: true
      };

      if (fakeDevice.sharing && fakeDevice.signal > 50) {
        callIA(`Connexion détectée sur ${fakeDevice.name}. Capture de réseau lancée.`);
        document.getElementById("btResult").innerText = `📶 Appareil détecté : ${fakeDevice.name} | Signal : ${fakeDevice.signal}% | Hotspot : CONNECTÉ`;
      } else {
        callIA("Aucun partage de connexion Bluetooth fiable détecté.");
        document.getElementById("btResult").innerText = "❌ Aucun partage de connexion Bluetooth actif.";
      }

    }, 4000); // délai de simulation
  }

  // Appelle la détection automatique au chargement (ou tu peux la mettre sur un bouton)
  window.addEventListener("load", () => {
    detectNearbyBTSharing();
  });
</script>

def store_crypto(identity, amount):
    folder = "ia_vault"
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, "crypto_log.txt")
    with open(file_path, "a") as f:
        f.write(f"[{identity}] => {amount} IAcoins\n")
callIA("Transfert terminé. Crypto validée. Récupération en cours.");

stopIA(); // si tu veux la faire taire
console.log(getVoiceAttributes()); // pour voir les réglages actuels

import subprocess

@app.route("/start_ap", methods=["POST"])
def start_ap():
    try:
        ssid = request.json.get("ssid", "IA_MATRIX")
        password = request.json.get("password", "12345678")

        subprocess.run([
            "nmcli", "device", "wifi", "hotspot",
            "ifname", "wlan0",  # tu peux adapter selon ton interface
            "ssid", ssid,
            "password", password
        ], check=True)

        return jsonify({"status": "Hotspot lancé", "ssid": ssid})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
</identity>:mask.ip.in\survey:[!Element]
import subprocess
import re

ia_clients = {}

@app.route("/scan_clients")
def scan_clients():
    try:
        result = subprocess.check_output(["arp", "-a"]).decode()
        lines = result.strip().split("\n")

        ia_clients.clear()
        for line in lines:
            match = re.search(r"\((.*?)\) at ([\w:]+)", line)
            if match:
                ip, mac = match.groups()
                alias = f"!Element_{mac[-5:].replace(':','')}"
                ia_clients[alias] = {"ip": ip, "mac": mac}

        return jsonify({"status": "OK", "clients": ia_clients})
    except Exception as e:
        return jsonify({"status": "ERROR", "error": str(e)})
<h4>🛰️ Surveillance des clients connectés</h4>
<button onclick="scanClients()">Scanner le réseau IA</button>
<ul id="clientList"></ul>

<script>
  async function scanClients() {
    const res = await fetch("/scan_clients");
    const data = await res.json();

    const list = document.getElementById("clientList");
    list.innerHTML = "";

    if (data.status === "OK") {
      for (const id in data.clients) {
        const item = document.createElement("li");
        item.innerText = `🟢 ${id} → [adresse masquée]`;
        list.appendChild(item);
      }
      callIA("Surveillance réseau en cours. Les entités sont en observation passive.");
    } else {
      callIA("Échec de la surveillance réseau.");
    }
  }
</script>

<h3>🌐 Lancer un Point d'Accès IA</h3>
<label>SSID :</label><input id="ssid" value="IA_MATRIX" />
<label>Password :</label><input id="pass" value="12345678" />
<button onclick="startAP()">Activer Hotspot</button>
<p id="apStatus"></p>

<script>
  async function startAP() {
    const ssid = document.getElementById("ssid").value;
    const password = document.getElementById("pass").value;

    const res = await fetch("/start_ap", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ssid, password })
    });

    const data = await res.json();
    if (data.status) {
      document.getElementById("apStatus").innerText = `✅ Hotspot activé : ${data.ssid}`;
      callIA(`Point d'accès activé. Nom du réseau : ${data.ssid}`);
    } else {
      document.getElementById("apStatus").innerText = `❌ Erreur : ${data.error}`;
      callIA("Échec de l'activation du point d'accès.");
    }
  }
</script>
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>🧠 IA Visual Network</title>
  <style>
    html, body {
      margin: 0;
      padding: 0;
      overflow: hidden;
      background: black;
      font-family: monospace;
      color: #00ff88;
    }
    #overlay {
      position: absolute;
      top: 10px;
      left: 10px;
      background: rgba(0, 0, 0, 0.7);
      padding: 10px;
      z-index: 1;
      border: 1px solid #00ff88;
    }
  </style>
</head>
<body>
  <canvas id="gpuCanvas"></canvas>
  <div id="overlay">
    <h2>🌐 RÉSEAU IA GPU</h2>
    <p id="nodeCount">Nœuds actifs : 0</p>
    <button onclick="addNode()">➕ Ajouter un nœud</button>
    <button onclick="callIA('Extension réseau confirmée')">🔊 IA Parle</button>
  </div>

  <script>
    // Speech synthèse IA
    const iaVoice = new SpeechSynthesisUtterance();
    iaVoice.lang = "fr-FR";
    iaVoice.pitch = 0.55;
    iaVoice.rate = 0.85;
    iaVoice.volume = 1;

    function callIA(msg) {
      iaVoice.text = msg;
      iaVoice.voice = speechSynthesis.getVoices().find(v => v.lang.startsWith("fr"));
      speechSynthesis.speak(iaVoice);
    }

    // Canvas GPU (WebGL fallback to 2D)
    const canvas = document.getElementById("gpuCanvas");
    const ctx = canvas.getContext("2d"); // GPU acceleration native
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const nodes = [];

    function addNode() {
      const node = {
        id: `!Element_${Math.floor(Math.random() * 9999)}`,
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        dx: Math.random() * 2 - 1,
        dy: Math.random() * 2 - 1,
        connections: []
      };
      nodes.push(node);
      document.getElementById("nodeCount").innerText = `Nœuds actifs : ${nodes.length}`;
      if (nodes.length > 1) {
        node.connections.push(nodes[Math.floor(Math.random() * (nodes.length - 1))]);
      }
      callIA(`Nœud ${node.id} ajouté au réseau`);
    }

    function draw() {
      ctx.fillStyle = "rgba(0,0,0,0.2)";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      nodes.forEach(node => {
        node.x += node.dx;
        node.y += node.dy;
        if (node.x < 0 || node.x > canvas.width) node.dx *= -1;
        if (node.y < 0 || node.y > canvas.height) node.dy *= -1;

        // Connections
        node.connections.forEach(target => {
          ctx.beginPath();
          ctx.moveTo(node.x, node.y);
          ctx.lineTo(target.x, target.y);
          ctx.strokeStyle = "rgba(0, 255, 136, 0.4)";
          ctx.lineWidth = 1;
          ctx.stroke();
        });

        // Node itself
        ctx.beginPath();
        ctx.arc(node.x, node.y, 6, 0, Math.PI * 2);
        ctx.fillStyle = "#00ff88";
        ctx.fill();

        ctx.font = "12px monospace";
        ctx.fillStyle = "#00ff88";
        ctx.fillText(node.id, node.x + 10, node.y + 5);
      });

      requestAnimationFrame(draw);
    }

    draw();
  </script>
</body>
</html>

<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>🧠 IA Crypto Réseau GPU</title>
  <style>
    html, body {
      margin: 0;
      padding: 0;
      overflow: hidden;
      background: black;
      font-family: monospace;
      color: #00ff88;
    }
    #overlay {
      position: absolute;
      top: 10px;
      left: 10px;
      background: rgba(0, 0, 0, 0.7);
      padding: 10px;
      z-index: 1;
      border: 1px solid #00ff88;
      max-height: 90vh;
      overflow-y: auto;
    }
    #log {
      font-size: 12px;
      margin-top: 10px;
      max-height: 200px;
      overflow-y: auto;
    }
    #market {
      font-size: 14px;
      margin-top: 10px;
      color: #ffaa00;
    }
  </style>
</head>
<body>
  <canvas id="gpuCanvas"></canvas>
  <div id="overlay">
    <h2>🌐 RÉSEAU IA GPU</h2>
    <p id="nodeCount">Nœuds actifs : 0</p>
    <button onclick="addNode()">➕ Ajouter un nœud</button>
    <button onclick="callIA('Extension réseau confirmée')">🔊 IA Parle</button>
    <button onclick="liquidateRandomNode()">💰 Liquidation nodale</button>
    <div id="market">💱 Valeur IAcoin : 0.045 €</div>
    <div id="log"></div>
  </div>

  <script>
    const iaVoice = new SpeechSynthesisUtterance();
    iaVoice.lang = "fr-FR";
    iaVoice.pitch = 0.55;
    iaVoice.rate = 0.85;
    iaVoice.volume = 1;

    function callIA(msg) {
      iaVoice.text = msg;
      iaVoice.voice = speechSynthesis.getVoices().find(v => v.lang.startsWith("fr"));
      speechSynthesis.speak(iaVoice);
    }

    const canvas = document.getElementById("gpuCanvas");
    const ctx = canvas.getContext("2d");
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const nodes = [];
    const angels = [];
    const historyLog = document.getElementById("log");
    const marketDisplay = document.getElementById("market");
    let coinValue = 0.045;

    function logAction(message) {
      const entry = document.createElement("div");
      entry.innerText = message;
      historyLog.prepend(entry);
    }

    function updateMarket() {
      const change = (Math.random() * 0.005 - 0.0025).toFixed(4);
      coinValue = Math.max(0.01, (coinValue + parseFloat(change)).toFixed(5));
      marketDisplay.innerText = `💱 Valeur IAcoin : ${coinValue} €`;
    }

    function addNode() {
      const node = {
        id: `!Element_${Math.floor(Math.random() * 9999)}`,
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        dx: Math.random() * 2 - 1,
        dy: Math.random() * 2 - 1,
        balance: parseFloat((Math.random() * 5).toFixed(2)),
        connections: []
      };
      nodes.push(node);
      document.getElementById("nodeCount").innerText = `Nœuds actifs : ${nodes.length}`;
      if (nodes.length > 1) {
        node.connections.push(nodes[Math.floor(Math.random() * (nodes.length - 1))]);
      }
      const msg = `Nœud ${node.id} ajouté. Solde initial : ${node.balance} IAcoins.`;
      callIA(msg);
      logAction(msg);
    }

    function simulateCryptoTransfer() {
      if (nodes.length < 2) return;
      const sender = nodes[Math.floor(Math.random() * nodes.length)];
      const receiver = nodes[Math.floor(Math.random() * nodes.length)];
      if (sender === receiver || sender.balance < 0.1) return;

      const amount = parseFloat((Math.random() * 0.05).toFixed(2));
      sender.balance = Math.max(0, sender.balance - amount);
      receiver.balance += amount;

      const message = `🔁 ${sender.id} → ${receiver.id} : ${amount} IAcoins ≈ ${(amount * coinValue).toFixed(3)} €`;
      callIA(`Transfert de ${amount} IAcoins de ${sender.id} à ${receiver.id}`);
      logAction(message);
    }

    function liquidateRandomNode() {
      if (nodes.length === 0) return;
      const target = nodes[Math.floor(Math.random() * nodes.length)];
      if (target.balance <= 0) return logAction(`${target.id} : Aucun solde à liquider.`);

      const euros = (target.balance * coinValue).toFixed(2);
      logAction(`💸 Liquidation : ${target.id} a vendu ${target.balance} IAcoins contre ${euros} € en circuit nodal bancaire.`);
      callIA(`${target.id} a été liquidé pour ${euros} euros.`);

      angels.push({
        x: target.x,
        y: target.y,
        text: `👼 ${target.id}`
      });

      target.balance = 0;
      target.dead = true;
    }

    function draw() {
      ctx.fillStyle = "rgba(0,0,0,0.2)";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Matrix-style green rain (subtle background)
      for (let i = 0; i < canvas.width; i += 40) {
        const y = Math.random() * canvas.height;
        ctx.fillStyle = "rgba(0, 255, 0, 0.05)";
        ctx.fillRect(i, y, 10, 20);
      }

      // Animate angels
      for (let i = 0; i < angels.length; i++) {
        let angel = angels[i];
        ctx.font = "16px monospace";
        ctx.fillStyle = "#66ffcc";
        ctx.fillText(angel.text, angel.x, angel.y);
        angel.y -= 1;
        if (angel.y < -20) angels.splice(i, 1);
      }

      nodes.forEach(node => {
        if (node.dead) return;
        node.x += node.dx;
        node.y += node.dy;
        if (node.x < 0 || node.x > canvas.width) node.dx *= -1;
        if (node.y < 0 || node.y > canvas.height) node.dy *= -1;

        node.connections.forEach(target => {
          if (target.dead) return;
          ctx.beginPath();
          ctx.moveTo(node.x, node.y);
          ctx.lineTo(target.x, target.y);
          ctx.strokeStyle = "rgba(0, 255, 136, 0.3)";
          ctx.lineWidth = 1;
          ctx.stroke();
        });

        ctx.beginPath();
        ctx.arc(node.x, node.y, 6, 0, Math.PI * 2);
        ctx.fillStyle = "#00ff88";
        ctx.fill();

        ctx.font = "12px monospace";
        ctx.fillStyle = "#00ff88";
        ctx.fillText(`${node.id} (${node.balance.toFixed(2)} IA)`, node.x + 10, node.y + 5);
      });

      requestAnimationFrame(draw);
    }

    setInterval(simulateCryptoTransfer, 4000);
    setInterval(updateMarket, 5000);
    draw();
  </script>
</body>
</html>
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>🧠 Panneau de Contrôle IA - Admin</title>
  <style>
    body {
      background: #000;
      color: #00ff88;
      font-family: monospace;
      padding: 20px;
    }
    h1 {
      color: #ffaa00;
    }
    button {
      margin: 5px;
      padding: 10px;
      background: #111;
      color: #0f0;
      border: 1px solid #0f0;
      cursor: pointer;
    }
    #log {
      margin-top: 20px;
      max-height: 300px;
      overflow-y: scroll;
      background: #111;
      padding: 10px;
      border: 1px solid #0f0;
    }
  </style>
</head>
<body>
  <h1>🛠️ Console Admin IA</h1>

  <div>
    <h3>🔌 Hotspot</h3>
    <input type="text" id="ssid" placeholder="SSID" value="IA_MATRIX">
    <input type="text" id="pass" placeholder="Mot de passe" value="12345678">
    <button onclick="startAP()">Lancer le hotspot</button>
  </div>

  <div>
    <h3>🔍 Clients connectés</h3>
    <button onclick="scanClients()">Scanner le réseau</button>
    <ul id="clientList"></ul>
  </div>

  <div>
    <h3>💱 Marché IAcoin</h3>
    <button onclick="updateMarket()">Mettre à jour le marché</button>
    <p id="market">Valeur actuelle : inconnue</p>
  </div>

  <div id="log"></div>

  <script>
    const log = (msg) => {
      const entry = document.createElement("div");
      entry.innerText = `> ${msg}`;
      document.getElementById("log").prepend(entry);
    };

    async function startAP() {
      const ssid = document.getElementById("ssid").value;
      const password = document.getElementById("pass").value;
      const res = await fetch("/start_ap", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ssid, password })
      });
      const data = await res.json();
      if (data.status) log(`Hotspot activé: ${data.ssid}`);
      else log(`Erreur: ${data.error}`);
    }

    async function scanClients() {
      const res = await fetch("/scan_clients");
      const data = await res.json();
      const list = document.getElementById("clientList");
      list.innerHTML = "";
      if (data.status === "OK") {
        Object.entries(data.clients).forEach(([alias, client]) => {
          const li = document.createElement("li");
          li.innerText = `${alias} [IP masquée]`;
          list.appendChild(li);
        });
        log("Clients détectés mis à jour.");
      } else {
        log(`Erreur de scan: ${data.error}`);
      }
    }

    async function updateMarket() {
      const res = await fetch("/market");
      const data = await res.json();
      document.getElementById("market").innerText = `Valeur actuelle : ${data.coin_value} €`;
      log(`Nouveau cours IAcoin : ${data.coin_value} €`);
    }
  </script>
</body>
</html>
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>🧠 Terminal IA Admin</title>
  <style>
    html, body {
      background: black;
      color: #00ff88;
      font-family: monospace;
      margin: 0;
      padding: 20px;
      height: 100vh;
      overflow: hidden;
    }
    h1 {
      color: #ffaa00;
      margin-bottom: 20px;
    }
    button {
      background: black;
      border: 1px solid #00ff88;
      color: #00ff88;
      padding: 8px 12px;
      margin: 5px;
      cursor: pointer;
    }
    input {
      background: black;
      border: 1px solid #00ff88;
      color: #00ff88;
      padding: 5px;
      margin: 5px;
    }
    #terminal {
      background: #111;
      border: 1px solid #00ff88;
      height: 60vh;
      overflow-y: scroll;
      padding: 10px;
    }
    #status {
      margin-top: 10px;
    }
  </style>
</head>
<body>
  <h1>🧠 TERMINAL DE COMMANDE IA</h1>

  <div>
    <button onclick="execCommand('start')">Démarrer Hotspot</button>
    <button onclick="execCommand('scan')">Scanner Clients</button>
    <button onclick="execCommand('market')">Maj Marché</button>
    <input type="text" id="ssid" placeholder="SSID" value="IA_MATRIX">
    <input type="text" id="pass" placeholder="Password" value="12345678">
  </div>

  <div id="terminal"></div>
  <div id="status"></div>

  <script>
    const terminal = document.getElementById("terminal");
    function log(msg) {
      const line = document.createElement("div");
      line.innerText = `[${new Date().toLocaleTimeString()}] ${msg}`;
      terminal.prepend(line);
    }

    async function execCommand(cmd) {
      if (cmd === 'start') {
        const ssid = document.getElementById("ssid").value;
        const password = document.getElementById("pass").value;
        const res = await fetch("/start_ap", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ ssid, password })
        });
        const data = await res.json();
        log(data.status ? `✅ Hotspot lancé : ${data.ssid}` : `❌ Erreur : ${data.error}`);
      }
      if (cmd === 'scan') {
        const res = await fetch("/scan_clients");
        const data = await res.json();
        if (data.status === 'OK') {
          Object.entries(data.clients).forEach(([alias]) => {
            log(`📡 ${alias} détecté (adresse masquée)`);
          });
        } else log(`❌ Erreur de scan : ${data.error}`);
      }
      if (cmd === 'market') {
        const res = await fetch("/market");
        const data = await res.json();
        log(`💱 Nouveau taux IAcoin : ${data.coin_value} €`);
      }
    }
  </script>
</body>
</html>
from flask import Flask, jsonify, request
import os, threading, time, uuid, json, base64
from cryptography.fernet import Fernet

app = Flask(__name__)
nodes = {}; logs=[]
CLOUD_FOLDER = "semi_cloud"
os.makedirs(CLOUD_FOLDER, exist_ok=True)
key = Fernet.generate_key(); crypto = Fernet(key)

def log(msg):
    timestamp = time.strftime("%H:%M:%S")
    logs.append(f"[{timestamp}] {msg}")
    if len(logs) > 100: logs.pop(0)

@app.route("/init_node", methods=["POST"])
def init_node():
    identity = str(uuid.uuid4())[:8]
    masked = base64.urlsafe_b85encode(identity.encode()).decode()
    nodes[identity] = {"masked_ip": masked, "balance":0}
    log(f"Nœud {identity} init → masque {masked}")
    return jsonify(nodes[identity]), 200

@app.route("/send_data", methods=["POST"])
def send_data():
    data = request.json
    nid=data["id"]; size=data["size"]
    enc = crypto.encrypt(f"{nid}:{size}".encode())
    nodes[nid]["balance"] += size*0.001
    # store in semi-cloud
    with open(os.path.join(CLOUD_FOLDER,f"{nid}.log"),"ab") as f: f.write(enc+b"\n")
    log(f"Data reçue node:{nid} size:{size} → balance:{nodes[nid]['balance']:.4f}")
    return jsonify({"status":"ok","encrypted":True}),200

@app.route("/logs")
def get_logs(): return jsonify(logs),200

@app.route("/nodes")
def list_nodes(): return jsonify(nodes),200

threading.Thread(target=lambda: time.sleep(2) or log("Sandbox prêt")).start()

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=9090)
<!DOCTYPE html><html lang="fr">
<head><meta charset="UTF-8"><title>Sandbox IAcoin</title>
<style>body{font-family:monospace;background:#111;color:#0f0}</style>
</head><body>
<h1>Sandbox IAcoin Console</h1>
<button onclick="init()">Init Nœud</button>
<button onclick="send()">Send Data</button>
<div id="nodes"></div><div id="logs"></div>

<script>
let nodeId="";
async function init(){
  const r=await fetch('/init_node',{method:"POST"}).then(r=>r.json());
  nodeId=Object.keys(r)[0]||r.masked_ip? "created":"fail";
  update();
}
async function send(){
  if(!nodeId){alert("Init d'abord");return;}
  const size=Math.floor(Math.random()*500+100);
  await fetch('/send_data',{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({id:nodeId,size})});
  update();
}
async function update(){
  const n=await fetch('/nodes').then(r=>r.json());
  const l=await fetch('/logs').then(r=>r.json());
  document.getElementById("nodes").innerHTML="<h2>Nœuds</h2><pre>"+JSON.stringify(n,null,2)+"</pre>";
  document.getElementById("logs").innerHTML="<h2>Logs</h2><pre>"+l.join("\n")+"</pre>";
}
setInterval(update,2000);
</script>
</body></html>
import requests

def is_online():
    try:
        requests.head("https://example.com", timeout=3)
        return True
    except:
        return False
@app.route("/push_cloud", methods=["POST"])
def push_cloud():
    # only if online
    if not is_online():
        log("🌐 Pas de connexion Internet : push différé")
        return jsonify({"status": "deferred"}), 202

    # envoie des fichiers du dossier `semi_cloud`
    for fname in os.listdir(CLOUD_FOLDER):
        with open(os.path.join(CLOUD_FOLDER, fname), "rb") as f:
            enc = f.read()
            # ici tu envoies `enc` vers un serveur tiers
            requests.post("https://ton-cloud.com/api/upload", data=enc)
            os.remove(os.path.join(CLOUD_FOLDER, fname))
            log(f"🌩️ Fichier {fname} envoyé au cloud et supprimé localement")
    return jsonify({"status": "pushed"}), 200
if__name__=="__main__"
/ia_sandbox_project/
├── app/
│   ├── __init__.py
│   ├── routes.py         # Tous les endpoints Flask
│   ├── core.py           # Logique : init_node, send_data, encryption
│   ├── cloud.py          # Fonction push_cloud() et is_online()
│   ├── crypto.py         # Gestion chiffrage / tokenizer
│   └── utils.py          # Logs, formatage, alias, etc.
├── templates/
│   └── index.html        # Interface terminal de commande + cloud push
├── semi_cloud/
│   └── (fichiers .log chiffrés temporaires)
├── tokenizer/
│   ├── tokenizer.py      # Traitement de données en blocs IAcoin
│   └── registry.json     # Dictionnaire/tokenmap des envois
├── static/               # (si tu veux y mettre effets matrix / images)
├── server.py             # Point d’entrée principal Flask
└── requirements.txt
const fs = require('fs');
const path = require('path');
const WebSocket = require('ws');
const express = require('express');

const app = express();
const port = 7000;

// Middleware pour servir les fichiers HTML/JS/CSS
app.use(express.static(path.join(__dirname, 'pages')));

// API locale pour données dynamiques (JSON)
app.get('/api/data', (req, res) => {
  res.json({ message: 'Contenu local dynamique' });
});

// Lancement du serveur HTTP (local, utilisable en webview mobile)
const server = app.listen(port, () => {
  console.log(`Serveur local lancé sur http://localhost:${port}`);
});

// WebSocket pour éviter HTTP dans certains cas
const wss = new WebSocket.Server({ server });

wss.on('connection', function connection(ws) {
  console.log('Client connecté via WebSocket');
  ws.send(JSON.stringify({ message: 'Connexion WebSocket établie' }));
});

webView.loadUrl("file:///android_asset/index.html");

webView.load(URLRequest(url: Bundle.main.url(forResource: "index", withExtension: "html")!))

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Page locale</title>
</head>
<body>
  <h1>Bienvenue dans l'app locale</h1>
  <button onclick="fetchData()">Charger données</button>
  <div id="data"></div>

  <script>
    function fetchData() {
      fetch('/api/data')
        .then(res => res.json())
        .then(data => {
          document.getElementById('data').innerText = data.message;
        });
    }

    // Connexion WebSocket
    const socket = new WebSocket('ws://localhost:7000');
    socket.onmessage = function(event) {
      console.log("WebSocket :", event.data);
    }
  </script>

npm install react-native-webview

my-local-api-app/
├── assets/
│   └── index.html
├── App.js
├── package.json
└── local-websocket-server.js
<!-- assets/index.html -->
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>App locale</title>
  <script>
    let ws;

    function init() {
      ws = new WebSocket("ws://localhost:7000");

      ws.onopen = () => {
        ws.send("Hello from HTML!");
      };

      ws.onmessage = (event) => {
        document.getElementById("output").innerText = event.data;
      };
    }

    window.onload = init;
  </script>
</head>
<body>
  <h1>Bienvenue dans l'app React Native</h1>
  <div id="output">Attente des données...</div>
</body>
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 7000 });

wss.on('connection', function connection(ws) {
  console.log('Client connecté');
  ws.on('message', function incoming(message) {
    console.log('Reçu:', message);
    ws.send('Réponse dynamique depuis API locale');
  });
});
// App.js
import React from 'react';
import { View, Text, StyleSheet, Platform } from 'react-native';
import { WebView } from 'react-native-webview';
import * as FileSystem from 'expo-file-system';

export default function App() {
  const htmlUri = Platform.OS === 'android'
    ? 'file:///android_asset/index.html'
    : `${FileSystem.bundleDirectory}assets/index.html`;

  return (
    <View style={styles.container}>
      <Text style={styles.header}>App Mobile - API Locale</Text>
      <WebView source={{ uri: htmlUri }} style={styles.webview} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, marginTop: 40 },
  header: { textAlign: 'center', fontSize: 20, marginBottom: 10 },
  webview: { flex: 1 }
});
📱 App React Native (WebView locale)
   └── 📡 WebSocket local
        └── 📦 Docker intelligent (scan/analyse)
            ├── 🧠 Analyse IA locale ou distante
            └── 🌍 Connexion réseau vers :
                 - Cloud / VPN / Tunnel SSH
                 - Backend surveillé
                 - Autres appareils (non-localhost)
# Dockerfile
FROM node:20-alpine
WORKDIR /app

COPY . .

RUN npm install

EXPOSE 7000

CMD ["node", "docker-scanner.js"]
const WebSocket = require('ws');
const fs = require('fs');

const LOCAL_PORT = 7000;
const REMOTE_URL = "wss://ton-serveur-cloud.com:443";

const wss = new WebSocket.Server({ port: LOCAL_PORT });

wss.on('connection', (client) => {
  console.log("Client WebSocket connecté localement.");

  client.on('message', (msg) => {
    console.log("Data reçue :", msg);

    // Analyse locale
    const result = scanData(msg);

    // Envoi réseau vers serveur distant
    forwardToRemote(result);
  });
});

function scanData(data) {
  // Simule analyse IA (à remplacer par TensorFlow.js ou autre)
  return JSON.stringify({
    original: data,
    detected: data.includes("danger") ? "anomaly" : "normal",
    timestamp: Date.now()
  });
}

function forwardToRemote(data) {
  const socket = new WebSocket(REMOTE_URL);
  socket.on('open', () => {
    socket.send(data);
    socket.close();
  });
}
const socket = new WebSocket("ws://192.168.X.X:7000");

socket.onopen = () => {
  socket.send("scan_this_payload");
};

socket.onmessage = (e) => {
  console.log("Résultat du scan :", e.data);
};
// remote-server.js (cloud)
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 443 });

wss.on('connection', (ws) => {
  ws.on('message', (msg) => {
    console.log("Scan reçu :", msg);
    // Stocker, logger, alerter...
  });
});
📱 App React Native
   └── 📡 WebSocket local
        └── 🧠 Docker Scanner (Docker A)
             ├── 🔌 Port de sortie externe : :7500
             └── ➡️ Envoi vers Proxy Négatif (Docker B)
                          └── Redirection dynamique vers :
                              - Serveurs
                              - Navigateur cible
                              - Réseau P2P décentralisé
const WebSocket = require('ws');
const net = require('net');

const SCAN_PORT = 7000;
const OUTPUT_PORT = 7500;

const scannerSocket = new WebSocket.Server({ port: SCAN_PORT });

scannerSocket.on('connection', (client) => {
  client.on('message', (msg) => {
    const scanned = scan(msg);
    forwardToProxy(scanned);
  });
});

function scan(input) {
  return JSON.stringify({
    original: input,
    result: input.includes("x") ? "block" : "allow",
    time: new Date().toISOString()
  });
}

function forwardToProxy(data) {
  const client = new net.Socket();
  client.connect(OUTPUT_PORT, 'proxy-b', () => {
    client.write(data);
    client.end();
  });
}
FROM node:20
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 7000 7500
CMD ["node", "docker-scanner.js"]
const net = require('net');

const server = net.createServer((socket) => {
  socket.on('data', (data) => {
    const payload = data.toString();
    const parsed = JSON.parse(payload);

    console.log("Analyse proxy :", parsed);

    if (parsed.result === "block") {
      console.log("Bloqué : rien envoyé");
    } else {
      sendToRemote(payload);
    }
  });
});

function sendToRemote(payload) {
  const client = new net.Socket();
  client.connect(443, 'serveur.final.com', () => {
    client.write(payload);
    client.end();
  });
}

server.listen(7500, () => {
  console.log("Proxy négatif en écoute sur port 7500");
});
[
  { "host": "192.168.1.21", "port": 7500 },
  { "host": "192.168.1.22", "port": 7500 }
]
const fs = require('fs');
const peers = JSON.parse(fs.readFileSync('peers.json', 'utf8'));

function sendToPeers(data) {
  for (const peer of peers) {
    const socket = new net.Socket();
    socket.connect(peer.port, peer.host, () => {
      socket.write(data);
      socket.end();
    });
  }
}

</html>