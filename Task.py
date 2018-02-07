import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#  generate data


STATES = SCHOOL_LOCATION = MOTHER_TONGUE = GENDER = PARENTS_INCOME_PER_ANNUM = PERCENT_IN_12TH_CLASS \
    = AVG_HRS_STUDIED = np.array(0)

PROBABILITY_IIT = 0
JEE_SCORE = 0

STATES = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh", "Delhi", "Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
#print(len(STATES))

# choose gender randomly over 100 values.
GENDER = np.random.randint(2, size=1000)

# choose MOTHER_TONGUE randomly from a distribution of any languages
lang = ['Marathi', 'Hindi', 'Kannada', 'Tamilian', 'Gujarati']
MOTHER_TONGUE = np.random.randint(5, size=1000)
MOTHER_TONGUE = [lang[MOTHER_TONGUE[x]] for x in MOTHER_TONGUE]
#print(MOTHER_TONGUE)

# Take Parents income around three range of values -
# 0 - Less than or equal to 1 LPA
# 1 - Less than or equal to 5 LPA but greater than 1 LPA
# 2 - greater than 5 LPA
PARENTS_INCOME_PER_ANNUM = np.random.randint(3, size=1000)
#print(PARENTS_INCOME_PER_ANNUM[:50])

# Distribute marks between 33 and 100
PERCENT_IN_12TH_CLASS = np.random.randint(33, 100, size=1000)
#print(PERCENT_IN_12TH_CLASS)


AVG_HRS_STUDIED = np.random.choice(range(4, 15), size=1000)
#print(AVG_HRS_STUDIED[AVG_HRS_STUDIED > 10])

# Now, JEE_SCORE is a function of AVG_HRS_STUDIED and PERCENT_IN_12TH_CLASS
JEE_SCORE = ((AVG_HRS_STUDIED * PERCENT_IN_12TH_CLASS) / (14.0*99.0)) * 100.0
JEE_SCORE *= 3.6
#print(JEE_SCORE[:10])

data = ["GENDER", "MOTHER_TONGUE", "PARENTS_INCOME_PER_ANNUM", "PERCENT_IN_12TH_CLASS", "AVG_HRS_STUDIED", "JEE_SCORE"]
#print(data)

col = np.array(zip(GENDER, MOTHER_TONGUE, PARENTS_INCOME_PER_ANNUM, PERCENT_IN_12TH_CLASS, AVG_HRS_STUDIED, JEE_SCORE))
#print(col[:10])


df = pd.DataFrame(col.reshape(-1, 6), columns=data)
#print(df[:10])


# Plot the JEE_SCORE vs PERCENT_IN_12TH_CLASS
#------------------------------------------------------------------------------------------
# plt.scatter(JEE_SCORE, PERCENT_IN_12TH_CLASS)
# plt.xlabel("JEE_SCORE")
# plt.ylabel("range_per")
# plt.xticks(range(36, 361, 36))
# plt.yticks(range(10, 101, 10))
# plt.show()
#-------------------------------------------------------------------------------------------


# Only uncomment to save dataFrame - df to csv file
file_name = "data_IIT.csv"
df.to_csv(file_name, sep=',')


