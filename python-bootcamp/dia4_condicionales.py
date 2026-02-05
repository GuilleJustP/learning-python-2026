# PARTE 1: Ejemplo básico de calificaciones
print("=== SISTEMA DE CALIFICACIONES ===")
nota = 85

if nota >= 90:
    print("Excelente - A")
elif nota >= 80:
    print("Muy bien - B")
elif nota >= 70:
    print("Bien - C")
else:
    print("Necesitas mejorar")

# PARTE 2: Tracker de horas de estudio semanal
print("\n=== TRACKER DE HORAS SEMANALES ===")
horas_estudio = 9

if horas_estudio >= 15:
    print("¡Vas excelente esta semana!")
elif horas_estudio >= 10:
    print("Buen progreso, sigue así")
else:
    print("Necesitas dedicar más tiempo")

# PARTE 3: Calculadora de IMC simple
print("\n=== CALCULADORA DE IMC ===")
peso = 65  # kg (cámbialo por tu peso real si quieres)
altura = 1.70  # metros (cámbialo por tu altura)

imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Categoría: Bajo peso")
elif imc < 25:
    print("Categoría: Peso normal")
elif imc < 30:
    print("Categoría: Sobrepeso")
else:
    print("Categoría: Obesidad")
