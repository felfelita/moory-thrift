# Link Deployment : 
http://felita-zahra-moorythrift2.pbp.cs.ui.ac.id/
# Cara mengimplementasikan checklist secara step-by-step
1. Buat direktori lokal:
- Membuat direktori bernama "moory-thrift" 
- Membuka direktori tersebut di terminal.
2. Mengaktifkan virtual environment untuk isolasi proyek. 
3, Membuat file .gitignore di dalam repositori untuk mengabaikan file-file yang tidak perlu dimasukkan dalam version control (seperti virtual environment, cache, dll.).
4. Setup proyek django dan buat proyek django bernama "moory-thrift" dengan menjalankan perintah " django-admin startproject moory_thrift . "
5. Membuat aplikasi bernama "main" di dalam proyek Django.
6. Melakukan konfigurasi aplikasi di settings.py dengan menambahkan aplikasi main ke dalam daftar INSTALLED_APPS.
7. Membuat direktori templates dan mengisi direktori tersebut dengan file main.html
8. Menambahkan atribut pada models.py/main (name, price, description, condition).
9. Perubahan pada model harus dimigrasi dengan menjalankan perintah 
python3 manage.py makemigrations
python3 manage.py migrate
10. Pada views.py saya menggunakan "from django.shortcuts import render" agar dapat mengimpor fungsi render. Fungsi render akan digunakan untuk render tampilan HTML.
11. Menggunakan Impor path dari django.urls agar pola URL dpaat terdefinisi. Lalu saya juga menggunakan fungsi show_main dari modul main.views sebagai tampilan URL terkait saat diakses. Pola nama unik URL juga dibentuk dari app_name.
12. Melakukan deployment pada PWS dengan create new project dengan nama "moorythrift2" lalu menambahkan URL deployment PWS pada ALLOWED_HOSTS.

