from LinRegFinal import *
from Task import *

fileName = raw_input("Enter the name of the file with extension(.csv or any other): ")
initialize = CreateDataSet(fileName)
initialize.define_parameters()
initialize.generate_dataset()

linearRegInit = LinearRegressionClass(fileName)
PlotResult(linearRegInit).plot()
PlotResult(linearRegInit).print_score()
