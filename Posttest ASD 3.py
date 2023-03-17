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
            print("Linked List Kosong")
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
        
        input("Daftar Akhir. Tekan Enter Untuk Keluar...")


shoe_list = LinkedList()

# Untuk Menambah daftar list
shoe_list.tambah("Hermes Birkin")
shoe_list.tambah("Chanel Diamond Forever Classic Bag")
shoe_list.tambah("Lana Marks Cleopatra Bag")
shoe_list.tambah("Mouawad 1001 Nights Diamond Purse")
shoe_list.tambah("Louis Vuitton Urban Satchel Bag")
shoe_list.tambah("The Row Alligator Backpack")
shoe_list.tambah("Judith Leiber Precious Rose Bag")
shoe_list.tambah("Marc Jacobs Carolyn Crocodile Handbag")
shoe_list.tambah("Fendi Selleria Bag")
shoe_list.tambah("Debbie Wingham's Upcycled Easter Egg Purse")
shoe_list.tambah("Hermes Kelly Rose Gold")
shoe_list.tambah("Gucci Jackie Crocodile Shoulder Bag")
shoe_list.tambah("Bottega Veneta Knot Clutch")
shoe_list.tambah("Prada Galleria Bag")
shoe_list.tambah("Dior Lady Dior Bag")
shoe_list.tambah("Valentino Rockstud Spike Chain Bag")
shoe_list.tambah("Givenchy Antigona Soft Tote")
shoe_list.tambah("Celine Luggage Tote")
shoe_list.tambah("Chloe Drew Bijou Mini Shoulder Bag")
shoe_list.tambah("Saint Laurent Sac de Jour Tote")
shoe_list.tambah("Balenciaga City Bag")
shoe_list.tambah("Tom Ford Natalia Chain Crossbody Bag")
shoe_list.tambah("Alexander McQueen Skull Clutch Box Bag")
shoe_list.tambah("Loewe Puzzle Leather Shoulder Bag")
shoe_list.tambah("Burberry Banner")
shoe_list.tambah("Hilde Palladino Gadino")
shoe_list.tambah("Louis Vuitton Tribute Patchwork bag")
shoe_list.tambah("Judith Leiber Precious Rose Baguette")
shoe_list.tambah("Hermes Himalaya Birkin Bag")
shoe_list.tambah("Chanel Grand Shopping Tote")
shoe_list.hapus()

# Untuk mengatur daftar tas per halaman
shoe_list.tampilkan(page_size = 4)