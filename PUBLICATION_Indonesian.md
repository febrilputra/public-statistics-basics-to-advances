# Atribusi, penanganan sumber, dan publikasi

Materi pembelajaran ini terdiri atas penjelasan orisinal, contoh sintetis baru, latihan dan jawaban baru, serta gambar yang dihasilkan dari kode Python pendamping. Materi mengikuti urutan topik *The StatQuest Illustrated Guide to Statistics* karya Josh Starmer dan mengutip bacaan tersebut dalam setiap bab serta dalam [Referensi](Reference.md). Materi ini tidak mendistribusikan halaman, tangkapan layar, kartun, atau teks hasil ekstraksi buku sebagai isi pembelajaran.

PDF untuk belajar dan berkas bacaan hasil ekstraksi tetap berada dalam direktori `sources/` yang diabaikan Git. Ringkasan tugas privat tetap berada dalam direktori `plan/` yang diabaikan. Keduanya tidak diperlukan untuk menjalankan notebook. `.venv/`, checkpoint notebook, dan artefak QA lokal juga diabaikan. Pengecualian ini menjaga materi pendukung lokal agar tidak ikut dalam penambahan biasa ke Git; pengecualian tersebut tidak menghapus apa pun yang sudah dilacak.

## Riwayat Git yang ada memerlukan pemeriksaan tersendiri

PDF sumber lama masih berada dalam commit Git yang sudah ada di repositori ini, meskipun tidak ada jalur PDF yang dilacak dalam indeks saat ini pada pemeriksaan akhir. Membuat berkas pembelajaran baru atau mengabaikan `sources/` tidak menghapus PDF lama tersebut dari commit, branch, tag, atau repositori remote yang sudah ada. Penghapusan berkas tersebut dari direktori kerja yang telah dilakukan sebelumnya dipertahankan.

Sebelum menjadikan repositori privat sebagai publik, periksa perubahan yang belum disimpan dalam commit dan riwayatnya. Perintah berikut hanya membaca keadaan repositori:

```bash
git status --short
git diff --name-status
git ls-files '*.pdf'
git log --all --name-only --format=oneline -- '*.pdf'
```

Jika berkas sumber berhak cipta terdapat dalam commit yang akan menjadi publik, selesaikan persoalan distribusinya sebelum publikasi. Bergantung pada riwayat yang diinginkan, pilihannya mencakup menyiapkan repositori bersih yang hanya berisi materi pembelajaran orisinal, atau secara sengaja menghapus berkas dari riwayat terkait dengan koordinasi dan cadangan yang sesuai. Commit penghapusan saja tetap membuat versi terdahulu tersedia. Tidak ada penulisan ulang riwayat, commit, atau push yang dilakukan saat menyiapkan catatan ini.

## Atribusi dan penggunaan kembali

Atribusi mengidentifikasi sumber gagasan dan mengarahkan pembaca kepada penulis. Atribusi sendiri bukan izin untuk mendistribusikan kembali materi yang dilindungi atau jaminan bahwa persoalan hukumnya telah tuntas. Pengecualian penggunaan wajar dan pengecualian sejenis bergantung pada keadaan serta yurisdiksi; [panduan U.S. Copyright Office](https://www.copyright.gov/help/faq/faq-fairuse.html) menjelaskan hal ini untuk hukum Amerika Serikat. Pembaca sebaiknya memperoleh buku sumber dari [halaman resmi penulis](https://statquest.org/statquest-store/).

Belum ada lisensi penggunaan kembali untuk seluruh repositori yang dipilih atas nama pemilik. Sebelum mengundang orang lain menggunakan kembali materi ini, pilih lisensi yang sesuai untuk materi yang berhak Anda lisensikan, dengan membedakan teks dan gambar dari kode bila diinginkan. Karya dan perangkat lunak pihak ketiga tetap mengikuti ketentuannya masing-masing. Membuat repositori terlihat secara publik tidak dengan sendirinya memberikan lisensi penggunaan kembali untuk isinya.

Untuk kontribusi mendatang, tulis penjelasan dengan kata-kata sendiri, susun contoh baru, buat gambar atau gunakan gambar dengan lisensi yang sesuai, catat sumber, dan simpan materi bacaan privat di luar materi publik. Mengganti nama atau angka dalam kutipan yang disalin bukan pengganti yang memadai bagi penulisan orisinal.
