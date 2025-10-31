<img width="1268" height="708" alt="Screenshot 2025-10-30 at 10 37 55 PM" src="https://github.com/user-attachments/assets/91016dc9-d9d6-4fce-98a0-25f6f57b6782" /># Lecture: 1-3

<img width="1000" height="520" alt="image" src="https://github.com/user-attachments/assets/aaec2896-f434-4523-adc7-2acc4b766d7e" />

<img width="1600" height="720" alt="image" src="https://github.com/user-attachments/assets/8178b351-2d31-4a64-957e-cc7cce993f04" />

> [!NOTE]
> Python is case sensitive

### Types of Languages (Easy → Hard)
1. Natural Language (Easiest) : Spoken languages like English, Spanish, Hindi.
2. High-level Language : Python, JavaScript.
3. Low-level Language : Assembly, C.
4. Machine Language (Hardest) : Pure binary (0s and 1s).

### Comment: 
A comment is a note n your code, which is use for only readable form. Comment make code more readable, understandable and professional.
```
# - Single line comment
/**/ - Multi line comment
```

# Lecture: 4-5-6-7

### What is function
Function is a collection of coherant task. A function is a seld defined block of code which can reuse multiple time on a same file.

#### Types of function:
1. Built-in Function - print(), input(), len()
2. Third party Function - Pandas, Numpy, Pyspark 
3. User-Defined Function 

#### print():
It's a built-in function that displays messages onthe output screen to communicate with users.
```
print("Hii");
print("--------");
print("   Learn Python   ");
```

### Special Character
1. \n - new line
2. \t - tab
3. \b - backspace
4. \" - double quotes
5. \' - Single quotes
6. \\ - backslash

> [!IMPORTANT]
> print("You learning Python:\n\t- python\n\t- React\n\t- SQL")

```
print("""You learning Python:       // three quotes denote new linw
\t - python
\t - React
\t - SQL """);
```

### Variable
```
x = 2
print(x);  // output : 2
x = 3
print (x) // output : 3

name = 'priti'
print("My name is", name); //output: My name is priti
```
>[!Note]
> when putting (,) python automatically keep space between words and sentence etc.

### input() function
A built-in python function that stops your program to get user input.
```
name = input("Enter your name:")
print("Your name is:", name)
role = input("Enter your role:")
print("You are:", role)
```

### Variable
- python automatically detect data types
```
name = 'Priti' //string
age = 22   // int
isFlag = True   //boolean  
```
- Dynamic data type can change anytime

### Data type 
Categories of Data Types
1. No Value
  - Nothing
  - Example: a = None
2. Single Value:
- Represented by a basket with a single fruit 🍎
- Examples:
  - int → 50
  - float → 3.14
  - str → "Hello"
  - bool → True
>[!Important]
> “In Python, the boolean values are True and False"

3. Multi Values (Data Structures / Collections)
- Represented by a basket with multiple fruits 🍍🍎🍌
- Examples:
  - list → [1, 2, 3]
  - set → {1, 2}
  - tuple → ('a', 'b', 'c')
  - dict → {'a': 1, 'b': 2, 'c': 3}
<img width="676" height="496" alt="Screenshot 2025-10-01 at 10 33 17 PM" src="https://github.com/user-attachments/assets/afb2eb8d-f9c8-4f55-b208-44e976ad8f04" />

<img width="665" height="402" alt="Screenshot 2025-10-01 at 10 36 01 PM" src="https://github.com/user-attachments/assets/36851c22-51db-4166-8baa-1b6eea5d68bd" />

## Diiference b/w Function and Method

### Function
- Independent block of reusable code.
- Defined with def or are built-in like print(), type().
- Not tied to any specific object or class.
- Syntax
```
function_name(value)
```
Example:
```
print("hello")
type(50)
```
### Methods
- Functions that belong to an object/class.
- Invoked using dot notation on a value (object).
- Can access and modify the object’s data.
- Syntax:
```
value.method_name()
```
```
'hello'.upper()     # String method → HELLO
(50).bit_length()   # Integer method → 6
```
<img width="828" height="443" alt="Screenshot 2025-10-01 at 10 55 23 PM" src="https://github.com/user-attachments/assets/92e66a06-e23b-48c0-b862-0abefb856825" />

# Lecture 8 Python Syring Function'

<img width="668" height="408" alt="Screenshot 2025-10-30 at 10 38 28 PM" src="https://github.com/user-attachments/assets/4ac7864e-1d4d-4f89-b2b4-f78209813c3b" />

```
let str = "hello"
print(len(str));

text = """
Pythin is very
simple langugae
it is very good.
"""
text.count('very');

price = "28347{23"
price.replace("{", "/");
```

## Concatanation
```
print("Hello" + " " + "World!");
```

## f String
- A modern, super-easy way to format and build strings
- The "f" stands for "formatted"
- Lets you easily put variables and expressions directly inside string values
  
```
name = "priti"
age = 24
print(f"My name is {name} and I am {age} years old.")
print(f"{{This is mee}}")
```

## Split()
```
text= " wnwe-qedqnkjed-qednqke-dew"
print(text.split("-"));
```
## Transaformation
```
print("Ha"*3) // hahaha
print("="*20) // ====================
```

## Extraction

| Element | Positive Index | Negative Index |
| ------- | -------------- | -------------- |
| 1       | 0              | -5             |
| 2       | 1              | -4             |
| 3       | 2              | -3             |
| 4       | 3              | -2             |
| 5       | 4              | -1             |

### Slicing: 
Slicing lets you extract a portion (or “slice”) of a sequence — like a list, tuple, or string — using index ranges.
```
sequence[start : stop : step]
```
- start → index where the slice begins (inclusive)
- stop → index where the slice ends (exclusive)
- step → how many elements to skip (optional)
- Example
```
word = "Python"
print(word[1:4])   # "yth"
print(word[::-1])  # "nohtyP"
```

## Cleaning
- strip(): clean left and right both side whitespace
- lstrip(): clean left side whitespace
- rstrip(): clean right side whitespace

```
text = " Engineering ".stript()
text = "   Engineering".lstript()
text = "Engineering ".rstript()

text = "#####Hello####".strip("#")

```
