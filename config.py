

class Config:
    vocab_path = './data/vocab.pkl'
    train_path = './data/train-v1.1.json'
    dev_path   = './data/dev-v1.1.json'
    save = './save'
    max_ctx_len = 600
    hid_size = 100
    emb_size = 300
    max_iter = 2
    maxout_pool_size = 4
    epochs = 10
    batch_size = 100
    learning_rate = 1e-3
    weight_decay = 1e-5
    device = '0'
    save_name = 'weights'
    early_stopping = 2
    dropout = 0.5
