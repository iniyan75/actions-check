import os

print(os.getcwd())
directory = '../check1/'
if os.path.exists(directory):
    print("Directory  exists")
