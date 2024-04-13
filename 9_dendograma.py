import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
import scipy.stats as stats
from sklearn.cluster import KMeans
import seaborn as sns
import numpy as np

''' Cluster Hierárquico Aglomerativo '''

dados_vest = pd.read_excel('data\\Vestibular.xlsx')
# Selecionado apenas variáveis métricas e realizando o ZScore
vest = dados_vest.drop(columns=['estudante'])

# Muitas vezes, é importante realizar o procedimento Z-Score nas variáveis
# Quando as variáveis estiverem em unidades de medidas distintas
# Poderia ser feito da seguinte forma, embora aqui não utilizaremos
                
# for coluna in vest.columns:
    # vest[coluna] = stats.zscore(vest[coluna])

# Gerando o dendrograma
plt.figure(figsize=(16,8))

dendrogram = sch.dendrogram(sch.linkage(vest, method = 'single', metric = 'euclidean'), labels = list(dados_vest.estudante))
plt.title('Dendrograma', fontsize=16)
plt.xlabel('Pessoas', fontsize=16)
plt.ylabel('Distância Euclidiana', fontsize=16)
plt.axhline(y = 4.5, color = 'red', linestyle = '--')
plt.show()

# Opções para o método de encadeamento ("method"):
    ## single
    ## complete
    ## average

# Opções para as distâncias ("metric"):
    ## euclidean
    ## sqeuclidean
    ## cityblock
    ## chebyshev
    ## canberra
    ## correlation