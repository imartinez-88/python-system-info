from flask import jsonify, render_template
import psutil
import platform
from datetime import datetime

def configure_routes(app):
    
    @app.route('/')
    def dashboard():
        """Serve the dashboard HTML"""
        return render_template('dashboard.html')
    
    @app.route('/health')
    def health():
        """Basic health check endpoint"""
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.utcnow().isoformat()
        })
    
    @app.route('/info')
    def info():
        """Detailed system information"""
        # CPU info
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        
        # Memory info
        mem = psutil.virtual_memory()
        
        # Disk info
        disk = psutil.disk_usage('/')
        
        # System uptime
        boot_time = psutil.boot_time()
        uptime = datetime.now().timestamp() - boot_time
        
        return jsonify({
            'hostname': platform.node(),
            'platform': platform.system(),
            'platform_version': platform.version(),
            'architecture': platform.machine(),
            'cpu_count': cpu_count,
            'cpu_percent': cpu_percent,
            'mem_total': mem.total,
            'mem_available': mem.available,
            'mem_used': mem.used,
            'mem_percent': mem.percent,
            'disk_total': disk.total,
            'disk_used': disk.used,
            'disk_free': disk.free,
            'disk_percent': disk.percent,
            'uptime': uptime
        })