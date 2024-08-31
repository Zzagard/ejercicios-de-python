fecha_nacimiento = input("Cuál es tu fecha de nacimiento? (dd/mm/aaaa): ")

dia, mes, year = fecha_nacimiento.split('/')

print(f"Día: {dia.zfill(2)}")
print(f"Mes: {mes.zfill(2)}")
print(f"Año: {year}")
