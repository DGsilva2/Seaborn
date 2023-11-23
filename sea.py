import seaborn as sns

tips = sns.load_dataset('tips')#criado uma base de dados com dados aleatorios

sns.distplot(tips['total_bill'])#mostrando o grafico
sns.distplot(tips['total_bill'], kde=False)# tirando o KDE('linha') do grafico 
sns.distplot(tips['total_bill'], kde=False, bins=30)

sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')

sns.pairplot(tips)

sns.pairplot(tips, hue='sex')#segregando o grafico por sexo


sns.kdeplot(tips['total_bill'])
sns.rugplot(tips['total_bill'])

#Plots de regressao
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['x', 'v'],scatter_kws={'s':100}, aspect=1.6)

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', col='time', row='day')


#PLOTS MATRICIAIS
import matplotlib.pyplot as plt

flights = sns.load_dataset('flights')

flights_matix=flights.pivot_table(index='year', columns='month', values='passengers')

fig, ax= plt.subplots(figsize=(20,8))
sns.heatmap(flights_matix, annot=True, fmt='.0f')

sns.clustermap(flights_matix)

#ESTILIZAÇÃO

sns.set_style('whitegrid')
sns.countplot(x='sex', data=tips)

sns.set_style('whitegrid')
sns.countplot(x='sex', data=tips, palette='deep')

sns.set_style('darkgrid')
sns.countplot(x='sex', data=tips, palette='deep')

sns.set_style('dark')
sns.countplot(x='sex', data=tips, palette='deep')

fig, ax= plt.subplots(figsize=(20,8))
sns.countplot(x='sex', data=tips, palette='deep', ax=ax)
ax.set_xlabel('Eixo X')
