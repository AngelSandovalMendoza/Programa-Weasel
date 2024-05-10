import random
import string

# Función para generar una cadena aleatoria del mismo tamaño que el objetivo
def generar_aleatorio(longitud):
    return ''.join(random.choice(string.ascii_letters + ' ') for _ in range(longitud))

# Función para calcular la aptitud de una cadena en comparación con el objetivo
def calcular_aptitud(objetivo, prueba):
    return sum(1 for i in range(len(objetivo)) if objetivo[i] == prueba[i])

# Función para mutar una cadena
def mutar(cadena, tasa_mutacion):
    return ''.join(c if random.random() > tasa_mutacion else random.choice(string.ascii_letters + ' ') for c in cadena)

# Función principal del algoritmo de Weasel de Dawkins
def weasel_dawkins(objetivo, tamano_poblacion, tasa_mutacion):
    poblacion = [generar_aleatorio(len(objetivo)) for _ in range(tamano_poblacion)]
    generaciones = 0

    while True:
        generaciones += 1
        aptitudes = [(cadena, calcular_aptitud(objetivo, cadena)) for cadena in poblacion]
        mejor_candidato, mejor_aptitud = max(aptitudes, key=lambda x: x[1])

        print(f"Generación {generaciones}: {mejor_candidato} - Aptitud: {mejor_aptitud}/{len(objetivo)}")

        if mejor_aptitud == len(objetivo):
            return mejor_candidato, generaciones

        poblacion = [mutar(mejor_candidato, tasa_mutacion) for _ in range(tamano_poblacion)]

if __name__ == "__main__":
    objetivo = input("Ingrese la frase objetivo: ").upper().strip()
    tamano_poblacion = 100
    tasa_mutacion = 0.05

    mejor_candidato, generaciones = weasel_dawkins(objetivo, tamano_poblacion, tasa_mutacion)

    print("Generaciones requeridas:", generaciones)
    print("Mejor candidato encontrado:", mejor_candidato)
