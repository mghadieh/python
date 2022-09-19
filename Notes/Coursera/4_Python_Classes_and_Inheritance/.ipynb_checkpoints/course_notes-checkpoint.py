{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "49f7c527",
   "metadata": {},
   "source": [
    "# Course 4: Python Classes and Inheritance"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "79ddfe39",
   "metadata": {},
   "source": [
    "## Week 1: Classes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3df99279",
   "metadata": {},
   "source": [
    "### Chapter 1: Constructing Classes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd19cc05",
   "metadata": {},
   "source": [
    "#### User-defined Classes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3d2a35de",
   "metadata": {},
   "source": [
    "Creating a class"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0901b97",
   "metadata": {},
   "source": [
    "class Point():\n",
    "    pass"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f3d98aad",
   "metadata": {},
   "source": [
    "Create an instance of point class"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d71eec86",
   "metadata": {},
   "source": [
    "#Code Block \n",
    "point1 = Point()\n",
    "\n",
    "print(point1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a90cbd5d",
   "metadata": {},
   "source": [
    "Create an instance variable which would live inside the instance"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "370d037f",
   "metadata": {},
   "source": [
    "#Code Block \n",
    "point1.x = 5"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb5feaf3",
   "metadata": {},
   "source": [
    "#Code Block \n",
    "print(point1.x)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2bacb996",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e2cc0f70",
   "metadata": {},
   "source": [
    "Instead of accessing the variable x directly, we can create a function inside Point class such as: (refer to part two in Point class definition) <br>\n",
    "class Point():\n",
    ">def getX(self):\n",
    ">>return self.x <br>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee2b9a4c",
   "metadata": {},
   "source": [
    "#Code Block \n",
    "class Point():    \n",
    "    def getX(self):\n",
    "        return self.x\n",
    "print(point1.getX())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f6d6f3e",
   "metadata": {},
   "source": [
    "in class point, 'self' is the instance itself. So, point1.getX() means that self is the instance point1."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f74a8c9b",
   "metadata": {},
   "source": [
    "**Docstrings**: is used to add documentation to a piece of code in python. For more info: https://www.geeksforgeeks.org/python-docstrings/\n",
    "<br>*Note: If the first line after the class header is a string, it becomes the docstring of the class, and will be recognized by various tools. (This is also the way docstrings work in functions.)*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dfe33e95",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bae08c60",
   "metadata": {},
   "source": [
    "#### Adding Parameters to the Constructor"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c456cc2a",
   "metadata": {},
   "source": [
    "**Constructor**: aka *'initializer method'*, is automatically called whenever a new instance of Point is created. It gives the programmer the opportunity to set up the attributes required within the new instance by giving them their initial state values. ( refert to part 3 in point class definition above)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f0389ad1",
   "metadata": {},
   "source": [
    "So now, `__init__(self,x,y)` is expecting two variables (x and y) when a new object is being created. (refer to part 3 in point1 instance creation above)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4dae566b",
   "metadata": {},
   "source": [
    "#Code Block \n",
    "class Point():    \n",
    "    def __init__(self,x,y):\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "        \n",
    "    def getX(self):\n",
    "        return self.x\n",
    "\n",
    "point1 = Point(1,2)\n",
    "\n",
    "print(point1.getX())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "63cebbb9",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "581cf824",
   "metadata": {},
   "source": [
    "#### Adding other Methods to a Class"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d28d7415",
   "metadata": {},
   "source": [
    "#Code Block \n",
    "class Point():    \n",
    "    def __init__(self,x,y):\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "        \n",
    "    def getX(self):\n",
    "        return self.x\n",
    "    \n",
    "    def getY(self):\n",
    "        return self.y\n",
    "        \n",
    "    def __str__(self):     # when print() function is called, this method will overwrite the built in function\n",
    "        return 'coordinates are ({},{})'.format(self.x, self.y)\n",
    "    \n",
    "point1 = Point(10,100)\n",
    "print(point1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "003af6c9",
   "metadata": {},
   "source": [
    "### Chapter 2: Objects and Instances"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e678f16a",
   "metadata": {},
   "source": [
    "Resume from first video"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f3d70f30",
   "metadata": {},
   "source": [
    "## Week 2: Inheritance"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2944ae75",
   "metadata": {},
   "source": [
    "### Chapter 3: Inheritance"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d94f13d4",
   "metadata": {},
   "source": [
    "## Week 3: Unit Testing and Exceptions"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f2a9685d",
   "metadata": {},
   "source": [
    "### Chapter 4: Writing Test Cases"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "02111b46",
   "metadata": {},
   "source": [
    "### Chapter 5: Exceptions"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
