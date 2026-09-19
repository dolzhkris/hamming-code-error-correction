# hamming-code-error-correction
Python implementation of the standard and extended Hamming codes for error detection and correction.

## About

The program works with an 8-bit data sequence and implements two approaches:

* standard Hamming code (12,8);
* extended Hamming code (13,8) with an additional overall parity bit.

The program can simulate transmission errors by changing selected bits, detect errors, correct single-bit errors, and decode the original data.

The project was developed as part of university work during the second/fourth year of university.

## Key Functions

* encode(data) - encodes 8 data bits into a 12-bit Hamming code.
* decode(code) - calculates the error syndrome, corrects a detected single-bit error, and extracts the original data bits.
* encode_rashirenniy(data) - creates the extended Hamming code by adding an overall parity bit.
* check_rashirenniy(code)- checks the extended Hamming code and determines the type of detected error.
* make_error(code, positions) - simulates errors by inverting bits at the specified positions.

## Key Variables

* data - input 8-bit data sequence;
* d - list of input data bits;
* p1, p2, p4, p8 - parity bits of the standard Hamming code;
* code - generated 12-bit Hamming code;
* e - list containing the bits of the encoded sequence;
* s1, s2, s4, s8 - syndrome components;
* error - calculated error position;
* code12 - 12-bit Hamming code used for extended encoding;
* bits - list of bits used to calculate overall parity;
* bit_chetnosti - overall parity bit;
* main - first 12 bits of the extended code;
* total - overall parity result;
* status - description of the detected error condition;
* positions - positions selected for error simulation;
* fixed - corrected standard Hamming code;
* decoded - extracted original data bits;
* fixed_rashirenniy - processed extended Hamming code.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/dolzhkris/hamming-code-error-correction.git
```

2. Run the program:

```bash
python main.py
```

First, enter an 8-bit data sequence. For the standard Hamming code, specify the position of a single error from positions 1 to 12. For the extended Hamming code, enter one or more error positions separated by spaces.
