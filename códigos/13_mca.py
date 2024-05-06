import pandas as pd
import prince
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

'''Análise de Correspondência Múltipla (MCA)'''

# Importar o banco de dados
perfil_mca = pd.read_excel("data\\Perfil Aplicação Civil.xlsx")
print(perfil_mca)

#Selecionando apenas variável para análise
perfil_mca_select = perfil_mca.drop(columns=['estudante'])
print(perfil_mca_select)

#Analisando as tabelas de contingência
tabela_mca_1 = pd.crosstab(perfil_mca["perfil"], perfil_mca["aplicacao"])
tabela_mca_2 = pd.crosstab(perfil_mca["perfil"], perfil_mca["estado_civil"])
tabela_mca_3 = pd.crosstab(perfil_mca["aplicacao"], perfil_mca["estado_civil"])
print(tabela_mca_1)
print(tabela_mca_2)
print(tabela_mca_3)

#Analisando a significância estatística das associações (teste qui²)
chi2, pvalor, df, freq_esp = chi2_contingency(tabela_mca_1)
print("Associação 1")
print(f"estatística qui²: {chi2}") # estatística qui²
print(f"p-valor da estatística: {pvalor}") # p-valor da estatística 
print(f"graus de liberdade: {df} \n") # graus de liberdade

chi2, pvalor, df, freq_esp = chi2_contingency(tabela_mca_2)
print("Associação 2")
print(f"estatística qui²: {chi2}") # estatística qui²
print(f"p-valor da estatística: {pvalor}") # p-valor da estatística
print(f"graus de liberdade: {df} \n") # graus de liberdade

chi2, pvalor, df, freq_esp = chi2_contingency(tabela_mca_3)
print("Associação 3")
print(f"estatística qui²: {chi2}") # estatística qui²
print(f"p-valor da estatística: {pvalor}") # p-valor da estatística
print(f"graus de liberdade: {df}") # graus de liberdade

#Elaborando a MCA 
#Utiliza o método da matriz de Burt
mca = prince.MCA()
mca = mca.fit(perfil_mca_select)

#Obtendo as coordenadas nas duas dimensões do mapa
print(mca.column_coordinates(perfil_mca_select))

#Obtendo as coordenadas de cada um das observações
print(mca.row_coordinates(perfil_mca_select))

#Obtendo os eigenvalues
print(mca.eigenvalues_)

#Inércia principal total
print(mca.total_inertia_)

#Obtendo a variância
print(mca.explained_inertia_)

#Plotando o mapa perceptual
mp_mca = mca.plot_coordinates(
             X = perfil_mca_select,
             figsize=(12,12),
             show_row_points = True,
             show_column_points = True,
             show_row_labels=False,
             column_points_size = 100,
             show_column_labels = True,
             legend_n_cols = 2)

plt.show()