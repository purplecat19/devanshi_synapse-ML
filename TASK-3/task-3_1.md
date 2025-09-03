# Techniques to convert text into numbers for NLP (on [docs](https://docs.google.com/document/d/1gTBhhQSipeKBMtELaNR7cuxIiogdwR89WRNh85X8DdY/edit?tab=t.0))

We humans read words and instantly “get” what they mean. But machines? Not really. To them, text is just a bunch of characters. They only understand numbers, so we need to translate these words into math. This is where **NLP (Natural Language Processing)** comes in. It turns language into vectors and stats. Once our text is converted to numbers, algorithms can finally spot patterns, trends, and meaning. 

There are a number of ways to do this, all of them having their own ups and downs.  

- **One-Hot encoding**  
- **Bag of Words**  
- **Bag of N-grams**  
- **TF-IDF**  
- **Word Embeddings**  
- **Document Embeddings**  

I’ll break all of them down below:



## 1. One-Hot encoding (simple but very limited)

Each word/character gets a number, and these numbers are represented as a vector of ones and zeros.

**Eg:** *I wanna go trekking*

Here, each word can be converted to a number (1,2,3,4), and now we one-hot encode these into vectors of length 4, so  
- *I* -> [1 0 0 0]  
- *wanna* -> [0 1 0 0]  
- *go* -> [0 0 1 0]  
- *trekking* -> [0 0 0 1]  

So our sentence becomes:  
[1 0 0 0], [0 1 0 0], [0 0 1 0], [0 0 0 1]

**Downside:** If your vocab has like 50,000 words, your vectors are gonna be really huge with 49999 zeros and one 1 chilling somewhere. Not efficient at all.



## 2. Bag of Words (simple but context-blind)

This one just counts how many times each word shows up, ignoring order and meaning.  
Considering our previous ex: *“I wanna go trekking”* -> [1 1 1 1]  
But if I write *“trekking trekking I go”*, it will be -> [1 0 1 2]

BoW is easy to set up and great for comparing documents. But vectors get massive with: large vocabs, words that mean similar, etc, and the order is completely lost.  
Sentences like *“jia ate icecream”* will be equal to *“icecream ate jia”*.



## 3. Bag of N-Grams (adds context but gets messy fast)

Instead of single words, here we take groups of words (called **n-grams**).  
**Eg:** bigrams (n=2): *“I wanna go trekking”* -> [“I wanna”, “wanna go”, “go trekking”]

We catch a bit of context this way, since phrases matter more than just loose words. But the vocabulary increases and gets really scattered, especially as n increases. If new phrases show up, your model will go *“???”*.



## 4. TF-IDF (smarter word weighting)

Not all words are equally useful. **TF-IDF** treats some words more important than others. Words that appear more often in one doc and less often in others are considered important to the meaning of a document, and thus get assigned a higher score. Words that have similar frequencies across all docs are given lower scores.

Here,  
- **TF** -> *Term Frequency* (how often a word appears in a doc)  
- **IDF** -> *Inverse Document Frequency* (how rare that word is across all docs)  

**TF*IDF** -> gives a TF-IDF score for a word, and each doc is encoded as a vector of all the TF-IDF scores for all the words in that doc.  

**Eg:** *“I wanna go trekking”*, *I* will have a really low score as it is super common while *trekking* will have a relatively high score, as it is context-specific.



## 5. Word Embeddings (Word2Vec, GloVe, fastText)

**Embedding** -> capture a word’s meaning in a low dimensional space.  
**Word2Vec** (in 2013) introduced word embeddings in NLP, and allowed capturing simple word analogy relationships like:  

*King - Man + Woman ≈ Queen*  

The algorithm creates a vector for each word in a doc to measure its relationship with other words and its meaning in general.

Most embeddings are pretrained (like Wikipedia), so you don’t waste compute. But out of vocab words (**OOV**) confuse the model and it has no clue what to do.  
Facebook’s **fastText** patched this by breaking words into smaller n-grams so even new words can be built from familiar groups.  
Embeddings also don’t care about word order in long texts, they just summarise meanings.



## 6. Document Embeddings (Doc2Vec)

Word vectors are cool but when you want to embed whole paragraphs or long documents, it’s very tedious. This is where **Doc2Vec** comes in. It extends word embeddings to represent entire texts while keeping context.

It is used in text classification, tagging, recommendations, and early chatbots that used to just copy FAQs back to you.

Embeddings are context-heavy so they’re only good as the data they were trained on. If trained on tech blogs, *“apple”* will mean iPhones, MacBooks. But if you train it on a fruit dataset, *“apple”* becomes a snack.

Still, embeddings are the foundation of modern NLPs!



## Beyond these, here are some of the “modern heavyweights”:

- **Contextual Embeddings (ELMo, BERT, GPT-style models):** Unlike Word2Vec/GloVe (which give one fixed vector per word), these adjust word meaning based on context. So *“bank”* in *river bank* ≠ *“bank”* in *money bank*.  

- **Transformers (BERT, RoBERTa, GPT, etc.):** The backbone of modern NLP. Use self-attention to understand relationships between words across an entire text. Extremely powerful, but heavy on compute.  

- **Sentence & Document Transformers (Sentence-BERT, Universal Sentence Encoder):** Extend contextual embeddings to full sentences/paragraphs, making them useful for semantic search, clustering, and recommendation.  

These capture meaning based on context, understand word relationships across entire texts, and power most of today’s apps. They’re insanely effective, but also way more resource-hungry than earlier methods.



## Conclusion

Turning words to numbers sounds like a boring technical step, but it’s literally the bridge that lets machines “read.” From baby methods like One-Hot and Bag of Words, to smarter ones like embeddings and transformers, each technique levels up how well computers can capture meaning.  

The choice depends on the problem: *small/simple -> go basic, complex/real-world -> bring out the complex ones.* Either way, it’s all just math helping machines make sense of our language.
