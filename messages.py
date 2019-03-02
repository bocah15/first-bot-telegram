# message start handler
start = (
    "<b>Selamat Datang {first_name} di Layanan Informasi Program Studi Teknik Informatika</b>"
    + "\n\n" +
    "Silahkan registrasi untuk bisa mengakses layanan PSTI"
    + "\n\n\n" +
    "Jika telah melakukan registrasi pilih /home untuk melihat layanan yang tersedia"
)

# unknown command handler
unknown = (
    "<b>Maaf Permintaan anda tidak tersedia</b>\n"
    +
    "Silahkan Pilih Layanan Informasi yang disediakan : \n"
    +
    "/layananpkl - Informasi Praktek Kerja Lapangan"
    + "\n" +
    "/layananta - Informasi Terkait Tugas Akhir"
    + "\n" +
    "/tatatulis - Informasi Penulisan Laporan"
)

# message home handler
home = (
    "<b>Selamat Datang di Layanan Informasi Program Studi Teknik Informatika</b>"
    + "\n\n" +
    "Berikut beberapa pelayanan yang dapat diakses :"
    + "\n" +
    "/home - Main Message"
    + "\n" +
    "/layananpkl - Informasi Praktek Kerja Lapangan"
    + "\n" +
    "/layananta - Informasi Terkait Tugas Akhir"
    + "\n" +
    "/tatatulis - Informasi Penulisan Laporan"
)


# message Tata Tulis PKL
tatatulispkl = (
    "<b>Aturan Penulisan Laporan Praktek Kerja Lapangan</b>\n\n"
    +
    "<b>Font : </b>\n"
    + "- Judul (cover) : Times New Roman (14, <b>Bold</b>, Rata Tengah)\n"
    + "- Nama dan NIM (cover) : Times New Roman (12, <b>Bold</b>, Rata Tengah)\n"
    + "- Judul BAB : Times New Roman (14, <b>Bold</b>, Rata Tengah)\n"
    + "- Paragraf : Times New Roman (12)\n\n"
    +
    "<b>Space : </b> 1.5\n\n"
    +
    "<b>Margin : </b> \n"
    + "- Atas : 3 cm\n"
    + "- Bawah : 2.5 cm\n"
    + "- Kiri : 3.5 cm\n"
    + "- Kanan : 2.5 cm\n\n"
    +
    "Selengkapnya dapat dilihat di "
    + "<a href='https://drive.google.com/file/d/1s1D4ACYWuEUVtKr0jPIUBk5VLKL_9NIb/view?usp=sharing'>"
    + "Buku Pedoman </a>"
)

# message Tata Tulis TA
tatatulista = (
    "<b>Aturan Penulisan Laporan Tugas Akhir</b>\n\n"
    +
    "<b>Font : </b>\n"
    + "- Judul (cover) : Times New Roman (14, <b>Bold</b>, Rata Tengah)\n"
    + "- Nama dan NIM (cover) : Times New Roman (12, <b>Bold</b>, Rata Tengah)\n"
    + "- Judul BAB : Times New Roman (14, <b>Bold</b>, Rata Tengah)\n"
    + "- Paragraf : Times New Roman (12)\n\n"
    +
    "<b>Space : </b> 1.5\n\n"
    +
    "<b>Margin : </b> \n"
    + "- Atas : 3 cm\n"
    + "- Bawah : 2.5 cm\n"
    + "- Kiri : 3.5 cm\n"
    + "- Kanan : 2.5 cm\n\n"
    +
    "Selengkapnya dapat dilihat di "
    + "<a href='https://drive.google.com/file/d/1s1D4ACYWuEUVtKr0jPIUBk5VLKL_9NIb/view?usp=sharing'>"
    + "Buku Pedoman </a>"

)

# message Pendaftaran PKL
pendaftaranpkl = (
    "<b>Pendaftaran Praktek Kerja Lapangan : </b>\n\n"
    +
    "1. Pendaftaran dilakukan dengan mengisi "
    + "<a href='https://if.unram.ac.id/wp-content/uploads/2017/05/Blangko-Permohonan-PKLBaru.pdf'>"
    + "Form Permohonan dan Pendaftaran PKL</a>. Setelah itu diajukan ke Program Studi\n"
    +
    "2. Surat Balasan dari Program Studi diantarkan bersama dengan Lampiran "
    + "<a href='https://if.unram.ac.id/wp-content/uploads/2017/06/Lampiran-Daftar-Bidang-Pekerjaan-dan-Kompetensinya-untuk-PKL.pdf'>"
    + "Daftar Bidang Pekerjaan dan Kompetensi</a> ke Instansi Tempat PKL\n"
    +
    "3. Surat Balasan dari Instansi Tempat PKL diberikan ke Program\n"
    +
    "4. Memilih Dosen Pembimbing dengan mengisi "
    + "<a href='https://if.unram.ac.id/wp-content/uploads/2017/06/Blangko-Penunjukan-Dosen-Pembimbing-PKL.pdf'>"
    + "Formulir Penunjukan Dosen Pembimbing</a>\n"
    +
    "5. PKL dimulai sesuai dengan tanggal pada poin 4\n"
)

