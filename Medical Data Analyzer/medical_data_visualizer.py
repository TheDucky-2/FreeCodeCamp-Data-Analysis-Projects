import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1

df = pd.read_csv('medical_examination.csv')                          # loading the csv file 

weight_in_kg = df['weight']                                          # weight already in kg
height_in_m = df['height']/100                                       # converting height into m from cm
 
df['BMI'] = round((weight_in_kg/(height_in_m)**2), 2)                # rounding off to 2 places


# 2

df['overweight'] = (df['BMI'] > 25).astype(int)                      # BMI > 25 to be overweight(1)

# 3

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)         # Normalized cholesterol
df['gluc'] = (df['gluc'] > 1).astype(int)                       # Normalized gluc

# 4

def draw_cat_plot():

    # 5

    df_cat = df.melt(id_vars = ['id', 'cardio'], value_vars= ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name= "variable", value_name= 'value')


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name = "total")
    

    # 7

    sns.catplot(data = df_cat, x = 'variable', y = 'total', col = 'cardio', height= 5, aspect= 1, sharey = False)

    # 8
    fig = sns.catplot(data = df_cat, x = 'variable', y = 'total', col = 'cardio', height= 5, aspect= 1, sharey = False).fig
    plt.tight_layout()


    # 9
    fig.savefig('catplot.png')
    return fig


# 10

# 10
def draw_heat_map():
    
    df = pd.read_csv('medical_examination.csv')

    df = df[(df['ap_lo'] <= df['ap_hi'])]   # diastolic pressure lower than systolic
    df = df[(df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))]   #  for height
    df = df[(df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]   # for weight
    
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)

    df['gluc'] = (df['gluc'] > 1).astype(int)

    weight_in_kg = df['weight']
    height_in_m = df['height']/100

    df['overweight'] = ((weight_in_kg/(height_in_m)**2) > 25).astype(int)

    df_heat = df

    # 12
    corr = df_heat.corr()
    print(corr.shape)

    # 13
    mask = np.triu(np.ones_like(corr, dtype= bool))

    # 14
    fig, ax = plt.subplots(figsize = (10, 8))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, square=True, linewidths=0.5, cbar_kws={"shrink": 0.5}, ax=ax)

    ax.set_title('Heatmap')


    # 16
    fig.savefig('heatmap.png')
    return fig

draw_heat_map()
