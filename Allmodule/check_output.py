# import subprocess
# output = subprocess.run(['ls', '-l'], check=True)
# print(output)
# import subprocess
# output = subprocess.check_output(['ls'])
# print(output)

# using run function as equivalent of check_output
import subprocess
output = subprocess.run(['ls'], check=True, stdout=subprocess.PIPE).stdout
print(output)
