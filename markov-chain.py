import numpy as np
from matplotlib import pyplot

TRANSITION=np.array([[0.3,0.3,0.4],[0.1,0.5,0.4],[0.2,0.6,0.2]]) #遷移行列
INIT=np.array([0.6,0.25,0.15]) #初期状態分布
ROOP=15 #遷移回数
n=np.arange(ROOP)
RED=np.zeros(ROOP)
BLUE=np.zeros(ROOP)
WHITE=np.zeros(ROOP)

 #状態分布の更新
 def renew_p(state):
    return np.dot(state,TRANSITION)

#プロット
def plot():
    pyplot.plot(n,RED,label='red')
    pyplot.plot(n,BLUE,label='blue')
    pyplot.plot(n,WHITE,label='white')

    pyplot.title('p_transition')
    pyplot.xlabel('n')
    pyplot.ylabel('p')
    pyplot.legend()
    
    pyplot.show()

def main():
    s=INIT
    for i in range(ROOP):
        s=renew_p(s)
        RED[i]=s[0]
        BLUE[i]=s[1]
        WHITE[i]=s[2]
    print("最終的な状態分布={}".format(s))
    plot()
    
main()
