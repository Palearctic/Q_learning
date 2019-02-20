def knn(data,X_train,y_train):
    min_dis=float("inf")
    for i in range(len(X_train)):
        dis=0
        for j in range(len(data)):
            dis+=(data[j]-X_train[i][j])**2
        if dis<min_dis:
            min_dis=dis
            ans=y_train[i]
    return ans 

def knn_test(X_train,y_train,X_test,y_test):
    score=0
    for i in range(len(X_test)):
        data=knn(X_test[i],X_train,y_train)
        if data==y_test[i]:
            score+=1
    return score/len(X_test)
