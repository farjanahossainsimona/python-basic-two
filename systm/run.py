#import subprocess
#output = subprocess.run(["ls", "-l"])
# print(output)
import subprocess
output = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
type(output)
print(output)
type(output.stdout)
print(type(output.stdout))
result = output.stdout.decode('UTF-8')
print(result)
