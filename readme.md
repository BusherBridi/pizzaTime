Pizza Time!!!
======
College circuit analysis project. Interface between Domino's Pizza API and physical circuitry. Uses lasers, photoresistors, and a Raspberry Pi microprocessor as the bridge between software and hardware.

## Getting Started
First, build the circuit, refer to the Ki-Cad schematic. Ideally, build a housing around the photoresistors to keep ambient light out. Then prepare the Raspberry Pi by flashing an operating system to an SD card. the Linux Debian flavor NOOBS for Pi was used in this project and is recomended.

### Prerequisits
Python 2.#.#

### Installing
After cloning the repository, start by installing the prequists from REQUIREMENTS.txt using pip: "pip install -r requirments.txt"

### Usage
First, run menuSearch.py, this allows to search the Domino's pizza menu and lookup the codes for pizzas, drinks, etc.
Then open pizzaTime.py in a terminal editor on the Pi such as vim (you can install vim on NOOBS by using the apt package manager, "apt get-install vim" you have to run this as root).
In the editor, at the bottom of pizzaTime.py, enter the codes of the pizzas you want to assign to each photoresistor. 
Then go back up and fill out all the info such as adress, payment information, phone number, etc.
after it is complete, exit out of the editor then simply run in the terminal on the Pi, "python pizzaTime.py"

--Alternativly, you can run the script on your desktop without a circuit. After installing the requirements.txt using pip simply run "python pizzaOrder.py" to run the script in a terminal. It will prompt you for your info and you can search and add to your order real time.

### Built With
1. Python
2. Ki-Cad
3. pizzaApi (https://github.com/gamagori/pizzapi)

### Contribuiting
Refer to CONTRIBUTORS.md

### Authors
Busher Bridi (https://github.com/busherbridi)

### License
This software is open-source and free to use with no restrictions.

