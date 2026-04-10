# 0027 - Remove Element

🔗 [Link para o problema no LeetCode](https://leetcode.com/problems/remove-element/)

## 📝 Descrição do Problema
O objetivo é remover todas as ocorrências de um valor específico (`val`) de um array de inteiros (`nums`). A remoção deve ser feita **in-place** (sem alocar memória extra para um novo array), e a função deve retornar o novo tamanho do array válido. A ordem dos elementos mantidos pode ser alterada.

---

## 🧠 Solução em C (Foco em Performance e Lógica de Baixo Nível)

Para a solução em C, a prioridade foi a eficiência de tempo e espaço, manipulando os índices do array diretamente. 

**Abordagem:** Utilizei a técnica de **Dois Ponteiros**. O ponteiro `i` percorre o array do início ao fim, enquanto o ponteiro `j` marca o tamanho atualizado do array a partir do final. Quando encontro o valor indesejado (`val`), em vez de deslocar todos os elementos seguintes para a esquerda (o que seria custoso), eu simplesmente pego o último elemento válido do array (`nums[j - 1]`) e o coloco na posição atual de `i`. Em seguida, reduzo o tamanho total `j`.

```c
int removeElement(int* nums, int numsSize, int val) {
    int i = 0;
    int j = numsSize;
    
    while (i < j) {
        if (nums[i] == val) {
            nums[i] = nums[j - 1]; 
            j--; 
        } else {
            i++;
        }
    }
    
    return j; 
}
```

---

## 🐍 Solução em Python (Foco em Agilidade e Legibilidade)

**Abordagem:** O código Python tira proveito dos métodos nativos da linguagem. O loop verifica se o valor existe na lista usando o operador `in` e o remove com o método `.remove()`. É um código "Pythônico", limpo e que resolve o problema de negócio rapidamente com apenas 3 linhas.

```python
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        
        return len(nums)
```

---

## 📊 Análise de Complexidade

Esta comparação ilustra bem a diferença entre o controle absoluto do C e as abstrações do Python:

| Linguagem | Tempo | Espaço | Observação |
| :--- | :--- | :--- | :--- |
| **C** | $O(N)$ | $O(1)$ | O array é percorrido no máximo uma vez. Excelente performance e sem alocação extra. |
| **Python** | $O(N^2)$ | $O(1)$ | Embora legível, o método `.remove()` no Python precisa buscar o elemento e depois deslocar todos os itens da lista internamente. Pior cenário: percorre e desloca múltiplos elementos repetidas vezes. |