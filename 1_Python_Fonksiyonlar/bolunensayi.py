def bolunensayibulma(min_sayi, max_sayi, bolunecek_sayi):
    bolunenler = []
    for i in range(min_sayi, max_sayi+1):
        if i % bolunecek_sayi == 0:
            bolunenler.append(i)
    return len(bolunenler),  bolunenler


bolunensayibulma(0, 49, 2)
