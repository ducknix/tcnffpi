# Turkish Citizen Number Finder From π Number Digits

![](https://img.shields.io/badge/Made%20for-Python-1f425f.svg)
![](https://img.shields.io/github/license/ducknix/tcnffpi.svg)

## Description
In this project, a script was written that detects the Turkish ID number in the pi number.  Results can obtained quickly with threads.

Completely offline. 

>### Algorithm
>* The first digit cannot be 0.
>* When the sum of the 2nd, 4th, 6th and 8th digits of the ID numbers is subtracted from 7 times the sum of the 1st, 3rd, 7th and 9th digits, the remainder of the division by 10 gives us the 10th digit.
>* The remainder of the 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, and 10th digits' sum divided by the 10th digit gives us the 11th digit.
> [(eksisozluk.com)](https://seyler.eksisozluk.com/tc-kimlik-numaralarindaki-inanilmaz-algoritma)

## Usage
```
usage: ./tcnffpi [options]

Turkish Citizen number finder from π number digits

options:
  -h, --help    show this help message and exit
  --digits N    Number of π digits to be processed
  --threads N   An integer for the number of threads
  --output DIR  Path to write found results
  --quiet       The program runs silently
```

## Requirements
* [Python 3.x](https://www.python.org/downloads/ "Download Python | Python.org")
* [mpmath 1.2.1](https://pypi.org/project/mpmath/ "mpmath · PyPI")

## Example
```
python main.py --threads 4 --digits 3000
```
```
Found: 17450284102
Found: 21339360726
Found: 81520920962
Found: 86021394946
Found: 31767523846
Found: 12714526356
Found: 19311881710
Found: 64201989380
Found: 93809525720
Found: 82953311686
Found: 10404753464
Found: 34797753566
Found: 47723501414
Found: 79178608578
Found: 56042419652
Found: 46575739624
Found: 57640789512
Found: 74623436454
Found: 85844479526
Found: 98387447808
Found: 91197939952
Found: 10159195618
Found: 56181467514
Found: 14269123974
```
