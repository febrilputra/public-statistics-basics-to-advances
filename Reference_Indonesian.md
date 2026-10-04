# Referensi dan kaitan bacaan

Materi ini menggunakan sumber di bawah untuk urutan pembelajaran, definisi statistik, konvensi inferensi, dan API perangkat lunak. Penjelasan, contoh, kumpulan data sintetis, latihan, kode, dan gambar yang dihasilkan ditulis untuk repositori ini. Buku sumber dan ilustrasinya bukan bagian dari distribusi materi pembelajaran. Referensi situs web diakses pada 4 Oktober 2026; versi perangkat lunak ditetapkan secara terpisah dalam [requirements.txt](requirements.txt).

## SQ: StatQuest

Starmer, Josh. (2026). *The StatQuest Illustrated Guide to Statistics*. StatQuest. Bacaan utama: edisi yang disediakan secara lokal, termasuk Bab 1–11 dan Lampiran A–F. [Halaman resmi penulis dan pembelian](https://statquest.org/statquest-store/).

Repositori mengikuti urutan topik tersebut, tetapi menggunakan teks, contoh, ilustrasi, dan kodenya sendiri. Repositori ini merupakan pendamping belajar independen dan tidak berafiliasi dengan atau didukung oleh StatQuest maupun Josh Starmer. PDF bacaan lokal tidak disertakan dalam materi yang didistribusikan.

| Bab repositori | Kaitan bacaan | Pengembangan tambahan dalam catatan ini |
|---|---|---|
| 00 | Bagian awal dan Bab 1 | Estimand, rancangan pengukuran, pengambilan sampel acak dibandingkan penempatan acak |
| 01 | Konsep dasar statistik | Penurunan varians tak bias, perbandingan Monte Carlo, populasi berhingga |
| 02 | Histogram dan probabilitas | Kelas kepadatan dengan lebar tidak sama, ECDF, ketidakpastian kejadian yang tidak teramati |
| 03 | Distribusi dan model | Perbedaan PMF/PDF/CDF, log-likelihood bersama, contoh diskret dan kontinu |
| 04 | Pengujian hipotesis dan hipotesis nol | Pengacakan eksak berdasarkan hipotesis nol tajam dan keterpertukaran |
| 05 | Nilai p | Kalibrasi diskret eksak, pemilihan arah, cakupan interval kepercayaan |
| 06 | Regresi linier | Asumsi eksplisit, interval kepercayaan dibandingkan interval prediksi, diagnostik residual |
| 07 | Regresi berganda | Rank matriks, interaksi, kolinearitas, kesalahan prediksi pada data yang disisihkan |
| 08 | Uji t | Rancangan Welch dan berpasangan, interval, kesetaraan dengan regresi varians gabungan |
| 09 | Daya uji dan analisis daya uji | Verifikasi t nonsentral, analisis sensitivitas, daya uji simulasi |
| 10 | Kekeliruan nilai p | FWER dibandingkan FDR, Holm dan BH, simulasi pemeriksaan berulang |
| 11 | ANOVA dan ANCOVA | Interval simultan, perbandingan model parsial, interaksi dan tumpang tindih |
| AA | Lampiran A–F | Aturan Bayes, kovarians, CLT, notasi matriks, Python yang dapat direproduksi |

Urutan referensi merupakan alat bantu belajar, bukan klaim bahwa setiap pengembangan terdapat dalam buku. Ketika intuisi sederhana memerlukan batasan, catatan menyatakan kondisi formal secara langsung, misalnya perkalian likelihood, interpretasi nilai p, dan uji varians sama dibandingkan uji Welch.

## Definisi, estimasi, dan model linier

NIST/SEMATECH. *e-Handbook of Statistical Methods*. National Institute of Standards and Technology. Bagian yang relevan:

- [Ukuran skala](https://www.itl.nist.gov/div898/handbook/eda/section3/eda356.htm): varians, simpangan baku, dan ukuran penyebaran lainnya; Bab 01.
- [Histogram](https://www.itl.nist.gov/div898/handbook/eda/section3/histogra.htm): eksplorasi distribusi; Bab 02.
- [Likelihood maksimum](https://www.itl.nist.gov/div898/handbook/apr/section4/apr412.htm): penyusunan dan estimasi likelihood; Bab 03.
- [Batas kepercayaan untuk rata-rata](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm): interval berbasis t; Bab 01, 05, dan 08.
- [Regresi linier kuadrat terkecil](https://www.itl.nist.gov/div898/handbook/pmd/section1/pmd141.htm): pencocokan dan interpretasi regresi; Bab 06, 07, dan AA.
- [Asumsi untuk uji statistik](https://www.itl.nist.gov/div898/handbook/pri/section2/pri245.htm): kondisi distribusi dan pemeriksaan residual; Bab 06–11.
- [Uji t dua sampel](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm): rumus varians gabungan dan varians tidak sama; Bab 08.
- [Analisis varians satu arah](https://www.itl.nist.gov/div898/handbook/eda/section3/eda354.htm): jumlah kuadrat, derajat kebebasan, dan uji F; Bab 11.

## Nilai p dan interpretasi

Wasserstein, R. L., & Lazar, N. A. (2016). The ASA's statement on p-values: Context, process, and purpose. *The American Statistician, 70*(2), 129–133. [DOI: 10.1080/00031305.2016.1154108](https://doi.org/10.1080/00031305.2016.1154108). American Statistical Association juga menyediakan [pernyataan dan ringkasan prinsipnya](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) yang dapat diakses.

Sumber ini mendasari Bab 04, 05, dan 10: interpretasi bergantung pada model dan proses analisis; signifikansi statistik tidak mengukur besar efek; kesimpulan tidak seharusnya hanya bergantung pada suatu ambang.

## Pengujian berganda

Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics, 6*(2), 65–70. [Publikasi asli](https://www.jstor.org/stable/4615733). Bab 10 mengimplementasikan penyesuaian bertahap menurun berdasarkan urutan dan memeriksanya terhadap statsmodels.

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B (Methodological), 57*(1), 289–300. [DOI: 10.1111/j.2517-6161.1995.tb02031.x](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x). Bab 10 mengembangkan tingkat penemuan palsu dan prosedur BH untuk uji independen, dengan simulasi yang mencatat proporsi penemuan palsu yang terealisasi dalam setiap keluarga pengujian.

Catatan membedakan kondisi independensi pada hasil BH asli dari pengembangan yang memerlukan kondisi ketergantungan tertentu. Korelasi saja tidak cukup untuk membenarkan penerapan jaminan yang didasarkan pada independensi.

## Dokumentasi perangkat lunak

Berikut adalah halaman dokumentasi utama untuk fungsi yang digunakan dalam notebook. Dokumentasi stabil dapat berkembang secara terpisah dari lingkungan dengan versi yang ditetapkan; eksperimen yang dapat dijalankan merupakan catatan pemanggilan yang benar-benar divalidasi di sini.

| Paket dan dokumentasi | Kegunaan |
|---|---|
| [NumPy histogram](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html) | Konvensi batas kelas dan normalisasi kepadatan |
| [NumPy least squares](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html) | Pencocokan matriks, rank, dan pemeriksaan koefisien |
| [Fungsi statistik SciPy](https://docs.scipy.org/doc/scipy/reference/stats.html) | Distribusi, kepadatan, kuantil, dan fungsi survival |
| [SciPy binomtest](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html) | Konvensi binomial eksak dua sisi |
| [SciPy permutation_test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.permutation_test.html) | Model nol berbasis pengambilan sampel ulang dan konvensinya |
| [SciPy ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html) | Uji sampel independen Welch dan varians gabungan |
| [SciPy ttest_rel](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html) | Perbandingan berpasangan |
| [SciPy noncentral t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nct.html) | Daya uji pada efek terstandarisasi yang tidak nol |
| [statsmodels TTestIndPower](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.html) | Perhitungan ukuran sampel dan daya uji |
| [statsmodels multipletests](https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html) | Bonferroni, Holm, BH, dan penyesuaian terkait |
| [statsmodels compare_f_test](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.RegressionResults.compare_f_test.html) | Perbandingan regresi tersarang |
| [statsmodels ANOVA](https://www.statsmodels.org/stable/generated/statsmodels.stats.anova.anova_lm.html) | Tabel ANOVA model linier |
| [statsmodels Tukey HSD](https://www.statsmodels.org/stable/generated/statsmodels.stats.multicomp.pairwise_tukeyhsd.html) | Perbandingan simultan semua pasangan |

## Penanganan sumber dan publikasi

U.S. Copyright Office. [Pertanyaan penggunaan wajar dan izin](https://www.copyright.gov/help/faq/faq-fairuse.html). Ini merupakan referensi umum untuk membedakan atribusi dan izin; sumber ini tidak memberikan kepastian izin hukum bagi repositori ini atau menentukan hukum negara mana yang berlaku. Lihat [Catatan publikasi](PUBLICATION.md) untuk keputusan konkret penanganan sumber dalam proyek ini.
