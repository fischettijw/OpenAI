# https://www.youtube.com/watch?v=eWrTSBIQess


# https://stackoverflow.com/questions/68582382/how-to-pip-install-pickle-under-python-3-9-in-windows#:~:text=I%20found%20a,pickle4%20as%20pickle
# I found a way that I'm not sure it's the optimal but it works.
# I did pip install pickle4
# And then in the script just

# import pickle4 as pickle

import pickle
import os; os.system("cls")

data1 = {'name': 'Mike',
        'age': 26,
        'hair color': 'brown'}
print("data1")
print(type(data1))
print(data1)
print()

data2 = [1,6,"hello", 4.67]
print("data2")
print(type(data2))
print(data2)
print()

with open('data.pkl', 'wb') as file:
    pickle.dump(data1, file)
    pickle.dump(data2, file)
    
with open('data.pkl', 'rb') as file:
    data1_depickled = pickle.load(file)
    data2_depickled = pickle.load(file)

print("data1_depickled")    
print(type(data1_depickled))
print(data1_depickled)
print()

print(print("data2_depickled")  )
print(type(data1_depickled))
print(data2_depickled)
print()