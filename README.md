# Book-recommendation

# Project Overview

Sistem rekomendasi telah menjadi inti dari banyak platform online, memungkinkan pengguna untuk menemukan konten yang sesuai dengan minat dan preferensi mereka. Dua pendekatan yang umum digunakan dalam pengembangan sistem rekomendasi adalah Content Based Filtering (CBF) dan Collaborative Filtering (CF). Dalam CBF, rekomendasi didasarkan pada analisis terhadap atribut-atribut konten yang terkait dengan item yang direkomendasikan, seperti teks, metadata, atau fitur lainnya. Sebaliknya, CF mengandalkan pola perilaku pengguna untuk menghasilkan rekomendasi, dengan mengidentifikasi kesamaan antara preferensi pengguna yang serupa. Penggabungan kedua pendekatan ini dapat meningkatkan kualitas rekomendasi dengan memperhitungkan baik konten item maupun interaksi pengguna. Oleh karena itu, penelitian ini bertujuan untuk membandingkan efektivitas kedua metode tersebut dalam konteks sistem rekomendasi buku, dengan harapan dapat memberikan wawasan yang berharga bagi pengembangan sistem rekomendasi yang lebih canggih dan personal.

# Business Understanding
## Problem Statement
Bagaimana cara menyajikan rekomendasi yang sesuai dengan minat dan preferensi pengguna secara akurat dan efisien.

## Goals
Mengembangkan sistem rekomendasi buku yang akurat dan efisien dengan memanfaatkan Content Based Filtering (CBF) dan Collaborative Filtering (CF).

## Solution Approach
Pendekatan ini akan mengintegrasikan Content Based Filtering (CBF) dan Collaborative Filtering (CF) dalam pengembangan sistem rekomendasi buku. Pertama, untuk CBF, akan dilakukan analisis terhadap atribut-atribut konten buku, seperti judul, genre, dan penulis, untuk memahami minat dan preferensi pengguna. Selanjutnya, akan dikembangkan model CF yang memanfaatkan pola perilaku pengguna untuk menghasilkan rekomendasi, dengan memperhatikan keterbatasan data interaksi pengguna. Integrasi kedua pendekatan ini akan dilakukan dengan memanfaatkan kekuatan keduanya: CBF untuk memahami konten buku dan CF untuk mengidentifikasi kesamaan antara preferensi pengguna. Dengan demikian, akan disajikan rekomendasi yang lebih personal dan relevan bagi pengguna, meningkatkan kepuasan dan retensi mereka dalam platform.

