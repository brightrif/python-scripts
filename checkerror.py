import paramiko
import sys
import time
ip= [List of IP address]
port=22
username='foo'
password='pass'

cmd='sudo cat /var/log/messages | grep error'

#loop for each IP address
for ips in ip:
    #initiate the connection to client
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ips,port,username,password)
    #execute the command
    stdin,stdout,stderr=ssh.exec_command(cmd,get_pty=True)
    time.sleep(2)
    #if the command executed sucessfully then read the output
    if stdout.channel.exit_status_ready():
        if not stdout.channel.recv_ready():
            outlines=stdout.readlines()
            if outlines :
                print ('not emty')
                print(outlines)
            else:
                print ('emty')
    else:
        print ("The command is not sucess")
    del stdout,ssh,stdin,stderr
