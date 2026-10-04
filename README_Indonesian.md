# Statistika: dari intuisi menuju analisis yang dapat direproduksi

Materi pembelajaran orisinal yang dapat dijalankan tentang dasar statistika, estimasi, pengujian hipotesis, dan model linier. Setiap bab mengembangkan pertanyaan dengan bahasa sederhana, menyatakan model formal, membahas contoh numerik kecil, dan menggunakan Python untuk menyelidiki apa yang terjadi ketika pengambilan sampel diulang.

Urutan pembelajaran mengikuti topik dalam *The StatQuest Illustrated Guide to Statistics* karya Josh Starmer. Ini adalah catatan belajar independen dengan penjelasan, kumpulan data, latihan, dan gambar baru yang dihasilkan secara terprogram. Catatan ini bukan sumber resmi StatQuest. Lihat [Referensi](Reference.md) untuk atribusi dan [Catatan publikasi](PUBLICATION.md) untuk pertimbangan berkas sumber dan lisensi.

## Mulai di sini

Baca [00 · Pendahuluan](00_Intro/00_Intro.md), lalu lanjutkan sesuai urutan bab. Gunakan [AA · Prasyarat](AA_Prerequisite/AA_Prerequisite.md) ketika perlu mengingat kembali notasi, kalkulus, probabilitas, atau array Python. Aritmetika dasar sudah cukup untuk memulai. Penurunan rumus regresi menggunakan aljabar; lampiran mengembangkan kalkulus dan notasi matriks.

Untuk setiap bab:

1. Baca gambaran umum dan ikuti contoh yang dibahas dengan menghitung secara manual.
2. Buka notebook, mulai ulang kernelnya, dan jalankan seluruh sel dari atas ke bawah.
3. Ubah besar efek, ukuran sampel, atau asumsi, lalu prediksi hasilnya sebelum menjalankan ulang.
4. Kerjakan soal latihan sebelum membaca pembahasan jawaban.

Materi ini mencakup hingga regresi berganda, perencanaan daya uji, pengujian berganda, ANOVA, dan ANCOVA. Materi ini membangun dasar untuk studi lanjutan; pembahasan menyeluruh tentang deret waktu, pemodelan Bayesian, identifikasi kausal, model multilevel, atau model linier tergeneralisasi berada di luar cakupannya.

## Peta pembelajaran

