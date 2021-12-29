# Turkish Citizen Number Finder From π Number Digits

![](https://img.shields.io/badge/Made%20for-Python-1f425f.svg)
![](https://img.shields.io/github/license/{ducknix}/{tcnffpi}.svg)

## Description
In this project, a script was written that detects the Turkish ID number in the pi number.  Results can obtained quickly with threads.

Completely offline. 

>### Algorithm
>* The first digit cannot be 0.
>* When the sum of the 2nd, 4th, 6th and 8th digits of the ID numbers is subtracted from 7 times the sum of the 1st, 3rd, 7th and 9th digits, the remainder of the division by 10 gives us the 10th digit.
>* The remainder of the 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, and 10th digits' sum divided by the 10th digit gives us the 11th digit.
> [(eksisozluk.com)](https://seyler.eksisozluk.com/tc-kimlik-numaralarindaki-inanilmaz-algoritma)

## Usage
```bash
python main.py --threads [1-4] --digits [11 - n+11] --output [PATH] --quiet [default: False]
```

## Requirements
* [Python 3.x](https://www.python.org/downloads/ "Download Python | Python.org")
* [mpmath 1.2.1](https://pypi.org/project/mpmath/ "mpmath · PyPI")

## Example
```zsh
./main.py --threads 4 --digits 14200 --output ../example.txt
```
