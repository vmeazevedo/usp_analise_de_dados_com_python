import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
import scipy.stats as stats
from sklearn.cluster import KMeans
import seaborn as sns
import numpy as np

''' Cluster Não Hierárquico K-means '''
# Importando os dados
dados_vest = pd.read_excel('data\\Vestibular.xlsx')
vest = dados_vest.drop(columns=['estudante'])

# Gerando 3 cluster de forma randomizada
kmeans = KMeans(n_clusters = 3, init = 'random').fit(vest)
# Dados do agrupamento
kmeans_clusters = kmeans.labels_
# Atribuindo os dados a uma coluna de nosso df
dados_vest['cluster_kmeans'] = kmeans_clusters
print(dados_vest)

# Alterando os nomes dos cluster
#kmeans_clusters = kmeans.labels_
cluster_names = {0: 'Cluster A', 1: 'Cluster B', 2: 'Cluster C'}
# Atribuindo os nomes atualizados ao nosso df
dados_vest['cluster_kmeans'] = pd.Series(kmeans_clusters).replace(cluster_names)
print(dados_vest)

# Identificando as coordenadas centróides dos clusters finais
# Criando um DF com os dados da coluna cluster_kmeans
cent_finais = pd.DataFrame(kmeans.cluster_centers_)
# Add os nomes das colunas
cent_finais.columns = vest.columns
# Add o nome do index
cent_finais.index.name = 'cluster'
# dados da centroides
print(cent_finais)


# Plotando as observações e seus centróides dos clusters
plt.figure(figsize=(10,10))
pred_y = kmeans.fit_predict(vest)

#Plotando as observações e seus clusters (onde o hue será a coluna cluster_kmeans)
sns.scatterplot(x='matemática', y='física', data=dados_vest, hue='cluster_kmeans', palette='viridis', s=100)

# Plotando as centroides de nosso cluster
plt.scatter(cent_finais['matemática'], cent_finais['física'], s = 20, c = 'red', label = 'Centróides', marker="X")
plt.title('Clusters e centróides', fontsize=16)
plt.xlabel('Matemática', fontsize=12)
plt.ylabel('Física', fontsize=12)
plt.legend()
plt.show()