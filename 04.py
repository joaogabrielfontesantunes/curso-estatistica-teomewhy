# %%
import pandas as pd
from scipy.stats import t as t_student 
df = pd.read_csv("data/points.csv")
df.head()

usuarios = ((df.groupby("idUsuario").agg({
                "qtdPontos": "sum"
            }).reset_index()))

# %%

def intervalo(sample, alpha=0.05):

    n = len(sample)
    x_barra = sample.mean()
    s = sample.std()
    t = t_student.ppf(1-alpha/2, n-1)

    inf = x_barra - t * s / (n ** 0.5)
    sup = x_barra + t * s / (n ** 0.5)

    return x_barra, s, inf, sup

stats = []
for i in range(10000):
    n = 100
    sample = usuarios["qtdPontos"].sample(n)
    stats.append(intervalo(sample))

stats = pd.DataFrame(stats, columns=["Média", "Desvio", "Inf", "Sup"])

# %% 
stats["Verdadeiro"] = usuarios["qtdPontos"].mean()

stats["Check"] = (stats["Verdadeiro"] > stats["Inf"]) & (stats["Verdadeiro"] < stats["Sup"])
stats["Check"].mean()

# %%
import matplotlib.pyplot as plt

plt.figure(dpi=400, figsize=(6,6))

for i in range(100):
    data = stats.iloc[i]
    color = 'green' if data["Check"] else 'red'
    plt.plot( data[['Inf', 'Sup']], [i,i], 'o--', color=color, alpha=0.5)

plt.vlines(data['Verdadeiro'].max(), -1, i+1, color='black', alpha=0.5)
plt.xlabel("Limites do Intervalo")
plt.ylabel("Amostra")
plt.title("Intervalos de Confiança")
plt.grid()
plt.show()
# %%