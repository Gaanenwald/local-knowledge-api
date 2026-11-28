from config import Settings
from registries import TOKENIZER_MODELS, TOKENIZER_BACKENDS


def tokenizer_init(settings: Settings):
    tokenizer_model = TOKENIZER_MODELS[settings.embedding_model]
    tokenizer_backend = TOKENIZER_BACKENDS[settings.tokenizer_backend]
    return tokenizer_backend(model_name=tokenizer_model)
