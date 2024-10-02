# Bit-Rate Calculation Program

This Python program calculates the **Bit-Rate** based on user input such as the average size of a package, delay, and time intervals. It also computes the number of bits transmitted in a specific time frame.

## Features

- User inputs average package size, maximum delay, propagation delay, and time intervals.
- The program checks for valid inputs, ensuring that the propagation delay is within the maximum delay.
- It calculates the **Bit-Rate** and the number of bits transmitted between two time intervals.
  
## How the Program Works

1. **Input Package Size (L)**: The user inputs the average size of the package. The input is validated to ensure it is non-negative.
2. **Input Maximum Delay (D_max)**: The user inputs the maximum allowable delay, which is also checked to be non-negative.
3. **Input Propagation Delay (prop)**: The user inputs the actual propagation delay. The program ensures it is non-negative and does not exceed the maximum delay \(D_{\text{max}}\).
4. **Input Time Intervals (t1, t2)**: The user inputs two time points, \(t_1\) and \(t_2\), where \(t_2 > t_1\). Both time values must be non-negative.
5. **Bit-Rate Calculation**: Using the formula:
   \[
   \text{Bit-Rate} = \frac{L}{|D_{\text{max}} - \text{prop}|}
   \]
   the program computes the Bit-Rate.
6. **Number of Bits Transmitted**: The program calculates the total number of bits transmitted between \(t_1\) and \(t_2\) using the formula:
   \[
   \text{Bits Transmitted} = \text{Bit-Rate} \times (t_2 - t_1)
   \]

## Program Structure

- **Error Handling**: The program validates user inputs to ensure they are within acceptable ranges. It continuously prompts the user to re-enter values until valid inputs are provided.
- **Formulas**:
  - **Bit-Rate**: 
    \[
    \text{Bit-Rate} = \frac{L}{|D_{\text{max}} - \text{prop}|}
    \]
  - **Number of Bits**:
    \[
    \text{Bits Transmitted} = \text{Bit-Rate} \times (t_2 - t_1)
    \]

## How to Use

### Prerequisites

- **Python 3.x** installed.

### Running the Program

1. **Clone the repository** (or download the code):

   ```bash
   git clone https://github.com/yourusername/Bit-Rate-Calculation.git
   ```

2. **Run the program**:

   ```bash
   python bit_rate_calculation.py
   ```

3. **Input Parameters**:

   The program will prompt you to enter the following parameters:

   - Average size of the package \(L\).
   - Maximum delay \(D_{\text{max}}\).
   - Propagation delay \( \text{prop} \).
   - Time intervals \(t_1\) and \(t_2\).

   For example:

   ```
   Please enter the average size of the package (L)
   L: 1500
   Please enter the max value of delay (D_max)
   D_max: 0.5
   Please enter the value of delay (prop)
   prop: 0.3
   Please enter the time (t1,t2)
   t1: 2.0
   t2: 5.0
   ```

4. **Program Output**:

   After providing the inputs, the program will output the **Bit-Rate** and the number of bits transmitted between \(t_1\) and \(t_2\).

   Example output:

   ```
   The Bit-Rate is: 7500.0
   The number of bits of the package: 22500.0
   ```

### Example Input and Output

```
Please enter the average size of the package (L)
L: 1500
Please enter the max value of delay (D_max)
D_max: 0.5
Please enter the value of delay (prop)
prop: 0.3
Please enter the time (t1,t2)
t1: 2.0
t2: 5.0
The Bit-Rate is: 7500.0
The number of bits of the package: 22500.0
```
