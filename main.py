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