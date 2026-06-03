import ahpy

A_comparisons = {

    ('CARACTERÍSTICAS GEOLÓGICO-GEOTÉCNICAS', 'CARACTERÍSTICAS GEOLÓGICO-GEOTÉCNICAS'): 1,
    ('CARACTERÍSTICAS GEOLÓGICO-GEOTÉCNICAS', 'CARACTERÍSTICAS ESPACIAIS E GEOMÉTRICAS'): 3,
    ('CARACTERÍSTICAS GEOLÓGICO-GEOTÉCNICAS', 'RELAÇÕES ANTRÓPICAS E INFRAESTRUTURA'): 5,
    ('CARACTERÍSTICAS GEOLÓGICO-GEOTÉCNICAS', 'PROCESSOS HIDROLÓGICOS'): 7,
    ('CARACTERÍSTICAS GEOLÓGICO-GEOTÉCNICAS', 'VEGETAÇÃO'): 9,

    ('CARACTERÍSTICAS ESPACIAIS E GEOMÉTRICAS', 'CARACTERÍSTICAS GEOLÓGICO-GEOTÉCNICAS'): 1/3,
    ('CARACTERÍSTICAS ESPACIAIS E GEOMÉTRICAS', 'CARACTERÍSTICAS ESPACIAIS E GEOMÉTRICAS'): 1,
    ('CARACTERÍSTICAS ESPACIAIS E GEOMÉTRICAS', 'RELAÇÕES ANTRÓPICAS E INFRAESTRUTURA'): 3,
    ('CARACTERÍSTICAS ESPACIAIS E GEOMÉTRICAS', 'PROCESSOS HIDROLÓGICOS'): 5,
    ('CARACTERÍSTICAS ESPACIAIS E GEOMÉTRICAS', 'VEGETAÇÃO'): 5,

    ('RELAÇÕES ANTRÓPICAS E INFRAESTRUTURA', 'CARACTERÍSTICAS GEOLÓGICO-GEOTÉCNICAS'): 1/5,
    ('RELAÇÕES ANTRÓPICAS E INFRAESTRUTURA', 'CARACTERÍSTICAS ESPACIAIS E GEOMÉTRICAS'): 1/3,
    ('RELAÇÕES ANTRÓPICAS E INFRAESTRUTURA', 'RELAÇÕES ANTRÓPICAS E INFRAESTRUTURA'): 1,
    ('RELAÇÕES ANTRÓPICAS E INFRAESTRUTURA', 'PROCESSOS HIDROLÓGICOS'): 3,
    ('RELAÇÕES ANTRÓPICAS E INFRAESTRUTURA', 'VEGETAÇÃO'): 3/1,

    ('PROCESSOS HIDROLÓGICOS', 'CARACTERÍSTICAS GEOLÓGICO-GEOTÉCNICAS'): 1/7,
    ('PROCESSOS HIDROLÓGICOS', 'CARACTERÍSTICAS ESPACIAIS E GEOMÉTRICAS'): 1/5,
    ('PROCESSOS HIDROLÓGICOS', 'RELAÇÕES ANTRÓPICAS E INFRAESTRUTURA'): 1/3, #1/3
    ('PROCESSOS HIDROLÓGICOS', 'PROCESSOS HIDROLÓGICOS'): 1,
    ('PROCESSOS HIDROLÓGICOS', 'VEGETAÇÃO'): 3/1,

    ('VEGETAÇÃO', 'CARACTERÍSTICAS GEOLÓGICO-GEOTÉCNICAS'): 1/9,
    ('VEGETAÇÃO', 'CARACTERÍSTICAS ESPACIAIS E GEOMÉTRICAS'): 1/5,
    ('VEGETAÇÃO', 'RELAÇÕES ANTRÓPICAS E INFRAESTRUTURA'): 1/3,
    ('VEGETAÇÃO', 'PROCESSOS HIDROLÓGICOS'): 1/3,
    ('VEGETAÇÃO', 'VEGETAÇÃO'): 1,

}

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


A = ahpy.Compare(name='A', comparisons=A_comparisons, precision=3, random_index='saaty')

print('TARGET WEIGHTS')
print(A.target_weights)

print('\nCONSISTENCY RATIO')
print(A.consistency_ratio)

#debug_linhas(A)



