import time
start = time.clock()
count = 0
while count <= 1000:
    count += 1
stop = time.clock()
print('Computational cost:', stop-start)
# time.clock() was removed in 3.8 because it had platform-dependent behavior:
