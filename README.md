# 🧮 Validação Prática das Propriedades de Matrizes em Python

Este projeto apresenta uma implementação em **Python puro** (sem o uso de bibliotecas externas como NumPy) para realizar operações básicas de álgebra linear — **multiplicação**, **soma**, **geração de matriz identidade** e **verificação de igualdade** — e testar empiricamente as principais propriedades da multiplicação de matrizes.

Além da validação matemática, o código contabiliza o **custo computacional** (quantidade de operações aritméticas executadas) em cada abordagem.

---

## 📌 Propriedades Demonstradas

1. **Propriedade Associativa**: $A \times (B \times C) = (A \times B) \times C$
2. **Propriedade Distributiva**: $A \times (B + C) = A \times B + A \times C$
   * *Destaque:* Demonstra a diferença do número de operações ao somar antes de multiplicar vs. multiplicar antes de somar.
3. **Elemento Neutro (Matriz Identidade)**: $A \times I = I \times A = A$
4. **Não-Comutatividade**: $A \times B \neq B \times A$ (em regra)

---

