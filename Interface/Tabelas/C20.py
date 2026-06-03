import ahpy


C20_comparisons = {

    ('de média profundidade (até 1m)', 'de média profundidade (até 1m)'): 1,
    ('de média profundidade (até 1m)', 'de grande profundidade (até 3m)'): 7/1,

    ('de grande profundidade (até 3m)', 'de média profundidade (até 1m)'): 1/7,
    ('de grande profundidade (até 3m)', 'de grande profundidade (até 3m)'): 1,

}
compara = ahpy.Compare(name='A', comparisons=C20_comparisons, precision=3, random_index='saaty')

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
print(compara.target_weights)

print('\nCONSISTENCY RATIO')
print(compara.consistency_ratio)

debug_linhas(compara)



report = compara.report(show=True)