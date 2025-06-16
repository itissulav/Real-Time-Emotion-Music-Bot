from context_extractor import extract_context
from predict_emotion import predict_emotion
from genius_lyrics import search_song_by_context
from lyrics_matcher import rank_lyrics_by_context
from spotify_player import play_song
from SpotifyAuth import authenticate_spotify

sp = authenticate_spotify()


text = input("Tell me how your day was: ")
# Step 1: Understand the input
emotion = predict_emotion(text)
context_keywords = extract_context(text)

print("🧠 Emotion:", emotion)
print("🧩 Context:", context_keywords)

# Step 2: Search Genius for candidate songs
songs = search_song_by_context(context_keywords)

# Step 3: Match most relevant lyrics
best_match = rank_lyrics_by_context(context_keywords, songs)

if best_match:
    print(f"🎧 Best Match: {best_match['title']} by {best_match['artist']}")
    print(f"Similarity Score: {best_match['similarity']:.3f}")
    
    # Step 4: Play it on Spotify
    play_song(best_match["title"], best_match["artist"], sp)
else:
    print("No good match found.")
