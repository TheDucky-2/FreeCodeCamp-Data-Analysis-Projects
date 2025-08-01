import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
np.float = float  # Patch deprecated np.float used by seaborn

import seaborn as sns


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('pageviews.csv', parse_dates= True, index_col= 'date')

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot

    
    sns.lineplot(data = df)
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019.')
    fig = plt.gcf()
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    df_bar['month'] = pd.Categorical(df_bar['month'], categories= month_order, ordered= True)
    
    df_bar = df_bar.groupby(['year', 'month'], observed = True)['value'].mean().unstack()

    # Draw bar plot

    ax = df_bar.plot(kind = 'bar', figsize = (12, 8))

    fig = ax.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    sns.boxplot(x = 'year', y = 'value', data = df_box, ax = axes[0])
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.title('Year-wise Box Plot (Trend)')
    #plt.show()

    sns.boxplot(x = 'month', y = 'value', data = df_clone, ax = axes[1])
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.title('Month-wise Box Plot (Seasonality)')
    #plt.show()


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
