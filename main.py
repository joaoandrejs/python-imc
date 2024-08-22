def calcImc(peso, altura):
  imc = peso / (pow(altura, 2))
  return imc

def infoImc(imc):
    if imc < 18.5:  
        print('Abaixo do peso')
    elif 18.5 <= imc < 24.9:
        print('Peso Normal')
    elif 25 <= imc < 29.9:
        print('Sobrepeso')
    elif 30 <= imc < 34.9:
        print('Obesidade Grau I')
    elif 35 <= imc < 39.9:
        print('Obesidade Grau II')
    else:
        print('Obesidade Grau III ou Mórbida')

def main():
  altura = float(input('Qual sua altura: (1.75) '))
  peso = float(input("Qual seu peso: (76.5) "))
  
  imc = calcImc(peso, altura)
  print(f"Seu IMC é: {imc:.2f}")
  
  infoImc(imc)

main();
