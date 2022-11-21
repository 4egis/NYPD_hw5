def create_code_dicts(code):
    code_dict = {code[i]: code[i+1] for i in range(0, len(code), 2)}
    inv_code_dict = {v: k for k, v in code_dict.items()}
    return code_dict, inv_code_dict


def check_code(code):
    if len(code) != len(set(code)):
        return False
    return True


def select_code():
    print('Wybierz z jakiego szyfru chcesz korzystac:')
    print('1. GADERYPOLUKI')
    print('2. POLITYKARENU')
    print('3. chce podac wlasny')
    answ = int(input('1/2/3?: '))

    if answ == 1:
        return create_code_dicts('GADERYPOLUKI')
    elif answ == 2:
        return create_code_dicts('POLITYKARENU')
    elif answ == 3:
        code = input('Podaj wlasny kod. Nie uzywaj spacji, ani myslnikow. Np. GADERYPOLUKI: \n')

        if check_code(code):
            return create_code_dicts(code)
        else:
            print('Niepoprawny kod, czy chcialbys wybrac ponownie?')
            if input('T/N?: ') == 'T':
                return select_code()
            else:
                exit()
    exit()


def szyfruj(tekst):
    tekst = tekst.upper()
    code_dict, inv_code_dict = select_code()
    zaszyfrowany = ''

    for l in tekst:
        if l in code_dict:
            zaszyfrowany += code_dict[l]
        elif l in inv_code_dict:
            zaszyfrowany += inv_code_dict[l]
        else:
            zaszyfrowany += l
    return zaszyfrowany


print(szyfruj("GUG MG IPTG"))