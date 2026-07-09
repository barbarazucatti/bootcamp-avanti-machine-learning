### 6. Como identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis?

Outliers são valores que se diferenciam significativamente da maior parte dos dados de um conjunto. É possível identificá-los por diferentes métodos, como o desvio padrão e os quartis.

No método do _desvio padrão_, calcula-se a média e o desvio padrão da variável, que mede o quanto os valores se afastam da média. Valores que estão muito distantes da média, geralmente acima ou abaixo de um determinado número de desvios padrão são considerados outliers.

Já no método dos _quartis_, os dados são organizados em ordem e divididos em quatro partes. Depois, calcula-se o intervalo interquartil (IQR), que é a diferença entre Q3 e Q1. Valores que ficam fora do intervalo (Q1 − 1,5 × IQR) e (Q3 + 1,5 × IQR) podem ser considerados outliers.

Após identificados, os outliers podem ser removidos, substituídos por valores estimados ou mantidos no conjunto de dados, dependendo da sua origem e do objetivo da análise.


### 7. Como concatenar vários DataFrames (empilhando linhas ou colunas), mesmo que tenham colunas diferentes? Dica: Utiliza-se pd.concat() especificando axis=0 (linhas) ou axis=1 (colunas). Quando há colunas diferentes, os valores ausentes são preenchidos com NaN.

A concatenação de DataFrames consiste em unir dois ou mais conjuntos de dados em um único DataFrame. Para isso, utiliza-se a função pd.concat(). Ao definir _axis=0_, os DataFrames são empilhados pelas linhas, adicionando novos registros. Já com _axis=1_, eles são unidos pelas colunas, adicionando novos atributos lado a lado.

Quando os DataFrames possuem colunas diferentes, o Pandas preserva todas as colunas existentes. Nos casos em que uma determinada coluna não está presente em um dos DataFrames, os valores correspondentes são preenchidos automaticamente com NaN, indicando a ausência de dados.

### 8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?

Para ler um arquivo CSV em um DataFrame utilizando o Pandas, utiliza-se a função pd.read_csv(), informando o caminho do arquivo. Em seguida, pode-se utilizar o método head() para exibir as primeiras linhas do DataFrame.

Exemplo:

import pandas as pd

df = pd.read_csv("arquivo.csv")
print(df.head())

Por padrão, o método head() exibe as cinco primeiras linhas do DataFrame, mas é possível informar a quantidade desejada, como df.head(10) para visualizar as dez primeiras linhas.


### 9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?

Para selecionar uma coluna específica em um DataFrame, utiliza-se o nome da coluna entre colchetes. Já para filtrar linhas, aplica-se uma condição lógica sobre a coluna desejada.

Exemplo:

import pandas as pd

_Seleciona apenas uma coluna_
print(df["nome_da_coluna"])

_Filtra as linhas em que o valor da coluna "idade" é maior que 18_
df_filtrado = df[df["idade"] > 18]

print(df_filtrado)

Nesse exemplo, _df["nome_da_coluna"]_ retorna apenas a coluna desejada, enquanto _df[df["idade"] > 18]_ retorna somente as linhas que satisfazem a condição especificada.

### 10. Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

O Pandas oferece diferentes funções para identificar e tratar valores ausentes (NaN). Para verificar a presença desses valores, pode-se utilizar _isnull()_ (ou _isna()_), que retorna quais posições do DataFrame possuem valores ausentes.

Após identificá-los, é possível removê-los utilizando _dropna()_ ou substituí-los por outros valores com _fillna()_, como a média, a mediana, a moda ou um valor definido pelo usuário, dependendo do contexto da análise.


