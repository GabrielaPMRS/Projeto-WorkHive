import json

def list_anucios_id():
    with open('anuncios.json', 'r') as arquivo:
        anuncios = json.load(arquivo)
    ids = []
    for item in anuncios:
        ids.append(item["ID"])
    print(ids)

list_anucios_id()