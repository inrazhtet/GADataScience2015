# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:12:43 2015

@author: zarnihtet
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.rcParams['figure.figsize'] = (8,6)
plt.rcParams['font.size'] =14


'''
Reading in the data and checking out the different feature columns
'''

waterindep = pd.read_csv('waterindependent.csv', header = 0,index_col = 0)
type(waterindep)
waterindep.columns

'''
Checking out the first couple of rows
'''

waterindep.head(10)
waterindep.shape

'''
Reading in the response variable
'''

waterdep = pd.read_csv('waterdependent.csv', header = 0,index_col = 0)
waterdep.shape
waterdep.head(10)

'''
Checking out the three response counts 
'''
waterdep.status_group.value_counts()
waterdep.shape
waterdep.columns

'''
Joining the two dependent and independent features so that I can make visualizations
out of this
'''

waterjoined = waterindep.join(waterdep, how = 'left', sort =False)
waterjoined.head(10)

'''
Sorting out hte null values
'''
waterjoined.isnull().sum()

'''
Converting the Null Values to NA
'''
waterjoined.fillna(value='NA', inplace = True)
waterjoined.isnull().sum()

'''
Checking out who the funders are
'''

waterjoined.funder.value_counts()

'''
Checking out the water point types
'''
waterjoined.waterpoint_type.value_counts()

'''
Checking out the amount of water from the tap
'''
waterjoined.amount_tsh.value_counts()

'''
Checking out water quality
'''
waterjoined.water_quality.value_counts()

'''
Chekcing out water payment types
'''
waterjoined.payment.value_counts()

waterjoined.payment_type.value_counts()

'''
Checking out water scheme names
'''
waterjoined.scheme_management.value_counts()

waterjoined.scheme_name.value_counts()

'''
Checking out GPS height, Construction Year, Date Recorded, Population -->Management values
'''

waterjoined.gps_height.value_counts()
waterjoined.construction_year.value_counts()
waterjoined.date_recorded.value_counts()
waterjoined.population.value_counts()

waterjoined.population.value_counts()

waterjoined.management.value_counts()

waterjoined.management_group.value_counts()

waterjoined.region.value_counts()

waterjoined.district_code.value_counts()

waterjoined.public_meeting.value_counts()

waterjoined.management.value_counts().plot(kind='pie')
waterjoined.management.value_counts().plot(kind='bar')


'''
Visualization Begins
'''

'''
Checking out the management to status_group(response) relation
'''


waterjoined.groupby(['management','status_group']).count()


'''
Plotting management by status_group and stsackig it in bar graph
'''

uwmgmt = waterjoined.groupby(['management','status_group'])['management'].count().unstack('status_group')
uwmgmt.plot(kind='bar',stacked = True)

'''
Summing across the colums (i.e by each row )
'''

uwmgmt['sum'] = uwmgmt.sum(axis = 1)

'''
Calculating the percentages of functional and non-function based on management type
'''

uwmgmt['perfunct'] = (uwmgmt['functional']/uwmgmt['sum']) * 100
uwmgmt['perfunctnedrepair'] = (uwmgmt['functional needs repair']/uwmgmt['sum']) * 100
uwmgmt['pernfunct'] = (uwmgmt['non functional']/uwmgmt['sum']) * 100
wmgmt = uwmgmt.loc[:,'perfunct':'pernfunct'].plot(kind='bar',stacked = True, sort_columns = True)

uwmgmt['logfunctional'] = np.log2(uwmgmt['perfunct'])
loggraph = uwmgmt.loc[:,'logfunctional'].plot(kind='bar')
nlograph = uwmgmt.loc[:,'perfunct'].plot(kind='bar')


'''
Just the running functional water pump by management
'''
functionalmgmt = uwmgmt.loc[:,'perfunct'].plot(kind='bar', logy=True)


'''
This is getting the region across all functional percent rate heat map

'''
regionfunct =pd.crosstab(waterjoined.region, waterjoined.status_group).apply(lambda r: (r/r.sum()) * 100, axis =1 )
sns.heatmap(regionfunct)

'''
Justfocusing on the functional water pump rate bar graph
'''
regionfunctgraph = regionfunct.loc[:,'functional'].plot(kind='bar')

'''
Getting the management and region relation percentage heat map
'''

managementregion = pd.crosstab(waterjoined.management, waterjoined.region).apply(lambda r: (r/r.sum()) * 100, axis =1)
managementregion.plot(kind='bar')
sns.heatmap(managementregion)

#managementregion = pd.crosstab(waterjoined.region, waterjoined.management).apply(lambda r: (r/r.sum()) * 100, axis =1)

#Most Successful
#Iringa, #Arusha, Manyara

'''
Getting down to most specific successful regions by management
'''
specificregionmgmt1 = managementregion.loc[:, ['Iringa','Arusha','Manyara']].plot(kind='bar')

'''
Getting down to the least successful regions by management
'''

specificregionmgmt2 = managementregion.loc[:,['Lindi','Mtwara','Rukwa']].plot(kind='bar')

