import matplotlib.pyplot as plt
import numpy as np

#we want to keep our root install clean, so we installl in specific projects through a virtual environment
#when we do it this way, the thrid party installer will be on one project
#1: Create a virtual environment (for windows, the command is py-3-m venv __name of your virtual environment____)
#All it does it make a copy of the root install (python) and put it in the folder
#2: Activate your virtual environment (for pc, it is directory locations/scripts/activate)
#3: Install your third party library (pip3 install ___name of the library____)

x = np.linspace(0, 20, 100)
plt.plot(x,np.sin(x))
plt.show()

print("Hello there!")

#github: an application that allows us to keep track of changes to our website
#source control and version control
#version control: Everything related to your project (html, css, photos, videos)
#source control: talking specifically about source code (only css and html)
#initialize repository button is our baseline code

print("Hello again!")