import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

preco_acao = pd.read_excel("data\(2) precos_acao.xlsx")

# Como temos 4 ações no banco de dados, vamos implementar o seguinte gráfico
# Note que vamos separar cada empresa por meio da cor do gráfico
sns.lineplot(data=preco_acao, x="data", y="preco", hue="acao")
plt.show()

# Vamos formatar um pouco mais o gráfico
# Nos é apresentado o espectro de max e min e uma linha media/mediana guia dos nossos dados
sns.set_theme(style="darkgrid", palette="bright") 
sns.lineplot(data=preco_acao, x="data", y="preco", marker="o")

plt.title("Série Histórica das Ações",fontsize=14)
plt.xlabel('Mês de Referência',fontsize=12)
plt.ylabel('Cotação de Fechamento',fontsize=12)
plt.legend(title='Empresa')
plt.show()


# Vamos adcionar o hue para delimitar cada empresa
sns.set_theme(style="darkgrid", palette="bright") 
sns.lineplot(data=preco_acao, x="data", y="preco",hue="acao", marker="o")

plt.title("Série Histórica das Ações",fontsize=14)
plt.xlabel('Mês de Referência',fontsize=12)
plt.ylabel('Cotação de Fechamento',fontsize=12)
plt.legend(title='Empresa')
plt.show()