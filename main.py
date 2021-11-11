print("Calculadora de IMC")
paciente = input("Digite o nome do paciente: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura**2)

if (imc <= 18.5):
  print("O paciente: ", paciente, " tem: Magreza")
elif (imc <= 18.5 <25):
  print("O paciente", paciente, " é: Normal")
elif(imc <= 25 < 30):
  print("O paciente: ", paciente,  " tem: Obesidade")
elif(imc <= 30 < 40):
  print("O paciente: ", paciente, " tem: OBESIDADE GRAVE")
else:
  print("Error do programa")