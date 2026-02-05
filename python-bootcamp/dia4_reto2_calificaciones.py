# ===================================
# RETO 2: Sistema de Calificaciones Avanzado
# ===================================

# Sistema con 5 rangos:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Variables de prueba
estudiante1_nota = 95
estudiante2_nota = 67
estudiante3_nota = 88
estudiante4_nota = 45

print("=== RESULTADOS DE CALIFICACIONES ===")


# Estudiante 1
print(f"\nEstudiante 1 - Nota: {estudiante1_nota}")
if estudiante1_nota >= 90:
    print("Calificación: A")
elif estudiante1_nota >= 80:
    print("Calificación: B")
elif estudiante1_nota >= 70:
    print("Calificación: C")
elif estudiante1_nota >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")

# Estudiante 2
print(f"\nEstudiante 2 - Nota: {estudiante2_nota}")
if estudiante2_nota >= 90:
    print("Calificación: A")
elif estudiante2_nota >= 80:
    print("Calificación: B")
elif estudiante2_nota >= 70:
    print("Calificación: C")
elif estudiante2_nota >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")

# Estudiante 3
print(f"\nEstudiante 3 - Nota: {estudiante3_nota}")
if estudiante3_nota >= 90:
    print("Calificación: A")
elif estudiante3_nota >= 80:
    print("Calificación: B")
elif estudiante3_nota >= 70:
    print("Calificación: C")
elif estudiante3_nota >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")
# Estudiante 4
print(f"\nEstudiante 4 - Nota: {estudiante4_nota}")
if estudiante4_nota >= 90:
    print("Calificación: A")
elif estudiante4_nota >= 80:
    print("Calificación: B")
elif estudiante4_nota >= 70:
    print("Calificación: C")
elif estudiante4_nota >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")

# BONUS: Calcula el promedio de las notas y su calificación
notas = [estudiante1_nota, estudiante2_nota, estudiante3_nota, estudiante4_nota]
promedio_notas = sum(notas) / len(notas)
print(f"Promedio de notas: {promedio_notas:.2f}")

# Calificación del promedio
if promedio_notas >= 90:
    print("Calificación del promedio: A")
elif promedio_notas >= 80:
    print("Calificación del promedio: B")
elif promedio_notas >= 70:
    print("Calificación del promedio: C")
elif promedio_notas >= 60:
    print("Calificación del promedio: D")
else:
    print("Calificación del promedio: F")