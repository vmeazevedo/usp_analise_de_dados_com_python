import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
import scipy.stats as stats
from sklearn.cluster import KMeans
import seaborn as sns
import numpy as np

''' Comparando clusters resultantes por diferentes métodos de encadeamento '''

## Deve ser realizada a parametrização:
    ## Número de clusters
    ## Medida de distância
    ## Método de encadeamento

# Importando os dados
dados_vest = pd.read_excel('data\\Vestibular.xlsx')
vest = dados_vest.drop(columns=['estudante'])
print(vest)

# Realizando a identificação do melhor número de clusters
# Gerando o dendrograma
plt.figure(figsize=(16,8))
dendrogram = sch.dendrogram(sch.linkage(vest, method = 'single', metric = 'euclidean'))
plt.title('Dendrograma', fontsize=16)
plt.xlabel('Pessoas', fontsize=12)
plt.ylabel('Distância Euclidiana', fontsize=12)
plt.axhline(y = 4.5, color = 'red', linestyle = '--')
plt.show()

# Realizando as medidas de distância
# método de encadeamento - Single
cluster_sing = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'single')
indica_cluster_sing = cluster_sing.fit_predict(vest)
dados_vest['cluster_single'] = indica_cluster_sing

# método de encadeamento - Complete
cluster_comp = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'complete')
indica_cluster_comp = cluster_comp.fit_predict(vest)
dados_vest['cluster_complete'] = indica_cluster_comp

# método de encadeamento - Average
cluster_avg = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'average')
indica_cluster_avg = cluster_avg.fit_predict(vest)
dados_vest['cluster_average'] = indica_cluster_avg

print(dados_vest)

#Plotando as observações e seus clusters (single)
plt.figure(figsize=(10,10))
fig = sns.scatterplot(x='matemática', y='física', s=60, data=dados_vest, hue='cluster_single')
plt.title('Clusters', fontsize=16)
plt.xlabel('Matemática', fontsize=12)
plt.ylabel('Física', fontsize=12)
plt.legend()
plt.show()

