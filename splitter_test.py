from langchain_text_splitters import NLTKTextSplitter, RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter  
from langchain_community.document_loaders import PyPDFLoader
import time
import numpy as np
from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import sent_tokenize

def compute_bleu(reference, candidate):
    return sentence_bleu([reference.split()], candidate.split())

def check_sentence_integrity(chunks):
    for i, chunk in enumerate(chunks):
        sentences = sent_tokenize(chunk)
        print(f"Chunk {i+1}: {sentences}")

file_path = (
    "/home/azureuser/Athar/gpt-researcher/my-docs/10k_amd.pdf"
)
loader = PyPDFLoader(file_path)
pages = loader.load_and_split()

page_texts = [page.page_content for page in pages]

# Combine all pages into a single string if needed
full_text = "\n\n".join(page_texts)
# print(full_text)
start_time = time.time()

text_splitter = RecursiveCharacterTextSplitter(
    
    chunk_size=5000,
    chunk_overlap=0,
    length_function=len,
    is_separator_regex=False,separators = ['\n\n']
)


# text_splitter = NLTKTextSplitter(chunk_size=1000, chunk_overlap = 0)i998

# splitter = SentenceTransformersTokenTextSplitter(
#     tokens_per_chunk=384,
#     chunk_overlap=0,
#     )



texts = text_splitter.split_text(full_text)

end_time = time.time()

lengths = [len(chunk) for chunk in texts]
mean_length = np.mean(lengths)
std_deviation = np.std(lengths)
median = np.median(lengths)

print(f"average chunk length is {mean_length} and standard deviation is {std_deviation} and median is {median} and min is {np.min(lengths)} max is {np.max(lengths)}")
# for i in range(10):
#     print(f"chunk {i + 1}: {texts[i]}")
#     print('\n\n')

print(f"chunking time is {end_time - start_time}")

# reference = full_text
# candidate = ' '.join(chunk for chunk in texts)

# bleu_score = compute_bleu(reference, candidate)

# print(bleu_score)



# check_sentence_integrity(texts[:1])