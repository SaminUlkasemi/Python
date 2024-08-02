# ---------------------------------------------------------------------------- #
#                          Executing External Command                          #
# ---------------------------------------------------------------------------- #
# 
# Ref: https://www.datacamp.com/tutorial/python-subprocess
# Ref: Python cookbook 2013

import subprocess, os

print("Current dir: ", os.getcwd())

# subprocess.check_output() return the result in byte format
try:
    res = subprocess.check_output(['dir'])
    print(res.decode('utf-8'))
except Exception as e:
    print(e) 

# subprocess.run() execute & show the output of the code in realtime
try:
    res = subprocess.run(['ping', 'gooertgle.com'],
                                  stderr=subprocess.STDOUT, #? standard output and error collected
                                  timeout=5,
                                  check=True
                                  )
    #? print("stdout: ", res.stdout)
    #? print("stderr: ", res.stderr)
except Exception as e:
    print(e)
 
 

 
'''   
try:
    res = subprocess.check_output('grep Python | wc > out', shell=True, timeout=3)
except Exception as e:
    print(e)
'''