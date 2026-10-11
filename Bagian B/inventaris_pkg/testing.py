# testing.py
import os
import tempfile
import unittest

from inventaris_pkg.fileio import FileHandler
from inventaris_pkg.processing import Produk, OlahInventaris
from inventaris_pkg.validasi import NilaiNegatifError, DataKosongError


class TestInventaris(unittest.TestCase):
    def setUp(self):
        self.p1 = Produk("E01", "Laptop", 8000000, 5, kategori="Elektronik")
        self.p2 = Produk("E02", "Mouse", 100000, 2, kategori="Aksesoris")
        self.olah = OlahInventaris([self.p1, self.p2])

    def test_total_nilai(self):
        self.assertEqual(self.olah.hitung_total_nilai(), 40200000)

    def test_filter_stok_kritis(self):
        self.assertEqual(len(self.olah.filter_stok_kritis(batas=3)), 1)

    def test_urutan_termahal(self):
        self.assertEqual(self.olah.urutkan_termahal()[0].nama, "Laptop")

    def test_stok_per_kategori_args(self):
        self.assertEqual(self.olah.hitung_stok_kategori("Elektronik"), 5)
        self.assertEqual(self.olah.hitung_stok_kategori("Elektronik", "Aksesoris"), 7)
        self.assertEqual(self.olah.hitung_stok_kategori(), 7)

    def test_nilai_negatif(self):
        with self.assertRaises(NilaiNegatifError):
            Produk("E03", "Keyboard", -50000, 5)

    def test_nama_kosong(self):
        with self.assertRaises(DataKosongError):
            Produk("E04", "", 50000, 5)

    def test_stok_bukan_bulat_assert(self):
        with self.assertRaises(AssertionError):
            Produk("E05", "Kabel", 1000, 2.5)

    def test_baris_rusak_dilewati(self):
        isi = ("kode;nama;harga;stok;kategori\n"
               "E01;Laptop;8000000;5;Elektronik\n"
               "E02;Mouse;abc;2;Aksesoris\n"
               "E03;Kabel;-5000;3;Aksesoris\n"
               ";Tanpa;1000;1;Umum\n")
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "uji.csv")
            with open(path, "w", encoding="utf-8") as f:
                f.write(isi)
            hasil = FileHandler(path).baca_semua_produk()
        self.assertEqual(len(hasil), 1)

    def test_mode_x_tidak_menimpa(self):
        with tempfile.TemporaryDirectory() as folder:
            handler = FileHandler(os.path.join(folder, "baru.csv"))
            self.assertTrue(handler.inisialisasi_file())
            self.assertFalse(handler.inisialisasi_file())


if __name__ == "__main__":
    unittest.main()
