import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Kalkulator(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("form_uts.ui", self)

        self.pushButton_hitung.clicked.connect(self.hitung)

    def hitung(self):
        try:
            panjang = float(self.panjang_2310010148.text())
            lebar = float(self.lebar_2310010148.text())
            tinggi = float(self.tinggi_2310010148.text())
            operasi = self.comboBox_operasi.currentText()

            if operasi == "Volume Balok":
                hasil = panjang * lebar * tinggi
                QMessageBox.information(self, "Hasil", f"Volume Balok: {hasil}")
            elif operasi == "Keliling Persegi Panjang":
                hasil = 2 * (panjang + lebar)
                QMessageBox.information(self, "Hasil", f"Keliling Persegi Panjang: {hasil}")
            else:
                QMessageBox.warning(self, "Peringatan", "Pilih operasi yang valid.")

        except ValueError:
            QMessageBox.critical(self, "Error", "Input tidak valid! Masukkan angka.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Kalkulator()
    window.show()
    sys.exit(app.exec_())