| Bab | Pertanyaan dan eksperimen utama | Catatan | Notebook yang sudah dijalankan |
|---|---|---|---|
| 00 · Pendahuluan | Pertanyaan, estimand, rancangan, dan variasi pengambilan sampel | [Baca](00_Intro/00_Intro.md) | [Jalankan](00_Intro/00_Intro.ipynb) |
| 01 · Dasar-dasar | Populasi dan sampel, varians, SD dan SE, ketakbiasan | [Baca](01_Fundamental_Concepts_in_Statistics/01_Fundamental_Concepts_in_Statistics.md) | [Jalankan](01_Fundamental_Concepts_in_Statistics/01_Fundamental_Concepts_in_Statistics.ipynb) |
| 02 · Histogram | Frekuensi, probabilitas, kepadatan, lebar kelas, ECDF | [Baca](02_Histogram/02_Histogram.md) | [Jalankan](02_Histogram/02_Histogram.ipynb) |
| 03 · Model probabilitas | PMF, PDF, CDF, distribusi umum, likelihood | [Baca](03_Probability_Models/03_Probability_Models.md) | [Jalankan](03_Probability_Models/03_Probability_Models.ipynb) |
| 04 · Pengujian hipotesis | Model nol, pengacakan eksak, kesalahan, aturan keputusan | [Baca](04_Hypothesis_Testing/04_Hypothesis_Testing.md) | [Jalankan](04_Hypothesis_Testing/04_Hypothesis_Testing.ipynb) |
| 05 · Nilai p dan interval | Konvensi ekor, kalibrasi, cakupan interval kepercayaan | [Baca](05_P-Values_for_Confidence_Quantification/05_P-Values_for_Confidence_Quantification.md) | [Jalankan](05_P-Values_for_Confidence_Quantification/05_P-Values_for_Confidence_Quantification.ipynb) |
| 06 · Regresi linier | Kuadrat terkecil, inferensi, interval prediksi, diagnostik | [Baca](06_Linear_Regression/06_Linear_Regression.md) | [Jalankan](06_Linear_Regression/06_Linear_Regression.ipynb) |
| 07 · Regresi berganda | Efek bersyarat, indikator, interaksi, overfitting | [Baca](07_Multiple_Regression/07_Multiple_Regression.md) | [Jalankan](07_Multiple_Regression/07_Multiple_Regression.ipynb) |
| 08 · Uji t | Satu sampel, Welch, gabungan, berpasangan, kesetaraan regresi | [Baca](08_T-test_for_Testing_the_Differences/08_T-test_for_Testing_the_Differences.md) | [Jalankan](08_T-test_for_Testing_the_Differences/08_T-test_for_Testing_the_Differences.ipynb) |
| 09 · Daya uji | t nonsentral, ukuran sampel, sensitivitas, simulasi | [Baca](09_Power_and_Power_Analysis/09_Power_and_Power_Analysis.md) | [Jalankan](09_Power_and_Power_Analysis/09_Power_and_Power_Analysis.ipynb) |
| 10 · Kekeliruan nilai p | FWER dan FDR, Holm, BH, seleksi, penghentian opsional | [Baca](10_P-Values_Pitfalls/10_P-Values_Pitfalls.md) | [Jalankan](10_P-Values_Pitfalls/10_P-Values_Pitfalls.ipynb) |
| 11 · ANOVA dan ANCOVA | Dekomposisi, kontras, perbandingan tersesuaikan, interaksi | [Baca](11_Anova_and_Ancova/11_Anova_and_Ancova.md) | [Jalankan](11_Anova_and_Ancova/11_Anova_and_Ancova.ipynb) |
| AA · Prasyarat | Probabilitas, Bayes, CLT, turunan, OLS, array | [Baca](AA_Prerequisite/AA_Prerequisite.md) | [Jalankan](AA_Prerequisite/AA_Prerequisite.ipynb) |

Setiap bab memuat gambaran umum Mermaid, contoh orisinal, asumsi eksplisit, latihan, dan pembahasan jawaban. Notebook memuat seluruh teks bab dengan kode yang disisipkan di antaranya. Kode yang sama menyimpan setiap gambar sebagai PNG untuk catatan dan SVG agar tetap tajam saat diperbesar. PDF buku, kumpulan data eksternal, akun, kunci API, atau akses jaringan tidak diperlukan untuk menjalankan materi setelah dependensi terpasang.

## Jalankan secara lokal

Lingkungan yang divalidasi menggunakan Python 3.12.14; pasang Python 3.12 dan dependensi dengan versi yang ditetapkan dalam [requirements.txt](requirements.txt). Dari direktori utama repositori pada Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --user --name statistics-course --display-name "Statistics course (.venv)"
.\.venv\Scripts\python.exe -m jupyterlab
```

Pada macOS atau Linux:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m ipykernel install --user --name statistics-course --display-name "Statistics course (.venv)"
.venv/bin/python -m jupyterlab
```

Buka `<folder_name>.ipynb` suatu bab dan pilih **Statistics course (.venv)** sebagai kernelnya. Jupyter dapat dimulai dari direktori utama repositori atau direktori bab; sel penyiapan menemukan direktori utama secara otomatis. Pertahankan struktur direktori. Notebook yang sudah dijalankan dan PNG juga dapat dibaca tanpa memasang Python.

