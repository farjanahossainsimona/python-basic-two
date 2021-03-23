# import subprocess
# output = subprocess.Popen('uname')
# print(type(output))
# print(output)

# import shlex
# import subprocess
# command = 'uname -r'
# args = shlex.split(command)
# print(args)
# output = subprocess.Popen(args)
# print(output)
# code = output.wait()
# print(code)
import subprocess
proc = subprocess.Popen('ls')
try:
    outs, err = proc.communicate(timeout=15)
except TimeoutExpired:
    proc.kill()
    outs, err = proc.communicate()
