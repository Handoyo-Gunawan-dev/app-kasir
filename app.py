import streamlit as st
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

st.title("App Kasir Sederhana")
st.subheader("Tambah Transaksi")


produk = st.text_input("Nama Produk")
qty = st.number_input("Qty", min_value=0,step=1)
harga = st.number_input("Harga",min_value=0, step=1000)
    

if st.button("Tambah"):
    if produk == "":
        st.warning("Produk tidak boleh kosong")
    else:
        tambah_transaksi(produk,qty,harga)
        st.success("Transaksi Berhasil Ditambahakan")
        

st.subheader("Data Transaksi")

if st.button("Reset Data"):
    save_data([])
    st.warning("Data Berhasil Dihapus")

data= load_data()

total_semua = 0

for t in data:
    total = t["qty"] * t["harga"]
    total_semua += total

    st.write(f"{t['produk']} | Qty: {t['qty']} | Total: {total}")

st.write("______")
st.write(f"Total Semua:{total_semua}")