# Workshop 4 — nanoGPT Training Observations

## Experiment 1: Baseline Training

**Dataset:** Tiny Shakespeare  
**Model:** nanoGPT (Character-Level GPT)  
**Device:** CPU

### Model Configuration

| Parameter | Value |
|---|---|
| Training iterations | 2,000 |
| Layers | 4 |
| Attention heads | 4 |
| Embedding dimension | 128 |
| Block size | 64 |
| Batch size | 12 |
| Evaluation iterations | 20 |
| Dropout | 0.0 |

### Training Results

| Metric | Result |
|---|---|
| Final training loss | 1.7648 |
| Final validation loss | 1.8857 |
| Final iteration loss | 1.6958 |
| Model checkpoint | `out-shakespeare-char/ckpt.pt` |

### Observations

The model successfully completed 2,000 training iterations on the Shakespeare dataset using CPU-based training.

During the final iterations, individual batch losses fluctuated, with values generally between 1.6 and 2.0.

The final evaluated training loss was 1.7648, while validation loss was 1.8857. The validation loss being slightly higher suggests the model performs better on its training data than on unseen validation data.

The trained model checkpoint was successfully saved for future text generation experiments.


## Experiment 2: Reduced Training Iterations

**Objective:** Observe how reducing training iterations affects model loss.

**Configuration:**
- Maximum iterations: 1,000
- Layers: 4
- Attention heads: 4
- Embedding dimension: 128
- Block size: 64
- Batch size: 12
- Learning-rate decay iterations: 1,000

**Results:**
- Final training loss: 2.0461
- Final validation loss: 2.1114
- Model checkpoint: `out-experiment-2/ckpt.pt`

**Comparison:**

The 2,000-iteration experiment achieved lower training and validation losses than the 1,000-iteration experiment.

The results suggest that additional training helped the model learn more effectively from the Shakespeare dataset. Individual batch losses fluctuated during training, which is expected.

Because the learning-rate decay schedule was also changed, the results should be interpreted as a comparison of two training configurations rather than an isolated test of iteration count.

**Conclusion:**

The longer training configuration achieved better final loss values. Further controlled experiments would help isolate the effect of training iterations on model performance.

## Experiment 3: Increasing Transformer Layers

**Objective:** Analyze how increasing transformer layers affects model performance and training time.

**Configuration:**
- Training iterations: 1,000
- Transformer layers: 6
- Attention heads: 4
- Embedding dimension: 128
- Block size: 64
- Batch size: 12
- Evaluation iterations: 20
- Learning-rate decay iterations: 1,000

**Results:**
- Final training loss: 2.0932
- Final validation loss: 2.1266
- Final batch loss: 2.0625
- Model checkpoint: `out-experiment-3/ckpt.pt`

**Comparison with Experiment 2:**

The 4-layer model achieved a training loss of 2.0461 and validation loss of 2.1114, while the 6-layer model achieved a training loss of 2.0932 and validation loss of 2.1266.

Increasing the number of transformer layers did not improve the final loss in this experiment. The 6-layer model also appeared to require more computation per training iteration.

**Conclusion:**

Increasing model depth does not automatically guarantee better performance. Training duration, optimization settings, and model initialization can influence the results.

## Experiment 4: Increasing Embedding Dimensions

**Objective:** Evaluate how increasing the embedding dimension affects training performance and computational cost.

**Configuration:**
- Training iterations: 1,000
- Transformer layers: 4
- Attention heads: 4
- Embedding dimension: 256
- Block size: 64
- Batch size: 12
- Evaluation iterations: 20
- Learning-rate decay iterations: 1,000

**Results:**
- Final training loss: 1.7512
- Final validation loss: 1.8783
- Final batch loss: 1.8490
- Checkpoint: `out-experiment-4/ckpt.pt`

**Comparison with Experiment 2:**

The model with embedding dimension 128 achieved a training loss of 2.0461 and validation loss of 2.1114.

Increasing the embedding dimension to 256 reduced training loss to 1.7512 and validation loss to 1.8783.

However, training iterations became slower, increasing from approximately 40–50 milliseconds to 105–120 milliseconds in the observed final iterations.

**Conclusion:**

Increasing the embedding dimension improved model performance in this experiment but required more computation. This illustrates the trade-off between model capacity and training efficiency.

## Experiment 5: Increasing Evaluation Iterations

**Objective:** Investigate how increasing evaluation iterations affects loss estimation and evaluation overhead.

**Configuration:**
- Maximum training iterations: 1,000
- Transformer layers: 4
- Attention heads: 4
- Embedding dimension: 128
- Evaluation iterations: 50
- Batch size: 12
- Block size: 64
- Learning-rate decay iterations: 1,000

**Results:**
- Final training loss: 2.0685
- Final validation loss: 2.1164
- Final batch loss: 2.1215
- Checkpoint: `out-experiment-5/ckpt.pt`

**Comparison with Experiment 2:**

Experiment 2 used 20 evaluation iterations and achieved a training loss of 2.0461 and validation loss of 2.1114.

Experiment 5 used 50 evaluation iterations and achieved a training loss of 2.0685 and validation loss of 2.1164.

The evaluated loss values were similar, with small differences between the experiments.

Increasing evaluation iterations increases the number of batches used to estimate training and validation loss. This can produce a more stable estimate but requires additional evaluation computation.

Because the models were trained separately, the observed loss differences cannot be attributed solely to the change in evaluation iterations.

## Overall Workshop 4 Findings

1. **Training iterations:** The 2,000-iteration configuration achieved lower loss than the 1,000-iteration configuration.
2. **Transformer layers:** Increasing layers from 4 to 6 did not improve loss in the observed experiment.
3. **Embedding dimensions:** Increasing embeddings from 128 to 256 improved training and validation losses but increased training time.
4. **Evaluation iterations:** Increasing evaluation iterations from 20 to 50 produced similar loss estimates and required more evaluation computation.
5. **Best observed configuration:** Experiment 4 achieved the lowest training loss (1.7512) and validation loss (1.8783).

## Conclusion

Successfully trained and evaluated nanoGPT on the Tiny Shakespeare dataset using CPU-based training.

Completed five experiments exploring the effects of training iterations, transformer layers, embedding dimensions, and evaluation iterations.

The results demonstrate trade-offs between model capacity, training duration, evaluation settings, and predictive performance.