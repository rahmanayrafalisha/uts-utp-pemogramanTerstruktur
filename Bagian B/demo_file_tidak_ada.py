# demo_file_tidak_ada.py
#membuktikan pesan jika file data belum ada
from inventaris_pkg.fileio import FileHandler

print(FileHandler("tidak_ada.csv").baca_semua_produk())
