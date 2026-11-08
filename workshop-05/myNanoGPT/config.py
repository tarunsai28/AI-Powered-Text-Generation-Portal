
"""
Workshop 5 - Twitter Text Generation with nanoGPT
Resume training from 1,000 to 2,000 iterations.
"""

# Output and checkpoint settings
out_dir = 'out_twitter'
init_from = 'resume'
always_save_checkpoint = True

# Evaluation and logging
eval_interval = 1000
eval_iters = 50
log_interval = 10
eval_only = False

# Weights & Biases logging
wandb_log = False
wandb_project = 'twitter-nanogpt'
wandb_run_name = 'twitter-2000-iterations'

# Dataset
dataset = 'twitter'

# Batch and context settings
gradient_accumulation_steps = 1
batch_size = 12
block_size = 64

# GPT model architecture
n_layer = 4
n_head = 4
n_embd = 128
dropout = 0.2
bias = False

# Optimizer settings
learning_rate = 1e-3
weight_decay = 1e-1
beta1 = 0.9
beta2 = 0.99
grad_clip = 1.0

# Training duration
max_iters = 10000

# Learning rate scheduling
decay_lr = True
warmup_iters = 100
lr_decay_iters = 10000
min_lr = 1e-4

# CPU training settings
device = 'cpu'
dtype = 'float32'
compile = False

# Distributed training settings
backend = 'nccl'
