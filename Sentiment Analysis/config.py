
import transformers
DEVICE = 'cuda'
MAX_LEN = 256
TRAIN_BATCH_SIZE = 4
Truncation = True
VALID_BATCH_SIZE = 4
EPOCHS =10
ACCUMULATION = 2
BERT_PATH = "/content/drive/My Drive/NLP/input/bert_base_uncased"
MODEL_PATH = "model.bin"
TRAINING_FILE = "/content/drive/My Drive/NLP/input/IMDB.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(
        BERT_PATH,
        do_lower_case = True
    )