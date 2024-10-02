# Project Kelompok 8

   Project ini adalah sebuah unit converter.
   Unit converter adalah sebuah alat yang membantu mengubah satuan pengukuran yang berbeda untuk berbagai kuantitas fisik. Dalam kasus Project ini, unit converter dapat mengubah satuan untuk:

   1. **Kecepatan** (misalnya dari km/jam ke hm/jam)
   2. **Berat** (misalnya dari kilogram ke gram)
   3. **Suhu** (misalnya dari Celsius ke Fahrenheit)
   4. **Jarak** (misalnya dari kilometer ke meter)
   5. **Waktu** (misalnya dari jam ke menit)

   Tujuannya adalah untuk memudahkan pengguna dalam mengubah satuan pengukuran yang berbeda, sehingga menjadi alat yang berguna untuk kehidupan sehari-hari atau untuk aplikasi ilmiah dan teknik.

# Cara penggunaanya

   1. **Satuan Berat**
   
       Untuk mengkonversi berat, Anda dapat menggunakan fungsi 'berat' dari modul 'fraier'.
       Berikut adalah contoh cara penggunaannya:
       1. Import modul 'fraier'

          ```python
             import fraier
          ```
          
       2. Tentukan nilai berat yang ingin dikonversi,    
          serta satuan asli dan satuan yang akan dikonversi.
          Contoh:

          ```python
             from_unit = "g"  # satuan asli (gram)
             to_unit = "kg"  # satuan yang akan dikonversi (kilogram)
             nilai = 50  # nilai berat dalam gram yang akan dikonversi ke kilogram


             CATATAN:
             from_unit harus diisi string
             to_unit harus diisi string
             nilai harus diisi float/integer
          ```
          
       4. Panggil fungsi 'berat' dengan parameter 'from_unit', 'to_unit', dan 'nilai':

          ```python
             hasil = fraier.berat(from_unit, to_unit, nilai)
          ```
          
       5. Contoh lengkap:

          ```python
             import fraier

             hasil = fraier.berat("g", "kg", 50)
             print(hasil)

             Output:
             50 g adalah 0.05 kg
          ```

