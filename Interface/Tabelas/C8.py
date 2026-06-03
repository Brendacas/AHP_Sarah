import ahpy
import numpy as np
 
#target_weights: Prioridades globais de todos os nós folha (alternativas) em relação ao objetivo raiz.
#local_weights: Prioridades relativas ao pai ou mãe imediato na hierarquia.
#global_weights: Prioridades de critérios ou subcritérios relativos ao objetivo raiz.


C8_comparisons = {

    ('Aterro irregular', 'Aterro irregular'): 1,
    ('Aterro irregular', 'Lixo / Resíduos Sólidos'): 1,
    ('Aterro irregular', 'Entulho de construção'): 1,
    ('Aterro irregular', 'Destroços de sistema de esgoto'): 1/5,
    ('Aterro irregular', 'Destroços de sistema de drenagem'): 1/7,

    ('Lixo / Resíduos Sólidos', 'Aterro irregular'): 1,
    ('Lixo / Resíduos Sólidos', 'Lixo / Resíduos Sólidos'): 1,
    ('Lixo / Resíduos Sólidos', 'Entulho de construção'): 3,
    ('Lixo / Resíduos Sólidos', 'Destroços de sistema de esgoto'): 1/3,
    ('Lixo / Resíduos Sólidos', 'Destroços de sistema de drenagem'): 1/5,

    ('Entulho de construção', 'Aterro irregular'): 1,
    ('Entulho de construção', 'Lixo / Resíduos Sólidos'): 1/3,
    ('Entulho de construção', 'Entulho de construção'): 1,
    ('Entulho de construção', 'Destroços de sistema de esgoto'): 1/3,
    ('Entulho de construção', 'Destroços de sistema de drenagem'): 1/5,

    ('Destroços de sistema de esgoto', 'Aterro irregular'): 5,
    ('Destroços de sistema de esgoto', 'Lixo / Resíduos Sólidos'): 3,
    ('Destroços de sistema de esgoto', 'Entulho de construção'): 3,
    ('Destroços de sistema de esgoto', 'Destroços de sistema de esgoto'): 1,
    ('Destroços de sistema de esgoto', 'Destroços de sistema de drenagem'): 3,

    ('Destroços de sistema de drenagem', 'Aterro irregular'): 7,
    ('Destroços de sistema de drenagem', 'Lixo / Resíduos Sólidos'): 5,
    ('Destroços de sistema de drenagem', 'Entulho de construção'): 5,
    ('Destroços de sistema de drenagem', 'Destroços de sistema de esgoto'): 1/3,
    ('Destroços de sistema de drenagem', 'Destroços de sistema de drenagem'): 1,

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


C7 = ahpy.Compare(name='C7', comparisons=C8_comparisons, precision=3, random_index='saaty')

print('TARGET WEIGHTS')
print(C7.target_weights)

print('\nCONSISTENCY RATIO')
print(C7.consistency_ratio)

#debug_linhas(C7)
