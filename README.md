###ABOUT

Computer Programming lab manual written in Python.

###IMPORTANT NOTE

There is no main() function in python but a runtime variable named __name__ is passed with __main__ as value to acknowledge that this program was executed from command line.

For example following line is executed before executing your Python program by default: 

__name__ = "__main__"

###NOMENCLATURE

I am using some nomenclature for file names to write lab manual programs from C to Python.

Examples:

e2_e1.py - Where e2 = "Experiment 2" and e1 = "Excercise 1"<br>
e2_a1.py - Where e2 = "Experiment 2" and a1 = "Assignment 1"

Please note Excercises and Examples are considered one thing. So if an experiment has some examples and some exercises, count them linearly from 1 to N.

###HOW TO RUN

If you have Python installed, you can write following command in either Command Prompt or Terminal to execute programs.

$ python e2_e1.py

###OTHER NOTES

1. \#include from C is import in python.

    Examples:

    from module import anything<br>
    from module.file import anything

    Relevant Examples:

    from helpers import getch <br>
    from helpers.getch import getch

2. There is no getch() in Python. To clarify there is no built-in way in Python to read single character from console so we use custom made functions. They are located in helpers/ folder.

3. Some examples/excercises are repeated in some experiments and those programs are not written.

4. For experiment no. 8, I am not doing examples but only exercises.

5. Experiment no. 9 assignments are not done because there is no do while in Python. 