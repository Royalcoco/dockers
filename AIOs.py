ia_alert/
├── app/
│   ├── main.py         # Backend Flask + WebSocket
│   ├── alerts.py       # Module IA / gestion des alertes
│   └── utils.py        # Logs, gestion des flux et des clients
├── templates/
│   └── index.html      # Interface utilisateur
├── static/
│   ├── style.css       # Styles UI
│   └── client.js       # WebSocket client
├── requirements.txt
├── Dockerfile
└── docker-compose.yml

from .utils import log

current_message = None

def set_alert(msg):
    global current_message
    current_message = msg
    log(f"ALERTE déclenchée: {msg}")

def clear_alert():
    global current_message
    log("Alerte effacée")
    current_message = None
    
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from .alerts import set_alert, clear_alert, current_message
from .utils import log, get_streams

app = Flask(__name__, template_folder="../templates", static_folder="../static")
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    streams = get_streams()
    return render_template("index.html", streams=streams, alert=current_message)

@app.route("/alert", methods=["POST"])
def alert():
    data = request.json
    set_alert(data.get("message", ""))
    socketio.emit("alert", {"message": current_message})
    return jsonify(status="ok")

@app.route("/clear", methods=["POST"])
def clean():
    clear_alert()
    socketio.emit("clear", {})
    return jsonify(status="ok")

@socketio.on("connect")
def on_connect():
    if current_message:
        emit("alert", {"message": current_message})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
logs = []
streams = [
    {"name": "Météo webcam", "src": "https://www.youtube.com/embed/your_public_weather_stream"},
    {"name": "Flux info en direct", "src": "https://www.youtube.com/embed/your_public_news_stream"}
]

def log(msg):
    logs.append(msg)
    if len(logs) > 200: logs.pop(0)

def get_streams():
    return streams

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>IA‑ALERTE Hub</title>
  <link rel="stylesheet" href="/static/style.css">
  <script src="https://cdn.socket.io/4.7.2/socket.io.min.js"></script>
  <script src="/static/client.js"></script>
</head>
<body>
  <h1>IA‑ALERTE</h1>
  <div id="streams">
    {% for s in streams %}
      <div class="stream">
        <h2>{{ s.name }}</h2>
        <iframe src="{{ s.src }}" frameborder="0" allowfullscreen></iframe>
      </div>
    {% endfor %}
  </div>
  <div id="alertBox" class="hidden"></div>
  <div id="controls">
    <textarea id="alertMsg" placeholder="Message d'alerte..."></textarea>
    <button onclick="sendAlert()">Déclencher alerte</button>
    <button onclick="clearAlert()">Effacer alerte</button>
  </div>
</body>
</html>

const socket = io();

socket.on("alert", d => {
  const box = document.getElementById("alertBox");
  box.innerText = "⚠️ " + d.message;
  box.classList.remove("hidden");
});

socket.on("clear", () => {
  const box = document.getElementById("alertBox");
  box.classList.add("hidden");
  box.innerText = "";
});

function sendAlert() {
  const msg = document.getElementById("alertMsg").value;
  fetch("/alert", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: msg })
  });
}

function clearAlert() {
  fetch("/clear", { method: "POST" });
}

