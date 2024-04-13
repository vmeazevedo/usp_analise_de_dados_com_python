import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

# O boxplot apresenta medidas de posição das variáveis
# Mínimo, máximo, 1º quartil, mediana e 3º quartil
# Vemos a distribuição dos dados nas variáveis e eventuais outliers univariados

atlas_ambiental = pd.read_excel("data\(2) atlas_ambiental.xlsx")

# Inicialmente, vamos apresentar o boxplot de uma única variável
var_boxplot = atlas_ambiental[['cód_ibge','renda']]

sns.set_theme(style="darkgrid", palette="bright") 
sns.boxplot(data=var_boxplot, y='renda')
plt.xlabel('Renda',fontsize=12)
plt.ylabel('Valores',fontsize=12)
plt.show()
"---------------------------------------------------------------------------------------------------"

# Carregamento da base de dados 'sacarose'
df_sacarose = pd.read_csv('data\sacarose.csv', delimiter=',')

# Programando um objeto com o banco de dados agrupado pelo critério
df_sacarose_grupo = df_sacarose.groupby(by=['fornecedor'])

# Apresentação de dados apenas com boxplot
sns.boxplot(data=df_sacarose, x='fornecedor', y='sacarose', linewidth=2, orient='v', color='darkorchid')
plt.title('Boxplots de sacarose por fornecedor', fontsize=14)
plt.xlabel('Fornecedor', fontsize=12)
plt.ylabel('Sacarose', fontsize=12)
plt.show()

# Add o stripplot ao nosso gráfico
# Representa distribuições univariadas ou bivariadas de dados categórico
sns.boxplot(data=df_sacarose, x='fornecedor', y='sacarose', linewidth=2, orient='v', color='darkorchid')
sns.stripplot(data=df_sacarose, x='fornecedor', y='sacarose', color="orange", jitter=0.1, size=7)
plt.title('Boxplots de sacarose por fornecedor', fontsize=14)
plt.xlabel('Fornecedor', fontsize=12)
plt.ylabel('Sacarose', fontsize=12)
plt.show()