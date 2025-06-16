import lyricsgenius


GENIUS_ACCESS_TOKEN = "MYeDg48iy_bsYQTmf7nMHl9SUK5gXHLh5kt5qcPToHf3JPtFGi6ndxkqJoEkHEZm"

# Initialize the Genius API client
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN,
                             skip_non_songs=True,
                             excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True,
                             timeout=15,
                             retries=3)

def search_song_by_context(context_keywords, max_results=3):
    results = []
    
    for keyword in context_keywords:
        print(f"🔍 Searching for keyword: {keyword}")
        try:
            song = genius.search_song(keyword)
            if song and song.lyrics:
                results.append({
                    "title": song.title,
                    "artist": song.artist,
                    "lyrics": song.lyrics.strip()
                })
        except Exception as e:
            print(f"⚠️ Error while searching for '{keyword}': {e}")
        
        if len(results) >= max_results:
            break

    return results

# Test it
if __name__ == "__main__":
    keywords = ["breakup", "lonely", "regret"]
    songs = search_song_by_context(keywords)

    for i, song in enumerate(songs):
        print(f"\n🎵 {i+1}. {song['title']} by {song['artist']}")
        print(f"--- Lyrics Preview ---\n{song['lyrics'][:500]}\n")
