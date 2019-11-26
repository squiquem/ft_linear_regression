# ft_linear_regression

____

The aim of this project is to introduce you to the basic concept behind machine learning. For this project, you will have to create a program that predicts the price of a car by using a linear function train with a gradient descent algorithm.

## Run
	
To train the model with gradient descent:

	python3 train.py [-h] [-e EPOCHS] [-lr LEARNINGRATE] [-o OUTPUT] file

To predict with the model:

	python3 predict.py [-h] [-sc SCATTER] theta

To calculate the parameters with matrices:

	python3 calculate.py [-h] [-o OUTPUT] file


	positional arguments:
	file                train from data in file
	theta				text file for input

	optional arguments:
	-h, --help          show this help message and exit
	-e EPOCHS, --epochs EPOCHS
                        number of iterations
	-lr LEARNINGRATE, --learningrate LEARNINGRATE
                        learning rate
	-o OUTPUT, --output OUTPUT
                        output file
	-sc SCATTER, --scatter SCATTER
                        data scatter plot
____

## Screenshots

Training
![Rendu 1](https://github.com/squiquem/ft_linear_regression/blob/master/screenshots/train.PNG)

Prediction
![Rendu 2](https://github.com/squiquem/ft_linear_regression/blob/master/screenshots/predict.PNG)

____

If you have any questions or suggestions, feel free to send me an email at squiquem@student.42.fr
