# Python 2nd Doc   
## Import Conventions
Naming Conventions for modules imported:
```Python
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    import statsmodels as sm
```

i.e np.array is a reference to the array function in NumPy. It is bad practice to import everything (`from numpy import *`) from a large package.

Do not forget the [Python official language docs](https://docs.python.org/3/)

## Python Interpreter vs IPython Shell
Create hello_world.py with these contents:
```Python
print('Hello world')
```
Run it using the following (hello_world.py must be in your current working directory):
```
$ python hello_world.py
Hello world
```
or in ipython:
```Python
$ ipython
Python 3.8.10 (default, Nov 26 2021, 20:14:08)
Type 'copyright', 'credits' or 'license' for more information
IPython 8.0.1 -- An enhanced Interactive Python. Type '?' for help.
In [1]: %run hello_world.py
Hello world
```
Typing just a variable into IPython, renders a string representation of the object:
```Python
In [2]: import numpy as np
In [3]: np.random.seed(0)
In [4]: data = {i: np.random.randn() for i in range(5)}
In [5]: data
Out[5]:
{0: 1.764052345967664,
 1: 0.4001572083672233,
 2: 0.9787379841057392,
 3: 2.240893199201458,
 4: 1.8675579901499675}
```
We assign a variable named data that references a Python dictionary. Then we print the value of data in the console.

### Tab Completion
In IPython, pressing the Tab key will search the namespace for any variables (objects, functions, etc.) matching the characters you have typed so far:
```Python
first_num = 31
first_str = "first String"
first<Tab>
# first_num first_str
```
```Python
l1 = [5,6,7,8,9]
l1.<Tab>
# append()  count()   insert()  reverse()
# clear()   extend()  pop()     sort()
# copy()    index()   remove()
```
Tab complete also works for modules:
```Python
import datetime
datetime.<Tab>
#datetime.date datetime.MAXYEAR datetime.timedelta
#datetime.datetime datetime.MINYEAR datetime.timezone
#datetime.datetime_CAPI datetime.time datetime.tzinfo
```
### Matplotlib 
[Matplotlib example](https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/)
[Official Matplotlib documentation](https://matplotlib.org/)
[]
```Python
import matplotlib.pyplot as plt
plt.plot(np.random.randn(50).cumsum())
plt.savefig("test1.png")
```

## Language Basics
Python uses whitespace (tabs or spaces) to structure code instead of using braces as in many other languages like R, C++, Java, and Perl. A colon is used at the beginning of a code block, and all code after is indented by the same amount until the end of the block:
```Python
l2=[1,2,3,4] # a list named array
pivot=2
less=[]
greater=[]

for num in l2:
    if num < pivot:
        less.append(num)
    else:
        greater.append(num)
```

### Pass by Object Reference
Python utilizes an object model. Every number, string, collection, function, class, module, and so on exists in is a reference to a Python object. Each object has an associated type (e.g., string or function) and internal data. 

When you assign a variable (or name) in Python, you are creating a reference to the object on the righthand side of the equals sign. 
```Python
l3 = [0,1,2]
```
Suppose we assign `l3` to a new variable `l4`:
```Python
l4 = l3
```
In some languages, this assignment would cause the data `[0,1,2]` to be copied. In Python, `l3` and `l4` refer to the same object, the original list `[0, 1, 2]`.

You can prove this to yourself by appending an element to `l3` and then examining `l4`:
```Python
l3.append(3)
l4
#[0, 1, 2, 3]
```
We have two references for the same object.

Also, when you pass objects as arguments to a function, new local variables are created referencing the original objects without any copying. 
```Python
def append_element(some_list, element):
    some_list.append(element)
```
Then we have:
```Python
data = [1, 2, 3]
append_element(data, 4)

#[1, 2, 3, 4]
```
### Operators
[Operators](https://www.w3schools.com/python/python_operators.asp)


### Mutable and Immutable Objects
Most objects in Python, such as lists, dicts, NumPy arrays, and most userdefined types (classes), are mutable, i.e. the object or values that they contain can be modified:
```Python
a_list = ['foo', 2, [4, 5]]
a_list[2] = (3, 4)
a_list
#['foo', 2, (3, 4)]
```
Others, like strings and tuples, are immutable:
```Python
a_tuple = (3, 5, (4, 5))
a_tuple[2] = (1,2)

#---------------------------------------------------------------------------
#TypeError                                 Traceback (most recent call last)
#Input In [33], in <module>
#----> 1 a_tuple[2] = (1, 2)
#
#TypeError: 'tuple' object does not support item assignment
```

### Strings
Many Python objects can be converted to a string using the str function:
```Python
num1 = 10.2
s = str(num1)
print(num1)
#10.2
```
Strings are a sequence of Unicode characters and therefore can be treated like other sequences, such as lists and tuples:
```Python
s = 'python'
list(s)
#['p', 'y', 't', 'h', 'o', 'n']
s[:3]
#'pyt'
```
The syntax `s[:3]` is known as slicing and is implemented for many kinds of Python sequences. 

The backslash character `\` is an escape character, meaning that it is used to specify special characters like newline `\n` or Unicode characters. To write a string literal with backslashes, you need to escape them:
```Python
s = '12\\34'
print(s)
#12\34
```
If you have a string with a lot of backslashes and no special characters, you might find this a bit annoying. Fortunately you can preface the leading quote of the string with `r`, which means that the characters should be interpreted as is:
```Python
s = r'this\has\no\special\characters'
s
#'this\\has\\no\\special\\characters'
```
The `r` stands for raw. Adding two strings together concatenates them and produces a new string:
```Python
a = 'this is the first half '
b = 'and this is the second half'
a + b
#'this is the first half and this is the second half'
```
String templating or formatting is another important topic. The number of ways to do so has expanded with the advent of Python 3, and here I will briefly describe the mechanics of one of the main interfaces. String objects have a format method that can be used to substitute formatted arguments into the string, producing a new string:
```Python
template = '{0:.2f} {1:s} are worth US${2:d}'
```
In this string,
`{0:.2f}` means to format the first argument as a floating-point number with two decimal places.`{1:s}` means to format the second argument as a string. `{2:d}` means to format the third argument as an exact integer. To substitute arguments for these format parameters, we pass a sequence of arguments to the format method:
```Python
template.format(4.5560, 'Argentine Pesos', 1)
#'4.56 Argentine Pesos are worth US$1'
```

## Dates and Times
Dates and times
The built-in Python datetime module provides datetime, date, and time
types. The datetime type, as you may imagine, combines the information
stored in date and time and is the most commonly used:
```Python 
from datetime import datetime, date, time
dt = datetime(2022, 1, 27, 20, 35, 15)
dt.day
#27
dt.minute
#35
```
Given a datetime instance, you can extract the equivalent date and time objects by calling methods on the datetime of the same name:
```Python
dt.date()
#datetime.date(2022, 1, 27)
dt.time()
#datetime.time(20, 35, 15)
```
The strftime method formats a datetime as a string:
```Python
dt.strftime('%m/%d/%Y %H:%M')
#'01/27/2022 20:35'
```
Strings can be converted (parsed) into datetime objects with the strptime function:
```Python
datetime.strptime('20220214', '%Y%m%d')
#datetime.datetime(2022, 2, 14, 0, 0)
```
When you are aggregating or otherwise grouping time series data, it will occasionally be useful to replace time fields of a series of datetimes — for example, replacing the minute and second fields with zero:
```Python
dt.replace(minute=0, second=0)
#datetime.datetime(2022, 1, 27, 20, 0)
```
Since `datetime.datetime` is an immutable type, methods like these always produce new objects. The difference of two datetime objects produces a datetime.timedelta type:
```Python
dt2 = datetime(2022, 2, 15, 22, 30)
delta = dt2 - dt
delta
#datetime.timedelta(days=19, seconds=6885)
type(delta)
#datetime.timedelta
```
The output `datetime.timedelta(days=19, seconds=6885)` indicates that the timedelta encodes an offset of 19 days and 6885 seconds. Adding a timedelta to a datetime produces a new shifted datetime:
``` Python
dt
#datetime.datetime(2022, 1, 27, 20, 35, 15)
dt + delta
#datetime.datetime(2022, 2, 15, 22, 30)
```

## Control Flow
Python has several built-in keywords for conditional logic, loops, and other
standard control flow concepts found in other programming languages. 
### if, elif, and else
The if statement is one of the most well-known control flow statement types.
It checks a condition that, if True, evaluates the code in the block that follows:
``` Python
x=-6
if x < 0:
    print("It's negative")
```
An if statement can be optionally followed by one or more elif blocks and a catch-all else block if all of the conditions are False:
``` Python
if x < 0:
    print("It's negative")
elif x == 0:
    print("Equal to zero")
elif 0 < x < 5:
    print("Positive but smaller than 5")
else:
    print("Positive and larger than or equal to 5")
```
If any of the conditions is True, no further elif or else blocks will be reached. With a compound condition using and or or, conditions are evaluated left to right and will short-circuit:
``` Python
a = 5; b = 7
c = 8; d = 4
if a < b or c > d:
    print('Made it')
```
In this example, the comparison `c > d` never gets evaluated because the first comparison was True. It is also possible to chain comparisons:
``` Python
In [120]: 4 > 3 > 2 > 1
#True
```
### for loops
for loops are for iterating over a collection (like a list or tuple) or an iterater. The standard syntax for a for loop is:
```Python
for value in collection:
```
You can advance a for loop to the next iteration, skipping the remainder of the block, using the continue keyword. Consider this code, which sums up integers in a list and skips None values:
```Python
sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
    if value is None:
        continue
    total += value
```
A for loop can be exited altogether with the break keyword. This code sums
elements of the list until a 5 is reached:
```Python
sequence = [1, 2, 0, 4, 6, 5, 2, 1]
total_until_5 = 0
for value in sequence:
    if value == 5:
        break
    total_until_5 += value
```
The `break` keyword only terminates the innermost for loop; any outer for loops will continue to run:
```Python
for i in range(4):
    for j in range(4):
        if j > i:
            break
        print((i, j))
```
As we will see in more detail, if the elements in the collection or iterator are sequences (tuples or lists, say), they can be conveniently unpacked into variables in the for loop statement:
```Python
for a, b, c in iterator:
# do something
```
### while loops
A while loop specifies a condition and a block of code that is to be executed until the condition evaluates to False or the loop is explicitly ended with break:
```Python
x = 256
total = 0
while x > 0:
    if total > 500:
        break
    total += x
    x = x // 2
```

### pass
pass is the "no-op" statement in Python. It can be used in blocks where no action is to be taken (or as a placeholder for code not yet implemented); it is only required because Python uses whitespace to delimit blocks:
```Python
if x < 0:
    print('negative!')
elif x == 0:
# TODO: put something smart here
    pass
else:
    print('positive!')
```
### Range
The range function returns an iterator that yields a sequence of evenly spaced integers:
```Python
range(10)
range(0, 10)
list(range(10))
```
Both a start, end, and step (which may be negative) can be given:
```Python
list(range(0, 20, 2))
list(range(5, 0, -1))
```
As you can see, range produces integers up to but not including the endpoint. A common use of range is for iterating through sequences by index:
```Python
seq = [1, 2, 3, 4]
for i in range(len(seq)):
    val = seq[i]
```
While you can use functions like `list` to store all the integers generated by range in some other data structure, often the default iterator form will be what you want. This snippet sums all numbers from 0 to 99,999 that are multiples of 3 or 5:
```Python
sum = 0
for i in range(100000):
    # % is the modulo operator
    if i % 3 == 0 or i % 5 == 0:
        sum += i
```
While the range generated can be arbitrarily large, the memory use at any given time may be very small. 

### Ternary expressions 
Ternary expression in Python allows you to combine an if-else block that produces a value into a single line or expression. The syntax for this in Python is:
```Python
value = true-expr if condition else false-expr
```
Here, true-expr and false-expr can be any Python expressions. It has the identical effect as the more verbose:
```Python
if condition:
    value = true-expr
else:
    value = false-expr
```
This is a more concrete example:
```Python
x = 5
'Non-negative' if x >= 0 else 'Negative'
```
As with `if-else` blocks, only one of the expressions will be executed. Thus, the `if` and `else` sides of the ternary expression could contain costly computations, but only the true branch is ever evaluated. While it may be tempting to always use ternary expressions to condense your code, realize that you may sacrifice readability if the condition as well as the
true and false expressions are very complex.

## List, Set, and Dict Comprehensions
List comprehensions are one of the most-loved Python language features. They allow you to concisely form a new list by filtering the elements of a collection, transforming the elements passing the filter in one concise expression. 
They take the basic form:
```Python
[expr for val in collection if condition]
```
This is equivalent to the following for loop:
```Python
result = []
for val in collection:
    if condition:
        result.append(expr)
```
The filter condition can be omitted, leaving only the expression. For example, given a list of strings, we could filter out strings with length 2 or less and also convert them to uppercase like this:
```Python
list_strings = ['b', 'is', 'cat', 'far', 'love', 'python']
[y.upper() for y in list_strings if len(y) > 2]
#['CAT', 'FAR', 'LOVE', 'PYTHON']
```
Set and dict comprehensions are a natural extension, producing sets and dicts in an idiomatically similar way instead of lists. A dict comprehension looks like this:
```Python
dict_comp = {key-expr : value-expr for value in collection if condition}
```
A set comprehension looks like the equivalent list comprehension except with curly braces instead of square brackets:
```Python
set_comp = {expr for value in collection if condition}
```
Like list comprehensions, set and dict comprehensions are mostly conveniences, but they similarly can make code both easier to write and read.

Consider the list of strings from before. Suppose we wanted a set containing just the lengths of the strings contained in the collection; we could easily compute this using a set comprehension:
```Python
string_lengths = {len(x) for x in list_strings}
string_lengths
#{1, 2, 3, 4, 6}
```
More functionally we can use the map function:
```Python
set(map(len, list_strings))
#{1, 2, 3, 4, 6}
```
As a simple dict comprehension example, we could create a lookup map of these strings to their locations in the list:
```Python
loc_mapping = {index : val for index, val in enumerate(list_strings)}
loc_mapping
#{'b': 0, 'is': 1, 'cat': 2, 'far': 3, 'love': 4, 'python': 5}
```
### Nested list comprehensions
Take a list of lists containing some names:
```Python
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
    ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
```
Now, suppose we wanted to get a single list containing all names with two or more e’s in them. We could certainly do this with a simple for loop:
```Python
names_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e') >= 2]
    names_of_interest.extend(enough_es)
```
You can actually wrap this whole operation up in a single nested list comprehension, which will look like:
```Python
flattenedName=[x for List in all_data for x in List]
result = [name for name in flattenedName if name.count('e')>=2]
```
Take another example where we “flatten” a list of tuples of integers into a simple list of integers:
```Python
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
flattened
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Keep in mind that the order of the for expressions would be the same if you wrote a nested for loop instead of a list comprehension:
```Python
flattened = []
for tup in some_tuples:
    for x in tup:
        flattened.append(x)
```
You can have arbitrarily many levels of nesting, though if you have more than two or three levels of nesting you should probably start to question whether this makes sense from a code readability standpoint. It’s important to distinguish the syntax just shown from a list  comprehension inside a list comprehension, which is also perfectly valid:
```Python
[[x for x in tup] for tup in some_tuples]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
This produces a list of lists, rather than a flattened list of all of the inner elements.

### More on Functions
Since Python functions are objects, many constructs can be easily expressed that are difficult to do in other languages. Suppose we were doing some data cleaning and needed to apply a bunch of transformations to the following list of strings:
```Python
states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda','south carolina##', 'West virginia?']
```
Anyone who has ever worked with user-submitted survey data has seen messy results like these. Lots of things need to happen to make this list of strings uniform and ready for analysis: stripping whitespace, removing punctuation symbols, and standardizing on proper capitalization. One way to do this is to use built-in string methods along with the re standard library for regular expressions:
```Python
import re
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result
```
The result looks like this:
```Python
clean_strings(states)
#['Alabama',
#'Georgia',
#'Georgia',
#'Georgia',
#'Florida',
#'South Carolina',
#'West Virginia']
```
An alternative approach that you may find useful is to make a list of theoperations you want to apply to a particular set of strings:
```Python
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]
def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result
```
Then we have the following:
```Python
clean_strings(states, clean_ops)
#['Alabama',
#'Georgia',
#'Georgia',
#'Georgia',
#'Florida',
#'South Carolina',
#'West Virginia']
```
A more functional pattern like this enables you to easily modify how the strings are transformed at a very high level. The clean_strings function is also now more reusable and generic. You can use functions as arguments to other functions like the built-in map
function, which applies a function to a sequence of some kind:
```Python
for x in map(remove_punctuation, states):
    print(x)

#Alabama
#Georgia
#Georgia
#georgia
#FlOrIda
#south carolina
#West virginia

[x for x in map(remove_punctuation, states)]

#[' Alabama ',
# 'Georgia',
# 'Georgia',
# 'georgia',
# 'FlOrIda',
# 'south carolina',
# 'West virginia']
```

### Anonymous (Lambda) Functions
Python has support for so-called anonymous or lambda functions, which are a way of writing functions consisting of a single statement, the result of which is the return value. They are defined with the lambda keyword, which has no meaning other than "we are declaring an anonymous function":
```Python
def short_function(x):
    return x * 2
equiv_anon = lambda x: x * 2
```
I usually refer to these as lambda functions in the rest of the book. They are especially convenient in data analysis because, as you’ll see, there are many cases where data transformation functions will take functions as arguments. It’s often less typing (and clearer) to pass a lambda function as opposed to writing a full-out function declaration or even assigning the lambda function to a local variable. For example, consider this silly example:
```Python
def apply_to_list(some_list, f):
    return [f(x) for x in some_list]
ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)
```
You could also have written `[x * 2 for x in ints]`, but here we were able to succinctly pass a custom operator to the apply_to_list function. As another example, suppose you wanted to sort a collection of strings by the number of distinct letters in each string:
```Python
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
```
Here we could pass a lambda function to the list’s sort method:
```Python
strings=['foo','card','bar','aaaa','abab']
strings2=sorted(strings,key=lambda x: len(x))
strings2

strings.sort(key=lambda x: len(x))
strings
```

One reason lambda functions are called anonymous functions is that , unlike functions declared with the def keyword, the function object itself is never given an explicit `__name__` attribute

## Generators
Having a consistent way to iterate over sequences, like objects in a list or lines in a file, is an important Python feature. This is accomplished by means of the iterator protocol, a generic way to make objects iterable. For example, iterating over a dict yields the dict keys:
```Python
some_dict = {'a': 1, 'b': 2, 'c': 3}
for key in some_dict:
    print(key)

#abc
```
When you write for key in some_dict, the Python interpreter first attempts to create an iterator out of some_dict:
```Python
dict_iterator = iter(some_dict)
dict_iterator
```
An iterator is any object that will yield objects to the Python interpreter when used in a context like a for loop. Most methods expecting a list or list-like object will also accept any iterable object. This includes built-in methods such as min, max, and sum, and type constructors like list and tuple:
```Python
list(dict_iterator)
#['a', 'b', 'c']
```
A generator is a concise way to construct a new iterable object. Whereas normal functions execute and return a single result at a time, generators return a sequence of multiple results lazily, pausing after each one until the next one is requested. To create a generator, use the yield keyword instead of return in a function:
```Python
def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2
```
When you actually call the generator, no code is immediately executed:
```Python
gen = squares()
gen
```
It is not until you request elements from the generator that it begins executing its code:
```Python
for x in gen:
    print(x, end=' ')

#Generating squares from 1 to 100
#1 4 9 16 25 36 49 64 81 100
```
### Generator expresssions
Another even more concise way to make a generator is by using a generator expression. This is a generator analogue to list, dict, and set comprehensions; to create one, enclose what would otherwise be a list comprehension within
parentheses instead of brackets:
```Python
gen = (x ** 2 for x in range(100))
gen
```
This is completely equivalent to the following more verbose generator:
```Python
def _make_gen():
    for x in range(100):
        yield x ** 2
gen = _make_gen()
```
Generator expressions can be used instead of list comprehensions as function arguments:
```Python
sum(x ** 2 for x in range(100))
```
or with dictionaries for example:
```Python
dict((i, i **2) for i in range(5))
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Itertools Module
The standard library itertools module has a collection of generators for many common data algorithms. For example, groupby takes any sequence and a function, grouping consecutive elements in the sequence by return value of the function. Here’s an example:
```Python
import itertools
  
  
L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]
  
# Key function
key_func = lambda x: x[0]
  
for key, group in itertools.groupby(L, key_func):
    print(key + " :", list(group))
```
Check out the [official Python documentation](https://docs.python.org/3/library/itertools.html) for more on this useful built-in utility module.

## NumPy

While NumPy by itself does not provide modeling or scientific functionality, having an understanding of NumPy arrays and array-oriented computing will help you use tools with array-oriented semantics, like pandas, much more effectively. 

While NumPy provides a computational foundation for general numerical data processing. Use Pandas and/or Spark as the basis for most kinds of statistics or analytics. 

- One of the reasons NumPy is so important for numerical computations in Python is because it is designed for efficiency on large arrays of data. There are a number of reasons for this: NumPy internally stores data in a contiguous block of memory, independent of other built-in Python objects. NumPy’s library of algorithms written in the C language can operate on this memory without any type checking or other overhead. NumPy arrays also use much less memory than built-in Python sequences.

- NumPy operations perform complex computations on entire arrays without the need for Python for loops.

To give you an idea of the performance difference, consider a NumPy array of ten million integers, and the equivalent Python list:
```Python
import numpy as np
arr1 = np.arange(10000000)
list1 = list(range(10000000))
```
create a redundant loop for timing and purposes and within it multiply each sequence by 2:
```Python
%time for _ in range(10): arr2 = arr1 * 2
#CPU times: user 86.5 ms, sys: 106 ms, total: 192 ms
#Wall time: 191 ms
%time for _ in range(10): arr2 = [y * 2 for y in list1]
#CPU times: user 3.64 s, sys: 1.04 s, total: 4.67 s
#Wall time: 4.69 s
%time list2 = [y * 2 for y in list1]
#CPU times: user 595 ms, sys: 112 ms, total: 707 ms
#Wall time: 705 ms
```
NumPy-based algorithms are generally 10 to 100 times faster (or more) than
their pure Python counterparts and use significantly less memory.

### NumPy ndarray: A Multidimensional Array

NumPy has an N-dimensional array object, or ndarray, which is a fast, flexible container for large datasets in Python. Arrays enable you to perform mathematical operations on whole blocks of data using similar syntax to the equivalent operations between scalar elements.

First import NumPy and generate a small array of random data:
```Python
import numpy as np
# Generate some random data
np.random.seed(0)
data = np.random.randn(2, 3)
data
#array([[ 1.76405235,  0.40015721,  0.97873798],
#       [ 2.2408932 ,  1.86755799, -0.97727788]])
```

```Python
data * 10
#array([[17.64052346,  4.00157208,  9.78737984],
#       [22.40893199, 18.6755799 , -9.7727788 ]])
data + data
#array([[ 3.52810469,  0.80031442,  1.95747597],
#       [ 4.4817864 ,  3.73511598, -1.95455576]])
```
First, all of the elements are multiplied by 10. Then, the corresponding values in each "cell" in the array are added to each other.

An ndarray is a generic multidimensional container for homogeneous data; that is, all of the elements must be the same type. Every array has a shape, a tuple indicating the size of each dimension, and a dtype, an object describing the data type of the array:
```Python
data.shape
#(2, 3)
data.dtype
#dtype('float64')
```
#### Creating ndarrays
[NumPy ndarrays documentation](https://numpy.org/doc/stable/reference/arrays.html)

The easiest way to create an array is to use the array function. This accepts any sequence-like object (including other arrays) and produces a new NumPy array containing the passed data. For example, a list is a good candidate for conversion:
```Python
data1 = [9, 17.5, 12, 0, 0.5]
arr1 = np.array(data1)
arr1
#array([ 9. , 17.5, 12. ,  0. ,  0.5])
```
Nested sequences, like a list of equal-length lists, will be converted into a multidimensional array:
```Python
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2
#array([[1, 2, 3, 4],
#[5, 6, 7, 8]])
```
Since data2 was a list of lists, the NumPy array arr2 has two dimensions with shape inferred from the data. We can confirm this by inspecting the ndim and shape attributes:
```Python
arr2.ndim
#2
arr2.shape
#(2, 4)
```
Unless explicitly specified (more on this later), np.array tries to infer a good data type for the array that it creates. The data type is stored in a special dtype metadata object; for example, in the previous two examples we have:
```Python
arr1.dtype
#dtype('float64')
arr2.dtype
#dtype('int64')
```
In addition to np.array, there are a number of other functions for creating new arrays. As examples, zeros and ones create arrays of 0s or 1s, respectively, with a given length or shape. empty creates an array without initializing its values to any particular value. To create a higher dimensional array with these methods, pass a tuple for the shape:
```Python
np.zeros(10)
#array([ 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
np.zeros((3, 6))
#array([[ 0., 0., 0., 0., 0., 0.],
#[ 0., 0., 0., 0., 0., 0.],
#[ 0., 0., 0., 0., 0., 0.]])
np.empty((2, 3, 2))
#array([[[ 0., 0.],
#[ 0., 0.],
#[ 0., 0.]],
#[[ 0., 0.],
#[ 0., 0.],
#[ 0., 0.]]])

np.arange(15)
#array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
```
or one of my personal favorites:
```Python
In [58]: np.eye(10)
#array([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
#       [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
#       [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
#       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
#       [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
#       [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
#       [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
#       [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
#       [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
#       [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]])
```
### Pandas 
```Python
import pandas as pd

first_letter1=lambda x:(x[0],x)
names = ['Alan','Adm','Wes','Will','Albert','Steven']
namesPairs=list(map(first_letter1,names))

df = pd.DataFrame(namesPairs, columns =['first letter','name'])
#print(df)
x=df.groupby('first letter').groups
print(x)
```
### Other Examples
Be careful with:

[Classes And Instance Variables](https://docs.python.org/3.9/tutorial/classes.html#method-objects)

Generally speaking, instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class:
```Python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
d.kind                  # shared by all dogs

e.kind                  # shared by all dogs

d.name                  # unique to d

e.name                  # unique to e
```
Shared data can have possibly surprising effects with involving mutable objects such as lists and dictionaries. 
For example, the tricks list in the following code should not be used as a class variable because just a single list would be shared by all Dog instances:

```Python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks                # unexpectedly shared by all dogs
#['roll over', 'play dead']
```
Correct design of the class should use an instance variable instead:
```Python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
#['roll over']
e.tricks
#['play dead']
```
### Collections
```Python
# Tally occurrences of words in a list
import collections as col
cnt = col.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
     cnt[word] += 1
print(cnt)
print(type(cnt))
```
There are several more. see language docs for [collections](https://docs.python.org/3/library/collections.html)

Along with links, sources:

McKinney, Wes. Python for data analysis: Data wrangling with Pandas, NumPy, and IPython. " O'Reilly Media, Inc.", 2018.

Lutz, Mark. Learning python: Powerful object-oriented programming. " O'Reilly Media, Inc.", 2013.