import platform
import jsonify


class Flask:
    pass


app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Bem-vindo à API da VM!",
        "status": "operacional"
    });

# Informações do sistema
def jsonify(param):
    pass


@app.route("/system")
def system_info():
    return jsonify({
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor()
    });

# Uso da CPU
@app.route("/cpu")
def cpu_usage(psutil=None):
    return jsonify({
        "cpu_percent": psutil.cpu_percent(interval=1),
        "cores": psutil.cpu_count(logical=True)
    });

# Uso da memória
@app.route("/memory")
def memory_usage(psutil=None):
    memory = psutil.virtual_memory()
    return jsonify({
        "total_memory": memory.total,
        "available_memory": memory.available,
        "used_memory": memory.used,
        "memory_percent": memory.percent
    });

# Espaço em disco
@app.route("/disk")
def disk_usage(psutil=None):
    disk = psutil.disk_usage('/')
    return jsonify({
        "total_disk": disk.total,
        "used_disk": disk.used,
        "free_disk": disk.free,
        "disk_percent": disk.percent
    });

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000);