import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

# Vamos gerar um gráfico de calor que distingue informações por meio de cores
tempo_dist = pd.read_excel("data\(2) tempo_dist.xls")

# Inicialmente, vamos selecionar as variáveis quantitativas do banco de dados
tempo_dist = tempo_dist[['tempo','distancia','semaforos']]

# Vamos trabalhar o gráfico de calor no contexto das correlações entre variáveis
# Portanto, primeiramente, vamos criar a matriz de correlações (função "cor")
# Lembrando: selecionar apenas as variáveis quantitativas da base de dados
corr = tempo_dist.corr()

# Agora vamos elaborar um gráfico de calor (heatmap) com algumas formatações
sns.heatmap(corr, center=0)
plt.show()

# Poderíamos trocar as cores para facilitar a visualização
# Ao mesmo tempo, vamos adicionar rótulos aos dados
sns.heatmap(corr, center=0, annot=True, cmap="Greens")
plt.show()

# Algumas opções de cores:
    # cmap="YlGnBu"
    # cmap="Blues"
    # cmap="BuPu"
    # cmap="PiYG"
    # cmap="Greens"