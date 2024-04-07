# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

desempenho_aluno_escola = pd.read_csv("data\(2) desempenho_aluno_escola.csv", delimiter=",")

# Iniciando com o gráfico básico utilizando o próprio pandas dataframe com o método "hist"
# Analisando o desempenho dos alunos
desempenho_aluno_escola['desempenho'].hist(bins=30)
plt.show()

# Podemos também utilizar a biblioteca do seaborn para fazer o histograma
# Vamos adicionar algumas formatações
sns.set_theme(style="darkgrid", palette="bright") 
sns.histplot(data=desempenho_aluno_escola, x="desempenho", bins=50)
plt.title("Histograma dos desempenhos das escolas",fontsize=14)
plt.xlabel('Desempenho escolar',fontsize=12)
plt.ylabel('Frequência',fontsize=12)
plt.show()


'''
Um histograma é uma ferramenta poderosa para visualizar a distribuição dos dados em um conjunto de dados numéricos. Aqui estão algumas informações que você pode extrair de um histograma:

Forma da Distribuição: 
O formato do histograma pode revelar informações sobre a forma da distribuição dos dados. Por exemplo, se a distribuição é simétrica, assimétrica (positiva ou negativa), uni ou multimodal.

Centralidade: 
Você pode identificar onde está o centro da distribuição olhando para o pico do histograma. Isso pode ser útil para estimar a média dos dados.

Variabilidade: 
A largura do histograma pode indicar a variabilidade dos dados. Um histograma mais largo sugere uma maior dispersão dos dados em relação à média.

Outliers: 
Os valores extremos ou outliers podem ser identificados como pontos fora do padrão do histograma.

Tendências: 
Padrões de tendência podem ser observados no histograma. Por exemplo, se há agrupamentos em determinadas faixas de valores, isso pode indicar a presença de subpopulações nos dados.

Assimetria: 
A simetria da distribuição pode ser observada visualmente, se é perfeitamente simétrica, inclinada para a direita (positiva) ou inclinada para a esquerda (negativa).

Valores Críticos: 
Em algumas situações, pode ser importante identificar intervalos específicos de valores. Por exemplo, em estudos de controle de qualidade, você pode querer identificar intervalos onde a maioria dos dados está concentrada e definir limites de controle com base nisso.

Resumo Estatístico: 
O histograma pode ser usado para derivar várias medidas estatísticas, como a média, a mediana, o desvio padrão, o quartil, etc.

'''