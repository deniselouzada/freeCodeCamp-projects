#Demographics Analyzer
#import numpy as np
import pandas as pd

print()

#Read file
df = pd.read_csv('adult.data.csv')

#Counting the number of each race
race_count = df.value_counts(subset=['race'], sort=True)

#Calculating the average age of men
male = df.loc[df.sex == 'Male']
male_age_count = male.age.value_counts().reset_index()
male_age_count['age_weight'] = male_age_count.age * male_age_count['count']
average_age_men = male_age_count.age_weight.sum() / len(male)

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
number_who_work_min = df.loc[df['hours-per-week'] == min_work_hours]
min_hours_over_50k = number_who_work_min.loc[number_who_work_min['salary'].isin(['>50K'])]
rich_percentage = (len(min)/len(number_who_work_min))*100

#Country with the highest earners and percentage
people_per_country = df.value_counts('native-country')
salary_over_50k = df.loc[df.salary.isin(['>50K'])]
over_50k_per_country = salary_over_50k.value_counts('native-country')

comparison = pd.concat([people_per_country, over_50k_per_country], axis=1)
comparison.columns = ['total', 'over_50k']
ratios = comparison.over_50k / comparison.total
highest_earning_country = ratios.idxmax()
highest_earning_country_percentage = ratios.max() * 100

#Most popular ocupation for >50K earners in India
indians_over_50k = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
occupation_count = indians_over_50k.value_counts('occupation')
top_IN_occupation = occupation_count.idxmax()




