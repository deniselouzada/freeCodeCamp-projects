import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
w = df['weight']
h = df['height']*0.01
bmi = w/h**2
df['overweight'] = bmi.apply(lambda x: 0 if x <= 25 else 1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)

# Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
stats = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
df_cat = pd.melt(df, id_vars=['cardio'], value_vars=stats)

# Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
total = df_cat.value_counts(sort=False)
total = total.reset_index()
total = total.rename(columns={'count': 'total'})
fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=total, kind='bar')

# Clean the data
df_heat = df.loc[df['ap_lo'] <= df['ap_hi']]
df_heat = df_heat.loc[(df_heat['height'] >= df_heat['height'].quantile(0.025)) & (df_heat['height'] <= df_heat['height'].quantile(0.975))]
df_heat = df_heat.loc[(df_heat['weight'] >= df_heat['weight'].quantile(0.025)) & (df_heat['weight'] <= df_heat['weight'].quantile(0.975))]



# Calculate the correlation matrix
corr = df_heat.corr()

# Generate a mask for the upper triangle
mask = np.triu(corr)
col = corr.columns.tolist()
row = corr.index.tolist()
mask = np.array(mask)
mask = pd.DataFrame(mask, columns=col, index=row)
mask = mask.mask(mask == 0)
mask = mask == corr

corr = corr.mask(corr == 1,0)

# Draw Heat Map

# Set up the matplotlib figure
plt.rcParams.update({'font.size': 10})
fig, ax = plt.subplots(figsize=(12,10))


g = sns.heatmap(corr, vmax=0.32, vmin=-0.16, mask=mask, fmt='.1f', annot=True, center=0, cbar_kws={'shrink': .5, 'ticks': [-0.08, 0, 0.08, 0.16, 0.24]}, linewidths= .6)

# Do not modify the next two lines

fig.savefig('heatmap.png')
    


# Draw the heatmap with 'sns.heatmap()'


# Draw Categorical Plot
'''def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    stats = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=stats)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    total = df_cat.value_counts(sort=False)
    total = total.reset_index()
    total = total.rename(columns={'count': 'total'})
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=total, kind='bar')

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

draw_cat_plot()'''
"""# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()
draw_heat_map()"""