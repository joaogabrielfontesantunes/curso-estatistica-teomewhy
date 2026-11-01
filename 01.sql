WITH tb_freq AS (
SELECT descProduto,
count(idTransacao) AS "Freq. Abs"
FROM POINTS

GROUP BY descProduto
),

tb_freq_acum AS (
SELECT *,
sum("Freq. Abs") OVER (ORDER BY "Freq. Abs") AS "Freq. Abs Acum"
FROM tb_freq
)

SELECT *,
"Freq. Abs" * 1.0 / SUM("Freq. Abs") OVER () AS "Freq. Rel",
"Freq. Abs Acum" * 1.0 / SUM("Freq. Abs") OVER () AS "Freq. Rel Acum"
FROM tb_freq_acum