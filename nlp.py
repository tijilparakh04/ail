import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, ngrams
from textblob import TextBlob

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')


a = """
"Too much of a good thing"... that is definitely the dictionary definition!"
"Beauty is Painful vs Painful is beauty"
"Is this Aliens 6?"

- no spoilers -

Eeew-licious!
Juicy Trippy Desperate!
One Way Road to Beautytown!
A Full Blown Spectacular Film of Self Image!
Magnificent Cynical
Superb and not to be missed!
An Instant Classic!

Futuristically but so now.
Beauty Youth and Allure is the Hollywood line in the sand.
If you're old mature charismaless and your sap is dried out, you're just plain out.
There has never been a film like this!
Not for the squeamish!

A clever mix of Dorian Grey, science's "crisp", and what a staple gun can staple together
This berserk fun 22nd Century narrative of I'll do anything, whatever it takes,
with no scruples is representative of all the collagen, hyaluronic fillers, botoxy, peptides,
plant stem cells, cryo roller sundaes with sprinkles.

However it boils down to self value and self devalue, the horrors and ecstacies of both.
The industries of cosmetics, body sculpting, plastic surgery,weaves-hair transplant rule the world today of appearances, pressuring females and now males: taunting them with ageism.

Cinematography Benjamin Kracun mashes raw meat, raw eggs, grey hair, and lythe body in a pallets of maddening horror.

Perfect curves against aching joints
Lifeless hair against a perfect blow out

Spectacular Casting Starring:
Demi Moore - brave epic Sunset Blvd
Margaret Qualley - finnesed viciously
Dennis Quaid - ferocious stats

Directed by Coralie Fargeat
Written by Coralie Fargeat
Fine fine job of directing and dialogue.
Hidden in this film is the silent loathing for women and their natural right to age or not to age without endless anger and scrutiny.
And this is the brutal frank truthful horror story She expertly reflects that makes women's aging a monstrosity today in the real world. She's not exaggerating!
Trillions are spent on products and procedures to keep women young.

Finally, Self love is everything.
Twists and Turns with a brilliant resolve. Go in blind and enjoy.

5/5 - unchecked hotness becomes hot messes
10/10 - everything good and bad comes with a human price tag.

Aside:
The Irony is critics say Demi Moore looks fantastic for 62 as if She should be punished for not looking like a sagging crone, the same sort of derision Madonna faces for doing whatever possible to keep a youthful restored face. Women are punished and thrown away for aging, and punished for doing whatever possible to remain youthful. Men age and reach that midlife crisis and dispose of them for a new younger version, especially wealthy men.
You have to ask, what entitles and gives Elton John the right to say Madonna should "retire gracefully at her age" or 50 Cents to mock and say "Grandma under the bed". And Women criticizing Nicole Kidman's "AI Artificial Face". All the While Hugh Jackson's 8 pack abs in Deadpool vs Wolverine are celebrated at the Senior age of 55.

Hollywood only shows these concentrated attitudes that have always always always been defining society norms.
Can you find anything untrue about the prevalent attitudes in this film?
The answer is emphatically "No".
"""

b = re.sub(r'[^a-zA-Z\s]', '', a)
b = re.sub(r'\s+', ' ', b)
print("\nAfter removing punctuation, special characters, numbers, extra spaces:\n", b)

b = b.lower()
print("\nAfter converting to lowercase: \n", b)

c = word_tokenize(b)
print("\nAfter Tokenization: \n", c)

d = [w for w in c if w not in stopwords.words('english')]
print('\nAfter removing stopwords:\n', d)

e = [str(TextBlob(w).correct()) for w in d]
print("\nAfter correcting misspelled words: \n", e)

stemmer = PorterStemmer()
f = [stemmer.stem(w) for w in e]
print("\nAfter Stemming:\n", f)

lemmatizer = WordNetLemmatizer()
g = [lemmatizer.lemmatize(w) for w in e]
print("\nAfter Lemmatization:\n", g)

h = list(ngrams(g, 3))
print("\nList of ngrams(n=3):\n", h)

i = pos_tag(g)
print("\nAfter POS tagging:\n", i)