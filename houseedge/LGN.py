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

# Exemplo de uso
seed = 123456
a = 1664525
c = 1013904223
m = 2**32  # módulo comum para geradores LCG
lcg = LinearCongruentialGenerator(seed, a, c, m)

# Gerando 10 números pseudo-aleatórios
for _ in range(10):
    print(lcg.next())