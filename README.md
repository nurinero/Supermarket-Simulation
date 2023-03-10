# Supermarket Simulation using Markov Chain
This project simulates a supermarket by utilizing the Markov Chain model. The project aims to mimic the behavior of customers in a real supermarket, and uses an MCMC model to predict customer satisfaction. The simulation takes into account product availability to make predictions about customer satisfaction.

## Technologies Used
* Python
* pandas
* numpy
* random
* argparse
## Project Structure
The project contains two Python files:

1. **market.py**: This file contains the **Supermarket** and **Customer** classes that are used to simulate the movement of customers within the supermarket. The Supermarket class utilizes OOP principles to organize the simulation code. It takes in parameters such as opening and closing times, inventory, transition matrix, and start probabilities to initialize the supermarket simulation. The **Customer** class is used to create customers and calculate their satisfaction scores based on their movement within the supermarket.

2. **main.py**: This file contains the main program that utilizes the **Supermarket** and **Customer** classes to simulate the supermarket.

## How to Run
1. Clone the repository to your local machine.
2. Install the required libraries by running the following command in your terminal: **pip install pandas numpy random argparse**
3. Open the terminal and navigate to the directory where the files are located.
4. Run the program by executing the following command: **python main.py**.
5. The program will run the simulation and display the results in the terminal.
## License
This project is licensed under the terms of the MIT license.
