import subprocess

def get_system_uptime():
    uptime = subprocess.run(['uptime'], capture_output=True, text=True)        
    uptime_line = uptime.stdout.strip().split(',')[0]
    return print(uptime_line)

def get_hostname():
    hostname = subprocess.run(['hostname'], capture_output=True, text=True)
    hostname_line = hostname.stdout.strip().split(',')[0]
    return print(hostname_line)

def get_cpu_info():
    cpu_architekture = subprocess.run([''], capture_output=True, text=True)
    cpu_architekture_line = cpu_architekture.stdout.strip().split(',')[0]

    cpu_model = subprocess.run([''], capture_output=True, text=True)
    cpu_model_line = cpu_model.stdout.strip().split(',')[0]

def get_root_disk_size():
    pass

def get_network_interfaces():
    pass

def main():
    get_system_uptime()
    get_hostname()
    get_root_disk_size()
    get_network_interfaces()


if __name__ == "__main__":
    main()