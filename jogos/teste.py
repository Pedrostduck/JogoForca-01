frutas = ['Pera', 'Banana', 'Melância', 'Manga', 'Maçâ', 'Morango']

fruta_pedida=input('Qual a fruta que deseja?')

if(fruta_pedida.upper in frutas):
    print('Sim, temos a fruta')
else:
    print('Não temos a fruta')