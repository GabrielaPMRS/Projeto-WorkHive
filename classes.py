class MASTER:
    all_users = []
    current_user #cpf
    logged #bool

    def criar_usuario():
        pass
    def deletar_usuario():
        pass
    def editar_usuario():
        pass
    def empregar():
        pass

class Users:
    usuario
    cpf
    senha
    favoritos = [] #lista de id(int)
    empregados = [] #lista de cpf()
    empregadores = [] #lista de cpf()

    anuncios = [] #lista de anuncios

class Anuncios:
    servico
    descricao
    valor
    categoria
    feedback = []#lista de string
    cpf_user
    id_anuncio

    def criar_anuncio():
        pass