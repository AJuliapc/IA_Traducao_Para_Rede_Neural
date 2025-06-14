# Traduzir Programa em Lógica Proposicional para Rede Neural Equivalente

**Equipe**

1. Alberth Viana de Lima
2. Ana Júlia Pereira Corrêa
3. Daniel Silveira Gonzales
4. Júlio Melo Campos

# Etapas do trabalho

1 - Implementar um programa em Python que leia um programa em Lógica Proposicional (LP), representado em uma planilha csv em que cada linha é um expressão em LP e gera uma rede neural que funcione como o programa. Siga o algoritmo do CILP apresentado pelo artigo do Garcez e Zaverucha (no material de classe).
   
2 - Testar a rede gerando uma tabela com entradas lógicas (1 e -1) para cada variável de entrada. Se a rede gerar com uma entrada de 5 variáveis, a tabela de teste deve ter 2 elevado a 5 linhas. Rode a rede e mostre os valores lógicos de saída para cada neurônio de saída.

# Resultados 

Foram implementados 4 códigos em python, cada um com uma função distinta mas complementar. São eles:

1. `regras.py`: Esse código cria um arquivo chamado regras.csv e escreve nele um conjunto de regras lógicas, cada uma em uma linha. As regras seguem o formato de implicações, como "A, B -> C", representando relações entre condições. Ao final, ele exibe uma mensagem informando que o arquivo foi gerado com sucesso.
2. `entradas.py`: Esse código gera todas as combinações possíveis de valores 1 e -1 para as variáveis A, B, C e D, representando verdade e falso. Ele salva essas combinações em um arquivo CSV chamado entradas_logicas.csv, com um cabeçalho indicando os nomes das variáveis. Por fim, exibe uma mensagem confirmando que o arquivo foi criado com sucesso.
3. `main.py`: Esse código cria uma rede neural simbólica que aprende e executa regras lógicas representadas em um CSV. Ele lê as regras e as combinações de entrada, processa essas entradas aplicando as regras até estabilizar os valores e gera um CSV com os resultados das inferências. No final, informa que os resultados foram salvos e pode exibir os passos da propagação, se desejar.
4. `verifica.py`: O código lê um CSV com entradas e saídas lógicas e verifica se um conjunto de regras lógicas foi seguido em cada linha. Ele compara as premissas com a entrada e testa se a conclusão está correta na saída, considerando também negações. No final, informa no terminal se cada regra foi satisfeita, violada ou não se aplicou para cada conjunto de dados.

Em resumo, `regras.py` e `entradas.py` devem ser executadas primeiro, para gerar então os arquivos `csv`. Logo em seguida, `main.py` deve ser executado para gerar a saída e `verifica.py` para testar os conjuntos de regras.
