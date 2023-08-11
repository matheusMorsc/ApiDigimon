import requests
# Função para fazer uma solicitação à API Digimon
def get_digimons(name=None, level=None):
    # Criar um objeto de requisição
    request = requests.get('https://digimon-api.vercel.app/api/digimon')

    # Verificar se a solicitação foi bem-sucedida
    if request.status_code == 200:
        # Obter o corpo da resposta
        response = request.json()

        # Filtrar os digimons pelo nome e/ou nível
        if name is not None:
            response = [digimon for digimon in response if digimon['name'] == name]
        if level is not None:
            response = [digimon for digimon in response if digimon['level'] == level]

        return response
    else:
        raise Exception('Erro ao fazer a solicitação à API Digimon')

# Fazer requisições continuamente até o usuário sair da aplicação
while True:
    # Solicitar ao usuário o que deseja fazer
    user_input = input('O que você deseja fazer?\n'
                         '1. Listar todos os digimons\n'
                         '2. Filtrar por nível\n'
                         '3. Filtrar por nome\n'
                         '4. Sair\n')

    # Executar a ação solicitada pelo usuário
    if user_input == '1':
        digimons = get_digimons()
        for digimon in digimons:
            print(digimon['name'], digimon['level'])
    elif user_input == '2':
        level = input('Digite o nível do digimon: ')
        digimons_level = get_digimons(level=level)
        for digimon in digimons_level:
            print(digimon['name'], digimon['level'])
    elif user_input == '3':
        digimon_name = input('Digite o nome do digimon: ')
        digimon_info = get_digimons(name=digimon_name)
        print(digimon_info)
    elif user_input == '4':
        break