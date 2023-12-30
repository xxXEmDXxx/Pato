meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD":"una cara de risa",
            "CREEPY":"algo aterrador que da miedo",
            "BOOMER":"Persona que se aferra mucho al pasado",
            "PA":"para",
            "TROLlEAR": "hacer una broma"
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("no se encontro la palabra")
