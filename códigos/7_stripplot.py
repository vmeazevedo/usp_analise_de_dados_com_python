
import seaborn 
import matplotlib.pyplot as plt 
       
seaborn.set_theme(style='whitegrid')   
tip = seaborn.load_dataset("tips")   
       
# Exemplificação de um stripplot simples
seaborn.stripplot(x="day", y="total_bill", data=tip) 
plt.show() 

# O jitter pode ser usado para fornecer deslocamentos ao longo do eixo horizontal, o que é útil quando há grandes grupos de pontos de dados
# O linewidth aumenta a grossura da linha
seaborn.stripplot(x="day", y="total_bill", data=tip, jitter=0.2, linewidth=1)
plt.show() 

# Embora os pontos sejam plotados em duas dimensões, outra dimensão pode ser adicionada ao gráfico colorindo os pontos de acordo com uma terceira variável.
seaborn.stripplot(x="sex", y="total_bill", data=tip, hue="day")
plt.show()


# Desenhe cada nível da variável matiz em diferentes locais no eixo categórico principal
# Ao usar o aninhamento de matiz, a configuração dodge deve ser True para separar as faixas para diferentes níveis de matiz ao longo do eixo categórico. 
seaborn.stripplot(x="day", y="total_bill", data=tip, hue="smoker", dodge=True)
plt.show()