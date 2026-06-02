import matplotlib.pyplot as plt
def graficar_metricas(tiempos, cantidades, id_participante):
    
    # Gráfico 1 - Tiempos de uso
    plt.figure(1)
    plt.bar(range(len(tiempos)), tiempos, color="blue")
    plt.title(f"Tiempos de uso - Participante {id_participante}")
    plt.xlabel("Registro")
    plt.ylabel("Tiempo (minutos)")

    # Gráfico 2 - Cantidades de uso
    plt.figure(2)
    plt.bar(range(len(cantidades)), cantidades, color="green")
    plt.title(f"Cantidades de uso - Participante {id_participante}")
    plt.xlabel("Registro")
    plt.ylabel("Cantidad")

    plt.show()

