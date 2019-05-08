import csv
import os 

path = os.getcwd() + '\\ex1data1.txt'
with open(path) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    features = []
    outputs = []
    for row in readCSV:
        feature = float(row[0])
        output = float(row[1])

        features.append(feature)
        outputs.append(output)

def gradientDescent(features, outputs, alpha=0.01, iters=10000, theta0=0, theta1=0):
    num_features = len(features)
    
    for i in range(0,iters):
        temp_theta0 = theta0
        temp_theta1 = theta1
        mse = cost(features,outputs,temp_theta0,temp_theta1,num_features)
        error_theta0 = 0
        error_theta1 = 0
        for i in range(0,num_features):
            error_theta0 += theta0 + theta1 * features[i] - outputs[i]
            error_theta1 += (theta0 + theta1 * features[i] - outputs[i])*features[i]                
        theta0 = temp_theta0 - alpha * error_theta0 / num_features
        theta1 = temp_theta1 - alpha * error_theta1 / num_features
        if(cost(features,outputs,theta0,theta1,num_features) >= mse):
            break
        print(f"theta0: {theta0}, theta1: {theta1}")
        print(mse)

def cost(features,outputs,theta0,theta1,num_features):
    x = 0
    for i in range(0,num_features):
        x += (theta0 + theta1*features[i] - outputs[i])**2
    mse = x/(2*num_features)
    return mse
    
gradientDescent(features,outputs)      
