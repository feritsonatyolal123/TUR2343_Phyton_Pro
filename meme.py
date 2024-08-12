meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "Bir şakaya karşılık cevap",
            "SHEESH": "Onaylamamak",
            "CREEPY": "Korkunç",
            "AGGRO": "Agresifleşmek/Sinirlenmek",
            "GOAT": "En iyisi",
            "TROLL": "İnternette insanları öfkeli yapan kışkırtma",
            "SHOOK": "Şok olmak",
            "CAP": "Yalan",
            "RANDOM": "Rasgele şeyler, rasgele yazmak"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
    k = input("Bunla İlgili Bir Kelime Yaz")
    print("Kafadan Sallamadın dimi :)")
else:
    print("Lütfen Doğru Yazınız Bide Büyük Harflerle")
