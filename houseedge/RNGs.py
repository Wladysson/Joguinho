class LinearCongruentialGenerator:
    def __init__(self, seed, a, c, m):
        self.state = seed  # estado inicial
        self.a = a  # multiplicador
        self.c = c  # incremento
        self.m = m  # módulo

    def next(self):
        # Aplicando a fórmula do LCG
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

class RandomNumberGenerator:
    def __init__(self, seed, a, c, m):
        self.lcg = LinearCongruentialGenerator(seed, a, c, m)

    def next_float(self):
        # Retorna um número entre 0 e 1
        return self.lcg.next() / float(self.lcg.m)  # Dividir por float para garantir precisão

# Parâmetros do LCG
seed = 123456
a = 1664525
c = 1013904223
m = 2**32  # módulo comum para geradores LCG

# Exemplo de uso do RNG
rng = RandomNumberGenerator(seed, a, c, m)

# Gerando 10 números aleatórios entre 0 e 1
for _ in range(10):
    print(rng.next_float())