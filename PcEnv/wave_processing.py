import numpy as np
import matplotlib.pyplot as plt
import wave

def wavread():
  wave_file = wave.open("PcEnv/TestWavs/explosion.wav","rb") 
  x = wave_file.readframes(wave_file.getnframes()) 
  x = np.frombuffer(x, dtype= "int16")
  return x

def sq(n):
  return n**2

def todb(x,n):
  #x=list(map(sq,x))
  sm=sum(x[:n])
  ret=[]
  for i in range(len(x)-n):
    #if 0<sm:
    ret.append(20*np.log10(np.sqrt((sm**2)*(1/n))))
    #else:
     # print(i)
     # ret.append(-1)
    sm+=(int(x[i+n])-int(x[i]))
  return ret

def to_db(x, N):
    pad = np.zeros(N//2)
    pad_data = np.concatenate([pad, x, pad])
    rms = np.array([np.sqrt((1/N) * (np.sum(pad_data[i:i+N]))**2) for i in range(len(x))])
    ret=20 * np.log10(rms)
    return ret

lis=todb(wavread(),1024)
x=range(len(lis))
plt.bar(x,lis)
plt.show()