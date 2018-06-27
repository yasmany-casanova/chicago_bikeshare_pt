# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\nTAREFA 1: Imprimindo as primeiras 20 amostras")

number_rows = data_list[1:21]
for row in number_rows:
    print(row)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

for row in number_rows:
    gender = row[-2]
    print(gender)

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")

def column_to_list(data: list, index: int):
    """ Função para criar uma lista a partir da coluna

    Argumentos:
    data: list. dados usados para extrair a coluna
    index: int. a coluna que será usada para criar a lista

    Retorna:
    Uma lista com a coluna informada
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for row in data:
        column_list.append(row[index])

    return column_list

print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")

male = female = 0
for row in data_list:
    gender = str.lower(row[-2])
    if gender == 'male':
        male += 1
    elif gender == 'female':
        female += 1

# Verificando o resultado
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
print("\nTAREFA 5: Imprimindo o resultado de count_gender")

def count_gender(data_list: list):
    """ Função para contar os gêneros

    Argumentos:
    data_list: list. dados usados para extrair a coluna

    Retorna:
    Uma lista com a quantidade de cada gênero
    """
    male = female = 0
    for row in data_list:
        gender = str.lower(row[-2])
        if gender == 'male':
            male += 1
        elif gender == 'female':
            female += 1
    return [male, female]

print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list: list):
    """ Função para buscar o gênero mais popular

    Argumentos:
    data_list: list. dados usados para extrair a coluna

    Retorna:
    Uma string com o gênero mais popular
    """
    answer = ""
    male, female = count_gender(data_list)

    if male > female:
        answer = 'Masculino'
    elif female > male:
        answer = 'Feminino'
    else:
        answer = 'Igual'

    return answer

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_user_types(data_list):
    """ Função para contar os tipos de usuários

    Argumentos:
    data_list: list. dados usados para extrair a coluna

    Retorna:
    Uma lista contendo a quantidade de usuários por tipo
    """
    customer = dependent = subscriber = 0
    for row in data_list:
        user_type = str.lower(row[-3])
        if user_type == 'customer':
            customer += 1
        elif user_type == 'dependent':
            dependent += 1
        elif user_type == 'subscriber':
            subscriber += 1
    return [customer, dependent, subscriber]

user_types_list = column_to_list(data_list, -3)
types = ["Customer", "Dependent", "Subscriber"]
quantity = count_user_types(data_list)

print(quantity)

y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "A quantidade de gender é inferior aos registros no arquivo, já que existem valores vazios na coluna gender."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")

trip_duration_list = column_to_list(data_list, 2)
item = lambda trip_duration: list(map(float, trip_duration))

def find_max(trip_duration_list: list):
    """ Função para localizar o maior valor na lista

    Argumentos:
    trip_duration_list: list. dados contendo o(s) valor(es) da viagem

    Retorna:
    Um float contendo o maior valor da viagem
    """
    data = item(trip_duration_list)
    data.sort()
    return data[-1]

def find_min(trip_duration_list: list):
    """ Função para localizar o menor valor na lista

    Argumentos:
    trip_duration_list: list. dados contendo o(s) valor(es) da viagem

    Retorna:
    Um float contendo o menor valor da viagem
    """
    data = item(trip_duration_list)
    data.sort()
    return data[0]

def find_mean_trip(trip_duration_list: list):
    """ Função para calcular a média

    Argumentos:
    trip_duration_list: list. dados contendo o(s) valor(es) da viagem

    Retorna:
    Um float contendo a média
    """
    data = item(trip_duration_list)
    data.sort()
    total = sum(data)
    return total / len(data)

def find_median_trip(trip_duration_list: list):
    """ Função para calcular a mediana

    Argumentos:
    trip_duration_list: list. dados contendo o(s) valor(es) da viagem

    Retorna:
    Um float contendo a mediana
    """
    data = item(trip_duration_list)
    data.sort()
    if len(data)%2 == 0:
        left_side = int(len(data)/2 - 1)
        right_side = int(len(data)/2)
        median_trip = float((int(data[left_side]) + int(data[right_side]))/2)
    else:
        middle = int(len(data)/2)
        median_trip = int(data[middle])
    return median_trip

min_trip = find_min(trip_duration_list)
max_trip = find_max(trip_duration_list)
mean_trip = find_mean_trip(trip_duration_list)
median_trip = find_median_trip(trip_duration_list)

print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
print("\nTAREFA 10: Imprimindo as start stations:")

user_types = set(column_to_list(data_list, 3))
print(len(user_types))
print(user_types)

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
""" Função de exemplo com anotações.
    Argumentos:
        param1: O primeiro parâmetro.
        param2: O segundo parâmetro.
    Retorna:
    Uma lista de valores x.
"""

# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list: list):
    """ Função para contar o valor numa determinada coluna

    Argumentos:
    column_list: list. dados contendo o(s) valor(es) numa determinada coluna

    Retorna:
    Os tipos e a quantidade
    """
    item_types = set(column_list)
    count_items = items = []
    for row in column_list:
        items.append(row)

    count_items = [len(items)]
    return item_types, count_items

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------