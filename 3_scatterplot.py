import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

atlas_ambiental = pd.read_excel("data\(2) atlas_ambiental.xlsx")

# Iniciando com o gráfico básico (scatterplot)
# Neste caso, devemos especificar as variáveis dos eixos x e y no
sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade")
plt.show()

# Como há variáveis nos dois eixos, podemos adicionar outras variáveis:
# Na forma de tamanho dos pontos ("size")
sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade", size="idade")
plt.title("Indicadores dos Distritos do Município de São Paulo",fontsize=14)
plt.xlabel('Renda',fontsize=12)
plt.ylabel('Escolaridade',fontsize=12)
plt.show()

"---------------------------------------------------------------------------------------------------"

# Para separar no gráfico alguma condição, é necessário fazer uma distinção dos dados no dataframe
# Selecionamos a coluna e a linha com uma seleção condicional e criamos uma nova coluna que sera atribuído o resultado 'ind_favel'
atlas_ambiental.loc[atlas_ambiental['favel']<6, "ind_favel"] = "Abaixo"
atlas_ambiental.loc[atlas_ambiental['favel']>=6, "ind_favel"] = "Acima"

# Na cor por categoria dos pontos ("hue")
sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade", size="idade", hue="ind_favel")
plt.title("Indicadores dos Distritos do Município de São Paulo",fontsize=14)
plt.xlabel('Renda',fontsize=12)
plt.ylabel('Escolaridade',fontsize=12)
plt.show()


# Para separar no gráfico alguma condição, é necessário fazer uma distinção dos dados no dataframe
# Selecionamos a coluna e a linha com uma seleção condicional e criamos uma nova coluna que sera atribuído o resultado 'ind_mortal'
atlas_ambiental.loc[atlas_ambiental['mortalidade'] < 18, "ind_mortal"] = "Abaixo"
atlas_ambiental.loc[atlas_ambiental['mortalidade'] >= 18, "ind_mortal"] = "Acima"

# Na forma por categoria dos pontos ("style")
sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade", size="idade", hue="ind_favel", style="ind_mortal")
plt.title("Indicadores dos Distritos do Município de São Paulo",fontsize=14)
plt.xlabel('Renda',fontsize=12)
plt.ylabel('Escolaridade',fontsize=12)
plt.show()