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


# However, if you're having trouble finding the path to the Python executable on your machine, you can have the sys 
# module do that for you. This module interacts very well with the subprocess, and a good use case for it is to 
# replace the path to the executable like this:
# Ref: https://www.dataquest.io/blog/python-subprocess/
import sys
result = subprocess.run([sys.executable, "-c", "print('This is a subprocess')"])