# %%
import pandas as pd

df = pd.read_csv("data/points.csv")
df.head()

# %%
minimo = df["qtdPontos"].min()
media = df["qtdPontos"].mean()
quartil_1 = df["qtdPontos"].quantile(0.25)
mediana = df["qtdPontos"].median()
quartil_3 = df["qtdPontos"].quantile(0.75)
maximo = df["qtdPontos"].max()
variancia = df["qtdPontos"].var()
desvio_padrao = df["qtdPontos"].std()
amplitude = df["qtdPontos"].max() - df["qtdPontos"].min()

print(f"Minimo: {minimo}")
print(f"Média: {media}")
print(f"1o Quartil: {quartil_1}")
print(f"Mediana: {mediana}")
print(f"3o Quartil: {quartil_3}")
print(f"Máximo: {maximo}")
print(f"Variância: {variancia}")
print(f"Desvio Padrão: {desvio_padrao}")
print(f"Amplitude: {amplitude}")
# %%
usuarios = (df.groupby(["idUsuario"])
             .agg({
                     "idTransacao":"count",
                     "qtdPontos":"sum",
             }).reset_index())
# %%
usuarios[["idTransacao", "qtdPontos"]].describe()
# %%
