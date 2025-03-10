# Neural Network Implementation

This repository contains two Python scripts that demonstrate the implementation of a simple neural network for binary classification. Below is an explanation of the general functionality of each script.

---

## 1. `main.py`

### Overview
This script serves as the entry point for the program. It imports a neural network function from a module and executes the training process.

### Functionality
- **Imports**: The script imports the `neuronal` function from the `neuronal` module located in the `src` package.
- **Main Function**:
  - Prints a message indicating the start of training.
  - Calls the `neuronal` function to train the neural network.
  - Prints a message indicating the completion of training.
- **Execution**: The script checks if it is being run directly (not imported as a module) and calls the `main` function to start the program.

---

## 2. `neuronal.py`

### Overview
This script implements a simple neural network from scratch using NumPy and Matplotlib. It generates a synthetic dataset, defines activation and loss functions, initializes network parameters, and trains the model using gradient descent.

### Functionality
1. **Dataset Generation**:
   - Creates a synthetic dataset using `make_gaussian_quantiles` from `sklearn.datasets`.
   - The dataset consists of 1000 samples with 2 features and 2 classes.
   - Plots the dataset using Matplotlib.

2. **Activation Functions**:
   - **Sigmoid**: Used for binary classification in the output layer.
   - **ReLU**: Used in hidden layers for non-linearity.

3. **Loss Function**:
   - **Mean Squared Error (MSE)**: Used to measure the difference between predicted and actual values.

4. **Network Initialization**:
   - Initializes weights and biases for each layer of the network using random values.

5. **Training**:
   - Implements forward propagation to compute predictions.
   - Implements backpropagation to update weights and biases using gradient descent.
   - Tracks and prints the loss during training.

6. **Testing**:
   - Generates a test dataset and uses the trained model to make predictions.
   - Plots the test dataset with predicted labels.

7. **Visualization**:
   - Plots the training error over time.
   - Visualizes the decision boundary of the trained model.

---

## How to Run

1. Clone the repository or download the source code.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
3. Run the main.py file:
   ```bash
   python main.py
4. The script will:
    - Train the neural network.
    - Display plots of the dataset, training error, and test predictions.