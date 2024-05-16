# Book-recommendation

# Project Overview

Sistem rekomendasi telah menjadi inti dari banyak platform online, memungkinkan pengguna untuk menemukan konten yang sesuai dengan minat dan preferensi mereka. Dua pendekatan yang umum digunakan dalam pengembangan sistem rekomendasi adalah Content Based Filtering (CBF) dan Collaborative Filtering (CF). Dalam CBF, rekomendasi didasarkan pada analisis terhadap atribut-atribut konten yang terkait dengan item yang direkomendasikan, seperti teks, metadata, atau fitur lainnya. Sebaliknya, CF mengandalkan pola perilaku pengguna untuk menghasilkan rekomendasi, dengan mengidentifikasi kesamaan antara preferensi pengguna yang serupa[[1]](https://ieeexplore.ieee.org/abstract/document/7684166?casa_token=oDbhmlwVkn8AAAAA:57XkjHpU74_TMag16JMEmzDyj3Hv2Ei0K12NHjfxTeIpF7GcZaFb2x9feWjD31r1lsjVLt61HAR-OT0). Penggabungan kedua pendekatan ini dapat meningkatkan kualitas rekomendasi dengan memperhitungkan baik konten item maupun interaksi pengguna. Oleh karena itu, penelitian ini bertujuan untuk membandingkan efektivitas kedua metode tersebut dalam konteks sistem rekomendasi buku, dengan harapan dapat memberikan wawasan yang berharga bagi pengembangan sistem rekomendasi yang lebih canggih dan personal.

# Business Understanding
Penerapan sistem rekomendasi buku dengan pendekatan Content Based Filtering (CBF) dan Collaborative Filtering (CF) memiliki dampak yang signifikan dari sudut pandang bisnis dan ekonomi. Sistem ini dapat meningkatkan penjualan dan pendapatan dengan memberikan rekomendasi buku yang lebih akurat dan relevan bagi pelanggan, yang pada gilirannya meningkatkan tingkat konversi penjualan. Pelanggan juga akan merasakan pengalaman yang lebih baik karena mereka dapat dengan mudah menemukan buku yang sesuai dengan minat mereka, meningkatkan kepuasan dan loyalitas mereka. Selain itu, bisnis dapat mengoptimalkan pengelolaan inventaris dan stok berdasarkan data preferensi pelanggan yang diperoleh, mengurangi kelebihan atau kekurangan stok. Secara kompetitif, teknologi rekomendasi yang canggih dapat menjadi keunggulan yang membedakan bisnis dalam pasar yang semakin digital dan kompetitif.

Stakeholder yang diuntungkan dari sistem ini meliputi penerbit dan penjual buku yang mendapatkan wawasan lebih baik tentang preferensi pembaca, toko buku fisik dan online yang mengalami peningkatan penjualan, dan platform distribusi buku digital seperti Amazon Kindle dan Google Books yang dapat meningkatkan engagement pengguna. Konsumen akhir, yaitu pembaca, juga sangat diuntungkan dengan mendapatkan rekomendasi buku yang personal dan relevan, yang meningkatkan kepuasan dan kesenangan mereka dalam membaca. Penulis, terutama yang baru atau kurang dikenal, juga mendapatkan eksposur lebih besar karena buku mereka dapat direkomendasikan kepada pembaca yang tertarik dengan genre serupa.

Penerapan sistem ini secara aplikatif dapat dilakukan dengan integrasi langsung ke dalam situs web atau aplikasi mobile penjual buku, menghadirkan fitur rekomendasi seperti "Buku yang Mungkin Anda Suka" atau "Pembaca Juga Membaca". Selain itu, hasil rekomendasi dapat digunakan untuk personalisasi email marketing dan notifikasi push kepada pengguna. Di toko buku fisik, sistem ini dapat digunakan untuk menata rak buku berdasarkan kategori yang paling diminati atau memasang perangkat interaktif yang membantu pelanggan menemukan buku berdasarkan minat mereka. Pengembangan aplikasi atau fitur tambahan yang memungkinkan pengguna membuat daftar bacaan, memberikan ulasan, dan menerima rekomendasi berbasis preferensi yang terus diperbarui juga merupakan langkah implementatif yang efektif. Dengan demikian, penelitian ini memiliki potensi besar untuk memberikan dampak positif yang luas bagi berbagai stakeholder dalam industri buku, meningkatkan efisiensi bisnis, pengalaman konsumen, dan pertumbuhan ekonomi di sektor penerbitan dan penjualan buku.

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

Pada projek kali ini variabel yang dipakai adalah newbooks dan ratings.
newbooks memiliki jumlah sampel data sebanyak 10000 dan 14 fitur, sedangkan ratings memiliki jumlah sampel data sebanyak 1048575 dan 3 fitur.

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

Fitur utama yang diguanakan adalah sebagai berikut :
1. Genre

![Eux54XvB](https://github.com/risdaaaa/Book-recommendation/assets/147994396/b940d33d-cbcd-40e8-9490-0ba19a7f4c54)


Gambar 1. Distribusi genre

Genre terdiri dari fiction, fantasy, young-adult, mystery, non-fiction, romance, classics, historical-fiction dan horror. pada data dirtribusi, genre yang paling banyak adalah fiction dengan jumlah lebih dari 1600 judul, sedangkan paling sedikit adalah genre horror dengan jumlah kurang dari 2000.

 
2. Average rating

![d7joDAHa](https://github.com/risdaaaa/Book-recommendation/assets/147994396/34c80992-f193-426d-b4e3-5ba4b93227f0)
   
Gambar 2. Distribusi average rating

Berdasarkan grafik, kisaran rating adalah 0-5 dengan rating terbanyak ada di kisaran rating 4 dengan jumlah lebih dari 1200.

- ratings :
1. user_id: ID unik untuk setiap pengguna yang memberikan rating.
2. book_id: ID unik untuk buku yang diberikan rating.
3. rating: Peringkat atau rating yang diberikan oleh pengguna untuk buku tersebut.

Fitur utama yang digunakan adalah sebagi berikut :
1. Rating

![2c6FDzTz](https://github.com/risdaaaa/Book-recommendation/assets/147994396/2f47fef3-d13e-4724-a5be-56abd604422e)

Gambar 3. Distribusi rating

Berdasarkan grafik, rating tertinggi adalah 4 dengan jumlah sebanyak lebih dari 350000.
  

# Data Preparation
Data preparation yang dilakukan memiliki beberapa langkah, yaitu:

1. **Mengatasi Missing Value**:
- Missing value adalah data yang hilang atau tidak tersedia dalam dataset. Penanganan missing value penting karena data yang hilang dapat menyebabkan bias atau kesalahan dalam analisis data dan pemodelan.
- Kegunaan penanganan missing value adalah:
    a. Meningkatkan akurasi model
    b. Meminimalkan bias
    c. Memastikan integritas dataset
- Teknik yang digunakan adalah `Drop missing values`, seluruh baris yang memiliki missing value akan dihapus dari dataset. Teknik ini dipilih karena asumsi bahwa data yang hilang tidak signifikan dalam jumlah dan menghapusnya tidak akan berdampak besar pada analisis keseluruhan.
  
2. **Pengurutan Data**
- Pengurutan data dilakukan untuk mengatur data berdasarkan suatu kolom tertentu agar lebih mudah dianalisis dan diproses.
- Kegunaan pengurutan data adalah mempermudah pencarian dan indexing data serta membantu dalam analisis yang memerlukan urutan tertentu.
- Teknik yang digunakan adalah `Sort values`, data diurutkan berdasarkan kolom 'book_id' secara ascending untuk memastikan setiap buku memiliki urutan yang konsisten dan logis.

3. **Penanganan Duplikasi Data**
- Duplikasi data adalah kemunculan berulang dari data yang sama dalam dataset. Menghapus duplikasi penting untuk memastikan analisis yang akurat dan efisien.
- Kegunaan penanganan duplikasi data adalah meningkatkan efisiensi analisis, mengurangi redundansi data dan meningkatkan kualitas dataset.
- Teknik yang digunakan adalah `drop duplicates`, menghapus baris yang memiliki 'book_id' yang sama untuk memastikan setiap buku hanya muncul sekali dalam dataset.
4. **Konversi Data Series ke Bentuk List**
- Konversi data series ke dalam bentuk list dilakukan untuk mempermudah manipulasi dan analisis data lebih lanjut.
- Kegunaan konversi data series ke list adalah mempermudah operasi manipulasi data serta memfasilitasi penggunaan data dalam berbagai algoritma dan model.

5. **Pembuatan Dictionary**
- Membuat dictionary dari data 'book_id', 'title', dan 'genre' bertujuan untuk menggabungkan informasi yang relevan tentang buku dalam satu struktur data yang terorganisir.
- Kegunaan pembuatan dictionary adalah mempermudah akses dan manipulasi data serta menyediakan struktur data yang lebih terorganisir

  
# Modeling dan Result
Sistem rekomendasi yang diimplementasikan dalam model ini terdiri dari dua pendekatan utama: Content Based Filtering (CBF) dan Collaborative Filtering (CF).

### Collaborative Filtering (CF)

Collaborative Filtering (CF) adalah pendekatan dalam sistem rekomendasi yang mendasarkan rekomendasinya pada interaksi antara pengguna dan item. CF menggunakan data dari banyak pengguna untuk menemukan pola dan memberikan rekomendasi berdasarkan kesamaan preferensi antar pengguna. Sistem ini bekerja dengan mengumpulkan data tentang interaksi pengguna dengan item, seperti rating, pembelian, atau ulasan. Setelah itu, sistem mencari kesamaan antara pengguna (User-Based CF) atau item (Item-Based CF). Misalnya, pengguna yang memiliki pola rating yang mirip akan dianggap serupa. Akhirnya, sistem merekomendasikan item yang disukai oleh pengguna yang serupa atau item yang memiliki pola interaksi yang mirip dengan item yang disukai pengguna. CF mampu menemukan hubungan yang kompleks dan mengatasi keterbatasan fitur spesifik dari item. Namun, CF menghadapi tantangan seperti cold start problem, di mana sulit memberikan rekomendasi kepada pengguna baru yang belum memiliki cukup interaksi atau item baru yang belum banyak diulas, serta masalah skalabilitas jika jumlah pengguna dan item sangat besar.


| book_id  |  title | genre  | 
|---|---|---|
|  3869 |  Vernom God Little | fiction  |

Gambar 4. Informasi buku

|  title | genre  |  
|---|---|
|  Infite Jest |  fiction | 
| Back When We Were Grownups  |  fiction |  
| True History of the Kelly Gang  |  fiction |   
| The Day of the Locust  | fiction  |
|  The End (A Series of Unfortunate Events, #13) | fiction  |

Gambar 5. Hasil rekomendasi CF

Sementara itu, pendekatan Collaborative Filtering (CF) melibatkan langkah-langkah berikut:
1. Menggunakan model neural network untuk mempelajari pola rating dari pengguna terhadap buku.
2. Membagi data menjadi data training dan validasi.
3. Membangun model RecommenderNet yang menggunakan layer embedding untuk merepresentasikan user dan buku, kemudian menggabungkan kedua embedding tersebut dan menghitung prediksi rating menggunakan sigmoid activation.
4. Melatih model menggunakan data training dan mengevaluasi kinerjanya menggunakan data validasi.

### Content Based Filtering (CBF)

Content Based Filtering (CBF) adalah pendekatan dalam sistem rekomendasi yang mendasarkan rekomendasinya pada karakteristik atau fitur dari item yang ada. Dalam konteks rekomendasi buku, fitur-fitur ini bisa berupa genre, penulis, deskripsi, atau atribut lain yang melekat pada buku. Sistem ini bekerja dengan membuat profil pengguna berdasarkan preferensi mereka terhadap fitur-fitur tertentu. Misalnya, jika seorang pengguna sering membaca buku fiksi ilmiah, profil mereka akan mencerminkan preferensi ini. Selanjutnya, setiap buku dianalisis berdasarkan fitur-fiturnya, seperti genre, penulis, dan deskripsi. Sistem kemudian mencocokkan profil pengguna dengan fitur-fitur buku yang tersedia, dan buku yang memiliki fitur yang mirip dengan preferensi pengguna akan direkomendasikan. Keuntungan utama dari CBF adalah personalisasi yang tinggi, di mana rekomendasi sangat sesuai dengan preferensi individu pengguna, dan independensi dari data pengguna lain. Namun, pendekatan ini terbatas pada fitur yang diketahui dan mungkin kurang efektif jika pengguna memiliki preferensi yang sangat bervariasi.

Rekomendasi berdasarkan collaborative filtering
Setelah menentukan buku dengan prediksi rating tertinggi, kita menampilkan hasil rekomendasi untuk user:

|   The Great Gatsby  |  F. Scott Fitzgerald  |
| Top 5 book recommendation for user  |  5603 | 
|---|---|
|  Harry Potter and the Half-Blood Prince (Harry Potter, #6) | J.K. Rowling, Mary GrandPré  |  
| Harry Potter and the Goblet of Fire (Harry Potter, #4)  |  J.K. Rowling, Mary GrandPré |  
|  Ptolemy's Gate (Bartimaeus, #3) |  Jonathan Stroud |   
| Harry Potter and the Deathly Hallows (Harry Potter, #7)  | J.K. Rowling, Mary GrandPré  |
|  The Naming (The Books of Pellinor, #1) | Alison Croggon  |

Gambar 6. Hasil rekomendasi CBF

Hasil rekomendasi merupakan top 5 judul buku yang direkomendasikan untuk user.

Untuk pendekatan Content Based Filtering (CBF), langkah-langkahnya adalah sebagai berikut:
1. Penggunaan TfidfVectorizer untuk menghitung nilai TF-IDF dari data genre buku. Ini membantu dalam menganalisis konten buku dan memahami preferensi pengguna berdasarkan genre.
2. Menggunakan cosine similarity untuk mengukur kemiripan antara buku berdasarkan nilai TF-IDF dari genre. Dengan demikian, sistem dapat merekomendasikan buku yang memiliki genre yang mirip dengan buku yang disukai pengguna.


Kedua pendekatan tersebut memiliki kelebihan dan kekurangan:
- Kelebihan Content Based Filtering: Tidak memerlukan data rating dari pengguna, dapat memberikan rekomendasi yang relevan berdasarkan karakteristik konten buku.
- Kekurangan Content Based Filtering: Rentan terhadap over-specialization, di mana rekomendasi cenderung terbatas pada preferensi yang sudah dikenal pengguna.
- Kelebihan Collaborative Filtering: Mampu menangani cold start problem dengan baik dan memberikan rekomendasi yang lebih personal berdasarkan perilaku rating pengguna.
- Kekurangan Collaborative Filtering: Memerlukan data rating dari pengguna, rentan terhadap sparsity data, di mana banyak buku tidak menerima rating dari sebagian besar pengguna.

Dengan mengintegrasikan kedua pendekatan ini, sistem rekomendasi dapat mengatasi kelemahan masing-masing pendekatan dan memberikan rekomendasi yang lebih baik secara keseluruhan.

# Evaluation

1. Hasil evaluasi untuk content based filtering

| book_id  |  title | genre  | 
|---|---|---|
|  3869 |  Vernom God Little | fiction  |

Gambar 7. Informasi buku

Hasil top 5 rekomendasi berdasarkan algoritma content based filtering adalah sebagai berikut :

|  title | genre  |  
|---|---|
|  Infite Jest |  fiction | 
| Back When We Were Grownups  |  fiction |  
| True History of the Kelly Gang  |  fiction |   
| The Day of the Locust  | fiction  |
|  The End (A Series of Unfortunate Events, #13) | fiction  |

Gambar 8. Hasil rekomendasi CF

$$ P = \frac{\text{number of our recommendations that are relevant}}{\text{number of items we recommended}} $$

Berdasarkan hasil rekomendasi Collaborative Filtering (CF), diketahui bahwa *Vernon God Little* merupakan genre fiksi. Dari 5 judul yang direkomendasikan, semuanya memiliki genre fiksi. Artinya, precision sistem adalah 5/5 atau 100%. Hasil proyek berdasarkan metrik evaluasi precision ini menunjukkan bahwa sistem CF berhasil dalam memberikan rekomendasi yang sesuai dengan preferensi pengguna, dalam hal ini, genre buku fiksi. Ini menunjukkan bahwa sistem rekomendasi CF dapat menjadi solusi yang efektif dalam membantu pengguna menemukan konten yang relevan dan sesuai dengan minat mereka.

2. Hasil evaluasi untuk collaborative filtering
Setelah menentukan buku dengan prediksi rating tertinggi, kita menampilkan hasil rekomendasi untuk user:

|   The Great Gatsby  |  F. Scott Fitzgerald  |
| Top 5 book recommendation for user  |  5603 | 
|---|---|
|  Harry Potter and the Half-Blood Prince (Harry Potter, #6) | J.K. Rowling, Mary GrandPré  |  
| Harry Potter and the Goblet of Fire (Harry Potter, #4)  |  J.K. Rowling, Mary GrandPré |  
|  Ptolemy's Gate (Bartimaeus, #3) |  Jonathan Stroud |   
| Harry Potter and the Deathly Hallows (Harry Potter, #7)  | J.K. Rowling, Mary GrandPré  |
|  The Naming (The Books of Pellinor, #1) | Alison Croggon  |

Gambar 9. Hasil rekomendasi CBF

Hasil rekomendasi merupakan top 5 judul buku yang direkomendasikan untuk user.


![TWr8-OdG](https://github.com/risdaaaa/Book-recommendation/assets/147994396/b810ba19-9ed2-4c09-a0ee-b5ae7d2e3088)

Gambar 10.Grafik matrik

Metrik evaluasi yang digunakan adalah Root Mean Squared Error (RMSE). Metrik ini ditambahkan saat model dikompilasi dengan `tf.keras.metrics.RootMeanSquaredError()` dan kemudian digunakan untuk mengukur performa model selama training dan validasi. RMSE memberikan informasi tentang seberapa dekat prediksi model dengan nilai sebenarnya, dengan penalti lebih besar untuk kesalahan yang lebih besar karena mengkuadratkan kesalahan sebelum menghitung rata-rata. Selama proses training, nilai RMSE untuk data training dan validasi divisualisasikan untuk memantau performa model dari waktu ke waktu. RMSE yang lebih rendah menunjukkan performa model yang lebih baik.

Setelah melatih model, kita melakukan evaluasi rekomendasi buku untuk sample user:

- Mengambil Sample User: Memilih satu user secara acak dari dataset ratings.
- Menentukan Buku yang Belum Dibaca: Menentukan buku-buku yang belum dibaca oleh user tersebut.
- Mempersiapkan Data untuk Prediksi: Meng-encode user dan buku, kemudian membuat array untuk prediksi.
- Prediksi Rating: Model memprediksi rating untuk buku yang belum dibaca oleh user.
- Top 5 Rekomendasi: Menentukan 5 buku dengan prediksi rating tertinggi.

Proyek ini berhasil mencapai tujuan utamanya yaitu mengembangkan sistem rekomendasi buku yang akurat dan efisien. Beberapa indikator keberhasilan proyek ini meliputi penurunan RMSE yang konsisten selama pelatihan, menunjukkan bahwa model belajar dengan baik dan menghasilkan prediksi yang lebih akurat seiring waktu. Selain itu, buku yang direkomendasikan sesuai dengan preferensi pengguna, menunjukkan bahwa model berhasil memahami pola dan preferensi pengguna. Dalam hal solusi yang diinginkan dan problem statement, hasil evaluasi menunjukkan bahwa model dapat memberikan rekomendasi yang relevan dan akurat, sesuai dengan preferensi pengguna, yang diindikasikan oleh nilai RMSE yang rendah pada data validasi. Selain itu, sistem rekomendasi ini juga efisien dalam hal proses pelatihan dan prediksi, memungkinkan pengguna untuk mendapatkan rekomendasi secara cepat. Kesimpulannya, proyek ini dianggap berhasil karena telah mencapai tujuan yang diinginkan, yaitu mengembangkan sistem rekomendasi buku yang akurat dan efisien. Sistem ini mampu menyelesaikan masalah utama dalam memberikan rekomendasi buku yang relevan kepada pengguna, sehingga meningkatkan pengalaman membaca dan potensi peningkatan penjualan buku.

# References

[1] Mathew, M. P., Kuriakose, M. B., & Hegde, M. (2016). Book Recommendation System through content based and collaborative filtering method. IEEE Xplore , 6.