# Bagan request client ke web aplikasi berbasis Django beserta responnya
![Bagan](https://github.com/user-attachments/assets/f4809100-35fa-4189-b02e-7df78dbcec55)

# Fungsi git dalam pengembangan perangkat lunak
Git berperan penting dalam pengembangan perangkat lunak, terutama dalam hal kontrol versi dan kolaborasi tim. Beberapa fungsi Git antara lain :
1. Melacak perubahan 
Git mencatat setiap perubahan yang dilakukan pada source code, sehingga pengembang dapat melihat riwayat perubahan dan memulihkan versi sebelumnya jika diperlukan.
2.  Kolaborasi tim
Git memfasilitasi kerja tim dengan memungkinkan banyak orang bekerja pada proyek yang sama tanpa khawatir akan merusak kode atau mencampurnya. Hal ini memungkinkan pengembang untuk bekerja secara bersama-sama pada kode sumber tanpa saling mengganggu
3. Backup kode 
Jika terjadi kegagalan sistem atau data hilang, maka Git dapat dengan mudah mengembalikan ke versi sebelumnya. Hal ini memungkinkan pengembang untuk memulihkan kode sumber dari repositori

# Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak
Django cocok bagi pemula karena memiliki dokumentasi yang lengkap dan mudah dipahami sehingga memudahkan proses belajar. Django juga memudahkan user dengan menyediakan banyak fitur bawaan. Framework ini menggunakan struktur pola MVT (Model-View-Template) yang membantu pengguna memahami dan mengorganisasi kode dengan lebih jelas. Selain itu, Django dibangun menggunakan bahasa pemrograman Python, yang sintaksisnya cukup sederhana dan mudah dipelajari, menjadikannya pilihan ideal bagi kami yang baru mulai belajar pengembangan perangkat lunak.

# Mengapa model pada Django disebut sebagai ORM
Model dalam Django disebut ORM (Object-Relational Mapping) karena ORM menghubungkan objek dalam kode dengan tabel di basis data relasional. Django ORM memungkinkan pengembang berinteraksi dengan basis data menggunakan objek Python, tanpa perlu menulis query SQL langsung. ORM meningkatkan keamanan dari serangan SQL Injection dan portabilitas serta membuat pengelolaan basis data lebih terstruktur dan intuitif, mengurangi kebutuhan untuk SQL.

# Tugas 3

# Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform
Data delivery sangat penting untuk memastikan informasi atau data dapat berpindah dari satu lokasi ke lokasi lain dengan efisien. Beberapa alasan mengapa implementasi pengiriman data sangat penting:

  - Perlindungan data: Pengiriman data yang efektif melibatkan enkripsi dan perlindungan selama proses transfer, sehingga keamanan data tetap terjaga.
  - Meningkatkan pengalaman pengguna: Pengiriman data yang baik menjamin pengalaman pengguna yang mulus, seperti menghindari buffering saat streaming.
  - Mengoptimalkan kinerja: Mekanisme pengiriman data yang efisien dapat meningkatkan performa dan efisiensi platform secara keseluruhan.

#  Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON (JavaScript Object Notation) lebih populer dan lebih baik daripada XML (Extensible Markup Language) karena memiliki struktur yang lebih sederhana, mudah dibaca, dan lebih ringan. Meskipun XML masih digunakan dalam beberapa konteks tertentu seperti dokumen yang kompleks, JSON menjadi pilihan utama dalam pengembangan aplikasi web dan mobile karena efisiensi dan kesederhanaannya.

#  Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() memiliki peran penting dalam memverifikasi bahwa data yang diterima dari form sudah valid, aman, dan sesuai dengan aturan yang telah ditetapkan. Validasi ini bertujuan untuk mencegah kesalahan serta menjaga keamanan aplikasi atau website dari potensi gangguan.

#  Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token berfungsi untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery dengan memverifikasi bahwa setiap permintaan yang mengubah data berasal dari sumber yang tepercaya. Tanpa csrf_token aplikasi lebih rentan dan berpotensi untuk diserang karena penyerang bisa mengeksploitasi sesi pengguna yang sah tanpa disadari oleh pengguna.

#  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. **Membuat forms.py:** Tambahkan file `forms.py` ke direktori `main` dan buat form yang didasarkan pada model `Product`.
2. **Implementasi fungsi create_thrift_entry di views.py:**
   - Import form yang sudah dibuat beserta `redirect`.
   - Tambahkan fungsi `create_thrift_entry` untuk memvalidasi input dan menyimpan data dari form tersebut.
   - Pada fungsi `show_main`, tambahkan `ThriftEntry.objects.all()` untuk mengambil semua data `Product` dari database dan kirimkan ke template melalui context.
3. **Routing URL:** Di `urls.py`, import fungsi `create_thrift_entry` dan tambahkan path untuk mengaksesnya.
4. **Template HTML (create_thrift_entry.html):** Buat file HTML di `main/templates` yang berisi form dengan metode POST, tambahkan {% csrf_token %}, serta tombol untuk submit.
5. **Fungsi untuk Mengembalikan Data dalam Format JSON dan XML:** Di `views.py`, buat empat fungsi: `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` untuk menampilkan data `Product` dalam format JSON dan XML.
6. **Routing untuk JSON dan XML:** Tambahkan path di `urls.py` untuk menampilkan data dalam format JSON dan XML.
7. **Push ke PWS dan GitHub:** Lakukan push perubahan ke repositori PWS dan GitHub.

# XML
<img width="1470" alt="Screen Shot 2024-09-18 at 08 55 49" src="https://github.com/user-attachments/assets/84a9ca7c-ca27-4e59-82a8-0772ce1f3ae9">

# XML by ID 
<img width="1470" alt="Screen Shot 2024-09-18 at 08 56 22" src="https://github.com/user-attachments/assets/0e6bed98-2671-49b2-a3d3-21de0ac68589">

# JSON
<img width="1470" alt="Screen Shot 2024-09-18 at 08 56 37" src="https://github.com/user-attachments/assets/85455625-52b4-4fdf-b376-2f9cb44e61ce">

# JSON by ID
<img width="1470" alt="Screen Shot 2024-09-18 at 08 56 47" src="https://github.com/user-attachments/assets/e63ae4c2-a5f4-4900-96c4-1a17e5d194ca">

# Tugas 4

# Apa perbedaan antara HttpResponseRedirect() dan redirect()
**HttpResponseRedirect()**:
Manual: Mengarahkan ke URL tertentu sehingga kita harus memberikan URL dalam bentuk string secara manual.
**redirect()**:
Shortcut: Lebih fleksibel. Kita bisa memasukkan URL, nama view, atau objek, dan redirect() otomatis menangani semuanya.

#  Jelaskan cara kerja penghubungan model Product dengan User!
Dalam Django, untuk menghubungkan model `Product` dengan `User`, Anda dapat menambahkan field `user` sebagai `ForeignKey` di dalam model `Product`, yang memungkinkan setiap produk terhubung ke satu pengguna (User), sementara seorang pengguna dapat memiliki banyak produk. Langkah-langkah implementasinya mencakup: mengimpor model `User` di `models.py`, menambahkan `ForeignKey` di model `Product`, dan memodifikasi fungsi `create_product` di `views.py` untuk menetapkan `product.user` ke `request.user`, sehingga produk terkait dengan pengguna yang membuatnya. Selain itu, fungsi `show_products` perlu diubah untuk menampilkan hanya produk yang dibuat oleh pengguna yang sedang login dengan memfilter query berdasarkan `request.user`. Setelah semua perubahan selesai, jalankan migrasi (`makemigrations` dan `migrate`) untuk memperbarui database. Terakhir, jalankan server untuk memastikan bahwa hanya produk milik pengguna yang login yang ditampilkan di aplikasi. Dengan cara ini, model `Product` akan terhubung otomatis dengan `User` menggunakan `ForeignKey`.

# Perbedaan Authentication dan Authorization dan cara Django mengimplementasinya
**Perbedaan Authentication dan Authorization:**

Authentication (Autentikasi): Verifikasi identitas pengguna, seperti login dengan username dan password.
Authorization (Otorisasi): Menentukan hak akses pengguna setelah mereka berhasil login.

**Yang Dilakukan Saat Pengguna Login:**

Authentication: Memeriksa kredensial (username dan password).
Authorization: Menentukan hak akses berdasarkan peran pengguna.

**Implementasi**
Dalam proses autentikasi di Django, saat pengguna login menggunakan authentication view, informasi yang mereka masukkan akan diperiksa apakah cocok dengan data yang ada. Jika verifikasi berhasil, Django akan membuat sesi user yang memungkinkan user mengakses sistem. Sedangkan untuk authorization, Django menggunakan permission classes dan decorators seperti `@login_required`, yang membatasi akses ke suatu *view* hanya bagi pengguna yang telah terautentikasi.

#  Cara Django mengingat pengguna yang telah login, kegunaan lain dari cookies dan keamanan cookies
Django menggunakan sesi untuk mengingat pengguna yang telah login. Setelah login berhasil, Django membuat sesi dan menyimpan identifier atau session ID sebagai cookie di browser pengguna.

**Pengelolaan Cookie**: Cookie memungkinkan Django mengenali pengguna yang kembali tanpa perlu login ulang, kecuali sesi telah berakhir atau pengguna melakukan logout. Selain otentikasi, cookie juga berguna untuk:

- **Melacak perilaku pengguna**: Cookie dapat menyimpan informasi seperti preferensi dan aktivitas pengguna selama sesi berlangsung.
- **Menyimpan pengaturan pengguna**: Seperti bahasa pilihan atau tema, sehingga pengalaman pengguna lebih dipersonalisasi.

**Keamanan Cookies:**

Tidak semua cookies aman, dan ada beberapa hal yang perlu diperhatikan:
Cookies Sesi: Cookies yang digunakan untuk menyimpan sesi biasanya lebih aman karena mereka hanya aktif selama sesi pengguna dan tidak memiliki masa berlaku yang panjang.
Secure Cookies: Cookies yang ditandai sebagai "Secure" hanya akan dikirim melalui HTTPS, membuatnya lebih aman dari serangan penyadapan.
HttpOnly Cookies: Cookies yang ditandai sebagai "HttpOnly" tidak dapat diakses melalui JavaScript, sehingga mengurangi risiko serangan XSS (Cross-Site Scripting).

**Risiko Cookies:**

Cookie Pencurian: Jika cookie tidak dikelola dengan benar, penyerang dapat mencuri cookie pengguna dan mendapatkan akses tidak sah.
Cookie Tidak Terlindungi: Cookies yang tidak menggunakan atribut Secure atau HttpOnly dapat lebih rentan terhadap serangan.

# Mengimplementasikan checklist secara step-by-step

**Membuat Formulir Pendaftaran:**
- Membuat fungsi `register` di views untuk menampilkan form pendaftaran akun baru.
- Menyiapkan file HTML agar pengguna dapat mendaftar dengan mengisi informasi yang diperlukan.
- Menambahkan path di file `urls.py` untuk menghubungkan fungsi `register`.

**Membuat Fungsi Login dan Logout:**
- Buat fungsi `login` yang memungkinkan pengguna masuk. Saat login berhasil, Django akan menyimpan cookie bernama `last_login` untuk mencatat waktu login terakhir pengguna.
- Buat fungsi `logout` yang menghapus cookie `last_login` dengan `response.delete_cookie('last_login')` saat pengguna keluar.

**Menampilkan Cookie last_login di Halaman Web:**
- Tambahkan `last_login: request.COOKIES['last_login']` di views untuk menampilkan cookie `last_login` di halaman web.
- Tambahkan path URL untuk fungsi login dan logout di `urls.py`.
- Gunakan decorator `@login_required` pada views untuk memastikan pengguna harus login sebelum mengakses halaman tertentu.

**Menghubungkan Produk dengan Pengguna:**
- Gunakan `ForeignKey` di `models.py` untuk mengaitkan produk dengan pengguna, kemudian lakukan migrasi untuk menyimpan perubahan.

# Tugas 5

# Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Prioritas pengambilan CSS selector diatur oleh konsep kaskade CSS. Urutannya dari tertinggi ke terendah adalah: **inline style, selektor ID, selektor klas/pseudo-klas, dan selektor tag/pseudo-élémen.** Semakin spesifik selector, semakin tinggi prioritasnya. Jika dua atau lebih selector memiliki spesifisitas yang sama, maka yang terakhir ditulis akan diaplikasikan. Namun, penggunaan !important akan mengalahkan semua jenis selector lainnya kecuali inline style.

# Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design penting dalam pengembangan aplikasi web karena memungkinkan pengalaman pengguna konsisten di berbagai perangkat dan ukuran layar. Hal ini juga membantu dalam meningkatkan visibilitas di mesin pencari, memudahkan akses konten di berbagai platform, dan mendukung optimisasi SEO. Beberapa contoh aplikasi yang sudah menerapkan responsive design antara lain Facebook, Twitter, dan Instagram. Sebaliknya, beberapa situs web tua atau kecil masih menggunakan desain statis yang tidak fleksibel untuk berbagai ukuran layar sebagai contoh, yaitu https://myspace.com/ sebagai aplikasi yang belum sepenuhnya menerapkan responsive design.

# Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
**Perbedaan**
**Margin (marge):**
Ruang kosong di luar elemen
Tidak termasuk dalam ukuran elemen
**Border (borders):**
Garis batas fisik di sekitar elemen
Bisa berupa garis, bayangan, atau teks
Menambahkan ukuran elemen
**Padding (padding):**
Ruang kosong di dalam elemen
Termasuk dalam ukuran elemen

**Cara Implementasi:**
Margin digunakan untuk jarak antar elemen
Border menentukan batasan visual elemen
Padding memberi ruang di dalam isi elemen
.box {
  margin: 20px; 
  border: 2px solid black; 
  padding: 10px; 
}

# Jelaskan konsep flex box dan grid layout beserta kegunaannya!
**Flex Box**
Flex box adalah sistem layout satu dimensi yang dirancang untuk membuat baris atau kolom. 
**Kegunaannya:**
Mengatur elemen dalam satu baris atau kolom.
Mudah digunakan untuk alignment vertikal dan horizontal.
Ideal untuk layout kecil dengan beberapa baris atau kolom.
Cocok untuk desain konten pertama, yaitu saat kita belum tahu pasti bagaimana konten akan terlihat.
**Grid Layout**
Grid layout adalah sistem layout dua dimensi yang dirancang untuk membuat layout kompleks dengan baris dan kolom simultan. 
**Kegunaannya:**
Membuat layout dua dimensi yang kompleks.
Lebih cocok untuk desain konten yang lebih rumit.
Ideal untuk membuat layout yang fleksibel dan responsif.
Cocok untuk membuat layout yang lebih konsisten dan mudah dipahami.

# Cara mengimplementasikan checklist 
1. Tambahkan fungsi edit_thrift ke views.py lalu buat path URL untuk fitur edit product di urls.py.
2. Tambahkan fungsi delete_thrift ke views.py yang menerima parameter request dan id, lalu buat path URL untuk fitur delete product di urls.py.
3. Buat file HTML khusus untuk mengedit produk dan file HTML untuk navigasi (navbar).
4. Konfigurasikan pengelolaan file statis di settings.py dengan menambahkan middleware WhiteNoise dan mengatur STATIC_ROOT, STATICFILES_DIRS, serta STATIC_URL.
5. Tambahkan Tailwind CSS dengan membuat folder static/css/global.css dan menambahkan script Tailwind ke dalam base.html.
6. Lakukan styling pada halaman login dan register agar lebih menarik.
7. Lakukan styling pada tampilan halaman untuk membuat produk dan mengedit produk.
8. Beri gaya pada elemen card info, card product, bagian utama, dan navbar.
9. Langkah-langkah di atas mencakup pengembangan fitur baru, konfigurasi server, pengelolaan 😄



