from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

# Simulación de datos del observatorio con cambios dinámicos
def generate_observatory_status():
    return {
        "status": "operational" if random.random() > 0.1 else "warning",
        "telescopes": {
            "orion": {"status": random.choice(["active", "calibrating", "offline"]), "target": random.choice(["Betelgeuse", "Andromeda", "Sirius"]), "last_check": time.time()},
            "cassiopeia": {"status": random.choice(["active", "maintenance", "offline"]), "target": random.choice(["Cassiopeia A", "Vega", "Polaris"]), "last_check": time.time()},
        },
        "systems": {
            "power": {"status": random.choice(["normal", "low power", "critical"]), "output": f"{random.randint(50, 100)}%"},
            "communication": {"status": random.choice(["normal", "intermittent", "failure"]), "signal_strength": random.choice(["excellent", "good", "weak"])}
        },
    }

observatory_data = generate_observatory_status()

@app.route('/')
def hello_world():
    """Ruta principal del observatorio."""
    return '🌌 Welcome to the Stellar Observatory! 🚀'

@app.route('/health')
def health():
    """Ruta de salud del observatorio."""
    return jsonify({"status": "OK", "message": "All systems operational."})

@app.route('/status')
def status():
    """Ruta de estado general del observatorio."""
    global observatory_data
    observatory_data = generate_observatory_status()
    time.sleep(random.uniform(0.5, 2))  # Simulación de retardo en la respuesta
    return jsonify({
        "observatory": "Stellar Laboratory",
        "status": observatory_data["status"],
        "systems": observatory_data["systems"],
    })

@app.route('/telescopes')
def telescopes():
    """Ruta para ver el estado de los telescopios."""
    global observatory_data
    observatory_data = generate_observatory_status()
    time.sleep(random.uniform(0.5, 2))  # Simulación de retardo en la respuesta
    return jsonify({
        "telescopes": observatory_data["telescopes"],
    })

@app.route('/monitor')
def monitor():
    """Ruta de monitoreo avanzado."""
    global observatory_data
    observatory_data = generate_observatory_status()
    time.sleep(random.uniform(0.5, 2))  # Simulación de retardo en la respuesta
    return jsonify({
        "observatory": "Stellar Laboratory",
        "status": observatory_data["status"],
        "telescopes": observatory_data["telescopes"],
        "systems": observatory_data["systems"],
        "message": "All systems are being monitored in real-time.",
    })

if __name__ == '__main__':
    app.run(debug=True)
