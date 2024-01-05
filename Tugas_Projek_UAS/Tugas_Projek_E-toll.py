# Project Python E-Toll

import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#buat object root 
root = ttk.Window(themename="vapor")


class ETolApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Pembayaran E-Toll")

        # Variable untuk menyimpan saldo
        self.saldo = tk.DoubleVar()
        self.saldo = 100000  # Saldo awal

        # Label "E-Toll"
        etoll_label = tk.Label(master, text="E-Toll", font=("Helvetica", 16, "bold"))
        etoll_label.pack()

        # Label saldo
        saldo_label = tk.Label(master, text="Saldo:")
        saldo_label.pack()

        # Entry saldo (hanya untuk menampilkan saldo, tidak bisa diubah langsung)
        saldo_entry = tk.Entry(master)
        saldo_entry.insert(0, self.saldo)
        saldo_entry.configure(state=READONLY)
        saldo_entry.pack()

        # Label transaksi
        transaksi_label = tk.Label(master, text="Jumlah Tol:")
        transaksi_label.pack()

        # Entry untuk memasukkan jumlah tol
        self.transaksi_entry = tk.Entry(master)
        self.transaksi_entry.pack()

        # Tombol untuk melakukan transaksi
        transaksi_button = tk.Button(master, text="Bayar Tol", command=self.bayar_tol)
        transaksi_button.pack()

    def bayar_tol(self):
        try:
            # Ambil jumlah tol dari entry
            jumlah_tol = float(self.transaksi_entry.get())

            # Periksa apakah saldo cukup
            if jumlah_tol > self.saldo:
                messagebox.showwarning("Saldo tidak mencukupi", "Saldo tidak mencukupi untuk membayar tol.")
            else:
                # Kurangi saldo
                self.saldo = self.saldo - jumlah_tol
                messagebox.showinfo("Pembayaran Tol", f"Pembayaran tol sebesar {jumlah_tol} berhasil.")

        except ValueError:
            messagebox.showerror("Error", "Masukkan jumlah tol dengan benar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ETolApp(root)
    root.mainloop()
