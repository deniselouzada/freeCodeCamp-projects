#Demographics Analyzer
#import numpy as np
import pandas as pd

print()

#Read file
df = pd.read_csv('adult.data.csv')

#Counting the number of each race
race_count = df.value_counts(subset=['race'], sort=True)

#Calculating the average age of men
male = df.loc[df['sex'] == 'Male']
age_male = male['age']
age_count = age_male.value_counts()
age_count = age_count.reset_index()
age_count['wt_age'] = age_count['age']*age_count['count']
average_age_men = age_count['wt_age'].sum()/len(male)

#Percentage with Bachelors degree
bachelors = df.loc[df['education'] == 'Bachelors']
percentage_bachelors = (len(bachelors)/len(df))*100

#Percentage of advanced education and salary >50K
adv = df.loc[df['education'].isin(['Bachelors','Masters','Doctorate'])]
advplus = adv.loc[adv['salary'].isin(['>50K'])]
higher_education_rich = (len(advplus)/len(adv))*100

#Percentage of no advanced degree and salary >50K
noadv = df.loc[~df['education'].isin(['Bachelors','Masters','Doctorate'])]
noadvplus = noadv.loc[noadv['salary'].isin(['>50K'])]
lower_education_rich = (len(noadvplus)/len(noadv))*100

#Minimun hours a week
min_work_hours = df['hours-per-week'].min()

#Percent of people who work minimum hours and earn >50K
n_min = df.loc[df['hours-per-week'] == min_work_hours]
min_plus = n_min.loc[n_min['salary'].isin(['>50K'])]
rich_percentage = (len(min_plus)/len(n_min))*100
#print(p_min_plus)

#Country with the highest earners and percentage
c_count = df.value_counts('native-country')
sal_plus = df.loc[df['salary'].isin(['>50K'])]
countries_plus = sal_plus['native-country']
cp_count = countries_plus.value_counts()
compare = pd.concat([c_count, cp_count], axis=1)
compare.columns = ['c_count','cp_count']
ratio = compare['cp_count']/compare['c_count']
highest_earning_country = ratio.idxmax()
highest_earning_country_percentage = 100*ratio.max()

#Most popular ocupation for >50K earners in India
india = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
ocp_cnt = india['occupation'].value_counts()
top_IN_occupation = ocp_cnt.idxmax()

print()




