var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# Metode Jump Search
def jumpSearch(var, x,):
    n = len(var)

    # Menentukan ukuran jump
    jump = int(n ** 0.5)

    # Menentukan indeks awal dan akhir
    left, right = 0, 0

    while right < n and var[right] <= x:
        left = right
        right += jump

    # Melakukan pencarian linear
    for i in range(left, min(right, n)):
        if var[i] == x:
            return i
    for kolom in range(len(var[i])):
        if (var[i][kolom] == x):
            return i
        
    # Jika tidak ditemukan
    return -1

# Mencari data pada list
print("1. Arsel di Index", jumpSearch(var, "Arsel"))
print("   Avivah di Index", jumpSearch(var, "Avivah"))
print("   Daiva di Index", jumpSearch(var, "Daiva"))
print("2. Wahyu di Index", jumpSearch(var, "Wahyu"), "pada kolom 0")
print("3. Wibi di Index", jumpSearch(var, "Wibi"), "pada kolom 1")