import numpy as np
import pandas as pd


LANGUAGE = ['Marathi', 'Hindi', 'Kannada', 'Tamilian', 'Gujarati']

STATES_NAME = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh", "Delhi", "Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]

COLUMN_NAME = ["GENDER", "STATES", "MOTHER_TONGUE", "PARENTS_INCOME_PER_ANNUM", "PERCENT_IN_12TH_CLASS", "AVG_HRS_STUDIED", "JEE_SCORE"]


class CreateDataSet:

    def __init__(self, file_name):

        self.file_name = file_name

        self.STATES = np.random.randint(len(STATES_NAME), size=1000)
        self.MOTHER_TONGUE = np.random.randint(len(LANGUAGE), size=1000)
        self.GENDER = np.random.randint(2, size=1000)

        # Take Parents income around three range of values -
        # 0 - Less than or equal to 1 LPA
        # 1 - Less than or equal to 5 LPA but greater than 1 LPA
        # 2 - greater than 5 LPA
        self.PARENTS_INCOME_PER_ANNUM = np.random.randint(3, size=1000)

        self.PERCENT_IN_12TH_CLASS = np.random.randint(33, 100, size=1000)
        self.AVG_HRS_STUDIED = np.random.choice(range(4, 15), size=1000)
        self.JEE_SCORE = np.zeros(1000)

    def define_parameters(self):

        self.STATES = [STATES_NAME[stateName] for stateName in self.STATES]
        self.MOTHER_TONGUE = [LANGUAGE[lang] for lang in self.MOTHER_TONGUE]

        self.JEE_SCORE = ((self.AVG_HRS_STUDIED * self.PERCENT_IN_12TH_CLASS) / (14.0 * 99.0)) * 100.0
        self.JEE_SCORE *= 3.6  # Convert to (0-360) range.

    def generate_dataset(self):
        data = np.array(
            zip(self.GENDER, self.STATES, self.MOTHER_TONGUE, self.PARENTS_INCOME_PER_ANNUM, self.PERCENT_IN_12TH_CLASS, self.AVG_HRS_STUDIED, self.JEE_SCORE))

        dataframe = pd.DataFrame(data.reshape(-1, 7), columns=COLUMN_NAME)
        # Only uncomment to generate dataset
        dataframe.to_csv(self.file_name, sep=',')
        print "File generation successful, file %s is generated in your local directory" % self.file_name
