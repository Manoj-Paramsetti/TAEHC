from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"Salary_Data.csv")
x=list(df["YearsExperience"])
y=list(df["Salary"])
df
def LinearRegressor(x,y):
 sumX=sum(x)
 sumY=sum(y)
 xMean=sumX/len(x)
 yMean=sumY/len(y)
 x_minus_xmean=[val-xMean for val in x]
 y_minus_ymean=[val-yMean for val in y]
 zip_li=zip(x_minus_xmean,y_minus_ymean)
 val=[x*y for x,y in zip_li]
 b1=sum(val)/sum([x**2 for x in x_minus_xmean])
 b0=yMean-b1*xMean
 return b0,b1
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/2,shuffle=True)
b=LinearRegressor(x_train,y_train)
y_pred=[b[0]+b[1]*val for val in x_test]

r2_score(y_test,y_pred)

plt.plot(x_test,y_pred)
plt.scatter(x_test, y_test,c="k")



from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np


#RMSE value
print( "RMSE: ",np.sqrt( mean_squared_error( y_test, y_pred ) ))
#R-squared value
print( "R-squared: ",r2_score( y_test, y_pred ) )