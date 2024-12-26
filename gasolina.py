
# código de geração do gráfico
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df= pd.read_csv('gasolina.csv')

# Configurar estilo com Seaborn (opcional)
sns.set(style="whitegrid")

# Criar o gráfico
plt.figure(figsize=(10, 6))
sns.lineplot(data=gasolina_df, x='dia', y='venda', marker='o')
plt.title('Preço da Gasolina por Dia', fontsize=16)
plt.xlabel('Dia', fontsize=14)
plt.ylabel('Preço (R$)', fontsize=14)
plt.tight_layout()

# Salvar o gráfico como PNG
plt.savefig('grafico.png')
plt.close()
