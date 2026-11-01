# %%

import pandas as pd
import sqlalchemy

df = pd.read_csv("data/points.csv")
df.head()

engine = sqlalchemy.create_engine("sqlite:///data/tmw.db")
df.to_sql("points", engine, if_exists="replace", index=False)
# %%

tabela_frequencia = (
    df.groupby("descProduto")["idTransacao"]
    .count()
    .reset_index()
    .rename(columns={"idTransacao": "Freq. Abs"})
)
# %%

tabela_frequencia["Freq. Abs Acum"] = tabela_frequencia["Freq. Abs"].cumsum()
tabela_frequencia["Freq. Rel"] = tabela_frequencia["Freq. Abs"] / tabela_frequencia["Freq. Abs"].sum()
tabela_frequencia["Freq. Rel Acum"] = tabela_frequencia["Freq. Rel"].cumsum()
tabela_frequencia.head()
# %%
