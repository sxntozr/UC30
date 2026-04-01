# SISTEMA DE GESTÃO DE BIBLIOTECA

# Dicionário p/ armazenar os livros
catalogo = {}

# Dicionário p/ armazenar os empréstimos ativos
emprestimosAtivos = {}

# Lista p/ armazenar o histórico de transição
histórico = []

# Função: Adicionar livro

def adicionarLivro(codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"Erro: Livro com código {codigo} já existe")
        return False
    
    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade
    }

    print(f"Livro '{titulo}' adicionado com sucesso")
    return True

adicionarLivro("L001", "Código Limpo", "Robert Cecil Martin", 2)

emprestimosAtivos = {
    "aluno1": ["L001", "L002"],
    "aluno2": ["L001"]
}

def contarLivrosAluno(aluno):
    if aluno not in emprestimosAtivos:
        print(f"O aluno {aluno} não possui empréstimos")
        return 0
    
    quantidade = len(emprestimosAtivos[aluno])
    print(f"O aluno {aluno} pegou {quantidade} livro(s)")
    return quantidade

emprestimosAtivos["João"] = ["L001", "L002"]
emprestimosAtivos["Maria"] = ["L001"]

contarLivrosAluno("João")   # Saída: 2
contarLivrosAluno("Maria")  # Saída: 1
contarLivrosAluno("Pedro")  # Saída: 0