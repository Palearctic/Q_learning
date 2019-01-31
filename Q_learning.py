#coding:utf-8
from numpy.random import *
import numpy as np

NODE=15 #ノードの個数(2分木)
ALPHA=0.1 #学習係数
GAMMA=0.9 #割引率
EPSILON=0.3 #ε-greedy法の閾値
ROTATION=1000 #繰り返し回数

#0からiの乱数を返す
def get_random(i):
    return randint(i+1)

#木を作り、ランダムなQ値を割り当て(0-100)
def make_tree():
    q_value=np.zeros(NODE)
    for i in range(NODE):
        q_value[i]=get_random(100)
    return q_value

#報酬を定義
def reward():
    reward_list=np.zeros(NODE)
    reward_list[14]=1000
    return reward_list

#ε-greedy法に基づいた経路選択
def which_way(s,q_value):
    if random()>EPSILON:
        if q_value[2*s+1]>=q_value[2*s+2]:
            return 2*s+1 #左
        else:
            return 2*s+2 #右
    else:
        return 2*s+1+get_random(1) #ランダムな経路選択

#Q値の更新
def update_q(s,q_value,reward_list):
    if s>6: #最下段
        return q_value[s]+ALPHA*(reward_list[s]-q_value[s])
    else: #それ以外
        return q_value[s]+ALPHA*(reward_list[s]+GAMMA*max(q_value[2*s+1],q_value[2*s+2])-q_value[s])

#結果確認
def print_q(q_value):
    for i in range(NODE):
        print("{}:{:.3f}".format(i,q_value[i]))
    print("------")
    
def main():
    q_value=make_tree()
    reward_list=reward()
    print_q(q_value) #Q値の初期値
    for i in range(ROTATION):
        s=0 #状態
        for i in range(3):
            s=which_way(s,q_value)
            q_value[s]=update_q(s,q_value,reward_list)
    print_q(q_value) #最終結果
    
main()
