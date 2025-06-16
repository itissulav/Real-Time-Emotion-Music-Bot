from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def rank_lyrics_by_context(user_context_keywords, song_list):
    query = " ".join(user_context_keywords)
    query_embedding = model.encode(query, convert_to_tensor=True)

    best_score = -1
    best_song = None

    for song in song_list:
        lyrics_embedding = model.encode(song["lyrics"], convert_to_tensor=True)
        score = util.cos_sim(query_embedding, lyrics_embedding).item()

        song["similarity"] = score

        if score > best_score:
            best_score = score
            best_song = song

    return best_song