# message Seminar PKL
seminarpkl = (
    "<b>Permohonan Seminar Praktek Kerja Lapangan : </b>\n\n"
    +
    "1. Laporan telah diACC Dosen Pembimbing\n"
    +
    "2. Mengisi <a href='https://if.unram.ac.id/wp-content/uploads/2018/12/Blangko-Permohonan-Seminar-PKL.doc'>"
    + "Blanko Permohonan Seminar</a>\n"
    +
    "3. Konfirmasi Jadwal dan Ruang Seminar pada Staf Program Studi"
)

# message Pembukuan PKL
pembukuanpkl = (
    "<b>Pembukuan Laporan Praktek Kerja Lapangan : </b>\n\n"
    +
    "1. Laporan yang sudah diACC dibukukan dengan urutan : \n"
    + "Cover - Lembar Pengesahan - Kata Penghantar - Ucapan Terima Kasih - "
    + "Daftar Isi - Daftar Gambar - Daftar Tabel - Laporan - Lampiran "
    + "(Surat Tugas, Daftar Hadir, Tolopogi(jika ada))"
    +
    "2. Laporan dan Source Code atau Topologi diburn-ing dalam CD"
    +
    "3. Laporan yang sudah dibukukan dan CD dikumpulkan di staf Program Studi"
)

# message Pendaftaran TA1
pendaftaranta1 = (
    "<b>Pendaftaran Tugas Akhir 1 : </b>\n\n"
    +
    "1. Pendaftaran dilakukan dengan mengisi "
    + "<a href='https://if.unram.ac.id/wp-content/uploads/2018/05/Form-Persetujuan-Dosen-Pembimbing.doc'>"
    + "Form Persetujuan Dosen Pembimbing</a> Sekaligus pengajuan Judul\n"
    +
    "2. Tugas Akhir sudah bisa dikerjakan\n"
)

# message Seminar TA1
seminarta1 = (
    "<b>Permohonan Seminar Tugas Akhir 1 : </b>\n\n"
    +
    "1. Laporan telah diACC Dosen Pembimbing\n"
    +
    "2. Mengisi <a href='https://if.unram.ac.id/wp-content/uploads/2018/06/Form-Seminar-Proposal-TA-1-New.pdf'>"
    + "Form Permohonan Seminar TA1</a>\n"
    +
    "3. Konfirmasi ke Staf Program Studi"
    +
    "4. Tunggu pengumuman jadwal Seminar yang telah diajukan"
)

# message Pembukuan TA1
pembukuanta1 = (
    "Lanjut ke Tugas Akhir 2"
)

# message Pendaftaran TA2
pendaftaranta2 = (
    "<b>Pendaftaran Tugas Akhir 2 : </b>\n\n"
    +
    "1. Telah menyelesaikan Tugas Akhir 1\n"
    +
    "2. Membuat Paper yang sudah sampai Tahap Review di "
    + "<a href='https://jcosine.if.unram.ac.id/'>JCosine</a> atau JTIKA\n"
    +
    "3. Daftar Ujian dilakukan dengan mengisi "
    + "<a href='https://if.unram.ac.id/wp-content/uploads/2018/12/Form-Permohonan-Ujian-TA-2.pdf'>"
    + "Form Permohonan Ujian Tugas Akhir 2</a> dan diajukan ke Program Studi"
)

# message Seminar TA2
seminarta2 = (
    "<b>Permohonan Seminar Tugas Akhir 2 : </b>\n\n"
    +
    "1. Telah melakukan Pendaftaran Ujian Tugas Ahir 2\n"
    +
    "2. Menghadiri Seminar sesuai dengan jadwal yang sudah ditentukan\n"
)

# message Pembukuan TA2
pembukuanta2 = (
    "<b>Pembukuan Tugas Akhir 2 : </b>\n\n"
    +
    "1. Laporan yang sudah diACC dibukukan dengan urutan : \n"
    + "Cover - Lembar Pengesahan - Kata Penghantar - Ucapan Terima Kasih - "
    + "Daftar Isi - Daftar Gambar - Daftar Tabel - Laporan - Lampiran "
    + "(Surat Tugas, Daftar Hadir, Tolopogi(jika ada))"
    +
    "2. Laporan dan Source Code atau Topologi diburn-ing dalam CD"
    +
    "3. Laporan yang sudah dibukukan dan CD dikumpulkan di staf Program Studi"
)