#specificregionmgmt1 = managementregion.loc[['Iringa','Arusha','Manyara'],: ].plot(kind='bar')
#Private Operator, Water board, WUA, WUG --> Pretty high
#Iringa --> WUA, VWC, Unknown
#Arusha --> Parastatal, WUA, Unknown
#Manyara --> Parastatal, Water Authority, VWC


#Least Successful
#Lindi, Mtwara, Rukwa
#Other - School, Unknown, Water Authority, VWC

#Lindi - unknown, Other, wua, vwc
#Mtwara - vwc, unknown, private operator
#Rukwa - Water Authority, Trust, Other

#Maybe the different types of water pumps tells the story. 
#I will see what water pumps mostly operated successfully by private operators..
#Then, I will get maybe what's the type of water pumps being used in those regions
#Successful Managements use which water pump type
'''
Getting down to functional water point type rate by most successful management plot to figure out 
which water point type to use as starting point 
'''
waterpointtype = pd.crosstab(waterjoined.management, waterjoined.waterpoint_type).apply(lambda r: (r/r.sum()) * 100, axis =1)
specificwaterpointtype1 = waterpointtype.loc[['private operator', 'water board', 'wua','wug','parastatal'],: ].plot(kind='bar')

#Successful Management appears to be using predominantly
#Communal Standpipe, Multiple Communal Standpipe and Handpump.. You can lump Standpipe and Multiple Standpipe together

'''
Successful Regions use which water pump type most?
'''
waterpointregiontype = pd.crosstab(waterjoined.region, waterjoined.waterpoint_type).apply(lambda r: (r/r.sum()) * 100, axis =1)
specificwaterregiontype1 = waterpointregiontype.loc[['Iringa','Arusha','Manyara'], :].plot(kind='bar')

#It becomes obvious that the communal standpipe plays a significant role in all three regions while 2 of them have both
#the communal standpipe and handpump

'''
Unsuccessful regions use which water pump type most?
'''
specificwaterpointtype2 = waterpointtype.loc[['other - school', 'Water Authority', 'VWC','Unknown'],: ].plot(kind='bar')
specificwaterregiontype2 = waterpointregiontype.loc[['Lindi','Mtwara','Rukwa'], :].plot(kind='bar')

#In this instance, we noticed a diminshed presnce of standpipe in the least successful regions a more prominent role
#of the 'other' type of water point. Is that significant?
#Maybe I should ask the question..what are the non functional rates look like across these variables and see if there are
#any more prominent things we can notice?
#Corollary code: Public, Private, Tied to Government or not

#Maybe I should look at who built it or the construction years etc?

#Of course, we were following the story so let's back up and see what percentage of water taps are what type.

'''
Weightd Volume Chart of the type of water pumps across functional groups.. 
'''

waterpointtypefunct = pd.crosstab(waterjoined.status_group, waterjoined.waterpoint_type).apply(lambda r: (r/r.sum()) * 100, axis =1)
waterpointtypefunct.plot(kind ='bar', stacked = True)

'''
Let's back up and ask the question.. which waterpoint type actually has the most success rate because
if there are a lot of communal standpipe.. you will see them concentrated in both successful and unsuccessful regions
'''
waterpointtypefunct1 = pd.crosstab(waterjoined.waterpoint_type, waterjoined.status_group).apply(lambda r: (r/r.sum()) * 100, axis =1)
waterpointtypefunct1.plot(kind ='bar', stacked = True)

'''
Modeling begins
'''

'''
Getting the select features up
'''
WaterX = waterjoined[['management','region','waterpoint_type']]
y=waterjoined['status_group']

'''
Creating dummies for for my features
'''
management_dummies = pd.get_dummies(WaterX.management,prefix ='Management')
region_dummies = pd.get_dummies(WaterX.region, prefix='Region')
waterpoint_dummies = pd.get_dummies(WaterX.waterpoint_type, prefix='WaterPoint')

'''
Putting my dummies to my separate X-feature data frame
'''

WaterX = pd.concat([WaterX, management_dummies,region_dummies,waterpoint_dummies], axis = 1)

'''
Just getitng out the dummy variables
'''

WaterX.columns[3:]

feature_cols = WaterX.columns[3:]
X = WaterX[feature_cols]
y

'''
Running the logistic function and evaluation
'''

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state =1)

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=1e9,multi_class='multinomial',solver = 'newton-cg' )
logreg.fit(X_train,y_train)

zip(feature_cols,logreg.coef_[0])

y_pred_class = logreg.predict(X_test)

from sklearn import metrics
print metrics.accuracy_score(y_test,y_pred_class)

print metrics.confusion_matrix(y_test,y_pred_class)

confusion =metrics.confusion_matrix(y_test,y_pred_class)

functional_TP = confusion[0][0]
functional_FP = confusion[1][0] + confusion[2][0]
functional_FN = confusion[0][1] + confusion[0][2]
functional_TN = confusion [1][1] + confusion[1][2] + confusion [2][1] + confusion [2][2]


functional_sensitivity = functional_TP/float(functional_TP+functional_FN)
functional_specificity = functional_TN/float(functional_TN+functional_FP)



































 