import numpy as np

val=[]
with open("output")as f:
    for i in f.readlines():
        if "value:" in i:
            val.append(eval(i[17:-1]))


data=[np.frombuffer(np.array(i),dtype="int16").tolist()[::2] for i in val]
print(len(data))