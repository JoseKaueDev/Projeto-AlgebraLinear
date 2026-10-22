import matplotlib.pyplot as plt
import numpy as np

def calcular_equacao_plano_e_gerar_grafico(matriz_A, matriz_B):
    # Extrair o Ponto P0 e o Vetor n de dentro das suas matrizes existentes
    P0 = matriz_A[0]  # Pega a primeira linha da matriz_A [1, 2, 3]
    n = matriz_B[0]   # Pega a primeira linha da matriz_B [9, 8, 7]
    
    # 2. Separar as coordenadas para facilitar o cálculo
    x0, y0, z0 = P0[0], P0[1], P0[2]
    a, b, c = n[0], n[1], n[2]
    
    # 3. Calcular o d: d = -(a*x0 + b*y0 + c*z0) e contando o custo 
    operacoes = 0
    termo_1 = a * x0; operacoes += 1
    termo_2 = b * y0; operacoes += 1
    termo_3 = c * z0; operacoes += 1
    soma_interna = termo_1 + termo_2 + termo_3; operacoes += 2
    d = -soma_interna; operacoes += 1
    
    print("==========================================================")
    print("      ATIVIDADE: EQUAÇÃO DO PLANO COM MATRIZES EM 3D     ")
    print("==========================================================")
    print(f"Ponto P0 extraído da Matriz A (linha 1): {P0}")
    print(f"Vetor Normal n extraído da Matriz B (linha 1): {n}")
    print(f"Cálculo: {a}*(x - {x0}) + {b}*(y - {y0}) + {c}*(z - {z0}) = 0")
    print(f"EQUAÇÃO CARTESIANA DO PLANO π: {a}x + {b}y + {c}z + ({d}) = 0")
    print(f"Operações computacionais no cálculo: {operacoes}")
    print("Gerando visualização gráfica em 3D...\n")
    
    # 4. Construção da Visualização 3D
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Criando a malha do plano deitado no espaço
    x = np.linspace(-5, 10, 20)
    y = np.linspace(-5, 10, 20)
    X, Y = np.meshgrid(x, y)
    
    # Resolvendo a equação para obter Z (altura do plano): z = (-a*x - b*y - d) / c
    Z = (-a * X - b * Y - d) / c
    
    # Plota a superfície do plano (translúcida para ver atrás)
    ax.plot_surface(X, Y, Z, alpha=0.5, color='royalblue', label='Plano π')
    
    # Plota o ponto P0 no espaço (como uma esfera vermelha)
    ax.scatter([x0], [y0], [z0], color='red', s=100, label=f'P0 {P0}', zorder=5)
    
    # Plota o vetor normal (vetor que "sai" do ponto em direção perpendicular)
    # n[0], n[1], n[2] divididos por 3 apenas para reduzir o tamanho visual da seta na escala
    ax.quiver(x0, y0, z0, a/2, b/2, c/2, color='black', linewidth=3, arrow_length_ratio=0.3, label=f'Vetor normal n {n}')
    
    # Legenda e formatação
    ax.set_title(f'Plano π: {a}x + {b}y + {c}z + ({d}) = 0', fontsize=12, fontweight='bold')
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')
    ax.legend()
    
    # Definindo os limites do gráfico
    ax.set_xlim([-5, 10])
    ax.set_ylim([-5, 10])
    ax.set_zlim([-10, 10])
    
    plt.show()

def multiplicar_matrizes(matriz_A, matriz_B):
    total_linhas_A = len(matriz_A)
    total_colunas_A = len(matriz_A[0])
    
    total_linhas_B = len(matriz_B)
    total_colunas_B = len(matriz_B[0])
    
    if total_colunas_A != total_linhas_B:
        raise ValueError("Multiplicação impossível: Colunas de A != Linhas de B")
    
    matriz_resultado = []
    for i_linha in range(total_linhas_A):
        linha_zerada = []
        for j_coluna in range(total_colunas_B):
            linha_zerada.append(0)
        matriz_resultado.append(linha_zerada)
        
    contador_operacoes = 0
    
    for i_linha in range(total_linhas_A):
        for j_coluna in range(total_colunas_B):
            soma_produto_escalar = 0
            for k_indice in range(total_colunas_A):
                elemento_A = matriz_A[i_linha][k_indice]
                elemento_B = matriz_B[k_indice][j_coluna]
                
                produto_parcial = elemento_A * elemento_B
                soma_produto_escalar = soma_produto_escalar + produto_parcial
                
                contador_operacoes = contador_operacoes + 2
            
            matriz_resultado[i_linha][j_coluna] = soma_produto_escalar
            
    return matriz_resultado, contador_operacoes


def somar_matrizes(matriz_A, matriz_B):
    total_linhas = len(matriz_A)
    total_colunas = len(matriz_A[0])
    
    matriz_resultado = []
    contador_operacoes = 0
    
    for i_linha in range(total_linhas):
        linha_resultante = []
        for j_coluna in range(total_colunas):
            soma = matriz_A[i_linha][j_coluna] + matriz_B[i_linha][j_coluna]
            linha_resultante.append(soma)
            contador_operacoes = contador_operacoes + 1
        matriz_resultado.append(linha_resultante)
        
    return matriz_resultado, contador_operacoes


