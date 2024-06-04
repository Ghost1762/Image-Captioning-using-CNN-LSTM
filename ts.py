from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# Exemple de batch de légendes
captions = [
    "This is a sample caption",
    "Another example of a caption",
    "Yet another caption for the model",
    # Ajoutez plus de légendes pour atteindre batch_size
]

tokenizer_instance = Tokenizer()
# Tokenisation des légendes
tokenized_captions = tokenizer_instance.texts_to_sequences(captions)

# Longueur maximale de la légende
caption_max_length = 20

# Padding des séquences
padded_captions = pad_sequences(tokenized_captions, maxlen=caption_max_length)

# Taille du tenseur
print(f"Taille du tenseur pour un batch de légendes: {padded_captions.shape}")
