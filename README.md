# Linear-Regression

Parameters - State, SchoolLocation, MotherTongue, Gender, ParentIncomePerAnnum, PercentInClass12, AvgNumberofHrsStudied
State, MotherTongue, Gender, ParentIncomePerAnnum, PercentInClass12, AvgNumberofHrsStudied are randomly generated and saved in a dataframe, which was saved in a csv file to generate dataset.

PercentInClass12 and AvgNumberofHrsStudied are used to calculate a new parameter called JEE_SCORE. The PercentInClass12, AvgNumberofHrsStudied are multiplied and normalized between (0, 360). However this is not the final model and some weights needs to be multiplied to make the model accurate.

Training and Test data is separated in the ratio of 80 : 20 (Out of 1000 data points 800: 200).

Linear regression is used to make the prediction. Matplotlib is used to see the plotting

