import numpy as np

def calculate(arr):
  if len(arr) != 9:
    raise ValueError("List must contain nine numbers.")

  arr = np.array(arr)
  matrice = arr.reshape(3,3)

  calculation = {  'mean': [matrice.mean(axis=0).tolist(), matrice.mean(axis=1).tolist(), arr.mean().tolist()],
  'variance': [matrice.var(axis=0).tolist(), matrice.var(axis=1).tolist(), arr.var().tolist()],
  'standard deviation': [matrice.std(axis=0).tolist(), matrice.std(axis=1).tolist(), arr.std().tolist()],
  'max': [matrice.max(axis=0).tolist(), matrice.max(axis=1).tolist(), arr.max().tolist()],
  'min': [matrice.min(axis=0).tolist(), matrice.min(axis=1).tolist(), arr.min().tolist()],
  'sum': [matrice.sum(axis=0).tolist(), matrice.sum(axis=1).tolist(), arr.sum().tolist()]
  }

  return calculation