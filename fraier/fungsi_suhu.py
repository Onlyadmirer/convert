def suhu(satuan1, satuan2, nilai):

    if satuan1 == 'c' and satuan2 == 'f':
        return f"{(nilai * 9/5) + 32:.2f}"
    elif satuan1 == 'c' and satuan2 == 'k':
        return f"{(nilai + 273.15):.2f}"
    elif satuan1 == 'c' and satuan2 == 'r':
        return f"{(nilai * 4/5):.2f}"
    elif satuan1 == 'f' and satuan2 == 'c':
        return f"{((nilai * 5/9) + 32):.2f}"
    elif satuan1 == 'f' and satuan2 == 'k':
        return f"{(nilai - 32) * 5/9 + 273.15}"
    elif satuan1 == 'f' and satuan2 == 'r':
        return f"{(nilai * 4/9 - 32):.2f}"
    elif satuan1 == 'k' and satuan2 == 'c':
        return (nilai - 273.15)
    elif satuan1 == 'k' and satuan2 == 'f':
        return f"{((nilai - 273.15) * 9/5 + 32):.2f}"
    elif satuan1 == 'k' and satuan2 == 'r':
        return f"{(nilai * 4/5 - 273.15):.2f}"
    elif satuan1 == 'r' and satuan2 == 'c':
        return f"{(nilai * 5/4):.2f}"
    elif satuan1 == 'r' and satuan2 == 'f':
        return f"{(nilai * 9/4 + 32):.2f}"
    elif satuan1 == 'r' and satuan2 == 'k':
        return f"{(nilai * 5/4 + 273.15):.2f}"
    