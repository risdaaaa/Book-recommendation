# -*- coding: utf-8 -*-
"""Salinan book.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d9zx0YF992Q6izSieflj8as9eN72m3kq
"""

from google.colab import files
files.upload()

! mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d danyalhyder/the-new-chapterbook-recommendation-system

!unzip the-new-chapterbook-recommendation-system

"""# Data Understanding"""

import numpy as np # linear algebra
import pandas as pd # data processing

newbooks = pd.read_csv('/content/newbooks.csv')
ratings = pd.read_csv('/content/ratings.csv')

"""newbooks"""

newbooks.info()

newbooks.describe()

"""Ratings"""

ratings.info()

ratings.describe()

"""# Data Preprocessing

Menggabungkan data
"""

# Baca data ke dalam DataFrame
newbooks = pd.read_csv('newbooks.csv')
ratings = pd.read_csv('ratings.csv')

# Gabungkan DataFrame berdasarkan kolom 'book_id'
all = pd.merge(newbooks, ratings, on='book_id')

# Tampilkan informasi tentang DataFrame yang telah digabungkan
print(all.info())

"""Missing value"""

all.isnull().sum()

"""# Data Preparation

Mengatasi missing value
"""

all = all.dropna()
all

all.isnull().sum()

"""Mengurutkan"""

all= all.sort_values('book_id', ascending=True)
all

len(all.book_id.unique())

preparation = all
preparation.sort_values('book_id')

# Membuang data duplikat pada variabel preparation
preparation = preparation.drop_duplicates('book_id')
preparation

# Mengonversi data series ‘book_id’ menjadi dalam bentuk list
book_id = preparation['book_id'].tolist()

# Mengonversi data series ‘title’ menjadi dalam bentuk list
title = preparation['title'].tolist()

# Mengonversi data series ‘genres’ menjadi dalam bentuk list
genre = preparation['genre'].tolist()

print(len(book_id))
print(len(title))
print(len(genre))

# Membuat dictionary untuk data ‘book_id’, ‘title’, dan ‘genre’
mybook = pd.DataFrame({
    'book_id': book_id,
    'title': title,
    'genre': genre
})
mybook

"""# Modeling and Result

**Model Development dengan Content Based Filtering**
"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data genre
tf.fit(mybook['genre'])

# Mapping array dari fitur index integer ke fitur nama
feature_names = tf.get_feature_names_out()
print(feature_names)

tfidf_matrix = tf.fit_transform(mybook['genre'])
tfidf_matrix.shape

tfidf_matrix.todense()

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=feature_names,
    index=mybook['title']
).sample(22, axis=1).sample(10, axis=0)

from sklearn.metrics.pairwise import cosine_similarity

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

cosine_sim_df = pd.DataFrame(cosine_sim, index=mybook['title'], columns=mybook['title'])
print('Shape:', cosine_sim_df.shape)

cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""Mendapatkan rekomendasi"""

