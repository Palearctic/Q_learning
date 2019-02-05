import numpy as np

ROOP=1000 #点を打つ回数

#a以上b未満の乱数をi個返す
def make_random(a,b,i):
    if a>b:    a,b=b,a  
    return (b-a)*np.random.rand(i)+a

#乱数により打たれた点と関数との位置関係を判定
def judge(f,locate_x,locate_y):
    count=0
    f_x=f(locate_x)
    for i in range(ROOP):
        if f_x[i]>=0:
            if locate_y[i]<=f_x[i] and locate_y[i]>=0:
                count+=1
        else:
            if locate_y[i]>=f_x[i] and locate_y[i]<=0:
                count-=1
    return count

#区間内において関数の最大値・最小値の近似値を求める
def get_min_and_max(f,x1,x2):
    division=int((x2-x1)*100) #分割回数は区間の大きさ×100[回]
    s=np.linspace(x1,x2,division)
    return np.min(f(s)),np.max(f(s))  

#モンテカルロ法 関数fをx1からx2まで定積分
def monte_carlo(f,x1,x2):
    f1,f2=get_min_and_max(f,x1,x2)  
    square_s=(x2-x1)*abs(f2-f1) #矩形の面積
    locate_x=make_random(x1,x2,ROOP) #ランダムに打たれた点のx座標
    locate_y=make_random(f1,f2,ROOP) #ランダムに打たれた点のy座標
    count=judge(f,locate_x,locate_y)
    return square_s*count/ROOP

def f(x):
    return np.sin(x)

#定積分に用いる関数はndarrayで値を返す
def g(x):
    return np.array((x**2)-2)

def main():
    print("定積分の近似値={:.3f}".format(monte_carlo(f,0,np.pi)))
    print("定積分の近似値={:.3f}".format(monte_carlo(g,0,2)))
