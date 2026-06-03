import ahpy


B2_comparisons = {

    ('Posição das residências em relação ao talude:', 'Posição das residências em relação ao talude:'): 1,
    ('Posição das residências em relação ao talude:', 'Distância da casa ao talude:'): 1,
    ('Posição das residências em relação ao talude:', 'Natureza do Talude'): 1,
    ('Posição das residências em relação ao talude:', 'Curvatura da Encosta'): 3,
    ('Posição das residências em relação ao talude:', 'Inclinação do Talude'): 1/3,
    ('Posição das residências em relação ao talude:', 'Características do Material:'): 1/3,

    ('Distância da casa ao talude:', 'Posição das residências em relação ao talude:'): 1,
    ('Distância da casa ao talude:', 'Distância da casa ao talude:'): 1,
    ('Distância da casa ao talude:', 'Natureza do Talude'): 1,
    ('Distância da casa ao talude:', 'Curvatura da Encosta'): 2,
    ('Distância da casa ao talude:', 'Inclinação do Talude'): 1/3,
    ('Distância da casa ao talude:', 'Características do Material:'): 1/7,

    ('Natureza do Talude', 'Posição das residências em relação ao talude:'): 1,
    ('Natureza do Talude', 'Distância da casa ao talude:'): 1,
    ('Natureza do Talude', 'Natureza do Talude'): 1,
    ('Natureza do Talude', 'Curvatura da Encosta'): 2,
    ('Natureza do Talude', 'Inclinação do Talude'): 1/3,
    ('Natureza do Talude', 'Características do Material:'): 1/5,

    ('Curvatura da Encosta', 'Posição das residências em relação ao talude:'): 1/3,
    ('Curvatura da Encosta', 'Distância da casa ao talude:'): 1/2,
    ('Curvatura da Encosta', 'Natureza do Talude'): 1/2,
    ('Curvatura da Encosta', 'Curvatura da Encosta'): 1,
    ('Curvatura da Encosta', 'Inclinação do Talude'): 1/3,
    ('Curvatura da Encosta', 'Características do Material:'): 1/5,

    ('Inclinação do Talude', 'Posição das residências em relação ao talude:'): 3,
    ('Inclinação do Talude', 'Distância da casa ao talude:'): 3,
    ('Inclinação do Talude', 'Natureza do Talude'): 3,
    ('Inclinação do Talude', 'Curvatura da Encosta'): 3,
    ('Inclinação do Talude', 'Inclinação do Talude'): 1,
    ('Inclinação do Talude', 'Características do Material:'): 1/9,

    ('Características do Material:', 'Posição das residências em relação ao talude:'): 3,
    ('Características do Material:', 'Distância da casa ao talude:'): 7,
    ('Características do Material:', 'Natureza do Talude'): 5,
    ('Características do Material:', 'Curvatura da Encosta'): 5,
    ('Características do Material:', 'Inclinação do Talude'): 9,
    ('Características do Material:', 'Características do Material:'): 1,

}
B2 = ahpy.Compare(name='B2', comparisons=B2_comparisons, precision=3, random_index='saaty')

def debug_linhas(compare):
    elementos = compare._elements
    matriz = compare._matrix
    somas_colunas = matriz.sum(axis=0)
    matriz_normalizada = matriz / somas_colunas
    pesos_por_media_linha = matriz_normalizada.mean(axis=1)

    print('\nSOMAS DAS COLUNAS')
    for elemento, soma in zip(elementos, somas_colunas):
        print(f'{elemento}: {soma:.3f}')

    print('\nDEBUG POR LINHA')
    for i, elemento_linha in enumerate(elementos):
        print(f'\n{elemento_linha}')
        for j, elemento_coluna in enumerate(elementos):
            valor_original = matriz[i, j]
            valor_normalizado = matriz_normalizada[i, j]
            print(
                f'  vs {elemento_coluna}: '
                f'original={valor_original:.3f}, normalizado={valor_normalizado:.3f}'
            )
        print(f'  media da linha normalizada: {pesos_por_media_linha[i]:.3f}')
        print(f'  target_weight ahpy: {compare.target_weights[elemento_linha]:.3f}')




print('TARGET WEIGHTS')
print(B2.target_weights)

print('\nCONSISTENCY RATIO')
print(B2.consistency_ratio)

debug_linhas(B2)



report = B2.report(show=True)