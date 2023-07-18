def mock_data(users, anuncios):
    users.append({'usuario': 'joao', 'cpf':'234', 'senha':'1', 'feedback': [], 'notificacoes': []})
    users.append({'usuario': 'maria', 'cpf':'12344', 'senha':'2', 'feedback': [], 'notificacoes': []})
    users.append({'usuario': 'rita', 'cpf':'1234567789', 'senha':'3', 'feedback': [], 'notificacoes': []})
    anuncios.append({
        'Usuario': 'joao', 
        'Nome': 'carro', 
        'Descrição': 'anda', 
        'Valor': '123', 
        'ID': 1, 
        'Categoria': 'automovel',
        'Feedbacks': ['util']
        })
    anuncios.append({
        'Usuario': 'maria', 
        'Nome': 'vestido', 
        'Descrição': 'veste', 
        'Valor': '1234', 
        'ID': 2, 
        'Categoria': 'roupa', 
        'Feedbacks': []
        })
    