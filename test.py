import numpy as np

def pop(i,t):
    
    M=[]
    ep = np.arange(start=0,stop=i)
    for e in range(0,t):
        M.append(np.random.choice(ep))
    return M    
