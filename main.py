# Import the function `neuronal` from the `neuronal` module in the `src` package
from src.neuronal import neuronal

def main():
    """
    Main entry point of the program.
    """
    # Print a message indicating the start of the training
    print("Iniciando el entrenamiento...")
    
    # Call the function to train the neuronal model
    neuronal()
    
    # Print a message indicating the completion of the training
    print("Entrenamiento completado.")

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the main function to start the program
    main()