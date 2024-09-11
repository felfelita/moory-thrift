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







