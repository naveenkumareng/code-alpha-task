from flask import Flask, render_template, jsonify
import threading
import time
import logging

app = Flask(__name__)
packets_data = []

# Try to import scapy; if unavailable or lacking privileges, fall back to demo data
has_scapy = False
try:
    from scapy.all import sniff
    from scapy.layers.inet import IP, TCP, UDP, ICMP
    has_scapy = True
except Exception as e:
    logging.warning("Scapy not available or failed to import: %s", e)
    has_scapy = False


def packet_sniffer():
    if has_scapy:
        def analyze(packet):
            try:
                if IP in packet:
                    info = {
                        "src": packet[IP].src,
                        "dst": packet[IP].dst,
                        "protocol": "TCP" if TCP in packet else "UDP" if UDP in packet else "ICMP" if ICMP in packet else "OTHER",
                        "payload": str(bytes(packet.payload))[:200]
                    }
                    packets_data.append(info)
                    # keep list bounded
                    if len(packets_data) > 1000:
                        del packets_data[:-500]
            except Exception:
                pass

        # Run sniff in a loop with timeout so exceptions/privilege errors don't kill the thread
        while True:
            try:
                sniff(prn=analyze, store=False, timeout=5)
            except Exception as e:
                logging.warning("Sniff failed: %s", e)
                time.sleep(5)
    else:
        # Fallback demo generator so the web UI still works without packet capture
        demo_count = 0
        while True:
            demo_count += 1
            packets_data.append({
                "src": f"192.0.2.{demo_count % 255}",
                "dst": f"198.51.100.{demo_count % 255}",
                "protocol": "TCP",
                "payload": f"demo payload {demo_count}"
            })
            if len(packets_data) > 200:
                packets_data.pop(0)
            time.sleep(2)


threading.Thread(target=packet_sniffer, daemon=True).start()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/packets")
def get_packets():
    return jsonify(packets_data[-20:])  # last 20 packets


if __name__ == "__main__":
    app.run(debug=True)
