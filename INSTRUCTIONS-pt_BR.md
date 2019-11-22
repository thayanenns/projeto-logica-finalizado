# Instruções

Iremos exercitar as definições de relações binárias em um projeto prático.
Os seguintes arquivos deverão ser implementados:

* _BinaryRelationUtils.py_ - classe responsável por verificar propriedades de uma relação binária (reflexiva, simétrica, transitiva, antissimétrica e de equivalência), bem como por obter as partições de um conjunto, dada uma relação binária de equivalência.
* _GreaterThanBinaryRelation.py_ - classe representando uma relação binária cujos elementos (pares ordenados) possuem a propriedade de que o primeiro item do par ordenado é maior que o segundo.
* _SameFirstLetterBinaryRelation.py_ - classe representando uma relação binária cujos elementos (pares ordenados) possuem a propriedade de que os dois itens do par ordenado iniciam com a mesma letra.
* _SameParityBinaryRelation.py_ - classe representando uma relação binária cujos elementos (pares ordenados) possuem a propriedade de que os dois itens do par ordenado possuem a mesma paridade (par ou ímpar).

## Ordem de Implementação

Eu sugiro, primeiramente, implementar um dos métodos de verificação de propriedades de conjuntos na classe _BinaryRelationUtils_. Em seguida, implemente as classes das relações binárias (_GreaterThanBinaryRelation_, _SameFirstLetterBinaryRelation_ e _SameParityBinaryRelation_). Por fim, implemente os outros métodos da classe _BinaryRelationUtils_.

## Testando o Progresso

Para saber se o seu projeto está completo, simplesmente execute `python BinaryRelationTests.py`.
O arquivo de testes deve ser executado sem nenhum erro.

## Observações Finais

Os conjuntos deste projeto devem ser representados pelo typo `set` em Python. Objetos deste tipo podem ser construídos com a sintaxe `conjunto = set()` ou `conjunto = {1, 2, 3, 4}`. Para adicionar elementos em um _set_, utilize o método `set.add(obj)`, onde _set_ é o conjunto, e _obj_ é o elemento a ser adicionado.