# import subprocess
# output = subprocess.call(['ls', '-l'])
# print(output)

# import subprocess
# output = subprocess.run(['ls', '-l']).returncode
# print(output)

# import subprocess
# output = subprocess.call('ls -l', shell=True)
# print(output)

import subprocess
subprocess.call(['ls', '-l'], shell=True)
