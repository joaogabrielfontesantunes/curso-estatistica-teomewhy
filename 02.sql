WITH tb_subset_mediana AS (
SELECT * FROM POINTS
ORDER BY qtdPontos

LIMIT 1 + (SELECT COUNT(*) % 2 == 0 FROM points)
OFFSET (
        SELECT COUNT(*) / 2 - 1
        FROM POINTS
    )
),

tb_mediana AS (
SELECT AVG(qtdPontos) AS Mediana
FROM tb_subset_mediana
),

tb_subset_quartil_o1 AS (
SELECT * FROM POINTS
ORDER BY qtdPontos

LIMIT 1
OFFSET (
        SELECT 1 * (COUNT(*) + 1) / 4 - 1
        FROM POINTS
    )
),

tb_quartil_o1 AS (
SELECT qtdPontos AS Q1
FROM tb_subset_quartil_o1
),

tb_subset_quartil_o3 AS (
SELECT * FROM POINTS
ORDER BY qtdPontos

LIMIT 1
OFFSET (
        SELECT 3 * (COUNT(*) + 1) / 4 - 1
        FROM POINTS
    )
),

tb_quartil_o3 AS (
SELECT qtdPontos AS Q3
FROM tb_subset_quartil_o3
),

tb_stats AS (
SELECT MIN(qtdPontos) AS Mínimo,
AVG(qtdPontos) AS Média,
MAX(qtdPontos) AS Máximo
FROM POINTS
)

SELECT * FROM tb_stats, tb_mediana, tb_quartil_o1, tb_quartil_o3