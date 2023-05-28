import paramiko
import time
import sys

arg = sys.argv
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('192.168.8.149', port=22, username='mroqa', password='Pa$$w0rd', allow_agent=False,look_for_keys=False)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

stdin, stdout, stderr = ssh.exec_command('cd \helloc && make deploy svr='+arg[1])
while int(stdout.channel.recv_exit_status()) != 0:
    time.sleep(1)
out = stdout.read().decode()
# in_ = stdin.read().decode()
err = stderr.read().decode()
print(out)
# print(in_)
print(err)

if ssh is not None:
    ssh.close()
    del ssh, out, err

