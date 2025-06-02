import heapq

class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:

        # 1° ordenar os cursos pela data limite de conclusão em ordem crescente
        courses.sort(key=lambda x: x[1])
        # 2° cria uma heap para guardar os cursos e inicializar o tempo total em 0
        max_heap = []
        tempo_total = 0
        
        for duracao, limite in courses:
            # 3° Atualiza o tempo total e adiciona o curso
            tempo_total += duracao
            heapq.heappush(max_heap, -duracao)  # heap máximo com negativos

            # 4° caso o curso ultrapasse o prazo, remover o curso mais longo
            if tempo_total > limite:
                tempo_total += heapq.heappop(max_heap)  # como é guardado uma duração negativa, basta somar

        return len(max_heap)
