import nltk

from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer, WordNetLemmatizer


def clase13_a():
    print("--- CLASE 13: Natural Language Toolkit ---------------------------------")
    print("--- 08-04-24 -----------------------------------------------------------")

    # Ejecutar la primera vez para descargar los
    print("Descargando recursos de nltk")
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')

    paragraph = (
        "As the sun dipped below the horizon, casting hues of orange and pink across the sky, the tranquil waves gently lapped against the shore. Seagulls soared overhead, their calls blending with the distant laughter of children playing in the sand. It was a moment frozen in time, a scene of serene beauty that whispered secrets of eternity.")

    tokens = nltk.word_tokenize(paragraph)
    sentences = nltk.sent_tokenize(paragraph)

    print("Tokens: ", tokens)
    print("----------------------------")
    print("Sentences: ", sentences)
    print("----------------------------")

    # Stop words -------------------------------------
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))  # Puede ser en español
    # Remove stop words from tokens
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    print("Filtered Tokens: ", filtered_tokens)
    print("----------------------------")

    # Stemming ---------------------------------------
    # Stemming is the process of reducing a word to its word stem
    ps = PorterStemmer()
    lematizar = WordNetLemmatizer()

    stemmed_words = [ps.stem(word) for word in filtered_tokens]
    lematizad_words = [lematizar.lemmatize(word) for word in filtered_tokens]

    print("Stemmed Words: ", stemmed_words)
    print("----------------------------")
    print("Lemmitized Words: ", lematizad_words)
    print("----------------------------")

    # Frequency Distribution --------------------------
    f_dist = FreqDist(filtered_tokens)
    print("Most common words: ", f_dist.most_common(5))
    print("----------------------------")

    # Part of speech tagging --------------------------
    tagged_words = nltk.pos_tag(filtered_tokens)
    print("Tagged Words: ", tagged_words)
    print("----------------------------")
