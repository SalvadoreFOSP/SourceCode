# import os
# os.system('clear')

# def quickSort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0] 

#         print(f"Pivot : {pivot}")
        
#         less = [x for x in arr[1:] if x <= pivot]

#         greater = [x for x in arr[1:] if x > pivot]
    
#         return quickSort(less) + [pivot] + quickSort(greater)
    
# arr = [11, 9, 0, 2, 4, 5]

# result = quickSort(arr)

# print(result)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data): # Untuk Menambah List Barang
        if self.head is None:
            self.head = Node(data)
        else:
            node_baru = Node(data)
            node_baru.next = self.head
            self.head = node_baru

    def hapus(self): # Untuk Menghapus List Barang
        if self.head is None:
            print("List Tas Kosong")
        else:
            self.head = self.head.next
  
    def tampilkan(self, page_size): 
        if not self.head: # Jika Tidak Ada Daftar Tas
            print("Data Tas Kosong")
            return
        
        count = 0
        daftar = self.head
        nomor = 1

        while daftar:
            count += 1
            # Awal Halaman
            if count % page_size == 1: 
                print("\nPage", (count-1)//page_size+1)
                print("-"*20)
            
            print(f"{nomor}. {daftar.data}")
            
            # Akhir Halaman
            if count % page_size == 0: 
                input("Tekan Enter untuk Lanjut...")
                
            daftar = daftar.next
            nomor += 1
        
        input("Daftar Akhir. Tekan Enter Untuk Kembali...")

    def tampil(self):
        if self.head is None:
            print("Linked List Kosong")
        else:
            n = self.head
            nomor = 1

            while n is not None:
                print(f"{nomor}. {n.data}")
                n = n.next
                nomor += 1

List_Tas = LinkedList()
List = []

# Untuk Menambah daftar list
List_Tas.tambah("Hermes Birkin")
List_Tas.tambah("Prada Galleria Bag")
List_Tas.tambah("Dior Lady Dior Bag")
List_Tas.tambah("Celine Luggage Tote")
List_Tas.tambah("Balenciaga City Bag")
List_Tas.tambah("Burberry Banner")
List_Tas.tambah("Hilde Palladino Gadino")
List_Tas.tambah("Hermes Himalaya Birkin Bag")
List_Tas.tambah("Chanel Grand Shopping Tote")

current = List_Tas.head
while current is not None:
    List.append(current.data)
    current = current.next

# ========================================================================================================================== #
# ================================================== MENU ADMIN ============================================================ #
# ========================================================================================================================== #

def show_tas():
    List_Tas.tampilkan(page_size = 4)
    menu_admin()

def add_tas():
    add = input("Masukkan Nama Tas: ")
    List_Tas.tambah(add)
    print(f"{add} Telah Ditambahkan")
    menu_admin()
    return

def del_tas():
    delete = input("Masukkan Nama Tas Yang Ingin Dihapus: ")
    List_Tas.hapus(delete)
    return

def edit_tas():
    delete = input("Masukkan Nama Tas Yang Ingin Dihapus: ")
    List_Tas.hapus(delete)
    add = input("Masukkan Nama Tas: ")
    List_Tas.tambah(add)
    print(f"{add} Telah Ditambahkan")
    return

def search(List, x):
    n = len(List)
    
    jump = int(n ** 0.5)
    
    left, right = 0, 0
    while right < n and List[right] <= x:
        left = right
        right += jump
    
    for i in range(left, min(right, n)):
        if List[i] == x:
            return True
    
    cari = input("Masukkan Nama Tas Yang Ingin Dicari: ")
    if search(List, cari) == True:
        print(f"{cari} Ada di Dalam List")
    else:
        print(f"{cari} Tidak Ada di Dalam List ")
    menu_admin()

def merge_sort(arr, ascending=True):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left, ascending)
    right = merge_sort(right, ascending)

    return merge(left, right, ascending)

def merge(left, right, ascending=True):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (left[i] < right[j] and ascending) or (left[i] > right[j] and not ascending):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

