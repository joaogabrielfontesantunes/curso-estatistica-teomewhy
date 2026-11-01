# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/points.csv")
df.head()
# %%
# GRÁFICO DE BARRAS
group_prod = (df.groupby("descProduto")["idTransacao"]
                .count()
                .reset_index())

group_prod = group_prod.sort_values(by="idTransacao")
# %%
sns.barplot(group_prod, x="idTransacao", y="descProduto")
plt.xlabel("Quantidade de Transações")
plt.ylabel("Produto")
plt.title("Frequência de Produtos")
# %%
# GRÁFICO DE LINHA
df["dataTransacao"] = pd.to_datetime(df["dtTransacao"]).dt.date
group_data = df.groupby("dataTransacao").agg(
    {
        "qtdPontos": "sum",
        "idTransacao": "count"
    }
).reset_index()

group_data = group_data.sort_values(by="dataTransacao")

plt.figure(figsize=(8, 6))
plt.plot(group_data["dataTransacao"], group_data["idTransacao"])
plt.ylabel("Quantidade de Transações")
plt.title("Série Histórica de Transações")
# %%
# HISTOGRAMA
plt.hist(group_data["qtdPontos"], bins=18)
plt.xlabel("Pontos")
plt.ylabel("Frequência")
# %%
# BOX-PLOT
plt.figure(figsize=(8, 6))
plt.boxplot(group_data["qtdPontos"])
plt.title("Box-plot")
plt.ylabel("Pontos")
# %%
# GRÁFICO DE DISPERSÃO
sns.scatterplot(group_data, x="qtdPontos", y="idTransacao")
# %%
