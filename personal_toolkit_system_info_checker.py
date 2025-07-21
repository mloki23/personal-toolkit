import platform
import psutil

def get_system_info():
    """
    Returns a dictionary containing system information.
    """
    info = {}
    info['system'] = platform.system()
    info['node_name'] = platform.node()
    info['release'] = platform.release()
    info['version'] = platform.version()
    info['machine'] = platform.machine()
    info['processor'] = platform.processor()
    info['cpu_usage'] = psutil.cpu_percent(interval=1)
    info['memory_usage'] = psutil.virtual_memory().percent
    info['disk_usage'] = psutil.disk_usage('/').percent
    return info