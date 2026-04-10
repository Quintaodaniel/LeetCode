# 0344 - Reverse String

🔗 [Link para o problema no LeetCode](https://leetcode.com/problems/reverse-string/)

## 📝 Descrição do Problema
O objetivo é inverter uma string (fornecida como um array de caracteres). A regra de ouro deste problema é que a inversão deve ser feita **in-place**, ou seja, modificando o array de entrada diretamente e utilizando apenas $O(1)$ de memória extra.

---

## 🧠 Solução em C (Foco em Lógica de Índices e Swapping)

Para atender ao requisito rigoroso de $O(1)$ de espaço, a solução em C manipula os índices diretamente para trocar as extremidades da string até chegar ao centro.

**Abordagem:** Utilizei uma variação da técnica de "Dois Ponteiros". O laço `for` controla o índice `i` (que avança da esquerda para a direita). Em vez de alocar uma segunda variável para o ponteiro da direita, calculei o índice oposto dinamicamente usando `tam - 1 - i`. Através de uma variável temporária `temp`, os caracteres nas extremidades são trocados. O laço é interrompido assim que o índice da esquerda encontra ou ultrapassa o índice da direita (`i >= tam - 1 - i`).

```c
void reverseString(char* s, int tam) {
    for (int i = 0;;i++) {
        if (i >= tam -1 -i) {
            break;
        }
        
        char temp = s[i];
        s[i] = s[tam -1 -i];
        s[tam -1 -i] = temp;
    }
}
```

---

## 🐍 Solução em Python (Foco em Eficiência e Métodos Nativos)

Em Python, a clareza e a utilização correta das estruturas de dados nativas são os maiores diferenciais de um bom código.

**Abordagem:** Como a estrutura fornecida é uma `list`, utilizei o método nativo `.reverse()`. Este método inverte os elementos da lista **in-place**, cumprindo exatamente o requisito de $O(1)$ de memória extra do problema. É a solução mais limpa e "Pythônica" possível, garantindo máxima performance, pois os métodos nativos do CPython são implementados e otimizados em C.

```python
class Solution:
    def reverseString(self, s: list) -> None:
        s.reverse()
```

---

## 📊 Análise de Complexidade

Ambas as abordagens resolvem o problema de forma ótima, respeitando as restrições de memória:

| Linguagem | Tempo | Espaço | Observação |
| :--- | :--- | :--- | :--- |
| **C** | $O(N)$ | $O(1)$ | O algoritmo percorre apenas a metade do array ($N/2$ operações de swap), o que simplifica para $O(N)$ em complexidade de tempo. Nenhuma estrutura auxiliar é criada. |
| **Python** | $O(N)$ | $O(1)$ | O método `.reverse()` opera diretamente na lista original sem criar cópias, sendo extremamente eficiente. |