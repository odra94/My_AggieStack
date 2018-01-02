To run my project you will need Python 3.6.

I ran my project originally using PyCharm. However, you should be able to run it on a terminal on a Mac with python 3.6 or a linux computer with python 3.6.

To run my program please move into the directory containing my project in your terminal. Once you are there type the following:

python3.6 Stack_P4.py

Once the program is running you will see the following symbols “>>” which mean that the program is waiting for input.

You will need to make sure that the following files are also in the directory:
Classes.py
Helpers.py


The Classes.py file contains the classes I made in order to make this project easier to implement

The Helpers.py contains functions that are called in the Stack_P4.py function
————————————————————————

- “python3.6” will specify what version of python to use when running Stack_P4.py.
In addition, every time you run the program the log file will get more information added to it.
It is named “log.txt” and if it does not exist it will be created. It it already exists, the program will add to it.

- The final command in part b, "aggiestack admin add" assumes that for each of the arguments that have a line in the pdf
that we were given, the long singular line is two dashes. There fore you would have to type the command using "--" instead of
a single line. In addition, this command assumes that the server that you are adding was already created at the beginning
when the hardware configuration was uploaded.

This means if you disable server k1, you can later enable server k1 again. But you cannot create a new server named k5 using that command.

- There is a text file called Commands.txt that contains commands supported by this program which can be copy and pasted to test to test out the program.
