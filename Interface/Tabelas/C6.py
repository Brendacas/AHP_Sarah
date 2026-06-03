import ahpy


C6_comparisons = {

    ('Encanada', 'Encanada'): 1,
    ('Encanada', 'Poço Artesiano'): 9,
    ('Encanada', 'Cisterna de Captação de Água da Chuva'): 7,

    ('Poço Artesiano', 'Encanada'): 1/9,
    ('Poço Artesiano', 'Poço Artesiano'): 1,
    ('Poço Artesiano', 'Cisterna de Captação de Água da Chuva'): 1/7,

    ('Cisterna de Captação de Água da Chuva', 'Encanada'): 1/7,
    ('Cisterna de Captação de Água da Chuva', 'Poço Artesiano'): 7,
    ('Cisterna de Captação de Água da Chuva', 'Cisterna de Captação de Água da Chuva'): 1,

}

C2 = ahpy.Compare(name='A', comparisons=C6_comparisons, precision=3, random_index='saaty')

print(C2.target_weights)
print(C2.consistency_ratio)

#report = C2.report(show=True)


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


#debug_linhas(C2)