body { background:#111; color:#0f0; font-family:monospace; padding:20px; }
.stream { margin-bottom:20px; }
iframe { width:100%; height:300px; }
#alertBox { background:#900; color:#fff; padding:10px; margin:10px 0; font-size:1.2em; border:2px solid #f00; }
.hidden { display:none; }
#controls textarea { width:100%; height:60px; background:#222; color:#0f0; }
button { margin:5px; background:#222; color:#0f0; border:1px solid #0f0; padding:10px; }

Flask
flask-socketio
eventlet

FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app app
COPY templates templates
COPY static static
CMD ["python","-u","app/main.py"]

version: "3.8"
services:
  ia_alert:
    build: .
    ports:
      - "5000:5000"

    <volumes:re>
    volumes:
      - ./app:/app/app
      - ./templates:/app/templates
      - ./static:/app/static
    environment:
      - FLASK_ENV=development
      - FLASK_APP=app.main
    command: python -u app/main.py
    depends_on:
      - redis
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
volumes:
  redis_data:
    driver: local
    driver_opts:
      type: none
      device: /var/lib/redis
      o: bind
    <:volumes:re>
    volumes:
      - redis_data:/data
    driver: local
    driver_opts:
      type: none
      device: /var/lib/redis
      o: bind
    </volumes:re>

    docker-compose up --build[:,/`:]<div class="proxy-bar" data-state="ok" style="--value:65%">
  <div class="label">Observer</div>
</div>
<div class="proxy-bar" data-state="error" style="--value:20%">
  <div class="label">Synth</div>
</div>
<div class="proxy-bar" data-state="idle" style="--value:45%">
  <div class="label">Proto</div>
</div>

.proxy-bar {
  --bar-color: #0f0;
  width: 40px;
  height: 150px;
  margin: 10px;
  border-radius: 10px;
  background: linear-gradient(to top, var(--bar-color) var(--value), #111 var(--value));
  display: inline-block;
  position: relative;
  transition: all 0.5s ease;
  box-shadow: inset 0 0 10px var(--bar-color);
}

.proxy-bar[data-state="ok"]   { --bar-color: #0f0; }
.proxy-bar[data-state="idle"] { --bar-color: #ffaa00; }
.proxy-bar[data-state="error"] { --bar-color: #f00; }

.proxy-bar .label {
  position: absolute;
  bottom: -25px;
  left: 50%;
  transform: translateX(-50%);
  color: #0f0;
  font-family: monospace;
  font-size: 0.8em;
}

function updateBar(id, state, percent) {
  const el = document.querySelector(`[data-label="${id}"]`);
  if (!el) return;
  el.dataset.state = state;
  el.style.setProperty('--value', percent + '%');
}

import random
buffer = []

def gen_freq():
    return random.randint(0,7)  # 3 bits => 0–7

def combine_and_process(n_entries=1):
    f1, f2 = gen_freq(), gen_freq()
    combo = f1 + f2
    total = combo * n_entries
    if total == 0:
        out = 0
    else:
        buffer.append({"f1":f1,"f2":f2,"n":n_entries,"total":total})
        out = None
    return {"f1":f1,"f2":f2,"total":total,"output":out}

def get_buffer():
    return buffer.copy()

def clear_buffer():
    buffer.clear()

import random
from flask import Flask, jsonify, request, render_template
from flask_socketio import SocketIO, <emit->
emit
from .utils import log, <get_streams class="diff<",/`>Flask
flask-socketio
eventlet
get_streams as get_streams
app = Flask(__name__, template_folder="../templates", static_folder="../static")
socketio = SocketIO(app, cors_allowed_origins="*")
@get_streams>
def index():
    streams = get_streams()
    return render_template("index.html", streams=streams, alert=current_message)
@get_streams>
@app.route("/alert", methods=["POST"])
def alert():
    data = request.json
    set_alert(data.get("message", ""))
    socketio.emit("alert", {"message": current_message})
    return jsonify(status="ok")
@get_streams>
@app.route("/clear", methods=["POST"])
def clean():
    clear_alert()
    socketio.emit("clear", {})
    return jsonify(status="ok")
@get_streams>
@socketio.on("connect")
def on_connect():
    if current_message:
        emit("alert", {"message": current_message})
@get_streams>
if __name__ == "__main__":
    socketio.run(app, host="5050.0", port=5000)
    from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from .logic import combine_and_process, get_buffer, clear_buffer
import threading, time

app = Flask(__name__, template_folder="../templates", static_folder="../static")
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/buffer")
def api_buffer():
    return jsonify(get_buffer())

@socketio.on("connect")
def on_connect():
    socketio.emit("update", combine_and_process())

def sync_loop():
    while True:
        time.sleep(3)
        result = combine_and_process()
        socketio.emit("update", result)

threading.Thread(target=sync_loop, daemon=True).start()

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)

const socket = io();
socket.on("update", data => {
  document.getElementById("status").innerText =
    `f1=${data.f1}, f2=${data.f2}, total=${data.total}, output=${data.output}`;
});

<!DOCTYPE html><html>
<head><meta charset=utf-8><title>IA Logic Sync</title>
<script src="https://cdn.socket.io/4.7.2/socket.io.min.js"></script>
<script src="/static/client.js"></script>
<style>
body{font-family:monospace;background:#111;color:#0f0;padding:20px;}
pre{background:#000;color:#0f0;padding:10px;}
button{padding:5px;margin:5px;background:#222;color:#0f0;}
</style>
</head><body>
<h1>IA Logic Sync Dashboard</h1>
<pre id="status">Connexion en cours...</pre>
<button onclick="fetch('/api/buffer').then(r=>r.json()).then(d=>document.getElementById('status').innerText += '\\nBUFFER: '+ JSON.stringify(d));">Voir buffer</button>
<button onclick="fetch('/api/buffer').then(fetch('/api/buffer?clear=true'));">Effacer buffer</button>
</get_streams>
</emit-></body></html>
--<get_streams class="diff<"--><emit-># IA Logic Sync Dashboard.
# This module handles the logic for combining frequencies and managing the buffer.
# It provides an API to fetch the current state and clear the buffer.
# It uses Flask and SocketIO for real-time updates.
from flask import Flask, jsonify, request:WindowsError  `\ /:\_/:\ /:.WindowsError/function get_streams():
    return [
        {"name": "Météo webcam", "src": "https://www.youtube.com/embed/your_public_weather_stream"},
        {"name": "Flux info en direct", "src": "https://www.youtube.com/embed/your_public_news_stream"}
    ]
from flask_socketio import SocketIO, emit # Initialize Flask app and SocketIO
app = Flask(__name__, template_folder="../templates", static_folder="../static")
socketio = SocketIO(app, cors_allowed_origins="*")
from .logic import combine_and_process, get_buffer, clear_buffer
