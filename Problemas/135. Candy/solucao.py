class Solution:
    def candy(self, ratings: list[int]) -> int:
        criancas = len(ratings)
        # Cada criança recebe pelo menos uma bala
        doces = [1] * criancas  

        # Passagem da esquerda para a direita
        for i in range(1, criancas):
            if ratings[i] > ratings[i - 1]:
                doces[i] = doces[i - 1] + 1

        # Passagem da direita para a esquerda
        for i in range(criancas - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                doces[i] = max(doces[i], doces[i + 1] + 1)

        return sum(doces)
