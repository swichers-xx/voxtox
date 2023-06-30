import subprocess

# Ping a server
def ping_server(server):
    response = subprocess.run(['ping', '-n', '1', server], stdout=subprocess.PIPE)
    return response.returncode == 0

# Check the status of all services with "voxco" in the name
def check_voxco_services():
    cmd = 'powershell "Get-Service *voxco* | Where-Object {$_.Status -eq \'Running\'} | Format-List -Property Name, Status"'
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = process.communicate()[0].decode('utf-8').splitlines()

    running_services = [line.split(':')[1].strip() for line in output if 'Name' in line]

    return running_services

# Test the functions
print(ping_server('localhost'))
print(check_voxco_services())
