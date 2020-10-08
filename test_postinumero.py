import urllib.request
import json

JSON_URL = 'https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json'


def hae_postinumerot():
    with urllib.request.urlopen(JSON_URL) as response:
        return json.loads(response.read())


postinumerot = hae_postinumerot()


def user_input():
    etsittava = input('Kirjoita postitoimipaikka: ').strip().upper()
    return etsittava


def luo_lista():

    toimipaikat_ja_numerot = {}

    for numero, toimipaikka in postinumerot.items():
        if toimipaikka in toimipaikat_ja_numerot:
            toimipaikat_ja_numerot[toimipaikka].append(numero)
        else:
            toimipaikat_ja_numerot[toimipaikka] = [numero]

    return toimipaikat_ja_numerot


toimipaikat_ja_numerot = luo_lista()


def etsi(etsittava, toimipaikat_ja_numerot):

    if etsittava in toimipaikat_ja_numerot:
        loydetyt = toimipaikat_ja_numerot[etsittava]
        return loydetyt
    else:
        return False


def test_etsi_nolla():

    etsittava = 'MUTALA'

    loydetut = etsi(etsittava, toimipaikat_ja_numerot)

    assert loydetut == True


def test_etsi_yksi():

    etsittava = 'MUTALA'

    loydetut = etsi(etsittava, toimipaikat_ja_numerot)

    assert len(loydetut) == 1


def test_etsi_monta():

    etsittava = 'HELSINKI'

    loydetut = etsi(etsittava, toimipaikat_ja_numerot)

    assert len(loydetut) > 1


def tulostus(loydetyt):
    if loydetyt == False:
        print('Postitoimipaikkaa ei löytynyt :(')
    else:
        print('Postinumerot: ' + ', '.join(loydetyt))


def main():

    etsittava = user_input()

    loydetyt = etsi(etsittava, toimipaikat_ja_numerot)

    tulostus(loydetyt)


if __name__ == '__main__':
    main()
