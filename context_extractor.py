from keybert import KeyBERT

# Load same model used in emotion classifier
kw_model = KeyBERT('all-MiniLM-L6-v2')

def extract_context(text, top_n=5):
    keywords = kw_model.extract_keywords(text, 
                                         keyphrase_ngram_range=(1, 2), 
                                         stop_words='english', 
                                         use_maxsum=False, 
                                         nr_candidates=10, 
                                         top_n=top_n)
    return [kw[0] for kw in keywords]  # Return only keyword strings


