import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
def f(inp):
    movies_df = pd.read_csv('movies.csv',dtype={'movieId': 'int32', 'title': 'str'})
    rating_df=pd.read_csv('ratings.csv',usecols=['userId', 'movieId', 'rating'])

    movies_df.head()

    rating_df.head()

    df = pd.merge(rating_df,movies_df,on='movieId')
    df.head()

    combine_movie_rating = df.dropna(axis = 0, subset = ['title'])
    movie_ratingCount = (combine_movie_rating.
         groupby(by = ['title'])['rating'].
         count().
         reset_index().
         rename(columns = {'rating': 'totalRatingCount'})
         [['title', 'totalRatingCount']]
        )
    movie_ratingCount.head()

    rating_with_totalRatingCount = combine_movie_rating.merge(movie_ratingCount, left_on = 'title', right_on = 'title', how = 'left')
    rating_with_totalRatingCount.head()

    pd.set_option('display.float_format', lambda x: '%.3f' % x)
    print(movie_ratingCount['totalRatingCount'].describe())

    popularity_threshold = 50
    rating_popular_movie= rating_with_totalRatingCount.query('totalRatingCount >= @popularity_threshold')
    rating_popular_movie.head()

    rating_popular_movie.shape

    movie_features_df=rating_popular_movie.pivot_table(index='title',columns='userId',values='rating').fillna(0)
    movie_features_df.head()

    """K NEAREST neighbourS """

    movie_features_df_matrix = csr_matrix(movie_features_df.values)
    model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
    model_knn.fit(movie_features_df_matrix)

    # Commented out IPython magic to ensure Python compatibility.
    '''
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure()
    sns.pairplot(movie_features_df)
    plt.show()
    '''
    #movie_features_df.to_csv("out.csv")
    #print(movie_features_df.columns)
      

    movie_features_df.shape
    print(movie_features_df.shape[0])
    query_index = np.random.choice(movie_features_df.shape[0])
    print(query_index)
    #q=input()
    indexx=0
    for i in movie_features_df.index:
        if i in inp:
            break
        else:
            indexx+=1 

    distances, indices = model_knn.kneighbors(movie_features_df.iloc[indexx,:].values.reshape(1, -1), n_neighbors = 6)

    movie_features_df.head()
    li=list()
    for i in range(0, len(distances.flatten())):
        if i == 0:
            li.append(movie_features_df.index[indexx])
        else:
            li.append(movie_features_df.index[indices.flatten()[i]])
    return(li)
#li=f()
#print(li)
