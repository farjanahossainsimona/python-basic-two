# import subprocess
# output = subprocess.check_call(['ls', '-l'])
# print(output)
# using run function as equivalent of check_call output
import subprocess
output = subprocess.run(['ls', '-l'], check=True)
print(output)
