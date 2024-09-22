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
   - Pada fungsi `show_main`, tambahkan `Product.objects.all()` untuk mengambil semua data `Product` dari database dan kirimkan ke template melalui context.
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
