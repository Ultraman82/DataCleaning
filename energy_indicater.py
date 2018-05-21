import pandas as pd
import numpy as np

def answer_one():
    df = pd.read_excel('Energy Indicators.xls', index_col = 0, skiprows= 16)
    df.columns
    
    df = df.iloc[1:228][df.columns[1:]]
    df = df.rename(columns = {df.columns[0]:'Country',
                         df.columns[1]:'Energy Supply',
                         df.columns[2]:'Energy Supply per Capita',
                         df.columns[3]:'% Renewable'}).set_index('Country')
    
    df = df.rename({"Republic of Korea": "South Korea",
    "United States of America20": "United States",
    "United Kingdom of Great Britain and Northern Ireland19": "United Kingdom",
    "China, Hong Kong Special Administrative Region3": "Hong Kong",
    "China, Macao Special Administrative Region4" : "Macao"})
    df.index = df.index.str.split('\,|\s\(|\d').str[0]
    df['Energy Supply'] *= 1000000
    
    
    dp = pd.read_csv('world_bank.csv', index_col = 0, skiprows= 4)
    GDP = dp[dp.columns[-10:]].rename({"Korea, Rep.": "South Korea", 
    "Iran, Islamic Rep.": "Iran",
    "Hong Kong SAR, China": "Hong Kong"})
    
    ScimEn = pd.read_excel('scimagojr-3.xlsx', index_col = 0,)
    
    sc = ScimEn.iloc[:15]
    sc
    
    M1 = pd.merge(sc, df, how = 'left', left_on="Country", right_index=True).reset_index().set_index('Country')
    M2 = pd.merge(M1, GDP, how = 'left', left_index=True, right_index=True).apply(pd.to_numeric)
    return M2
answer_one()


#M2['EstimatedPop'] = M2['EstimatedPop'].astype('float64')

ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
CD = pd.Series(ContinentDict)

M2['Continent'] = CD
M2.set_index(['Continent'])
arr = []
M2 = M2.reset_index
M2.set_index(['Continent','country'])
M2.index
M2.columns
for group, frame in M2.groupby('Continent'):
    Sum = np.sum(frame['EstimatedPop'])
    Size = len(frame['EstimatedPop'].index)
    Mean = np.average(frame['EstimatedPop'])
    Std = np.std(frame['EstimatedPop'])
    arr.append(pd.Series({'sum':Sum, 'size':Size, 'mean':Mean, 'std':Std, 'index':group}))
cf = pd.DataFrame(arr).set_index('index')
cf
n = 10000
M2['PopEst'] = M2.EstimatedPop.apply(lambda x : "{:,}".format(x))
M2['PopEst'] = (M2['Energy Supply'] / M2['Energy Supply per Capita']).astype('float')

M2.PopEst

M2.head()
M2['EstimatedPop'] = M2['EstimatedPop'].astype('float64')
cf = M2.groupby('Continent').agg({'EstimatedPop': np.average})
   

ContinentDict[M2.index]
M2['avgGDP'] = M2[M2.columns[-10:]].mean(axis = 1)
#M2['avgGDP2'] = GDP.mean(axis = 1).sort(ascending=False)
M2['EstimatedPop'] = M2['Energy Supply'] / M2['Energy Supply per Capita']
M2['EstimatedPop'].sort_values().index[-3]
M2['Citable docs per Capita'] = (M2['Citable documents'] / M2['EstimatedPop']).astype('float')


M2['Citable docs per Capita'] = M2['Citable docs per Capita']
M2['Energy Supply per Capita']
M2['Citable docs per Capita']




M2['HighRenew'] = (M2['% Renewable'] >= M2['% Renewable'].mean()).astype('int')
aa = M2.sort_values(by = ['Rank'])['HighRenew']
print (M2['Citable docs per Capita'].astype('float64').corr(M2['Energy Supply per Capita'].astype('float64')))
M2
M2.columns
renewable = M2['% Renewable'].astype('float')
#maxRen = (M2['% Renewable'].idxmax(), M2['% Renewable'].max())
maxRen = (renewable.idxmax(),renewable.max())
aa = pd.Series(M2['Self-citations'] / M2['Citations'])
M2.sort_values(['Rank'])['HighRenew']
M2['CitationRatio'] =  M2['Self-citations'] / M2['Citations']
maxCit = (M2['CitationRatio'].idxmax(), M2['CitationRatio'].max())
maxCit
maxRen



def answer_twelve():
    M2 = answer_one()
    
    M2['Continent'] = CD
    M2['country'] = M2.index
    M2.set_index(['Continent', 'country'], inplace=True)
    M2.sort_values(by 00) 
    return M2
answer_twelve()



aa = M2.index[M2['% Renewable'] == M2['% Renewable'].max()]
M2['Energy Supply per Capita']
M2['avgGDP'].sort_values(by=['avgGDP'])

a33 = M2['avgGDP'].sort_values(ascending=False).index[5]
a3 = M2[M2.columns[-10:]].mean(axis = 1)
a5 = M2['Energy Supply per Capita'].mean()

GDP
a4 = M2.loc[a3]['2015'] - GDP.loc[a3]['2006']
a4
print (M2['avgGDP'] == M2['avgGDP2'])
