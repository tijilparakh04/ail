def relu(x):
  return np.maximum(0,x)

def relu_derivative(x):
  return (x > 0).astype(float)

class MLP_relu:
  def __init__(self, n_inputs, n_hidden1, n_hidden2):
    self.w1 = np.random.randn(n_inputs, n_hidden1)
    self.b1 = np.random.randn(n_hidden1)
    self.w2 = np.random.randn(n_hidden1, n_hidden2)
    self.b2 = np.random.randn(n_hidden2)
    self.w3 = np.random.randn(n_hidden2, 1)
    self.b3 = np.random.randn(1)
  
  def train(self, X, y, epochs = 1000, lr =0.1):
    for epoch in range(epochs):
      z1 = X.dot(self.w1) + self.b1
      a1 = relu(z1)
      z2 = a1.dot(self.w2) + self.b2
      a2 = relu(z2)
      z3 = a2.dot(self.w3) + self.b3
      output = relu(z3)

      error = y-output

      d_output = error * relu_derivative(output)
      d_w3 = a2.T.dot(d_output)
      d_hidden2 = d_output.dot(self.w3.T) * relu_derivative(a2)
      d_w2 = a1.T.dot(d_hidden2)
      d_hidden1 = d_hidden2.dot(self.w2.T) * relu_derivative(a1)
      d_w1 = X.T.dot(d_hidden1)

      self.w3 += lr * d_w3
      self.w2 += lr * d_w2
      self.w1 += lr * d_w1
      self.b3 += lr * np.sum(d_output, axis = 0)
      self.b2 += lr * np.sum(d_hidden2, axis = 0)
      self.b1 += lr * np.sum(d_hidden1, axis=0)
    
    print("Training Complete")
    print("\nW1: ", self.w1)
    print("\nB1: ", self.b1)
    print("\nW2: ", self.w2)
    print("\nB2: ", self.b2)
    print("\nW3: ", self.w3)
    print("\nB3: ", self.b3)

X = np.random.randint(0, 2, (100, 4))
y = np.random.randint(0,2, (100,1))

mlp = MLP_relu(4, 5, 3)
mlp.train(X, y)
