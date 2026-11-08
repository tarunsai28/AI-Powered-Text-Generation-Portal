
"""
Workshop 5 - Twitter Text Generation with nanoGPT
Experiment: GPT-2 BPE Tokenization

Dataset: 10,628 cleaned Twitter conversations
Training tokens: 148,691
Validation tokens: 16,332
Vocabulary size: 50,257

Train a new GPT model from scratch using BPE tokens.
"""

# --------------------------------------------------
# Output and checkpoint settings
# --------------------------------------------------

out_dir = 'out_twitter_bpe'
init_from = 'scratch'
always_save_checkpoint = True

# --------------------------------------------------
# Evaluation and logging
# --------------------------------------------------

eval_interval = 500
eval_iters = 50
log_interval = 10
eval_only = False

wandb_log = False
wandb_project = 'twitter-nanogpt'
wandb_run_name = 'twitter-bpe-5000'

# --------------------------------------------------
# Dataset
# --------------------------------------------------

dataset = 'twitter_bpe'

# --------------------------------------------------
# Batch and context settings
# --------------------------------------------------

gradient_accumulation_steps = 1
batch_size = 12
block_size = 64

# --------------------------------------------------
# GPT model architecture
# --------------------------------------------------

n_layer = 4
n_head = 4
n_embd = 128

dropout = 0.2
bias = False

# GPT-2 BPE vocabulary
vocab_size = 50304

# --------------------------------------------------
# Optimizer settings
# --------------------------------------------------

learning_rate = 1e-3
weight_decay = 1e-1

beta1 = 0.9
beta2 = 0.99

grad_clip = 1.0

# --------------------------------------------------
# Training iterations
# --------------------------------------------------

max_iters = 5000

# --------------------------------------------------
# Learning rate scheduling
# --------------------------------------------------

decay_lr = True

warmup_iters = 100
lr_decay_iters = 5000

min_lr = 1e-4

# --------------------------------------------------
# CPU training configuration
# --------------------------------------------------

device = 'cpu'
dtype = 'float32'
compile = False

# --------------------------------------------------
# Distributed training
# --------------------------------------------------

backend = 'nccl'
