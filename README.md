###ABOUT

Computer Programming lab manual written in Python.

###IMPORTANT NOTE

There is no main() function in python but a runtime variable named \_\_name\_\_ is passed with \_\_main\_\_ as value to acknowledge that this program was executed from command line.

For example following line is executed before executing your Python program by default

\_\_name\_\_ = "\_\_main\_\_"

###NOMENCLATURE

I am using some nomenclature for file names to write lab manual programs from C to Python.

Examples:

e2_e1.py - Where e2 = "Experiment 2" and e1 = "Excercise 1"<br>
e2_a1.py - Where e2 = "Experiment 2" and a1 = "Assignment 1"

Please note Excercises and Examples are considered one thing. So if an experiment has some examples and some exercises, count them linearly from 1 to N.

###HOW TO SETUP ENVIRONMENT

####WINDOWS XP

1. Install Python 2.7.x (I used 2.7.4). Use MSI installer.
2. Add python to system PATH variable.
    1. Start > Right Click My Computer > Properties > Advanced Tab > Click Environment Variables
    2. Edit "Path" variable value under System Variables and append ";C:\Python27" or wherever you installed python.

###HOW TO RUN

If you have Python installed, you can write following command in either Command Prompt or Terminal to execute programs.

python e2_e1.py

For example if you are at directory **C:\CPLAB\Project**, you can write:

**C:\\CPLAB\Project\\ $** python e2_e1.py

###OTHER NOTES

1. \#include from C is import in python.

    Examples:

    from module import anything<br>
    from module.file import anything

    Relevant Examples:

    from helpers import getch <br>
    from helpers.getch import getch

2. There is no getch() or getche() in Python. To clarify there is no built-in way in Python to read single character from console so we use custom made functions. They are located in helpers/ folder.

3. Some examples/excercises are repeated in some experiments and those programs are not written.

4. For experiment no. 8, I am not doing examples but only exercises.

5. Experiment no. 9 assignments are not done because there is no do-while in Python. 

6. Experiment no. 14 is not done because Pyhton has no structs.
7. clrscr() in Unix/Linux is system("clear") but in windows it is system("cls"). My programs are written on Linux so it's system("clear") in all programs of mine.