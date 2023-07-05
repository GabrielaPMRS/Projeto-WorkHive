import json
'''
with open('anuncios.json', 'w') as arquivo:
    arquivo.write('[]')
'''
def New_anuncio(produto, discribe, valor):
    with open('anuncios.json', 'r') as arquivo:
        anuncios = json.load(arquivo)
    id = len(anuncios)+1

    new_anuncio = {
        'Name' : produto,
        'Discrebe' : discribe,
        'Valor' : valor,
        'ID' : id
    }
    anuncios.append(new_anuncio)
    anuncios = json.dumps(anuncios, indent=4)
    # Escrevendo o novo JSON de volta no arquivo
    with open('anuncios.json', 'w') as arquivo:
        arquivo.write(anuncios)

New_anuncio('lapis  dfjdg ', 'topahrfeuhtgfdfjhg vdo', 10.99)