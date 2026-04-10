# List transaksi sederhana (hardcode)
transaksi = [
    {"id": 1, "produk": "Beras", "qty": 2, "harga": 10000},
    {"id": 2, "produk": "Minyak", "qty": 1, "harga": 15000},
    {"id": 3, "produk": "Gula", "qty": 3, "harga": 8000}
]

# Tampilkan transaksi
print("=== DATA TRANSAKSI ===")
for t in transaksi:
    total=t["qty"]*t["harga"]
    print(f"{t['produk']} | qty: {t['qty']} | total: {total}")

import json
import os

FILE_PATH = "database/transaksi.json"

# fungsi baca data
def load_data():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        return json.load(file)

# fungsi simpan data
def save_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

# tambah transaksi
def tambah_transaksi(produk, qty, harga):
    data = load_data()
    
    transaksi_baru = {
        "id": len(data) + 1,
        "produk": produk,
        "qty": qty,
        "harga": harga
    }
    
    data.append(transaksi_baru)
    save_data(data)

# tampilkan transaksi
def tampilkan_transaksi():
    data = load_data()
    print("\n=== DATA TRANSAKSI ===")
    for t in data:
        total = t["qty"] * t["harga"]
        print(f"{t['produk']} | Qty: {t['qty']} | Total: {total}")

# TEST
tambah_transaksi("Beras", 2, 10000)
tambah_transaksi("Minyak", 1, 15000)

tampilkan_transaksi()