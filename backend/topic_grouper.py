from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight and fast

def group_headlines_by_topic(headlines, num_topics=5):
    embeddings = model.encode(headlines)

    kmeans = KMeans(n_clusters=num_topics, random_state=0)
    labels = kmeans.fit_predict(embeddings)

    topic_groups = {}
    for label, headline in zip(labels, headlines):
        topic_groups.setdefault(label, []).append(headline)

    return topic_groups