# Data Understanding
Dataset yang digunakan adalah [The New Chapter(book recommendation system)](https://www.kaggle.com/datasets/danyalhyder/the-new-chapterbook-recommendation-system)

Variabel-variabel pada The New Chapter(book recommendation system adalah sebagai berikut :
- book_tags : Variabel ini berisi informasi tentang tag-tag yang terkait dengan setiap buku.
- newbooks : Variabel ini mungkin berisi informasi tentang buku-buku.
- ratings : Variabel ini berisi informasi tentang peringkat atau rating yang diberikan oleh pengguna untuk buku-buku tertentu.
- tags : Variabel ini mungkin berisi daftar tag-tag yang tersedia

Pada projek kali ini variabel yang dipakai adalah
- newbooks :
  1. book_id: ID unik untuk setiap buku dalam sistem rekomendasi.
  2. goodreads_book_id: ID buku yang terkait dengan platform Goodreads, dapat digunakan untuk mendapatkan informasi tambahan tentang buku dari Goodreads.
  3. authors: Nama-nama penulis dari buku tersebut.
  4. original_publication_year: Tahun publikasi asli dari buku tersebut.
  5. original_title: Judul asli dari buku tersebut (jika berbeda dengan judul terjemahan).
  6. title: Judul dari buku tersebut (dapat berupa judul terjemahan).
  7. language_code: Kode bahasa buku (misalnya, "en" untuk bahasa Inggris).
  8. average_rating: Rata-rata peringkat atau rating yang diberikan oleh pengguna untuk buku tersebut.
  9. ratings_count: Jumlah total rating yang diberikan oleh pengguna untuk buku tersebut.
  10. medium_image_url: URL gambar medium untuk buku tersebut.
  11. small_image_url: URL gambar kecil untuk buku tersebut.
  12. desc: Deskripsi atau ringkasan dari buku tersebut.
  13. genre: Genre atau kategori buku tersebut.
  14. image_url: URL gambar utama untuk buku tersebut.
- ratings :
  1. user_id: ID unik untuk setiap pengguna yang memberikan rating.
  2. book_id: ID unik untuk buku yang diberikan rating.
  3. rating: Peringkat atau rating yang diberikan oleh pengguna untuk buku tersebut.

# Data Preparation
Data preparation yang dilakukan memiliki beberapa langkah, yaitu:

- **Mengatasi Missing Value**: Langkah pertama adalah menghapus baris yang mengandung nilai yang hilang (missing value) dari dataframe `all`. Hal ini dilakukan dengan menggunakan metode `dropna()`. Kemudian, digunakan `isnull().sum()` untuk memeriksa apakah masih terdapat nilai yang hilang setelah penghapusan.

- **Mengurutkan**: Data diurutkan berdasarkan kolom 'book_id' secara menaik (ascending) menggunakan fungsi `sort_values()`. Langkah ini membantu dalam memastikan bahwa data telah terurut sesuai dengan 'book_id' agar dapat diolah dengan lebih baik.

- **Membuang Data Duplikat**: Data duplikat pada kolom 'book_id' dihapus menggunakan fungsi `drop_duplicates('book_id')`. Langkah ini dilakukan untuk memastikan bahwa setiap 'book_id' unik dan hanya ada satu baris data yang sesuai dengan setiap 'book_id'.

- **Konversi Data ke dalam Bentuk List**: Data pada kolom 'book_id', 'title', dan 'genre' dikonversi menjadi bentuk list menggunakan metode `tolist()`. Hal ini dilakukan untuk mempersiapkan data agar dapat digunakan dalam pembuatan dictionary.

- **Membuat Dictionary**: Data yang telah dipersiapkan kemudian digabungkan dalam sebuah dataframe baru (`mybook`) yang berisi kolom 'book_id', 'title', dan 'genre'. Langkah ini bertujuan untuk memudahkan pengelolaan dan akses data dalam pembuatan sistem rekomendasi.
  
# Modeling dan Result
Sistem rekomendasi yang diimplementasikan dalam model ini terdiri dari dua pendekatan utama: Content Based Filtering (CBF) dan Collaborative Filtering (CF).

Untuk pendekatan Content Based Filtering (CBF), langkah-langkahnya adalah sebagai berikut:
1. Penggunaan TfidfVectorizer untuk menghitung nilai TF-IDF dari data genre buku. Ini membantu dalam menganalisis konten buku dan memahami preferensi pengguna berdasarkan genre.
2. Menggunakan cosine similarity untuk mengukur kemiripan antara buku berdasarkan nilai TF-IDF dari genre. Dengan demikian, sistem dapat merekomendasikan buku yang memiliki genre yang mirip dengan buku yang disukai pengguna.
   
![h16GEOM5](https://github.com/risdaaaa/Book-recommendation/assets/147994396/41052821-4c42-4855-adae-69aa6700f02f)


![25rw9peg](https://github.com/risdaaaa/Book-recommendation/assets/147994396/98c3e80b-8502-4278-8af8-2772bfa53255)


Sementara itu, pendekatan Collaborative Filtering (CF) melibatkan langkah-langkah berikut:
1. Menggunakan model neural network untuk mempelajari pola rating dari pengguna terhadap buku.
2. Membagi data menjadi data training dan validasi.
3. Membangun model RecommenderNet yang menggunakan layer embedding untuk merepresentasikan user dan buku, kemudian menggabungkan kedua embedding tersebut dan menghitung prediksi rating menggunakan sigmoid activation.
4. Melatih model menggunakan data training dan mengevaluasi kinerjanya menggunakan data validasi.

Kedua pendekatan tersebut memiliki kelebihan dan kekurangan:
- Kelebihan Content Based Filtering: Tidak memerlukan data rating dari pengguna, dapat memberikan rekomendasi yang relevan berdasarkan karakteristik konten buku.
- Kekurangan Content Based Filtering: Rentan terhadap over-specialization, di mana rekomendasi cenderung terbatas pada preferensi yang sudah dikenal pengguna.
- Kelebihan Collaborative Filtering: Mampu menangani cold start problem dengan baik dan memberikan rekomendasi yang lebih personal berdasarkan perilaku rating pengguna.
- Kekurangan Collaborative Filtering: Memerlukan data rating dari pengguna, rentan terhadap sparsity data, di mana banyak buku tidak menerima rating dari sebagian besar pengguna.

Dengan mengintegrasikan kedua pendekatan ini, sistem rekomendasi dapat mengatasi kelemahan masing-masing pendekatan dan memberikan rekomendasi yang lebih baik secara keseluruhan.

# Evaluation

