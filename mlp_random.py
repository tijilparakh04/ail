import numpy as np

class SimpleMLP_random:
  def __init__(self, n_inputs, n_hidden1, n_hidden2):
    self.n_inputs = n_inputs
    self.n_hidden1 = n_hidden1
    self.n_hidden2 = n_hidden2

  def run_steps(self, steps):
    for step in range(steps):
      w1 = np.random.randn(self.n_inputs, self.n_hidden1)
      b1 = np.random.randn(self.n_hidden1)
      w2 = np.random.randn(self.n_hidden1, self.n_hidden2)
      b2 = np.random.randn(self.n_hidden2)
      w3 = np.random.randn(self.n_hidden2, 1)
      b3 = np.random.randn(1)

      print(f"\nStep {step + 1}: ")
      print(f"w1: {w1}")
      print(f"b1: {b1}")
      print(f"w2: {w2}")
      print(f"b2: {b2}")
      print(f"w3: {w3}")
      print(f"b3: {b3}")

mlp = SimpleMLP_random(3, 4, 2)
mlp.run_steps(5)