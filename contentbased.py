from sklearn.metrics.pairwise import cosine_similarity

from sklearn.feature_extraction.text import CountVectorizer
df1=pd.read_csv("articles.csv")
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df1['title'])
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
df1 = df1.reset_index()
indices = pd.Series(df1.index, index=df1['contentId'])
def get_recommendations(contentId, cosine_sim):
    idx = indices[contentId]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df1['contentId'].iloc[movie_indices]
