import unittest
from analisis_suhu import analisis_suhu, hitung_rata_rata


class TestSuhu(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"hari": "Senin", "suhu": 31.0},
            {"hari": "Selasa", "suhu": 33.0},
            {"hari": "Rabu", "suhu": 29.0},
            {"hari": "Kamis", "suhu": 35.0},
        ]

    def test_rata_rata(self):
        self.assertAlmostEqual(analisis_suhu(self.data)["rata_rata"], 32.0)

    def test_tertinggi_terendah(self):
        hasil = analisis_suhu(self.data)
        self.assertEqual(hasil["tertinggi"]["hari"], "Kamis")
        self.assertEqual(hasil["terendah"]["hari"], "Rabu")

    def test_jumlah_panas(self):
        self.assertEqual(analisis_suhu(self.data, batas_panas=32)["jumlah_panas"], 2)

    def test_suhu_tepat_batas_dianggap_panas(self):
        hasil = analisis_suhu([{"hari": "Jumat", "suhu": 32.0}])
        self.assertEqual(hasil["detail"][0]["kategori"], "Panas")

    def test_hitung_rata_rata_args(self):
        self.assertAlmostEqual(hitung_rata_rata(30, 32, 34), 32.0)


if __name__ == "__main__":
    unittest.main()
