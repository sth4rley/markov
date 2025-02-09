import collections, random, sys, textwrap

MAX_LINE_WIDTH: int = 80

w1: str = ""
w2: str = ""

# tabela de possibilidades, indexadas por pares de palavras
possibles: dict[tuple[str, str], list[str]] = collections.defaultdict(list)

# realiza a leitura do texto, linha por linha e palavra por palavra
for line in sys.stdin:
    for nw in line.split():
        possibles[w1, w2].append(nw)
        w1, w2 = w2, nw

# Adiciona uma string vazia para os casos em que a palavra não tem sucessora
possibles[w1, w2].append('')
possibles[w2, ''].append('')

# se não for encontrado um par de palavras iniciais, escolhe um aleatório
start_candidates = [k for k in possibles if k[0][:1].isupper()]
if not start_candidates:
    start_candidates = list(possibles.keys())
w1, w2 = random.choice(start_candidates)

# gera a cadeira de markov com o comprimento desejado
output: list[str] = [w1, w2]
length: int = int(sys.argv[1])

while length > 0:
    nw: str = random.choice(possibles[w1, w2])
    output.append(nw)
    w1, w2 = w2, nw
    length -= 1

# imprime o texto gerado
print(textwrap.fill(' '.join(output), width=MAX_LINE_WIDTH))
