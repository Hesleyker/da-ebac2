
# código de geração do gráfico
# Criar o gráfico de linha com elementos adicionais
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.lineplot(data=gasolina_df, x='dia', y='venda', marker='o', label='Preço da Gasolina')
plt.title('Evolução do Preço da Gasolina por Dia', fontsize=16)
plt.xlabel('Dia', fontsize=14)
plt.ylabel('Preço (R$)', fontsize=14)
plt.legend(title='Legenda', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Salvar o gráfico como PNG
plt.savefig('grafico.png')
plt.close()
