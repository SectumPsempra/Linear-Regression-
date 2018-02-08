# Linear-Regression

Parameters - State, SchoolLocation, MotherTongue, Gender, ParentIncomePerAnnum, PercentInClass12, AvgNumberofHrsStudied
State, MotherTongue, Gender, ParentIncomePerAnnum, PercentInClass12, AvgNumberofHrsStudied are randomly generated and saved in a dataframe, which was saved in a csv file to generate dataset.

PercentInClass12 and AvgNumberofHrsStudied are used to calculate a new parameter called JEE_SCORE. The PercentInClass12, AvgNumberofHrsStudied are tweaked and normalized between (0, 360). However this is not the final model and some weights needs to be multiplied to make the model accurate.

Training and Test data is separated in the ratio of 80 : 20 (Out of 1000 data points 800: 200).

Linear regression is used to make the prediction. Matplotlib is used to see the plotting

![alt text](https://github.com/SectumPsempra/Linear-Regression-/blob/master/Figure_1.png?raw=true)


This project is completely automated now and can be run independently by executing "Execute.py".

Instructions for running the project - 

1) Clone/Download the repository by clicking on the clone button.
2) Run Execute.py
3) Enter the filename you want to save data in with appropriate file extension(.csv preferably otherwise some changes need to be made)
4) You can see the above figure in output.

The JEE_SCORE is plotted against AvgNumberofHrsStudied.
After running two times this gave an accuracy score of 53 - 57 %.
