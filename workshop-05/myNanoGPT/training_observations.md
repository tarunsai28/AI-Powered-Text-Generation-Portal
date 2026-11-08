# Workshop 5 — Twitter Text Generation with nanoGPT

## Objective
Train a character-level nanoGPT model using cleaned Twitter conversations from Workshop 3 and generate new text.

## Dataset
- Source: Workshop 3 cleaned Twitter conversations
- Total conversations: 10,628
- Total characters: 591,109
- Vocabulary size: 437
- Training tokens: 531,998
- Validation tokens: 59,111

## Model Configuration
- Transformer layers: 4
- Attention heads: 4
- Embedding dimension: 128
- Batch size: 12
- Block size: 64
- Training iterations: 1,000
- Device: CPU

## Training Results
- Final training loss: 2.4214
- Final validation loss: 2.4521
- Checkpoint directory: `out_twitter`

## Generated Text Sample

> you dol.....
> I you deay dit
> gent you itin some ofe be y tal, wie this she ay nou I a busing eve you beea tre dooo get told.

## Observations
1. The model successfully completed 1,000 training iterations.
2. Training and validation losses were relatively close.
3. Generated text contained recognizable English fragments but lacked coherent sentence structure.
4. The character-level vocabulary included emojis, punctuation, and multilingual characters.
5. The limited training duration and small model capacity likely contributed to poor text quality.

## Conclusion
Successfully prepared a custom Twitter dataset, trained nanoGPT, saved a checkpoint, and generated text. Future experiments could improve text quality through additional training, model tuning, and larger datasets.

## Experiment 2 — Continued Training to 2,000 Iterations

The existing Twitter nanoGPT checkpoint was resumed from 1,000 iterations and trained to 2,000 total iterations.

### Results
- Training loss at 1,000 iterations: 2.4214
- Validation loss at 1,000 iterations: 2.4521
- Training loss at 2,000 iterations: 2.2758
- Validation loss at 2,000 iterations: 2.3097

### Generated Text Sample

> whate his you art and there the so you shes dit frel annd pore stund its obed and afer I the fore for sto we

### Observations
1. Training loss decreased by approximately 6.0%.
2. Validation loss decreased by approximately 5.8%.
3. The model continued learning character-level patterns.
4. Generated text contained recognizable English words but remained largely incoherent.
5. Additional training improved predictive performance, but coherent text generation remains a challenge.

### Conclusion
Continuing training from 1,000 to 2,000 iterations improved both training and validation loss. Further experimentation with training duration, model architecture, and tokenization may improve generation quality.


## Experiment 3: GPT-2 BPE Tokenization

### Dataset
- Source: 10,628 cleaned Twitter conversations
- Total characters: 591,109
- Tokenizer: GPT-2 BPE
- Vocabulary size: 50,257
- Training tokens: 148,691
- Validation tokens: 16,332

### Model Configuration
- Transformer layers: 4
- Attention heads: 4
- Embedding dimension: 128
- Context length: 64
- Batch size: 12
- Device: CPU
- Training iterations: 5,000

### Training Results
- Final training loss: 3.7246
- Final validation loss: 6.2417
- Checkpoint: out_twitter_bpe

### Generated Text Observations
The BPE model generated recognizable English words,
informal Twitter-style expressions, and emojis.

Example:
"I'm still a person who tried to go back to be happy :)"

However, sentence coherence and grammar remained
inconsistent.

### Challenges
- Larger vocabulary increased computational cost.
- Limited training data contributed to poor generalization.
- The large gap between training and validation loss
  suggests overfitting.

### Conclusion
GPT-2 BPE tokenization reduced the number of tokens
needed to represent the dataset and enabled generation
of recognizable words and social-media expressions.

However, the limited dataset was insufficient for
strong conversational coherence.

Future improvements could include:
- Using a larger training dataset
- Training a smaller custom BPE vocabulary
- Fine-tuning a pretrained language model
- Evaluating generation quality on held-out prompts
