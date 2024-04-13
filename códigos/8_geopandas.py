import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd


# carregamento dos datasets que serão utilizados na análise
tb_pedidos = pd.read_csv("data\\tb_pedidos.csv")
tb_produtos = pd.read_csv("data\\tb_produtos.csv")
tb_clientes = pd.read_csv("data\\tb_clientes.csv")

# realizando o merge com a tabela de clientes
dataset = tb_pedidos.merge(tb_clientes, on='cliente_id', how='left')

# realizando o merge com a tabela de produtos
dataset = dataset.merge(tb_produtos, on='produto_id', how='left')

# percebam que as variáveis de data estão como tipo 'object', será necessário mudar para o tipo date
dataset['data_venda'] = pd.to_datetime(dataset['data_venda'])
dataset['data_entrega'] = pd.to_datetime(dataset['data_entrega'])

# verificando a soma do valor das vendas por categoria
dataset_agrupado_vendas_por_categoria = dataset.groupby('categoria').agg({'valor_vendas':'sum'})

# ajustando as opções para verificar os números sem notação científica
pd.options.display.float_format = '{:.2f}'.format

# adicionando a variável lucro no dataset com os valores das vendas, desconto e custos dos itens dos pedidos
dataset['lucro'] = dataset['valor_vendas'] * (1 - dataset['desconto']) - dataset['custo_produto'] - dataset['custo_entrega']

# adicionando a variável ano e mês no dataset
dataset['ano'] = dataset['data_venda'].dt.year
dataset['mes'] = dataset['data_venda'].dt.month

# verificando as vendas agrupadas por ano e mês
dataset_agrupado_ano_mes = dataset.groupby(by=['ano','mes']).agg({'valor_vendas':'sum'}).reset_index()

# filtrando o dataset em uma única categoria
dataset[dataset['categoria'] == 'Furniture']

# carregando o dataset auxiliar com as coordenadas dos países
dataset_auxiliar_coordenadas = pd.read_csv("data\\tb_coordenadas.csv")

# ajustando alguns nomes de colunas para que fique de fácil entendimento
dataset_auxiliar_coordenadas = dataset_auxiliar_coordenadas.rename(columns={
    'Latitude (average)':'latitude_media',
    'Longitude (average)':'longitude_media'
})

# carregando o dataset com os polígonos geométricos dos países utilizando a biblioteca GeoPandas
paises_geopandas = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# fazendo o merge do dataset de coordenadas com o dataset principal no pais e do tipo left
dataset = dataset.rename(columns={'pais':'Country'}).merge(
    dataset_auxiliar_coordenadas,
    on='Country',
    how='left'
)

# verificando o valor de vendas total dos países agrupando latitude e longitude 
vendas_paises_por_coordenadas = dataset.groupby(['latitude_media','longitude_media']).agg({'valor_vendas':'sum'}).reset_index()

# verificando o lucro resultante das vendas dos países agrupando latitude e longitude e resumindo pela soma do lucro
lucro_paises_por_coordenadas = dataset.groupby(['latitude_media','longitude_media']).agg({'lucro':'sum'}).reset_index()

# dando vida ao gráfico utilizando o mapa do mundo como plano de fundo
fig, ax = plt.subplots(figsize=(12,10))
paises_geopandas.plot(color="lightgrey", ax=ax)
sns.scatterplot(data=lucro_paises_por_coordenadas,
                x="longitude_media", y="latitude_media",
                hue='lucro', size='lucro', sizes=(1, 200), palette='viridis')
plt.title('Lucro total por país', fontsize=14)
plt.xlabel("Longitude", fontsize=12)
plt.ylabel("Latitude", fontsize=12)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14)
plt.show()