GitHub menampilkan diagram Mermaid dalam Markdown. Beberapa penampil notebook menampilkan kode sumbernya; setiap bab juga menjelaskan alurnya dalam teks. Persamaan LaTeX menggunakan pembatas matematika Markdown standar. Tautan gambar bersifat relatif terhadap folder bab.

Seluruh data bersifat sintetis dan dipilih untuk pembelajaran. Estimasi simulasi berfluktuasi di sekitar nilai teoretis; generator dengan seed membuat setiap eksperimen dapat direproduksi dalam lingkungan yang ditetapkan. Perbedaan kecil dalam bilangan titik mengambang dan tampilan antarplatform dapat terjadi.

## Bangun ulang dan verifikasi

Berkas yang ditulis sebagai sumber adalah `<folder_name>.md` setiap bab dan [sumber eksperimen Python](scripts/labs) yang terkait. Penanda seperti `<!-- lab: least_squares -->` menempatkan sel kode bernama dari `scripts/labs/06.py` setelah penjelasan yang relevan. Ini menjaga catatan dan notebook tetap sinkron.

Setelah mengubah teks atau eksperimen, bangun ulang dan jalankan:

```powershell
.\.venv\Scripts\python.exe scripts/build_notebooks.py
.\.venv\Scripts\python.exe scripts/validate_course.py --execute
```

Ganti jalur Python dengan `.venv/bin/python` pada macOS atau Linux. Untuk penyuntingan terbatas, kedua skrip menerima awalan bab:

```powershell
.\.venv\Scripts\python.exe scripts/build_notebooks.py --chapter 06
.\.venv\Scripts\python.exe scripts/validate_course.py --execute --chapter 06
```

Proses pembangunan menimpa notebook yang dihasilkan dan menghapus keluaran sebelumnya. Jalankan setelahnya untuk memulihkan keluaran dan membuat ulang gambar. Buat perubahan permanen pada Markdown dan sumber eksperimen, bukan hanya pada notebook yang dihasilkan. Menjalankan notebook secara interaktif juga membuat ulang gambar bab tersebut.

Validator memeriksa struktur notebook, sel yang telah dijalankan, kesalahan, sinkronisasi dengan catatan, tautan lokal, dan berkas gambar. Sel eksperimen juga memeriksa hasil ilmiah penting: probabilitas eksak, rumus varians, identitas regresi, kesesuaian dengan pustaka, perhitungan ukuran sampel, dan kesesuaian simulasi bila relevan. `--execute` menjalankan setiap notebook dalam kernel baru yang terpisah menggunakan lingkungan Python pemanggil. Tanpanya, validasi memeriksa keluaran dan berkas yang tersimpan. CI membangun ulang dan menjalankan materi yang sama pada Python 3.12.

## Konvensi statistik

- Nilai p adalah probabilitas ekor berdasarkan model nol tertentu, bukan probabilitas bahwa hipotesis nol benar.
- Tingkat kepercayaan menggambarkan cakupan dalam pengambilan sampel berulang; besar efek dan interval menyertai keputusan.
- SD menggambarkan variasi pengamatan; SE menggambarkan variasi suatu estimator.
- Tinggi kepadatan bukan probabilitas; probabilitas adalah massa atau luas.
- Kontribusi likelihood pengamatan independen dikalikan, dan kontribusi log-likelihood dijumlahkan.
- Inferensi, prediksi, dan kausalitas menjawab pertanyaan berbeda. Asumsi dan rancangan studi penting bagi masing-masing.
- Perbandingan model menggunakan pengamatan yang sama, jumlah parameter yang eksplisit, dan asumsi varians yang sesuai.

Catatan menjelaskan kapan rumus sampel berhingga bersifat eksak, kapan pendekatan digunakan, dan kapan analisis memperluas bacaan utama. Perlakukan contoh yang sengaja dibuat kecil sebagai kesempatan memahami perhitungan, bukan sebagai bukti untuk mengambil keputusan tentang sistem nyata.
