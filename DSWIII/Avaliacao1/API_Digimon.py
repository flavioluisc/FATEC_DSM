import requests
import deepl

auth_key = "dd0e1e92-46a9-4936-a520-55ccbf580226:fx"
translator = deepl.Translator(auth_key)

def tradutor(texto):
    return translator.translate_text(texto, target_lang="PT-BR").text

def get_digimon(nome):
    URL = f"https://digi-api.com/api/v1/digimon/{nome}"
    req = requests.get(URL)
    if req.status_code == 200:
        return req.json()
    else:
        return None

while True:
    digimon = input("Digite o nome do Digimon: ")
    resultado = get_digimon(digimon)

    if resultado:
        print("\nNome: " + resultado['name'])
        print("\nTipo: " + tradutor(resultado["types"][0].get('type')))
        print("\nAtributos: " + tradutor(resultado["attributes"][0].get('attribute')))
        campos = [tradutor(attr.get('field')) for attr in resultado["fields"]]
        print("\nCampos: " + ", ".join(campos))
        evolucoes = [attr.get('digimon') for attr in resultado["priorEvolutions"]]
        print("\nEvoluções: " + ", ".join(evolucoes))
        print("\nDescrição: " + tradutor(resultado["descriptions"][1].get('description')))
        break
    else:
        print("Digimon não encontrado. Por favor, tente novamente.")
