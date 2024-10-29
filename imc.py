def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC)"""
    return peso / (altura ** 2)

def clasificar_imc(imc):
    """Clasifica el IMC en diferentes categorías"""
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    print("Cálculo del Índice de Masa Corporal (IMC)")
    
    # Solicitar el peso al usuario
    peso = float(input("Introduce tu peso en kilogramos: "))
    
    # Solicitar la altura al usuario
    altura = float(input("Introduce tu altura en metros: "))
    
    # Calcular el IMC
    imc = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(imc)
    
    # Mostrar el resultado
    print(f"Tu IMC es: {imc:.2f}")
    print(f"Clasificación: {clasificacion}")

if __name__ == "__main__":
    main()