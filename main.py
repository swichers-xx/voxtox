import subprocess

# Ping a server
def ping_server(server):
    response = subprocess.run(['ping', '-n', '1', server], stdout=subprocess.PIPE)
    return response.returncode == 0

# Check the status of all services with "voxco" in the name
def check_voxco_services():
    cmd = 'sc query state= all | findstr /i "voxco SERVICE_NAME:"'
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    services = process.communicate()[0].decode('utf-8').splitlines()
    services = [s.split(':')[1].strip() for s in services]

    running_services = []
    for service in services:
        cmd = f'sc query "{service}" | find "RUNNING"'
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        output = process.communicate()[0]
        if "RUNNING" in output.decode('utf-8'):
            running_services.append(service)

    return running_services

# Test the functions
print(ping_server('localhost'))
print(check_voxco_services())
