import pandas as pd
# test
temperatures = pd.read_csv("/home/endserver/APP/python-project/face-detection/ml/basic_dataframe/data/GlobalTemperatures.csv")
#print(temperatures.head())

#sum LanAverageTemperature
# if you need to skip Nan, missing data you can use
# temperatures['LandAverageTemperature'].sum(skipna=True)
sumAVGTEMP = temperatures['LandAverageTemperature'].sum()
print("Summary values in dataframe: ",sumAVGTEMP)

meansValue = temperatures['LandAverageTemperature'].mean()
print("Mean values in dataframe: ", meansValue)

# if you need to list summary statics data for any column you can use
# or you need to see more data by percentiles you can add more function in describe() like..this
# temperatures['LandAverageTemperature'].describe(percentiles=[.10, .30, .65, 0.80]) 
# this... you will see 10%, 30%, 65% and 80% follow that you assigned in function
desc = temperatures['LandAverageTemperature'].describe(percentiles=[.10, .30, .65, 0.80])
print("summary statics data:\n", desc)

# for find max values in dataframe you can use..
maxValue = temperatures['LandAverageTemperature'].max()
# and you can find min by ==> temperatures['LandAverageTemperature'].min()
print("Max values in dataframe: ",maxValue)


# Median of the LandAverageTemperature column
med = temperatures['LandAverageTemperature'].median()
print("Median values in dataframe: ", med)

# Mode of the LandAverageTemperature column.
mode = temperatures['LandAverageTemperature'].mode()
print("Mode values in dataframe:\n\r", mode)