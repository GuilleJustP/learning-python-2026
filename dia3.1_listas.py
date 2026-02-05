# Lista de numeros
numeros = [10, 20, 30, 40, 50]
print(f"Lista completa: {numeros}")
print(f"Primer elemento: {numeros[0]}")
print(f"Último elemento: {numeros[-1]}")

# Operaciones con listas
numeros.append(60) # Agregar al final
print(f"Después de append: {numeros}")
numeros.remove(20) # Eliminar un elemento
print(f"Después de remove: {numeros}")

# Lista de strings
paises = ["Bolivia", "USA", "Canada", "Indonesia"]
for pais in paises:
    print(f"Vivire en: {pais}")

# Ejercicio: Crea lista de tus materias del MIcroBachelor
materias = ["Probabilidad", "Estadistica", "Métodos Numéricos"]
for materia in materias:
    print(f"Estudio: {materia}")
    # DESAFÍO 1: Lista de números del 1 al 10
numeros = list(range(1, 11))
print(f"Números del 1 al 10: {numeros}")

# DESAFÍO 2: Imprime solo números pares
print("\nNúmeros pares:")
for num in numeros:
    if num % 2 == 0:
        print(num)

# DESAFÍO 3: Calcula suma de todos los números
suma_total = sum(numeros)
print(f"\nSuma total: {suma_total}")

# DESAFÍO 4: Encuentra el número más grande
mas_grande = max(numeros)
print(f"Número más grande: {mas_grande}")

# DESAFÍO 5 (BONUS): Lista de tus horas de estudio por día
horas_estudio = [1.5, 2, 1, 0, 2.5, 3, 1.5]
print(f"\nHoras esta semana: {horas_estudio}")
print(f"Total horas: {sum(horas_estudio)}")
print(f"Promedio diario: {sum(horas_estudio) / len(horas_estudio):.2f}")