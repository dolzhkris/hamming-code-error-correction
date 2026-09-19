def encode(data):
    d = list(map(int, data))
    p1 = d[0] ^ d[1] ^ d[3] ^ d[4] ^ d[6]
    p2 = d[0] ^ d[2] ^ d[3] ^ d[5] ^ d[6]
    p4 = d[1] ^ d[2] ^ d[3] ^ d[7]
    p8 = d[4] ^ d[5] ^ d[6] ^ d[7]
    code = [p1, p2, d[0], p4, d[1], d[2], d[3], p8, d[4], d[5], d[6], d[7]]
    return ''.join(map(str, code))

def decode(code):
    e = list(map(int, code))
    s1 = e[0] ^ e[2] ^ e[4] ^ e[6] ^ e[8] ^ e[10]
    s2 = e[1] ^ e[2] ^ e[5] ^ e[6] ^ e[9] ^ e[10]
    s4 = e[3] ^ e[4] ^ e[5] ^ e[6] ^ e[11]
    s8 = e[7] ^ e[8] ^ e[9] ^ e[10] ^ e[11]
    error = s1 + s2 * 2 + s4 * 4 + s8 * 8
    if error != 0:
        e[error - 1] ^= 1
    data = [e[2], e[4], e[5], e[6], e[8], e[9], e[10], e[11]]
    return ''.join(map(str, e)), ''.join(map(str, data)), error

def encode_rashirenniy(data):
    code12 = encode(data)
    bits = list(map(int, code12))
    bit_chetnosti = 0
    for bit in bits:
        bit_chetnosti ^= bit
    return code12 + str(bit_chetnosti)

def check_rashirenniy(code):
    e = list(map(int, code))
    main = e[:12]
    bit_chetnosti = e[12]
    s1 = main[0] ^ main[2] ^ main[4] ^ main[6] ^ main[8] ^ main[10]
    s2 = main[1] ^ main[2] ^ main[5] ^ main[6] ^ main[9] ^ main[10]
    s4 = main[3] ^ main[4] ^ main[5] ^ main[6] ^ main[11]
    s8 = main[7] ^ main[8] ^ main[9] ^ main[10] ^ main[11]
    error = s1 + s2 * 2 + s4 * 4 + s8 * 8
    total = 0
    for bit in e:
        total ^= bit
    if error == 0 and total == 0:
        status = "Ошибок нет"
    elif error != 0 and total == 1:
        main[error - 1] ^= 1
        status = f"Исправлена одиночная ошибка в позиции {error}"
    elif error == 0 and total == 1:
        bit_chetnosti ^= 1
        status = "Ошибка в бите общей четности"
    else:
        status = "Обнаружена двухкратная ошибка"
    fixed_code = ''.join(map(str, main)) + str(bit_chetnosti)
    return fixed_code, status

def make_error(code, positions):
    code = list(code)
    for pos in positions:
        code[pos - 1] = '1' if code[pos - 1] == '0' else '0'
    return ''.join(code)

data = input("Введите 8 бит: ")

print("\nОбычный код Хэмминга")
code = encode(data)
print("Код:", code)

pos = int(input("Введите позицию ошибки (1-12): "))
code_with_error = make_error(code, [pos])
print("Код с ошибкой:", code_with_error)

fixed, decoded, error = decode(code_with_error)
print("Исправленный код:", fixed)
print("Декодированные данные:", decoded)

print("\nРасширенный код Хэмминга")
ext_code = encode_rashirenniy(data)
print("Код:", ext_code)

positions = input("Введите позиции ошибок через пробел: ").split()
positions = list(map(int, positions))
rashirenniy_with_error = make_error(ext_code, positions)
print("Код с ошибками:", rashirenniy_with_error)

fixed_rashirenniy, status = check_rashirenniy(rashirenniy_with_error)
print("Результат:", status)
print("Код после обработки:", fixed_rashirenniy)
