from random import randint

núm = (
        randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
)
print(f'Sua tupla: [{núm}]')
print(f'O maior valor da tupla é {max(núm)}\nE o menor valor é {min(núm)}')
