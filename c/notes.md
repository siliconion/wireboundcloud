# Compilation

To compile:
`gcc -o output [input.c]`

To run
`./output`

The compile pipeline includes:
1. Preprocess
2. Compile
3. Link

-Wall: flag for?
 
### Preprocess
`#include "some_file"`

Replace this line with the content of some_file.
If it's <some_file>, use the system search path.

`#define string_a string_b`:

replace string_a with b

```
#ifdef flag
 do_something
#endif
```
use `-D flag` to set the flag when compile 

To run preprocess
`cpp -p input_file`

### Compile
* type checking
* linear processing: you can ONLY use what's declared above

### Link
combine several .c files

# Makefile
`make [ -f makefile ] [ options ] ... [ targets ] ...` will look for `makefile`  in the directory, and execute it. 

qThe basic makefile is composed of:
```aidl
target: dependencies
[tab] system command
```


# Core C
### Variable
`type var_name;`: variable

`const type var_name;`: the value do not change

`static type var_name;`: retain the value through entire program

### Block
{}
Can have anonymous blocks!


# stack and heap

# Memory
declaration: data_type *pointer_name
&x: address of x
*p: value at address p

char x = 'a';
char *ptr = &x;
*ptr // 'a'

ptr+i has value: ptr + i * sizeof(data_type of ptr)

### Arrays
Are chunks of memory
data_type array_name[num_elements]

int data[3];
int data[] = {0, 1, 2} // compiler will figure out the size
`data` is a pointer, points to the beginning of the memory
you can think of `data[i]` as `*(data + i)`
Strings are char array

### Memory allocation
`#include <stdlib.h>`
sizeof: returns number of bypes of a data type
malloc/realloc: finds a specified amount of free momory and returns a void pointer to it

### Memory leaks
Valgrind

# Struct and unions
There's no objects. These only holds data, no functions.
```aidl
struct struct_name{
    type member1;
    type member2...
}

struct struct_name var_name = {val1, val2};
var_name.member1 = val;
```

unions can only access one member at a time. Store all data in the same chunk of memory.s