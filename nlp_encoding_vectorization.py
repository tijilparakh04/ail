import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import difflib

review_a = """
David Fincher’s Fight Club is a cinematic masterpiece that transcends its surface narrative to become an unforgettable exploration of identity, consumerism, and the human psyche. Adapted from Chuck Palahniuk’s novel, the film combines a razor-sharp screenplay by Jim Uhls, mesmerizing visuals, and career-defining performances by Brad Pitt, Edward Norton, and Helena Bonham Carter.

The story follows the disillusioned Narrator (Norton), a white-collar worker plagued by insomnia and existential despair, as he encounters the anarchic and enigmatic Tyler Durden (Pitt). Together, they create an underground fight club that evolves into something far more dangerous and transformative. The chemistry between Pitt and Norton is electric, with Pitt embodying raw charisma and rebellion while Norton delivers a deeply vulnerable and nuanced performance. Carter’s portrayal of the eccentric and self-destructive Marla Singer adds another layer of chaos and heart to the story.

Visually, Fincher’s direction is flawless as always, employing stark cinematography, frenetic editing, and a gritty aesthetic that reflects the film’s dark themes. The use of subliminal imagery and the pulsating score by The Dust Brothers enhance the immersive, almost hypnotic atmosphere.

What makes Fight Club a 5-star film is its ability to challenge and unsettle the audience. Beneath the visceral fight scenes and shocking twists lies a scathing critique of consumer culture, toxic masculinity, and the search for meaning in a soulless world. Its infamous twist ending is both shocking and thought-provoking, demanding a second viewing to fully appreciate its intricacies.

While controversial at its release, Fight Club has aged into a cultural touchstone, a film that continues to spark debate and interpretation. It’s bold, subversive, and unapologetically daring—qualities that solidify its place as one of the greatest films of the late 20th century.

If you haven’t joined the fight yet, it’s time to break the first rule and watch this film.
"""
review_b = """
This movie remains a provocative and stylish landmark, a visceral dive into late 20th-century malaise and fractured identity.Edward Norton gives a brilliant performance as the unnamed Narrator, an office drone drowning in consumerist ennui and plagued by insomnia.His life implodes when he encounters Tyler Durden (an iconic Brad Pitt), a charismatic, anarchic soap salesman who embodies everything the Narrator represses.
Together, they form an underground fight club, a brutal, primal outlet for disenfranchised men seeking escape from societal emasculation and the hollowness of modern life dictated by advertising.What starts as bare-knuckle therapy soon spirals into "Project Mayhem," a dangerous anti-capitalist movement aiming to dismantle societal structures through acts of terrorism.Helena Bonham Carter is unforgettable as Marla Singer, the cynical, chaotic "faker" who disrupts the Narrator's world and becomes entangled in their destructive orbit.
The film launches a scathing critique of consumer culture ("The things you own end up owning you") and tackles the perceived crisis of modern masculinity, exploring alienation and the dangerous allure of violence as a path to reclaiming identity.Central to its enduring power is the theme of fractured identity, masterfully revealed in one of cinema's most shocking twists: Tyler Durden isn't real, but a projection of the Narrator's own mind.This unreliable narration forces a radical reinterpretation of everything witnessed.
Fincher's direction is technically superb, featuring a dark, gritty aesthetic, meticulously controlled compositions, kinetic editing, and innovative visual effects, all pulsating to The Dust Brothers' distinctive electronic score.
Though initially a box office disappointment with mixed reviews , Fight Club achieved massive cult status through home video.It continues to spark debate, hailed as satire by some, condemned for its violence by others, and controversially appropriated by extremist groups—an interpretation Fincher rejects, insisting Tyler is a "negative influence".
Fight Club is a challenging, darkly funny, and unforgettable film. Its potent blend of style, subversive themes, and powerhouse performances makes it a complex and enduring cinematic touchstone that still resonates today.
"""
review_c = """
masterpiece that stands the test of time. Based on Chuck Palahniuk’s novel, it’s a gripping exploration of identity, consumerism, and the human psyche. The film is filled with sharp, thought-provoking dialogue and deep, often disturbing themes, making it a movie that invites viewers to reflect long after the credits roll.

The screenplay, written by Jim Uhls, is one of the film's standout elements. It’s full of dark humor, clever subtext, and quotes that have become iconic in pop culture. The film’s narrative structure, with its unpredictable twists and unreliable narrator played brilliantly by Edward Norton, keeps audiences on edge and rewards multiple viewings. What might seem like an action-packed, anarchistic romp on the surface is actually a profound critique of modern life and the toxic masculinity that pervades it.

David Fincher’s direction is meticulous and iconic, as you mentioned. His use of lighting, color, and camera angles heightens the sense of unease and discomfort, which fits perfectly with the story’s themes of existential disillusionment. The claustrophobic, gritty feel of the film complements its anti-consumerist message, creating a visual style that’s as memorable as the narrative itself.

The cinematography, led by Jeff Cronenweth, is another key factor in making Fight Club a visually striking experience. The use of harsh lighting, tight framing, and subtle transitions enhances the film’s themes and gives it an almost hyper-real, dreamlike quality. Every shot feels carefully composed to evoke a sense of chaos or a looming sense of doom.

The performances from the cast—especially Edward Norton and Brad Pitt—are electric. Norton’s portrayal of the disillusioned narrator is a masterclass in subtlety and internal struggle, while Brad Pitt’s charismatic, chaotic Tyler Durden is the perfect foil to Norton’s character. Their dynamic drives the film, and their chemistry is what makes the film’s unraveling so compelling.

One of the most fascinating aspects of Fight Club is how it subverts expectations. The movie’s opening scenes are built around a consumerist world that seems overly familiar and mundane, but as the story progresses, we see how far removed from reality it truly is. Fincher and the filmmakers use the character of Tyler Durden to expose the contradictions of modern masculinity, consumer culture, and the search for meaning in a materialistic society.

By the end, Fight Club doesn't just leave you with a visceral experience; it leaves you with questions about identity, purpose, and how we define ourselves. The film’s ambiguous conclusion—intentionally left open to interpretation—invites endless discussions and debates, ensuring its place as a cult classic.

For anyone who loves cinema that challenges the norm and leaves a lasting impact, Fight Club is essential viewing. It’s the kind of film that only gets richer the more you watch it, and it continues to resonate in an increasingly superficial world.
"""
# Reviews
reviews = [review_a, review_b, review_c]
onehot_encoder = OneHotEncoder(sparse_output = False)
labels = ['Review A', 'Review B', 'Review C']    
onehot_encoded = onehot_encoder.fit_transform(np.array(labels).reshape(-1,1))

