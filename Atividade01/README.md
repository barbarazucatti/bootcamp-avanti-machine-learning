
### 1. Explique, com suas palavras, o que é machine learning?

Machine learning é uma área da Inteligência Artificial dedicada ao desenvolvimento de algoritmos capazes de aprender a partir de dados. Em vez de serem programados com regras explícitas para cada situação, esses algoritmos identificam padrões em conjuntos de dados e utilizam esse conhecimento para fazer previsões ou tomar decisões sobre novos dados, reduzindo a necessidade de intervenção humana durante esse processo.

### 2. Explique o conceito de conjunto de treinamento, conjunto de validação e conjunto de teste em machine learning.

O _conjunto de treinamento_ é formado pelos dados utilizados para ensinar o modelo. A partir desses dados, o algoritmo aprende os padrões e relações existentes para realizar previsões ou classificações.

O *conjunto de validação* é utilizado durante o desenvolvimento do modelo para avaliar seu desempenho enquanto ele está sendo ajustado. Ele permite comparar diferentes configurações e hiperparâmetros (configurações definidas antes do treinamento), ajudando a escolher a melhor versão do modelo e a reduzir o risco de overfitting, que ocorre quando o modelo aprende excessivamente os padrões dos dados de treinamento, perdendo a capacidade de generalizar para novos dados.

O *conjunto de teste* é utilizado apenas ao final do treinamento e da validação. Ele serve para avaliar o desempenho do modelo em dados que nunca foram vistos anteriormente, fornecendo uma estimativa de como o modelo deverá se comportar em situações reais.

### 3. Explique como você lidaria com dados ausentes em um conjunto de dados de treinamento.

O tratamento de dados ausentes depende da quantidade de valores faltantes e da importância dessas informações para o problema. Quando há poucos valores ausentes, uma alternativa é *remover as linhas* que os contêm. Se uma coluna apresentar muitos valores nulos ou não agregar informações relevantes, ela também pode ser removida.

Outra estratégia é realizar a *imputação dos dados*, substituindo os valores ausentes por estimativas. Porém, um ponto importante para evitar vazamento de dados (data leakage), é que as estimativas devem ser calculadas apenas com base no conjunto de treinamento e, posteriormente, aplicadas aos conjuntos de validação e teste.

Além disso, existem alguns algoritmos de machine learning mais robustos que conseguem lidar diretamente com valores ausentes. Em vez de preencher esses valores, eles aprendem durante o treinamento como tratar as observações com dados faltantes, identificando padrões que permitem realizar previsões mesmo na ausência de algumas informações.

### 4. O que é uma matriz de confusão e como ela é usada para avaliar o desempenho de um modelo preditivo?

A matriz de confusão é uma ferramenta utilizada para avaliar o desempenho de um modelo preditivo de classificação. Ela consiste em uma tabela que compara as classes reais dos dados com as classes previstas pelo modelo, mostrando a quantidade de previsões corretas e incorretas para cada classe.

Em um modelo preditivo, o objetivo é que o algoritmo consiga identificar corretamente os padrões dos dados e realizar previsões em novos exemplos. A matriz de confusão permite analisar se o modelo está fazendo essas previsões corretamente, identificando os acertos e os diferentes tipos de erro cometidos, como falsos positivos e falsos negativos.

A partir dessas informações, é possível calcular métricas de desempenho, além de identificar quais classes o modelo apresenta mais dificuldade em prever e orientar possíveis melhorias no seu desenvolvimento.

### 5. Em quais áreas (tais como construção civil, agricultura, saúde, manufatura, entre outras) você acha mais interessante aplicar algoritmos de machine learning?

Vindo da área ambiental, vejo grande potencial no uso de machine learning para análise de imagens e vídeos provenientes de armadilhas fotográficas, auxiliando na identificação de espécies e no monitoramento da biodiversidade. Atualmente, muitos estudos utilizam esse tipo de equipamento para registrar a presença de animais em determinadas regiões, principalmente em áreas onde estão previstos grandes empreendimentos, como rodovias e ferrovias.

Um dos desafios desse tipo de estudo é o grande volume de dados gerados. Muitas vezes, a análise dessas imagens é realizada manualmente por pesquisadores, o que pode demandar meses de trabalho. Nesse contexto, algoritmos de machine learning podem ser utilizados para reconhecer padrões nas imagens e identificar automaticamente espécies, tornando o processo mais rápido e eficiente.

Além de otimizar o tempo de análise, essa aplicação pode contribuir para estudos de conservação e para tomadas de decisão mais rápidas em projetos que envolvem impactos ambientais..Existem diversos estudos e iniciativas utilizando inteligência artificial com esse objetivo, como aborda o artigo da WWF que mostra o potencial do uso de IA na identificação e monitoramento de espécies: https://www.worldwildlife.org/news/stories/using-the-power-of-ai-to-identify-and-track-species/
