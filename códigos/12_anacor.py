import pandas as pd
import prince
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

'''Análise de Correspondência Simples (ANACOR)'''
# Importar o banco de dados
perfil = pd.read_excel("data\\Perfil Aplicação.xlsx")
print(perfil)

#Analisando os dados do dataset
print(perfil.info())

#Analisando as características descritivas das variáveis do dataset
print(perfil.describe())

#Criando a tabela de contingência
#O input que calcula a anacor nao são os dados e sim essa tabela
tabela = pd.crosstab(perfil["Perfil"], perfil["Tipo de Aplicação"])
print(tabela)

#Analisando a significância estatística da associação (teste qui²)
chi2, pvalor, df, freq_esp = chi2_contingency(tabela)

print(f"estatística qui²: {chi2}") # estatística qui²
print(f"p-valor da estatística: {pvalor}") # p-valor da estatística.. tem q ser abaixo de 0.05 para ser usado
print(f"graus de liberdade: {df}") # graus de liberdade
print(f"{freq_esp}")

#Elaborando a ANACOR
# Inicializando a instância da Anacor
ca = prince.CA()

#Ajustes do dataframe
#Renomeando as linhas e colunas do dataframe
tabela.columns.rename('Investimento', inplace=True)
tabela.index.rename('Perfil', inplace=True)
print(tabela)

#Fit do modelo
#Note que o input é a tabela de contingência criada antes
#informando que queremos fazzer uma anacor com a tabela de contigencia
ca = ca.fit(tabela)

#Obtendo as coordenadas em linha e coluna
print(ca.row_coordinates(tabela), "\n")
print(ca.column_coordinates(tabela))

#Obtendo os eigenvalues
#calculo dos autovalores
print(ca.eigenvalues_)

#Inércia explicada por dimensão
#Indica o percentual da a inércia principal total explicado por cada dimensão
print(ca.explained_inertia_)

#Massas em linhas
print(ca.row_masses_)

#Massas em colunas
print(ca.col_masses_)

#Por fim, podemos plotar o mapa perceptual

ax = ca.plot_coordinates(X=tabela,
                         ax=None,
                         figsize=(10,10),
                         x_component=0,
                         y_component=1,
                         show_row_labels=True,
                         show_col_labels=True)

plt.show()