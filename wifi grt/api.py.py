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

