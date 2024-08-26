# Código que varre arquivos .txt no mesmo diretório que está o codigo e faz as operações que estão nos arquivos
# Gustavo Lona Grespan
from pathlib import Path


# Função para formatar os conjuntos que serão imprimidos no terminal
def formatar(x):
    elementos = ', '.join(sorted(x))
    conjunto = '{' + elementos + '}'
    return conjunto


# Variável com o caminho do diretório que contém este código e os arquivos.txt
caminhoAtual = Path(__file__).parent

# Variável para armazenar os nomes dos arquivos
listaNomeArquivosTxt = []

# Armazena apenas os nomes dos arquivos.txt em 'listaNomeArquivosTxt'
for e1 in caminhoAtual.iterdir():  # Varre oque está no 'Path(__file__).parent'
    if e1.is_file() and e1.suffix == '.txt':  # Verifica se é arquivo e .txt
        listaNomeArquivosTxt.append(e1.name)

# Faz as operações dos arquivos.txt
for arquivoNome in listaNomeArquivosTxt:
    with open(arquivoNome, 'r') as file:
        quantidadeOperacao = int(file.readline().strip())
        while quantidadeOperacao >= 1:
            linhaTipo = file.readline().strip()
            linha1 = file.readline().strip().split(',')
            linha2 = file.readline().strip().split(',')
            linha1 = [item.strip() for item in linha1]
            linha2 = [item.strip() for item in linha2]

            if linhaTipo == 'U':
                # Set listas para conjunto.
                conjunto1 = set(linha1)
                conjunto2 = set(linha2)
                # Calcula a União.
                Uniao = conjunto1 | conjunto2
                print(f'União: conjunto 1 {formatar(conjunto1)}, conjunto 2 {formatar(conjunto2)}. Resultado: {formatar(Uniao)}')
            elif linhaTipo == 'I':
                # Set listas para conjunto.
                conjunto1 = set(linha1)
                conjunto2 = set(linha2)
                # Calcula a Interseção.
                Intersecao = conjunto1 & conjunto2
                print(f'Interseção: conjunto 1 {formatar(conjunto1)}, conjunto 2 {formatar(conjunto2)}. Resultado: {formatar(Intersecao)}')
            elif linhaTipo == 'D':
                # Set listas para conjunto.
                conjunto1 = set(linha1)
                conjunto2 = set(linha2)
                # Calcula a Diferença.
                Diferenca = conjunto1 ^ conjunto2
                print(f'Diferença: conjunto 1 {formatar(conjunto1)}, conjunto 2 {formatar(conjunto2)}. Resultado: {formatar(Diferenca)}')
            elif linhaTipo == 'C':
                conjunto1 = set(linha1)
                conjunto2 = set(linha2)
                Cartesiano = []
                # Calcula o Cartesiano.
                for e1 in conjunto1:
                    for e2 in conjunto2:
                        Cartesiano.append((e1, e2))
                # Gambiarra pra formatar corretamente o Cartesiano
                print(f'Cartesiano: conjunto 1 {formatar(conjunto1)}, conjunto 2 {formatar(conjunto2)}. Resultado: {{{", ".join(f"({e1},{e2})" for e1, e2 in Cartesiano)}}}')
            else:
                print('O tipo de operação', linhaTipo, 'não é U, I, D ou C.')
            quantidadeOperacao -= 1
