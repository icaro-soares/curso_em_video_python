"""Pergunta a temperatura em graus Celsius e converte para Farenheit"""
celsius = float(input('Digite a temperatura: Cº '))
farenheit = (celsius * 9/5) + 32
print(f'Sua temperatura convertida é {farenheit:.1f}Fº')
