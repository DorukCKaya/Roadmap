def sayiAtama(x):
    try:
        if (x >= 100) or (x < 10) or (type(x) != type(1)):
            raise ValueError('Verilen sayı 2 basamaklı olmalıdır.')
    except Exception as ex:
        raise ex
    okunus = sayiOkunusu(x)
    print(okunus)


def sayiOkunusu(x):
    onlar = int(x // 10)
    birler = int(x % 10)
    onlar_mapping = ['on', 'yirmi', 'otuz', 'kırk', 'elli', 'altmış', 'yetmiş', 'seksen', 'doksan']
    birler_mapping = ['bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz']
    okunus = f'{onlar_mapping[onlar - 1]} {birler_mapping[birler - 1]}'
    return okunus


sayiAtama(95)
