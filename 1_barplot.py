# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

desempenho_aluno_escola = pd.read_csv("data\(2) desempenho_aluno_escola.csv", delimiter=",")

# Selecionando 3 colunas do nosso df
# Agrupando os dados por escola e tipo de escola
agrupamento_desempenho = desempenho_aluno_escola[[
    'escola',
    'desempenho',
    'priv']].groupby(by=['escola','priv']).mean()

# Realizando sorte dos dados por desempenho
agrupamento_desempenho_ordenado = agrupamento_desempenho.sort_values(
    by=['desempenho'],ascending=False).reset_index()

# Plotando os dados com barplot
ax = sns.barplot(x="escola", y="desempenho", data=agrupamento_desempenho_ordenado.head(10))
ax.bar_label(ax.containers[0], fmt='%.2f')

plt.title("Ranking dos desempenho da escola",fontsize=14)
plt.xlabel('Escola',fontsize=12)
plt.ylabel('Desempenho',fontsize=12)
plt.show()