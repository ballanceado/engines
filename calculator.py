# one of the first coding python call to the success
# calculator & job-workers
# developed by :: killabomb

#input-workers
nome = str(input('Qual seu nome? '))
primeiro_input = float(input(f'{nome}, digite um número: '))
segundo_input = float(input(f'{nome}, digite outro número: '))

#engine-workers
soma = primeiro_input + segundo_input
sub = primeiro_input - segundo_input
mult = primeiro_input * segundo_input
div = primeiro_input // segundo_input
div_resto = primeiro_input % segundo_input

#output-workers and #format-methods
print(f'********* \n {nome}, estes são os resultados obtidos utilizando os números: {primeiro_input} e {segundo_input}')

#condition-input-workers
#working when result is 1
if soma == 1:print('\n O Resultado é 1 na Soma')
if sub == 1:print('\n O Resultado é 1 na Subtração')
if mult == 1:print('\n O Resultado é 1 na Multiplicação')
if div == 1:print('\n O Resultado é 1 na Divisão')
if div_resto == 1:print('\n O Resultado é 1 no resto da Divisão')

#output-workers and #format-methods
print(f'. \n SOMA: {primeiro_input} + {segundo_input} = {soma}')
print(f'. \n SUBTRAÇÃO: {primeiro_input} - {segundo_input} = {sub}')
print(f'. \n MULTIPLICAÇÃO: {primeiro_input} * {segundo_input} = {mult}')
print(f'. \n DIVISÃO: {primeiro_input} / {segundo_input} = {div}')
print(f'. \n Números que sobraram da divisão: {primeiro_input} / {segundo_input} = {div_resto}')

#end-of-code
