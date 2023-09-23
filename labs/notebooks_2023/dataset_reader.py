import torch
from torch.utils.data import Dataset
# This will load the dataset and process it lazily in the __getitem__ function
class ClassificationDatasetReader(Dataset):
  def __init__(self, df, tokenizer):
    self.df = df
    self.tokenizer = tokenizer

  def __len__(self):
    return len(self.df)

  def __getitem__(self, idx):
    row = self.df.values[idx]
    # Calls the text_to_batch function
    input_ids,seq_lens = text_to_batch_bilstm([row[0]], self.tokenizer)
    label = row[1]
    return input_ids, seq_lens, label