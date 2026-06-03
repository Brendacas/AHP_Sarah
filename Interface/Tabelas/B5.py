import ahpy


B5_comparisons = {

    ('Presença de Vegetação:', 'Presença de Vegetação:'): 1,
    ('Presença de Vegetação:', 'Sitema radicular da vegetação'): 5/1,
    ('Presença de Vegetação:', 'Tipo de vegetação Presente:'): 5/1,
    ('Presença de Vegetação:', 'Ação do vento sobre as árvores:'): 5/1,
    ('Presença de Vegetação:', 'Impacto da Vegetação no solo:'): 5/1,

    ('Sitema radicular da vegetação', 'Presença de Vegetação:'): 1/5,
    ('Sitema radicular da vegetação', 'Sitema radicular da vegetação'): 1,
    ('Sitema radicular da vegetação', 'Tipo de vegetação Presente:'): 3,
    ('Sitema radicular da vegetação', 'Ação do vento sobre as árvores:'): 1/3,
    ('Sitema radicular da vegetação', 'Impacto da Vegetação no solo:'): 1/5,

    ('Tipo de vegetação Presente:', 'Presença de Vegetação:'): 1/5,
    ('Tipo de vegetação Presente:', 'Sitema radicular da vegetação'): 1/3,
    ('Tipo de vegetação Presente:', 'Tipo de vegetação Presente:'): 1,
    ('Tipo de vegetação Presente:', 'Ação do vento sobre as árvores:'): 1/3,
    ('Tipo de vegetação Presente:', 'Impacto da Vegetação no solo:'): 1/5,

    ('Ação do vento sobre as árvores:', 'Presença de Vegetação:'): 1/5,
    ('Ação do vento sobre as árvores:', 'Sitema radicular da vegetação'): 1/3,
    ('Ação do vento sobre as árvores:', 'Tipo de vegetação Presente:'): 3,
    ('Ação do vento sobre as árvores:', 'Ação do vento sobre as árvores:'): 1,
    ('Ação do vento sobre as árvores:', 'Impacto da Vegetação no solo:'): 1/5,

    ('Impacto da Vegetação no solo:', 'Presença de Vegetação:'): 1/5,
    ('Impacto da Vegetação no solo:', 'Sitema radicular da vegetação'): 5,
    ('Impacto da Vegetação no solo:', 'Tipo de vegetação Presente:'): 5,
    ('Impacto da Vegetação no solo:', 'Ação do vento sobre as árvores:'): 5,
    ('Impacto da Vegetação no solo:', 'Impacto da Vegetação no solo:'): 1,

}
compara = ahpy.Compare(name='A', comparisons=B5_comparisons, precision=3, random_index='saaty')

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

#debug_linhas(compara)



#report = compara.report(show=True)