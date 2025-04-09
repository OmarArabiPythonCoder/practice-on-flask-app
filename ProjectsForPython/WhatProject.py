import random
import time

projects = [
    "web scramper/graph maker", "lumber jack ripoff", "simple AI chatbot that makes fun at you"
]

for i in range(1, 4):
    time.sleep(1)
    print(i)

time.sleep(0.8)
print("THE CHOSEN PROJECT IS!")
time.sleep(0.8)
print(random.choice(projects))