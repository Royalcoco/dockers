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
setInterval(navAnalyticsPing, 5000);  // ping toutes les 5s


from flask import Flask, request, jsonify
import subprocess
import os
import threading
sudo python3 app.py
# This script sets up a Flask web application that captures network traffic using tcpdump,
# extracts DNS queries, and provides a mock AI response for user input.
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
# Note: This code requires root privileges to run tcpdump.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
# Note: This code requires root privileges to run tcpdump.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
# Note: This code requires root privileges to run tcpdump.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
# Note: This code requires root privileges to run tcpdump.
import os
import hashlib
import random
import string
from datetime import datetime

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
# Note: This code requires root privileges to run nmcli and access Wi-Fi information.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
# Note: This code requires root privileges to run nmcli and access Wi-Fi information.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
# Note: This code requires root privileges to run nmcli and access Wi-Fi information.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
# Note: This code requires root privileges to run nmcli and access Wi-Fi information.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
# Note: This code requires root privileges to run nmcli and access Wi-Fi information.
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
# Note: This code is a simulation and does not actually lock files.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
# Note: This code is a simulation and does not actually lock files.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
# Note: This code is a simulation and does not actually lock files.
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
    <hr>
    <p>Note: Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.</p>
</body>sudo python3 app.py
</html>

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
    <p id="aiResponse\sudo python3 app.py"></p>
</body>
</html>
import os
import subprocess
import threading
from flask import Flask, request, jsonify, render_template
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
    if "youtube" in user_input:
        return jsonify({"response": "Ah, encore un qui mate des vidéos pendant les heures de cours."})
    elif "google" in user_input:
        return jsonify({"response": "Chercher des trucs, hein ? Fascinant."})
    else:
        return jsonify({"response": "Hmm... je vois ça. Rien de très palpitant."})
if __name__ == "__main__":
    app.run(debug=True)
import os
import hashlib
import random
import string
from datetime import datetime
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
# Note: This code requires root privileges to run nmcli and access Wi-Fi information.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
# Note: This code requires root privileges to run nmcli and access Wi-Fi information.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
# Note: This code requires root privileges to run nmcli and access Wi-Fi information.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
# Note: This code requires root privileges to run nmcli and access Wi-Fi information.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
# Note: This code requires root privileges to run nmcli and access Wi-Fi information.
# Note: This code requires root privileges to run nmcli and access Wi-Fi information.
# Note: This code requires root privileges to run nmcli and access Wi-Fi information.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
# Note: This code requires root privileges to run nmcli and access Wi-Fi information.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
Execute : sudo python3 app.py
sudo tcpdump -i wlan0 -A port 80 > http_dump.log
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

console.log(navigator.connection);
def disable_wifi():
    print("Tentative de coupure Wi-Fi...")
    subprocess.run(["nmcli", "radio", "wifi", "off"])
if __name__ == "__main__":
    print("Analyse du trafic sortant en cours...")
    domains = extract_domains_from_log("http_dump.log")
    disable_wifi()
    print("Connexion coupée. Remplacement par du trafic simulé...")
    simulate_fake_requests(domains)

import os
import time
import subprocess

def scan_and_connect(target_ssid):
    print(f"Scan des réseaux Wi-Fi...")
    result = os.popen("nmcli dev wifi").read()
    if target_ssid not in result:
        print("Hotspot cible non trouvé.")
        return False
    os.system(f"nmcli dev wifi connect '{target_ssid}' password 'tape_ton_guess_ici'")
    print(f"Connecté à {target_ssid}")
    return True

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

def extract_domains_from_log(filepath):
    domains = set()
    with open(filepath, "r") as f:
        for line in f:
            if "Host:" in line:
                parts = line.strip().split()
                if len(parts) >= 2:
                    domains.add(parts[1])
    return list(domains)
📠 scan_fax_simulator.py      → Envoie un faux "scan fax" à une imprimante/proxy sur le réseau
🔊 voiceprint_emulator.py     → Génère une empreinte vocale IA unique par cible
🔐 keyboard_lock.py           → Simule un clavier crypté déverrouillable uniquement via cette empreinte
🌐 proxy_network.py           → Balaye le réseau pour toutes les machines "faxables"
🔣 symbol_transmitter.py      → Envoie les symboles de fermeture incompréhensibles à chaque noeud
import os
import subprocess
import time
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
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
    if "youtube" in user_input:
        return jsonify({"response": "Ah, encore un qui mate des vidéos pendant les heures de cours."})
    elif "google" in user_input:
        return jsonify({"response": "Chercher des trucs, hein ? Fascinant."})
    else:
        return jsonify({"response": "Hmm... je vois ça. Rien de très palpitant."})
