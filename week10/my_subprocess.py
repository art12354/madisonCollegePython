import subprocess
myProc = subprocess.run(['ps', '-axco', 'command'], stdout=subprocess.PIPE)
myProcString = myProc.stdout.decode()
myProcList = myProcString.split('\n')
for proc in myProcList:
    print(proc)
print(len(myProcList[1:]))
