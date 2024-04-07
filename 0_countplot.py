# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 


# Vamos começar analisando uma variável qualitativa, o perfil do investidor
perfil_investidor = pd.read_excel("data\(2) perfil_investidor.xlsx")

# Como é uma variável categórica, vamos criar um gráfico de contagem (countplot)
# Neste caso, o gráfico apresentará a contagem em cada categoria da variável
sns.countplot(x="perfil", data=perfil_investidor)
plt.show()

# Poderíamos mudar a ordem de apresentação reorganizando os níveis da variável
sns.countplot(x="perfil", data=perfil_investidor, order=["Agressivo","Moderado","Conservador"], color="blue")

plt.title("Perfil dos Investidores")            # add um título
plt.suptitle("Banco X")                         # add um subtitulo
plt.xlabel('Perfil do Investidor',fontsize=12)  # legenda eixo x
plt.ylabel('Quantidade',fontsize=12)            # legenda eixo y
plt.show()


# Vamos alterar o fundo do gráfico (theme)
sns.set_theme(style="whitegrid", palette="viridis") 
ax = sns.countplot(x="perfil", data=perfil_investidor, order=["Agressivo","Moderado","Conservador"])
ax.bar_label(ax.containers[0])                  # add um contador da coluna

plt.title("Perfil dos Investidores")
plt.suptitle("Banco X")
plt.xlabel('Perfil do Investidor',fontsize=12)
plt.ylabel('Quantidade',fontsize=12)
plt.show()