vectorizer_bow = CountVectorizer()
x_bow = vectorizer_bow.fit_transform(reviews)

vectorizer_tfidf = TfidfVectorizer()
x_tfidf = vectorizer_tfidf.fit_transform(reviews)

def get_similarity(text1, text2):
  return difflib.SequenceMatcher(None, text1, text2).ratio()

similarity_ab = get_similarity(review_a, review_b)
similarity_ac = get_similarity(review_b, review_c)
similarity_bc = get_similarity(review_c, review_a)

similarity_scores = {
    "A vs B": similarity_ab,
    "A vs C": similarity_ac,
    "B vs C": similarity_bc

}

most_similar_pair = max(similarity_scores, key=similarity_scores.get)

print("One Hot Encoding Output: ")
print(pd.DataFrame(onehot_encoded, columns = labels))

print("\nBag of words Output: ")
print(pd.DataFrame(x_bow.toarray(), columns = vectorizer_bow.get_feature_names_out()))

print("\nTFIDF Output: ")
print(pd.DataFrame(x_tfidf.toarray(), columns = vectorizer_tfidf.get_feature_names_out()))

print("\nSimilarity Scores:")
for pair, score in similarity_scores.items():
    print(f"{pair}: {score:.4f}")

print(f"\nMost similar pair: {most_similar_pair}")
