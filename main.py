import subprocess

# Ping a server
def ping_server(server):
    response = subprocess.run(['ping', '-n', '1', server], stdout=subprocess.PIPE)
    return response.returncode == 0

# Check the status of a service
def check_service(service):
    cmd = f'sc query "{service}" | find "RUNNING"'
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return "RUNNING" in output.decode('utf-8')

# Test the functions
print(ping_server('localhost'))
print(check_service('W32Time'))  # W32Time is a common Windows service
