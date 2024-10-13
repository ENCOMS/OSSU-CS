# Topic: Libraries
## Link: https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@ea6fc5c250bc4fc786575db3b93611a5/block-v1:HarvardX+CS50P+Python+type@vertical+block@ae607d49594541069761d6077d6c1fee

### What are Libraries

Libraries or modules are generally files of code that other people have written that you can use in your own program. Any language has the ability to share code with others, share code across your own projects.

This encourage reusability.

If you find yourself copy and pasting code from another project, this is a good candidate to put into a library that you can load into your programs.

This keep updated and in a single place a copy of the same code, that can be share in different projects.


### random library:
docs.python.org/3/library/random.html

This module provides functions that give us randomness to any code in our project.


### import keyword
import keyword in python allows you to import the contents of the functions from
some module in python.

Example: 
```
import random

random.choice(seq)



random            .choice           
name of module    function in random

(seq)
S E Q or sequence
```

### Sequence
A sequence generally means a list or something that is list-like if you have a list of numbers or strings or anything else.

Flipping a coin
In this example we have 50/50 change of head or tails in a coin

[First example:](generate.py?plain=1#L3)

code:
```
import random

coin = random.choice(["heads", "tails"])
print(coin)

```

output:
```
> head
> head
> tails
> ...

```

We could only import choice function from the random module:

 
[Second example:](generate.py?plain=1#L11)
```
from random import choice

coin = choice(["heads", "tails"])
print(coin)

```

output:
```
> head
> head
> tails
> ...

```

Use cases:

- This will make choice available locally in the code without the use of the word random.
- Could limit our use of the word choice, creating conflicts if we are using the name previously.
- can make our code a little more tighten our code a little bit.

On the other hand, if only import the random module:
- If we call random.function() it will let us use that function name, not colliding with one we have previously named.
- Could potentially make our code longer and longer, making it ugly and annoying.


There's not necessarily one right approach, it depends of the reason for using the function, lend of the program and guide lines. but in this case the better approach would be to simple import the module.


### random.randint(a, b)
the randint() function takes two values and randomise a number as output including a and b.


[Third example:](generate.py?plain=1#L21)
```
import random

number = random.randint(1, 10) #10% change of any number from 1 to 10
print(number)

```

output:
```
> 4
> 5
> 10
> ...

```

### random.shuffle(x)
This function will shuffle in a random way, a list of items, passing in the variable containing the list (it modify the list).

[Fourth example:](generate.py?plain=1#L29)
```
import random

cards = ["jack", "queen", "king"]

random.shuffle(cards)

#as to output the list not using the format that python use, we print only the cards using a for loop.

for card in cards:
    print(card)


```
output:
```
>python generate.py
> queen
> jack
> king
>python generate.py
> jack
> queen
> king
> ...

```

### statistics library
conformed by statistics modules for calculated medians or modes or other aspects of data set that you may want to analyze.

docs.python.org/3/library/statistics.html

### average function
allows you to calculate the average of some numbers

[Fifth example:](average.py?plain=1#L1)
```
import statistics

print(statistics.mean([100,90]))

```

Another feature is command-line arguments

### command-line arguments
This feature, not just in python, but of languages more generally that allow you to provide input not when prompted inside of a program as happens whenever we call the python function input. But rather, there's this feature, command-line arguments of programs, that allows you to provide arguments that is input to the program of just when you're executing at the command line.

For example we can pass several arguments after the call of the program in the same line, before the program even executed himself as the input.

In this case the sys module is the one in charge  of handling the system inputs to the program.

### sys module
The sys module gives the access to values that have been typed at the command line.

docs.python.org/3/library/sys.html

This module contains a list of various functions and variables that work in different situations, but for human inputs in command line would be the argv function.

### argv function
argv stands for arguments vector, that means that the vector is the list of all the words that the human typed in at their prompt before hit enter.

[Sixth example:](name.py?plain=1#L1)
```
import sys

print("hello, my name is", sys.argv[1])


```

notes on sys.argv[1]:
- We use square bracket notation to get at the various elements inside of a list.
- [1] we start in 1 since the [0] is the name of the program in this case 'name.py'
- if not argument is give after the name of the function a 'IndexError: list index out of range' is raise. this means that element you want to access is too far to the left or the right or the object list.


### Handling human error of IndexError:
If we have more experience we can anticipate this errors, but as we learn we may experience them more often, so a good habit is to catch this errors.

[Seventh example:](name.py?plain=1#L8)
```
import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

```

Note:
- We want to specially give the user a more refined advice.
- We don't want to just tell them no, something went wrong or we don't want to pass
- We want to tell them, not that's too few or no, thats too many.

[Eighth example:](name.py?plain=1#L18)
```
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])

```

## Important!
Keeping all of your error handling separate from the code that you really care about, having all the ifs, elifs, perhaps at the top of your code. For design sake not to hide in the else statement the actual code that you care about. In this case we could use sys.exit.

### sys.exit
as the name suggest, it's going to do exactly that. With the system's help, it's going to exit the program then and there.

[Ninth example:](name.py?plain=1#L30)
```
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")


print("hello, my name is", sys.argv[1])

```

### slices
we can slice a list using [start : end] so we could obtain a new list with a subset of the original list.

[Tenth example:](name.py?plain=1#L18)
```
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

```

Notes:

- `[1:]` it means that is gonna start from the index 1 and the end is not set, meaning that is gonna take rest as they come.
- `[1:-1]` will excluded


### third party library, called packages

a third party library, where packages is a module essentially

we can search for any type of packages in:

[pypi.org](https://pypi.org)

example of how to use PyPI

for this we gonna use a package called 'cowsay'

for the download and installation we use pip

### pip
pip is a package manager that come nowadays with Python itself, that allow to install packages onto your system.

in the terminal:
```
> pip install cowsay
...
...
...
...
> Successfully installed cowsay-x.x
```

### Importing and using the package cowsay

#### function cow:

[Tenth example:](say.py?plain=1#L1)
```
import cowsay
import sys

if len(sys.argv) == 2:
    #per doc it only accept a string, so we concatenate our string and argument.

    cowsay.cow("hello, " + sys.argv[1])
```

#### function trex:

[Eleventh example:](say.py?plain=1#L13)
```
import cowsay
import sys

if len(sys.argv) == 2:
    #per doc it only accept a string, so we concatenate our string and argument.

    cowsay.trex("hello, " + sys.argv[1])
```

## Note:
- Why the use of system input?
   As learning build up, we strive for productivity and feeding this commands to the program at the start from the command-line makes faster, more automate programs that for example you can re lunch with only a few keys from the keyboard.


## API
APIs are not something that's Python-specific, more generally, an API is an application programming interface. It can refer to python files and functions, but often, APIs really refer to third-party services that you can write code to talk to.

Many APIs , but not all, live in the internet these days. so that so long as you have a browser or so long as you have some experience with Python programming or programming in any language, you can write code that in effect pretends to be a browser, connects to that third-party API on a server, and download some data that you then incorporate into you own program.

In python there is a popular package that allows us to accomplish this, and is called `requests`

### requests package
The request library allows you to make web request, internet request using python code essentially as though you were a browser yourself. You can automate, therefore, the retrieval of URLs that start with HTTP or HTTPS.

Even though it's third party, it's one of the most popular and commonly used packages out there in Python.

the documentation:

pypi.org/project/requests

### JSON
JavaScript Object Notation, more commonly known by the acronym JSON, is an open data interchange format that is both human and machine-readable. Despite the name JavaScript Object Notation, JSON is independent of any programming language and is a common API output in a wide variety of applications.

- For many uses, is totally format agnostic for exchanging data between computers.
- Different languages can take JSON and translate to it and it can his own language and translate it to JSON.
- An API is a mechanism whereby I can access data on someone else´s server and somehow integrate it into my own program.

[Twelve example:](itunes.py?plain=1#L1)

```
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(response.json())


```

explain code:

- First we do an error check, with no comments atm.
- Second we use a function inside the requests package, called 'get'. This will literally get some response from a server.
- Third we feed the url with the correct format for the query, concatenating our input, as to make the program more user friendly.
- Fourth we store the response in a variable called response.
- Fifth we print our response in pure JSON using the function '.json()' from request library for now.

output:

```
❯ python .\itunes.py weezer
{'resultCount': 1, 'results': [{'wrapperType': 'track', 'kind': 'song', 'artistId': 115234, 'collectionId': 1440878798, 'trackId': 1440879325, 'artistName': 'Weezer', 'collectionName': 'Weezer', 'trackName': 'Buddy Holly', 'collectionCensoredName': 'Weezer', 'trackCensoredName': 'Buddy Holly', 'artistViewUrl': 
'https://music.apple.com/us/artist/weezer/115234?uo=4', 'collectionViewUrl': 'https://music.apple.com/us/album/buddy-holly/1440878798?i=1440879325&uo=4', 'trackViewUrl': 'https://music.apple.com/us/album/buddy-holly/1440878798?i=1440879325&uo=4', 'previewUrl': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/f0/ba/a8/f0baa81a-7449-c490-f43a-b5c6e3609e3f/mzaf_3988310882581261442.plus.aac.p.m4a', 'artworkUrl30': 'https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/fc/74/67/fc74674a-1eb0-d50d-33fe-215caee529d1/16UMGIM52971.rgb.jpg/30x30bb.jpg', 'artworkUrl60': 'https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/fc/74/67/fc74674a-1eb0-d50d-33fe-215caee529d1/16UMGIM52971.rgb.jpg/60x60bb.jpg', 'artworkUrl100': 'https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/fc/74/67/fc74674a-1eb0-d50d-33fe-215caee529d1/16UMGIM52971.rgb.jpg/100x100bb.jpg', 'collectionPrice': 10.99, 'trackPrice': 1.29, 'releaseDate': '1994-01-01T12:00:00Z', 'collectionExplicitness': 'notExplicit', 'trackExplicitness': 'notExplicit', 'discCount': 1, 'discNumber': 1, 'trackCount': 10, 'trackNumber': 4, 'trackTimeMillis': 159587, 'country': 'USA', 'currency': 'USD', 'primaryGenreName': 'Pop', 'isStreamable': True}]}
```

explain output:
- apple return is technically a JSON response, but python library, transform it to a Python dictionary which happens to use wonderfully coincidentally, almost the same syntax. 
- Since is a big block of text, we could use another library to format the data a little more cleanly called json.

### json library

doc.python.org/3/library/json.html

- Allow us to manipulated JSON data, or simple print it in a format that is easy to understand.
- It comes with python, so we don't need to install it.
- For pretty printing a JSON response we use the '.dumps' function.
- we can pass argument value of indent equal to two or more so to format it.

[thirtieth example:](itunes.py?plain=1#L14)

```
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(json.dumps(response.json(), indent= 2))


```


We can now know what is in the JSON response and infer how to obtain what we want from it. 
In this case we want to access the results and only obtain the value of the key trackName. 
Since the result dictionary is in a list, we can use a for loop as to access and retrieve more than one result if the search get wider.
In this case the search is for 50 songs and only print the name of the song omitting the rest of the information.


[Fourteenth example:](itunes.py?plain=1#L14)

```
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# we change the limit to 50
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])

```

### bundle all your code that you re use in a library
If you reach a point you are reusing code from old projects again and again, those are good candidates for creating a library, so you can access then all the time.

[Fiftieth example:](sayings.py?plain=1#L1)
if we define for example a library for sayings:

```
def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

main()

```

[Sixtieth example:](say2.py?plain=1#L1)

```
import sys

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
```

- we should use `if __name__ == "__main__"` then and only then should you actually call main.
- _ _ name _ _ is a special variable whose value is automatically set by Python to be, quote, unquote "main" when you run a file from the command line.
- if not, anytime the library is imported it will execute main regardless we wanted it or not.

Correcting this in the sayings module:

[Seventh example:](sayings.py?plain=1#L17)

```
def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()

```

calling again the [Sixtieth example](say2.py?plain=1#L1)

should output the correct function this time.

and the same would work for goodbye() function.









