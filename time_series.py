import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df = df.set_index('date')
df.index = pd.to_datetime(df.index)
# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    
    #Draw line plot
    fig = plt.figure(figsize=(15, 6), layout='tight')
    plt.plot(df.index, df['value'], color='red',)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.xticks(['2016-07-01', '2017-01-01', '2017-07-01', '2018-01-01', '2018-07-01', '2019-01-01', '2019-07-01', '2020-01-01'], labels=['2016-07', '2017-01', '2017-07', '2018-01', '2018-07', '2019-01', '2019-07', '2020-01'])
    plt.ylabel('Page Views')
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df_bar.index.month
    df_bar['year'] = df_bar.index.year
    df_bar = df_bar.reset_index()

    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().reset_index()
    df_bar['month'] = df_bar['month'].apply(lambda x: calendar.month_name[x])
    df_bar = df_bar.rename(columns={'year': 'Year', 'month': 'Month', 'value': 'Average Page Views'})

    # Draw bar plot
    fig = plt.figure(figsize=(12,10), layout='tight')
    plt.rcParams.update({'font.size': 16})
    plt.title('Average Page Views per Month/Year')

    ax = sns.barplot(data=df_bar, x='Year', y='Average Page Views', hue='Month', hue_order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], palette='tab10', width=0.5)

    ax.set_xlabel('Years')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', loc='upper left')

    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8), layout='tight')
    yaxis = np.arange(0, 220000, 20000)
    aspect_ratio = 0.75
    plt.axis('tight')
    #Plot 1
    sns.boxplot(data=df_box, x='Year', y='value', ax=ax1, hue='Year', legend=False, palette='tab10', flierprops={'marker': 'd', 'markersize': 3})
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_ylabel('Page Views')
    ax1.set_xlabel('Year')
    ax1.set_ylim(0, 200000)
    ax1.set_yticks(yaxis)
    ax1.set_box_aspect(aspect_ratio)

    #Plot 2
    sns.boxplot(data=df_box, x='Month', y='value', ax=ax2, hue='Month', legend=False, palette=sns.husl_palette(n_colors=12, h=0.3), order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], flierprops={'marker': 'd', 'markersize': 3})
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_ylim(0, 200000)
    ax2.set_yticks(yaxis)
    ax2.set_box_aspect(aspect_ratio)

    fig.savefig('box_plot.png')
    return fig

draw_line_plot()
draw_bar_plot()
draw_box_plot()