def book_recommendations(title, similarity_data=cosine_sim_df, items=mybook[['title', 'genre']], k=5):


    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,title].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop nama_movie agar nama movie yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(title, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

mybook[mybook.title.eq('Vernon God Little')]

book_recommendations('Vernon God Little')

"""**Model** Development dengan Collaborative Filtering"""

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from pathlib import Path
import matplotlib.pyplot as plt

# Membaca dataset
ratings = ratings
ratings

# Mengubah user_id menjadi list tanpa nilai yang sama
user_id = ratings['user_id'].unique().tolist()
print('list user_id: ', user_id)

# Melakukan encoding user_id
user_to_user_encoded = {x: i for i, x in enumerate(user_id)}
print('encoded userID : ', user_to_user_encoded)

# Melakukan proses encoding angka ke ke user_id
user_encoded_to_user = {i: x for i, x in enumerate(user_id)}
print('encoded angka ke userID: ', user_encoded_to_user)

# Mengubah book_id menjadi list tanpa nilai yang sama
book_id = ratings['book_id'].unique().tolist()
# Melakukan proses encoding book_id
# Melakukan proses encoding angka ke book_id
book_to_book_encoded = {x: i for i, x in enumerate(book_id)}
book_encoded_to_book = {i: x for i, x in enumerate(book_id)}

# Mapping user_id ke dataframe user
# Mapping book_id ke dataframe book
ratings['user'] = ratings['user_id'].map(user_to_user_encoded)
ratings['book'] = ratings['book_id'].map(book_to_book_encoded)

import numpy as np
# Mendapatkan jumlah user
num_users = len(user_encoded_to_user)
print(num_users)

# Mendapatkan jumlah BUKU
num_book = len(book_encoded_to_book)
print(num_book)

# Mengubah rating menjadi nilai float
ratings['rating'] = ratings['rating'].values.astype(np.float32)

# Nilai minimum rating
# Nilai maksimal rating
min_rating = min(ratings['rating'])
max_rating = max(ratings['rating'])

print('Number of User: {}, Number of Buku: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_book, min_rating, max_rating))

"""Membagi Data untuk Training dan Validasi"""

# Mengacak dataset
ratings = ratings.sample(frac=1, random_state=42)
ratings

# Membuat variabel x untuk mencocokkan data user dan resto menjadi satu value
x = ratings[['user', 'book']].values

# Membuat variabel y untuk membuat rating dari hasil
y = ratings['rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# Membagi menjadi 70% data train dan 20% data validasi
train_indices = int(0.70 * ratings.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

"""training"""

from tensorflow import keras
from tensorflow.keras import layers
import tensorflow as tf
class RecommenderNet(tf.keras.Model):

  # Insialisasi fungsi
  def __init__(self, num_users, num_resto, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_resto = num_resto
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user

        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1)# layer embedding user bias
    self.resto_embedding = layers.Embedding(# layer embeddings buku
        num_resto,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.resto_bias = layers.Embedding(num_resto, 1)#layer embedding book bias

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0])# memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0])# memanggil layer embedding 2
    resto_vector = self.resto_embedding(inputs[:, 1])# memanggil layer embedding 3
    resto_bias = self.resto_bias(inputs[:, 1])# memanggil layer embedding 4

    dot_user_resto = tf.tensordot(user_vector, resto_vector, 2)

    x = dot_user_resto + user_bias + resto_bias

    return tf.nn.sigmoid(x)# activation sigmoid

"""# Evaluasi"""

model = RecommenderNet(num_users, num_book, 50) # inisialisasi model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

# Memulai training

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 5,
    epochs = 10,
    validation_data = (x_val, y_val)
)

import matplotlib.pyplot as plt

# Visualisasi Metrik
plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

newbooks

# Mengambil sample user
user_id = ratings.user_id.sample(1).iloc[0]
books_have_been_read_by_user = ratings[ratings.user_id == user_id]

books_have_not_been_read_by_user = newbooks[newbooks['book_id'].isin(books_have_been_read_by_user.book_id.values)]['book_id']
books_have_not_been_read_by_user = list(
    set(books_have_not_been_read_by_user)
    .intersection(set(book_to_book_encoded.keys()))
)

books_have_not_been_read_by_user = [[book_to_book_encoded.get(x)] for x in books_have_not_been_read_by_user]
user_encoder = user_to_user_encoded.get(user_id)
user_book_array = np.hstack(
    ([[user_encoder]] * len(books_have_not_been_read_by_user), books_have_not_been_read_by_user)
)

ratings = model.predict(user_book_array).flatten()

top_ratings_indices = ratings.argsort()[-5:][::-1]
recommended_book_ids = [
    book_encoded_to_book.get(books_have_not_been_read_by_user[x][0]) for x in top_ratings_indices
]

top_books_recommended = (
    books_have_been_read_by_user.sort_values(
        by = 'rating',
        ascending=False
    )
    .head(5)
    .rating.values
)

books_row = newbooks[newbooks['book_id'].isin(top_books_recommended)]
for row in books_row.itertuples():
    print(row.title, ':', row.authors)

print('----' * 8)
print('Top 5 Book Recommendation for user: {}'.format(user_id))
print('----' * 8)

recommended_books = newbooks[newbooks['book_id'].isin(recommended_book_ids)]
for row in recommended_books.itertuples():
    print(row.title, ':', row.authors)

"""# Evaluation"""