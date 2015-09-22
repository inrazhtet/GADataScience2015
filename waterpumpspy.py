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

waterdep = pd.read_csv('waterdependent.csv', header = 0,index_col = 0)
type(waterdep)
waterdep.columns

waterdep.head(10)
waterdep.shape

waterindep = pd.read_csv('waterindependent.csv', header = 0,index_col = 0)

waterindep.head(10)
waterindep.shape
waterindep.head(10)
waterindep.status_group.value_counts()

waterindep.shape
waterindep.columns

waterjoined = waterdep.join(waterindep, how = 'left', sort =False)

waterjoined.head(10)

waterjoined.isnull().sum()
waterjoined.fillna(value='NA', inplace = True)
waterjoined.isnull().sum()

waterjoined.funder.value_counts()

waterjoined.columns
waterjoined.waterpoint_type.value_counts()

waterjoined.amount_tsh.value_counts()

waterjoined.water_quality.value_counts()

waterjoined.payment.value_counts()

waterjoined.payment_type.value_counts()

waterjoined.scheme_management.value_counts()

waterjoined.scheme_name.value_counts()

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

waterjoined.groupby(['management','status_group']).count()


uwmgmt = waterjoined.groupby(['management','status_group'])['management'].count().unstack('status_group')
uwmgmt.plot(kind='bar',stacked = True)


uwmgmt['sum'] = uwmgmt.sum(axis = 1)
uwmgmt['perfunct'] = (uwmgmt['functional']/uwmgmt['sum']) * 100
uwmgmt['perfunctnedrepair'] = (uwmgmt['functional needs repair']/uwmgmt['sum']) * 100
uwmgmt['pernfunct'] = (uwmgmt['non functional']/uwmgmt['sum']) * 100
wmgmt = uwmgmt.loc[:,'perfunct':'pernfunct'].plot(kind='bar',stacked = True, sort_columns = True)

uwmgmt['logfunctional'] = np.log2(uwmgmt['perfunct'])
loggraph = uwmgmt.loc[:,'logfunctional'].plot(kind='bar')
nlograph = uwmgmt.loc[:,'perfunct'].plot(kind='bar')


#This is functionality across different management types
functionalmgmt = uwmgmt.loc[:,'perfunct'].plot(kind='bar', logy=True)


#This is the region and different management type
regionfunct =pd.crosstab(waterjoined.region, waterjoined.status_group).apply(lambda r: (r/r.sum()) * 100, axis =1 )
sns.heatmap(regionfunct)
regionfunctgraph = regionfunct.loc[:,'functional'].plot(kind='bar')



#this is the management type across regions


managementregion = pd.crosstab(waterjoined.management, waterjoined.region).apply(lambda r: (r/r.sum()) * 100, axis =1)
managementregion.plot(kind='bar')
sns.heatmap(managementregion)

#managementregion = pd.crosstab(waterjoined.region, waterjoined.management).apply(lambda r: (r/r.sum()) * 100, axis =1)

#Most Successful
#Iringa, #Arusha, Manyara

specificregionmgmt1 = managementregion.loc[:, ['Iringa','Arusha','Manyara']].plot(kind='bar')
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

waterpointtype = pd.crosstab(waterjoined.management, waterjoined.waterpoint_type).apply(lambda r: (r/r.sum()) * 100, axis =1)
specificwaterpointtype1 = waterpointtype.loc[['private operator', 'water board', 'wua','wug','parastatal'],: ].plot(kind='bar')

#Successful Management appears to be using predominantly
#Communal Standpipe, Multiple Communal Standpipe and Handpump.. You can lump Standpipe and Multiple Standpipe together


#Successful Regions use which water pump Type

waterpointregiontype = pd.crosstab(waterjoined.region, waterjoined.waterpoint_type).apply(lambda r: (r/r.sum()) * 100, axis =1)
specificwaterregiontype1 = waterpointregiontype.loc[['Iringa','Arusha','Manyara'], :].plot(kind='bar')

#It becomes obvious that the communal standpipe plays a significant role in all three regions while 2 of them have both
#the communal standpipe and handpump


specificwaterpointtype2 = waterpointtype.loc[['other - school', 'Water Authority', 'VWC','Unknown'],: ].plot(kind='bar')
specificwaterregiontype2 = waterpointregiontype.loc[['Lindi','Mtwara','Rukwa'], :].plot(kind='bar')

#In this instance, we noticed a diminshed presnce of standpipe in the least successful regions a more prominent role
#of the 'other' type of water point. Is that significant?
#Maybe I should ask the question..what are the non functional rates look like across these variables and see if there are
#any more prominent things we can notice?
#Corollary code: Public, Private, Tied to Government or not

#Maybe I should look at who built it or the construction years etc?

#Of course, we were following the story so let's back up and see what percentage of water taps are what type.

waterpointtypefunct = pd.crosstab(waterjoined.status_group, waterjoined.waterpoint_type).apply(lambda r: (r/r.sum()) * 100, axis =1)
waterpointtypefunct.plot(kind ='bar', stacked = True)

waterpointtypefunct1 = pd.crosstab(waterjoined.waterpoint_type, waterjoined.status_group).apply(lambda r: (r/r.sum()) * 100, axis =1)
waterpointtypefunct1.plot(kind ='bar', stacked = True)
 