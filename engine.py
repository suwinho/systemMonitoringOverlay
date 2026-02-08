import psutil
import GPUtil


def get_system_stats():
    cpu_usage = psutil.cpu_percent(interval=None, percpu=True)
    cpu_freq = psutil.cpu_freq(percpu=True)
    ram_data = psutil.virtual_memory()
    ram_usage = round(ram_data.used / 1024 ** 3, 4)
    ram_total = round(ram_data.total / 1024 ** 3, 4)
    ram_available = round(ram_data.available / 1024 ** 3, 4)
    disk_io = psutil.disk_io_counters()
    gpu_info = GPUtil.getGPUs()
    if len(gpu_info) != 0:
        gpu_usage = gpu_info[0].load

    return {
        'cpu_usage': cpu_usage,
        'cpu_freq': cpu_freq,
        'ram_data': ram_data,
        'ram_usage': ram_usage,
        'ram_total': ram_total,
        'ram_available': ram_available,
        'disk_io': disk_io,
        'gpu_usage': gpu_usage
    }
def get_top_processes():
    processes = []
    for process in psutil.process_iter(['pid','name','cpu_percent']):
        try:
            processes.append(process.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return sorted(processes, key=lambda x: x['cpu_percent'], reverse = True)[:5]



def kill_process(pid):
    try:
        psutil.Process(pid).kill()
        return True
    except:
        return False