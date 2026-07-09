# PROJECT PERIGRINE - DURENDAL'S PROGRAMMING LANGUAGE STRUCTURE

Perigrine is a programming language developed by Durendal.

## Data Types

### Single-Value Types

Integer: `int`, sizes 8, 16, 32, 64, 128, optional `unsigned`  
Floats: `float`, sizes 32, 64, 128  
Complex: `complex`, sizes 128, 256  
Text: `char`  
Logical: `bool`  
Empty: `null` / `none`

### Data Structures

Text: `string` `(str)`  
Collections: `dict`, `hashset`, `array`, `vector`, `tree`, `list`, `graph`, `queue`, `stack`
Math/Physics: `matrix`, `tensor`

## Keywords

### Control Flow

Conditionals: `if`, `elif`, `else`  
Loops: `for`, `for` x `in` y, `while`  
Execution: `break`, `continue`, `return`

### Booleans

Any non-empty data type gets treated as True.

Operators: `and`, `or`, `not`  
Evaluation: `all()`, `any()`, `none()`

### Preprocessing

Modules: `import`, `from`  
Macros: `macro`, `endmacro`
Optimizations: `@nogc` (Garbage Collection disabled)

### Class Scope & Attributes

Declarations: `class`, `method`
Context/prefixes:

- `static` (static method)
- `dynamic` (class method)
- `asset` (property)
- `this` / `self` -> optional name for instance reference

### Function Modifiers & Scopes

Declaration: `function` / `func` / `fn`
Visibility: `private`, `public`, `protected`  
Concurrence: `async`

## Functions

Functions are declared using the `function` keyword.

### Syntax Rules

Group parameters by types and split using the `|` symbol. Separate each parameter in each group by a comma.
With Return Type: Use the `>` symbol followed by the type before the opening curly brace.  
Without Return Type (void): Prepend the definition with the `void` keyword and omit the `>` arrow and the type entirely.

### Function Examples

With explicit return type:

```perigrine
function functionExample(num1, num2, num3: int32 | multiple: float64) > int32 {
    return (num1 + num2 + num3) * multiple;
}
```

With void return type:

```perigrine
void function functionExample(content, path: str) {
    save_to_file(content, path);
}
```

### Variable Assignment

Perigrine uses explicit static typing for variable declarations. The data type must precede the variable name.

#### Syntax

```perigrine
<type> <variable_name> = <value>;
```

#### Variable Assignment Examples

```perigrine
float64 newnumber = 100.01;
int32 counter = 0;
str message = "Hello Perigrine";
bool isActive = true;
char letter = 'A';
```

#### Operators

Perigrine adopts Python-style operators for readability, combining traditional mathematical symbols with word-based logical and membership operators.

Arithmetic Operators

- `+` : Addition
- `-` : Subtraction
- `*` : Multiplication
- `/` : True division (returns floating-point)
- `//` : Floor division (integer division)
- `%` : Modulo (remainder)
- `**` : Exponentiation (power)

Assignment Operators

- `=`: Standard assignment
- `+=`, `-=`, `*=`, `/=`: Compound arithmetic assignment

Comparison Operators

- `==`: Equal to
- `!=`: Not equal to
- `>` , `<`: Greater than, Less than
- `>=` , `<=`: Greater than or equal to, Less than or equal to

Boolean Operators

- `and` / `&&` : Logical AND
- `or` / `??` : Logical OR
- `not` / `!` : Logical NOT

Membership & Identity Operators

- `in` : Checks if a value exists within a data structure (array, vector, dict).
- `not in` : Checks if a value does not exist within a data structure.
- `is` : Evaluates to true if two variables point to the same object / memory allocation (is True, is False, is None).
