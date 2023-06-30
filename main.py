import subprocess

# Ping a server
def ping_server(server):
    response = subprocess.run(['ping', '-n', '1', server], stdout=subprocess.PIPE)
    return response.returncode == 0

# Check the status of all services with "voxco" in the name on a specific server
def check_voxco_services(server):
    cmd = f'powershell "Get-Service -ComputerName {server} *voxco* | Where-Object {{$_.Status -eq \'Running\'}} | Format-List -Property Name, Status"'
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = process.communicate()[0].decode('utf-8').splitlines()

    running_services = [line.split(':')[1].strip() for line in output if 'Name' in line]

    return running_services

# List of servers
servers = ["VXSQL", "VXDIRSRV", "VXTCPA", "VXDLR1", "VXDIAL", "VXCATI1", "VXCATI2", "VXREPORT", "VXOADMIN", "VXONLINE"]

# Check each server
for server in servers:
    if ping_server(server):
        print(f'Server {server} is up.')
        print('Running Voxco services:', check_voxco_services(server))
    else:
        print(f'Server {server} is down.')
