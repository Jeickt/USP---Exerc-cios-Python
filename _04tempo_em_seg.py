tempo = input("Por favor, entre com o número de segundos que deseja converter: ")
temp = int(tempo)
dias = temp // 86400
temp2 = temp % 86400
horas = temp2 // 3600
temp3 = temp2 % 3600
minutos = temp3 // 60
segundos = temp3 % 60
print (dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")