def criar_matriz_identidade(ordem):
    matriz_identidade = []
    
    for i_linha in range(ordem):
        linha = []
        for j_coluna in range(ordem):
            if i_linha == j_coluna:
                linha.append(1)
            else:
                linha.append(0)
        matriz_identidade.append(linha)
        
    return matriz_identidade


def verificar_igualdade_matrizes(matriz_A, matriz_B):
    total_linhas_A = len(matriz_A)
    total_colunas_A = len(matriz_A[0])
    
    total_linhas_B = len(matriz_B)
    total_colunas_B = len(matriz_B[0])
    
    if total_linhas_A != total_linhas_B or total_colunas_A != total_colunas_B:
        return False
        
    for i_linha in range(total_linhas_A):
        for j_coluna in range(total_colunas_A):
            if matriz_A[i_linha][j_coluna] != matriz_B[i_linha][j_coluna]:
                return False
                
    return True


matriz_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

matriz_C = [
    [2, 0, 1],
    [1, 3, 4],
    [0, 1, 2]
]

matriz_I = criar_matriz_identidade(3)

print("=================================================================")
print("  TESTE EXPÍCITO DAS PROPRIEDADES DA MULTIPLICAÇÃO DE MATRIZES  ")
print("=================================================================\n")

matriz_BC, ops_BC = multiplicar_matrizes(matriz_B, matriz_C)
matriz_A_BC, ops_A_BC = multiplicar_matrizes(matriz_A, matriz_BC)
total_ops_lhs1 = ops_BC + ops_A_BC

matriz_AB, ops_AB = multiplicar_matrizes(matriz_A, matriz_B)
matriz_AB_C, ops_AB_C = multiplicar_matrizes(matriz_AB, matriz_C)
total_ops_rhs1 = ops_AB + ops_AB_C

eh_associativa = verificar_igualdade_matrizes(matriz_A_BC, matriz_AB_C)

print("1. PROPRIEDADE ASSOCIATIVA: A * (B * C) == (A * B) * C")
print(f"   - Propriedade Válida? : {eh_associativa}")
print(f"   - Operações em A*(B*C): {total_ops_lhs1}")
print(f"   - Operações em (A*B)*C: {total_ops_rhs1}")
print(f"   - Custo total do teste: {total_ops_lhs1 + total_ops_rhs1} operações\n")

matriz_B_mais_C, ops_soma_BC = somar_matrizes(matriz_B, matriz_C)
matriz_A_BmaisC, ops_mul_A_BC = multiplicar_matrizes(matriz_A, matriz_B_mais_C)
total_ops_lhs2 = ops_soma_BC + ops_mul_A_BC

matriz_AC, ops_AC = multiplicar_matrizes(matriz_A, matriz_C)
matriz_AB_mais_AC, ops_soma_AB_AC = somar_matrizes(matriz_AB, matriz_AC)
total_ops_rhs2 = ops_AB + ops_AC + ops_soma_AB_AC

eh_distributiva = verificar_igualdade_matrizes(matriz_A_BmaisC, matriz_AB_mais_AC)

print("2. PROPRIEDADE DISTRIBUTIVA: A * (B + C) == A*B + A*C")
print(f"   - Propriedade Válida? : {eh_distributiva}")
print(f"   - Operações em A*(B+C): {total_ops_lhs2} (Soma primeiro, multiplica depois)")
print(f"   - Operações em AB + AC: {total_ops_rhs2} (Duas multiplicações + uma soma)")
print(f"   - Custo total do teste: {total_ops_lhs2 + total_ops_rhs2} operações\n")

matriz_AI, ops_AI = multiplicar_matrizes(matriz_A, matriz_I)
matriz_IA, ops_IA = multiplicar_matrizes(matriz_I, matriz_A)

igual_AI = verificar_igualdade_matrizes(matriz_AI, matriz_A)
igual_IA = verificar_igualdade_matrizes(matriz_IA, matriz_A)
eh_elemento_neutro = igual_AI and igual_IA

print("3. ELEMENTO NEUTRO (MATRIZ IDENTIDADE): A * I == I * A == A")
print(f"   - Propriedade Válida? : {eh_elemento_neutro}")
print(f"   - Operações em A * I  : {ops_AI}")
print(f"   - Operações em I * A  : {ops_IA}")
print(f"   - Custo total do teste: {ops_AI + ops_IA} operações\n")

matriz_BA, ops_BA = multiplicar_matrizes(matriz_B, matriz_A)

sao_iguais_AB_BA = verificar_igualdade_matrizes(matriz_AB, matriz_BA)

print("4. NÃO-COMUTATIVIDADE: A * B != B * A")
print(f"   - A * B é igual a B * A? : {sao_iguais_AB_BA}")
print(f"   - Conclusão              : {'Comutou (Raro)' if sao_iguais_AB_BA else 'NÃO comutou (Confirmado)'}")
print(f"   - Operações para A * B   : {ops_AB}")
print(f"   - Operações para B * A   : {ops_BA}")
print(f"   - Custo total do teste   : {ops_AB + ops_BA} operações\n")

calcular_equacao_plano_e_gerar_grafico(matriz_A, matriz_B)