def menu_admin():
        print()
        print('='*5,"Menu Admin",'='*5)
        print('1.) Tampilkan Barang')
        print('2.) Tambah Barang')
        print('3.) Edit Barang')
        print('4.) Hapus Barang')
        print('5.) Search Barang')
        print('6.) Sorting Barang')
        print('0.) Kembali')  

        pilihan = input('Pilih Menu: ')
        if pilihan == "1" :
            show_tas()
        elif pilihan == "2" :
            add_tas()
        elif pilihan == "3" :
            edit_tas()
        elif pilihan == "4" :
            del_tas()
        elif pilihan == "5":
            cari = input("Masukkan Nama Tas Yang Ingin Dicari: ")
            if cari in List:
                print(f"{cari} Ada di Dalam List")
            else:
                print(f"{cari} Tidak Ada di Dalam List ")
            menu_admin()
        elif pilihan == "6":
            print("1.) Ascending")
            print("2.) Descending")
            sort = input("Pilih Urutan Sorting: ")
            if sort == "1":
                sorted_arr_ascending = merge_sort(List)
                for i, elem in enumerate(sorted_arr_ascending):
                    print(f"{i+1}. {elem}")
                menu_admin()
            elif sort == "2":
                sorted_arr_descending = merge_sort(List, False)
                for i, elem in enumerate(sorted_arr_descending):
                    print(f"{i+1}. {elem}")
                menu_admin()
            else:
                print()
                print('='*5,"Pilihan Tidak Ada",'='*5,)
                menu_admin()
        elif pilihan == "0" :
            print()
            menu_awal()
        else :
            print()
            print('='*5,'Pilihan tidak tersedia','='*5)
            menu_admin()


# ========================================================================================================================== #
# ================================================== MENU USER ============================================================= #
# ========================================================================================================================== #

def menu_user():
    print()
    print("1.) Pemesanan")
    print("0.) Kembali")
    milih = input('Pilih Menu: ')
    if milih == "1":
        pesan()
    elif milih == "0":
        print()
        menu_awal()
    else:
        print()
        print('='*5,'Menu Tidak Ada','='*5)
        menu_user()

def pesan():
    print()
    print('='*5,"List Tas",'='*5)
    List_Tas.tampil()
    print()
    pesan_tas = input("Masukkan Nama Tas Yang Ingin Dipesan: ")
    jumlah = int(input("Jumlah Pesanan: "))
    harga = jumlah * 100000
    print()
    print("Pesanan =", pesan_tas)
    print("Jumlah Pesanan =", jumlah)
    print("Total Harga =", harga)
    print()
    invoice = input("Cetak Invoice(y/t)? : ")
    while True:
        if invoice == "y":
            filenya = "invoice PA.txt"
            f = open(filenya, "w")
            d = {
                "Nama Tas" :  pesan_tas,
                "Harga" : "Rp 100000",
                "Jumlah Pesanan" : jumlah,
                "Total Harga" : harga
            }
            for k, v, in d.items():
                f.write(str(k) + " = " + str(v) + "\n")
            
            f.close()
            print()
            print('='*5,"Invoice Anda Sudah Dicetak",'='*5)
            menu_user()
            break
        elif invoice == "t":
            print()
            print('='*5,"Terimakasih Sudah Memesan",'='*5)
            menu_user()
            break 

# ========================================================================================================================== #
# =================================================== MENU LOG IN ========================================================== #
# ========================================================================================================================== #

def user_login():
    print()
    user = input("Masukkan Username: ")
    pass_user = input("Masukkan Password: ")
    if user == "user" and pass_user == "user":
        print()
        print('='*5,"Log In Berhasil",'='*5)
        menu_user()
    else:
        print('='*5,"Username atau Password Anda Salah",'='*5)
        print()
        menu_awal()

def admin_login():
    print()
    admin = input("Masukkan Username: ")
    pass_admin = input("Masukkan Password: ")
    if admin == "admin" and pass_admin == "admin":
        print()
        print('='*5,"Log In Berhasil",'='*5)
        menu_admin()
    else:
        print('='*5,"Username atau Password Anda Salah",'='*5)
        print()
        menu_awal()

# ========================================================================================================================== #
# ================================================== MENU AWAL ============================================================= #
# ========================================================================================================================== #

def menu_awal():
    print('='*62)
    print('='*10,"Selamat Datang di Toko Tas SERBA 100.000",'='*10)
    print('='*62)
    print("1.) Admin")
    print("2.) User")
    print('0.) Keluar')
    pilih = input("Pilih Menu: ")
    if pilih == "1":
        admin_login()
    elif pilih == "2":
        user_login()
    elif pilih == "0":
        print('='*40)
        print('Terima Kasih'.center(40))
        print('='*40)
    else:
        print('='*5,"Menu Tidak Ada",'='*5)
        print()
        menu_awal()

menu_awal()
# x_value = search(List, x)