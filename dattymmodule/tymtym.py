import time
start = time.time()
count = 0
while count <= 1000:
    count += 1
stop = time.time()
print('Computational cost:', stop-start)