if __name__ == "__main__":
    app.run(debug=True)
import os
import hashlib
import random
import string
from datetime import datetime
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
def send_fax_payload(target_ip):
    print(f"[📠] Envoi d'un faux FAX numérique vers {target_ip}...")
    payload = f"--FAKE-FAX--{target_ip}--"
    # Simulation d'écriture dans une imprimante réseau
    with open(f"sent_fax_{target_ip.replace('.', '_')}.bin", "w") as f:
        f.write(payload)
    return payload
def scan_network_for_faxable_devices():
    print("[🌐] Balayage du réseau pour les appareils faxables...")
    # Simulation de découverte d'appareils faxables
    devices = ["def discover_proxy_devices():
    print("[🌐] Scan du réseau local à la recherche de proxy/fax...")
    return ["192.168.0.21", "192.168.0.35", "192.168.0.108"]
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
import random
import string

def generate_symbols():
    symbols = ''.join(random.choices(string.ascii_uppercase + string.digits + "!@#¥₿%&*", k=20))
    print(f"[🔣] Envoi de symboles impossibles : {symbols}")
    return symbols
def keyboard_access(voiceprint_input, expected_voiceprint):
    if voiceprint_input == expected_voiceprint:
        print("[🔓] Clavier déverrouillé.")
        return True
    else:
        print("[🔐] Accès refusé. Tonalité biométrique incorrecte.")
        return False
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
    "       devices = ["meta\data-entry", "meta\proxy-server", "meta\fax-machine"]
    "       devices = ["
    "       devices = ["meta\data-entry", "meta\proxy-server", "meta\fax-machine"]
    "       devices = ["meta\data-entry", "meta\proxy-server", "meta\fax-machine"]
    "       devices = ["meta\data-entry", "meta\proxy-server", "meta\fax-machine"]
    "       devices = ["meta\data-entry", "meta\proxy-server", "meta\fax-machine"]
    "       devices = ["meta\data-entry", "meta\proxy-server", "meta\fax-machine"]
    "       devices = ["meta\data-entry", "meta\proxy-server", "meta\fax-machine"]
    "       devices = ["meta\data-entry", "meta\proxy-server", "meta\fax-machine"]
    "       devices = ["meta\data-entry", "meta\proxy-server", "meta\fax-machine"]
    "       devices = ["meta\data-entry", "meta\proxy-server", "meta\fax-machine"]
    "       devices = ["meta\data-entry", "meta\proxy-server", "meta\fax-machine"]
    "       devices = ["meta\data-entry", "meta\proxy-server", "meta\fax-machine"]  
    
    return devices
    "    "
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
# Note: This code is a simulation and does not actually lock files.
# Assurez-vous d'avoir les permissions nécessaires pour exécuter ce script.
# Note: This code is a simulation and does not actually lock files.
sector clean :[📠] Envoi d'un faux FAX numérique vers 192.168.0.35...
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
sport: sudo python3 app.py --host=0.0.0.0 --port=8080
from flask import Flask, jsonify
from proxy_network import discover_proxy_devices
app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>Hotspot Sniffer 9000</h1><p>Utilisez les endpoints pour interagir avec le système.</p>"
@app.route("/discover", methods=["GET"])
def discover():
    devices = discover_proxy_devices()
    return jsonify({"devices": devices})
    return ngrok http 8080

@app.route("/terminate", methods=["POST"])
def terminate_ops():
    devices = discover_proxy_devices()
    for ip in devices:
        fname = f"sent_fax_{ip.replace('.', '_')}.bin"
        if os.path.exists(fname):
            os.remove(fname)
    wipe_signature = encode_trace_wipe()
    return jsonify({"signature": wipe_signature})
    print("[💾] Journaux effacés de la mémoire volatile.")
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

Flask
cryptography
requests
pip install -r requirements.txt
python server.py
ia_sandbox_project/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── core.py
│   ├── cloud.py
│   ├── crypto.py
│   └── utils.py
├── tokenizer/
│   ├── tokenizer.py
│   └── registry.json
├── templates/
│   └── index.html
├── semi_cloud/
├── server.py
└── requirements.txt
from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="../templates")
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    return app
from flask import Blueprint, request, jsonify, render_template
from app.core import init_node, send_data, get_nodes, get_logs
from app.cloud import push_cloud, is_online
from app.crypto import encrypt_and_store

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/init_node", methods=["POST"])
def route_init():
    return jsonify(init_node())

@main_bp.route("/send_data", methods=["POST"])
def route_send():
    data = request.json
    nid = data["id"]
    size = data["size"]
    enc = encrypt_and_store(nid, size)
    return jsonify({"status": "ok", "balance": get_nodes()[nid]["balance"], "encrypted": True})

@main_bp.route("/nodes")
def route_nodes():
    return jsonify(get_nodes())

@main_bp.route("/logs")
def route_logs():
    return jsonify(get_logs())

@main_bp.route("/push_cloud", methods=["POST"])
def route_push():
    res = push_cloud()
    return jsonify(res)
import uuid, time
from app.utils import log
from app.crypto import crypto, store_encrypted
nodes = {}

def init_node():
    identity = str(uuid.uuid4())[:8]
    nodes[identity] = {"balance": 0}
    log(f"Nœud {identity} initialisé")
    return nodes[identity]

def send_data(nid, size):
    nodes[nid]["balance"] += size * 0.001
    log(f"Data de {size} ko reçue pour {nid}, nouveau solde : {nodes[nid]['balance']:.4f}")
    encrypted = store_encrypted(nid, size)
    return encrypted

def get_nodes():
    return nodes

def get_logs():
    from app.utils import logs
    return logs
import os
import base64
from cryptography.fernet import Fernet
from app.utils import log

CLOUD = "semi_cloud"
os.makedirs(CLOUD, exist_ok=True)

key = Fernet.generate_key()
crypto = Fernet(key)

def store_encrypted(nid, size):
    data = f"{nid}:{size}:{time.time()}".encode()
    token = crypto.encrypt(data)
    fname = os.path.join(CLOUD, f"{nid}.log")
    with open(fname, "ab") as f:
        f.write(token + b"\n")
    log(f"Écriture chiffrée dans {fname}")
    return True
import os, requests
from app.crypto import CLOUD
from app.utils import log

def is_online():
    try:
        requests.head("https://example.com", timeout=3)
        return True
    except:
        return False

def push_cloud():
    if not is_online():
        log("🌐 Hors ligne, push différé")
        return {"status": "deferred"}

    for fname in os.listdir(CLOUD):
        path = os.path.join(CLOUD, fname)
        with open(path, "rb") as f:
            data = f.read()
            requests.post("https://ton-cloud.com/api/upload", data=data)
        os.remove(path)
        log(f"🌩️ Envoyé {fname} au cloud et supprimé")
    return {"status": "pushed"}
import time
logs = []

def log(msg):
    logs.append(f"[{time.strftime('%H:%M:%S')}] {msg}")
    if len(logs) > 100:
        logs.pop(0)
import json, os
from datetime import datetime

REG = "tokenizer/registry.json"

def load_registry():
    if os.path.exists(REG):
        return json.load(open(REG))
    else:
        return {"tokens": [], "count": 0}

def save_registry(reg):
    json.dump(reg, open(REG, "w"), indent=2)

def tokenize_entry(nid, size):
    reg = load_registry()
    token = {
        "id": nid,
        "size": size,
        "timestamp": datetime.now().isoformat()
    }
    reg["tokens"].append(token)
    reg["count"] = len(reg["tokens"])
    save_registry(reg)
    return token
from app import create_app
app = create_app()

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=9090)
<!DOCTYPE html>
<html lang="fr">
<head><meta charset="UTF-8"><title>Sandbox IAcoin Admin</title>
<style>body{font-family:monospace;background:#111;color:#0f0}button{margin:5px;}</style>
</head><body>
<h1>Sandbox IAcoin Admin Console</h1>
<button onclick="init()">Init Node</button>
<button onclick="send()">Send Data</button>
<button onclick="document.location.reload()">Refresh</button>
<button onclick="push()">Push Cloud</button>
<pre id="nodes"></pre><pre id="logs"></pre>
<script>
let nid="";
async function init(){
  const r = await fetch("/init_node",{method:"POST"}).then(r=>r.json());
  nid = Object.keys(r)[0] || Object.keys(r)[0]? Object.keys(r)[0] : null;
  update();
}
async function send(){
  if(!nid){alert("Init d'abord");return;}
  const size=Math.floor(Math.random()*500+100);
  await fetch("/send_data",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({id:nid,size})});
  update();
}
async function push(){
  const r = await fetch("/push_cloud",{method:"POST"}).then(r=>r.json());
  alert("Push status: "+r.status);
  update();
}
async function update(){
  const [nodes, logs] = await Promise.all([fetch("/nodes"), fetch("/logs")]).then(r=>Promise.all(r.map(x=>x.json())));
  document.getElementById("nodes").innerText = JSON.stringify(nodes,null,2);
  document.getElementById("logs").innerText = logs.join("\n");
}
setInterval(update,2000);
</script>
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

</html>
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
