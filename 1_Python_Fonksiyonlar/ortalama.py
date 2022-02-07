def harfnot(vize1, vize2, final):
    ortalama = (vize1 * 0.3 + vize2 * 0.3 + final * 0.4),
    if ortalama >= 90:
        print('AA'),
    elif ortalama >= 85:
        print('BA'),
    elif ortalama >= 80:
        print('BB'),
    elif ortalama >= 75:
        print('CB'),
    elif ortalama >= 70:
        print('CC'),
    elif ortalama >= 65:
        print('DC'),
    elif ortalama >= 60:
        print('DD'),
    elif ortalama >= 55:
        print('FD'),
    else:
        print('FF')
