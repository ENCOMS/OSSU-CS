# File I/O

## Definition

Is all about writing code that can read from, that is load information
from, or write to, that is save information to, files themselves. (tf 00:01:00)

This way we can save data persistently. (tf 00:01:18)

[Example 1 - names.py - Simple program that collects peoples names](./names.py?plain=1#L16)

```python

    def main():
        names = []

        for _ in range(3):
            names.append(input("What's your name? "))

        for name in sorted(names):
            print(f"Hello, {name}")

```

📝 **Notes:**

+ If we want to use for loop and not use a normal i
variable, we use can use _ that is a pythonic convention that means
that the variable can be wharever since it wont be use later.
+ names = [] it means that we are assigning an empty list.
+ names.append(input()) means we append the input or any other type of
data to the list names.
+ In the second for loop we use name variable to store each of the strings
of names list. + sorted(names) Means we are gonna use the function sorted()
to sort a the list of values. tf 00:04:24

Unfurtunely this code wont allow to have the input information persistently
thats where file i/o comes in.

## Files - Persistently information

Files are a way of storing information persistently on any device or cloud, so
they are there when you come back and run the program. (tf 00:05:45)

## open()

Is a function to open a file, but to open it up programmatically, so that
the programmer, can actually read information from it or write information
to it. (tf 00:06:30)

Documentation link:
docs.python.org/3/library/functions-html#open

Example 2 - Using File I/O - open() function with "w" and write/close methods

```python

    def main():
        name = input("What's your name? ")
        
        file = open("names.txt", "w")
        file.write(name)
        file.close()

```

📝 **Notes:**

+ It use is pretty straight foward, it minimally just requires the name
of the file that we want to open and, optionally, how we want to open it.
+ names.txt is first argument, indicate the file we are gonna use or
create, in this case a text file.
+ "w" is the second argument write, it tells open() function to write on the file, and
if not yet created it will create it for us. (tf 00:07:29)
+ the open() function returns a file handle that is a special value that
allows us to access that file subsequently, that can be assign to a
variable, in this case variable name File. (tf 00:07:39)
+ file.write(name) is a method that comes with open files, that allows to write to the file. (tf 00:07:57)
+ file.close() will close and effectively save the file. (tf 00:08:03)
+ .write() not only write on file, it overwrite the content each time. (tf 00:10:14)
+ The only issue now is that "w" not only write or create, it overwrite the file each time.

Example 3 - Using File I/O - open() function with "a" and write/close methods

```python

    def main():
        name = input("What's your name? ")
        
        file = open("names.txt", "a")
        file.write(name)
        file.close()

```
📝 **Notes:**

+ Now to append and not overwrite the information we change "w" for "a" instead as argument,
this will result in appending the information on the file.(tf 00:10:33)
+ "a" append recreate the file if not already created. (tf 00:10:56)
+ In this version there is a flaw, is looks like is concatenating the names, but is appending them together,
difficulting getting them back later.
+ .write method take us literality and don't add anything else. For that we need to add a separator manually.
(tf 00:12:40)

Example 4 - Using File I/O - open() function with "a" and write/close methods and f-strings for new line

```python

    def main():
        name = input("What's your name? ")
        
        file = open("names.txt", "a")
        file.write(f"{name}\n")
        file.close()

```
📝 **Notes:**
+ In this case we can use f-strings that contains name and backslash "n"
at the end. This will print a new line. (tf 00:12:55)
+ Generally, when storing data long-term in a file, we should do it cleanly,
like one name at the time.(tf 00:13:50).

## Forgetting to close files

Its too easy to forget to close a file, but sometimes, it can create problems.
Files could get corrupted or accidentally deleted or the like depending on what
happens in our code. (tf 00:14:08)

There is another aproach, so we don't need to close the file ourself.

The pythonic way to manipulate files is to use a keyword called "with"

## with keyword

It allows to specify that we want to open and automatically close some file.

Example 5 - Using File I/O - pythonic way to close files, with statement

```python

    def main():
        name = input("What's your name? ")

        with open("names.txt", "a") as file:
            file.write(f"{name}\n")
        
```

📝 **Notes:**
+ with let us open the file and close it at the end of the program.
+ as file, is use to specify the name of the variable that should be
assigned the return value of open function with "with" statement. (tf 00:15:02)
+ In the context of the "with" statement, we indent the code bellow it
so that it close automatically if the code is no longer indented. (tf 00:15:21)

## Reading back a file - .readlines()

If we want to read a file to load and not save we use in open() the "r"
argument that indicate to load not save the file. (tf 00:16:29)

Example 6 - Read back files - .readlines

```python

    def main():
        with open("names.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            print("Hello,",  line.rstrip())

```

📝 **Notes:**

+ .readlines method read all the lines from a file and return them as a list. (tf 00:16:55)
+ In this case since each name exist after a new line, the print will print the
new line plus his default new line, making the output look ugly.
+ We can use .rstrip() method to eliminate the white space to the right of the string
solving the issue of the new line.


## Reading back a file - Python way to combine all for better design

In the last example we are doin twice as work, reading, storing
reading again then print. 

In python we can do a for loop to the file handle then print the results
of each iteraction as we read the file. (tf 00:20:14)

Example 7 - Read back files - Python way to combine all for better design

```python

    def main():
        with open("names.txt", "r") as file:
            for line in file:
                print("Hello,",  line.rstrip())

```

## Reading a file - Sorting

To sort the information, we need first read the file and store the names,
sort them, then hand back to be print function. (tf 00:21:32)

Example 8 - Read back files - Sorting

```python

    def main():
        names = []
        
        with open("names.txt") as file:
            for line in file:
                names.append(line.rstrip())

        for name in sorted(names):
            print("Hello,", name.rstrip())

```

📝 **Notes:**
+ names = [] create an empty list to store the lines (tf 00:21:48)
+ with open("names.txt") we don't need to specify "r" is the default behavior. (tf 00:22:03)
+ names.append(line.rstrip()) indicates to append the names to the list, not to the file.
+ line.rstrip() indicate to remove at each interaction the white space to the right.
+ sorted(names) indicate we use python sorted function to sort the list names.

Is a very common tecnique, create a variable, adding or appending information to it, just to
collect it in one place and then do something interesting with that collection, that list. (tf 00:24:15)

In case we only wanted to sort the file, we can do it like this:

```python

    def main():
           
        with open("names.txt") as file:
            for line in sorted(file):
                print("Hello,", line.rstrip())

```

But this way, it eliminate the possibility to do anything else with this information, like uppercasing or
other manipulations.

## Sorted() - Reverse

If we want to sort in reverse order we can check the documentation:
[docs.python.org/3/Library/functions.html#sorted](docs.python.org/3/Library/functions.html#sorted)

summary:

sorted(iterable, /, *, key=None, reverse=False)

+ iterable it means we can loop over it, one thing at a time.
+ key indicates how you want to sort it
+ reverse indicate if we want it to read in reverse order, by default is False.

```python

    def main():
        names = []
        
        with open("names.txt") as file:
            for line in file:
                names.append(line.rstrip())

        for name in sorted(names, reverse=True):
            print("Hello,", name.rstrip())

```

📝 **Notes:**
+ Whenever we have a question of how to do someting, we can consider,
what does the documentation say about it.

## Separate information

If we want to separate information, we need some type of convention to separate
chunks of information, for example csv.

## CSV comma-separated values

It's a very common convention to store multiple pieces of information that are
related in the same file. (tf 00:30:28)

Example of a CSV File: student.csv

```txt
Hermione,Gryffindor
Harry,Griffindor
Ron,Gryffindor
Draco,Slytherin
```

📝 **Notes:**
+ We can think these commas as representing a columnm, like in Excel, Google sheets or
Apple numbers. (tf 00:31:05)
+ CSV files are very common for import or export information to programms like Excel, Google sheets,
Apple numbers. (tf 00:31:29)
+ Is a very simple text format, that just separates values with commas and different types of values
with new lines. (tf 00:31:39)


## CSV - reading different values - list

Example 10 - Separate Information - CSV - reading two types of value - list

```python

    def main():
        with open("students.csv") as file:
            for line in file:
                row = line.rstrip().split(",")
                print(f"{row[0]} is in {row[1]}")


```

📝 **Notes:**
+ we use open("student.csv") without any other argument. by defaul it would
be read "r". (tf 00:32:42)
+ In this case, since we are using a loop the strings .split(",") method to
separate in two variables for each line using , as separator. (tf 00:34:40)
+ .split() method can split a string with a delimeter and return a list of
strings. (tf 00:34:57)
+ row variable because is common to think on a csv file, each line as row
and each value separated by comma a columms. (tf 00:35:09)
+ to access items on a list with indicate square brackets the position
row[0]. (tf 00:36:16)
+ We could write a program to edit a particular student house. But right
now we can read the file, manipulate the information and write it back.
This can be easier in small scale but could be slow in bigger files,
on that case we need to implement a better solution.  (tf 00:38:15).

## CSV - reading different values - assign to variables

Example 11 - Separate Information - CSV - reading two types of value - assign then to variables.

```python

    def main():
        with open("students.csv") as file:
            for line in file:
                name, house = line.rstrip().split(",")
                print(f"{name} is in {house}")

```

📝 **Notes:**

+ In python if we know the quantity of values, in this case two, we don´t have
to throw them all into a list, we can unpack them simultaneusly into two separated variables.
 
## CSV - reading different values - sorting

Example 12 - Separate Information - CSV - reading two types of value - sorting using list

```python

    def main():
        students = []
        
        with open("students.csv") as file:
            for line in file:
                name, house = line.rstrip().split(",")
                students.append(f"{name} is in {house}")
        
        for student in students:
            print(student)

```

📝 **Notes:**
+ We unpack the name in house in variables as before
+ There is no print since we want to store the information in the list
students.
+ We append the fstring with name and house at the same time.
+ We use another loop since the last one was for reading and creating a
list from the csv file.
+ We print all the values store in the student list.

## CSV - reading different values - sorting using list and dictionary

Example 13 - Separate Information - CSV - reading two types of value - sorting using list and dictionary

```python

    def main():
        students = []
        
        with open("students.csv") as file:
            for line in file:
                name, house = line.rstrip().split(",")
                student = {"name": name, "house": house}
                students.append(student)
        
        def get_house(student):
            return student["house"]
        
        for student in sorted(students, key=get_house, reverse=True):
            print(f"{student['name']} is in {student['house']}")

```

📝 **Notes:**
+ We can create an empty list to store dictionarys
+ We construct the dictionary with key and values
key=name/ value=student name, key=house/ value=student house.
+ We can´t use sorted() function right away to the list since it has dictionarys
not names inside.
+ We can create a temporally function to access the dictionary and return a value.
+ We can use the named parameter of the sorted() that is named "key", where we
can specify what key of the dictionary shall we use in the sort. (tf 00:47:19)
+ python allows to pass functions as argument to other functions. In this case 
a function that gets back the name from a dictionary and pass it to the key named parameter of sorted(). 
(tf 00:48:05)
+ We can change the function from get_names, to get_houses so to sort by house instead.
+ We change the named parameter reverse=True to reverse the sort. (tf 00:49:59)
+ By using a dictionary to keep data together until the last minute, we
can have full control over the information inself. (tf 00:50:21)

## Questions

### Sorting not using loops or dictionarys

With python alone, we have to create it, but maybe if using sorting with librarys
and other tecniques it may be posible. ecause someone else has written that code.

### why not use () in key=get_house function called

Because the named parameter key of sorted() function call the function by name
not needing the (). This is done in each interaction of the for loop.

### Why using a list of dictionarys

Because those dictionarys represent an student, where student has a name and house
and we want to maintain the association. (tf 00:52:45)
In this case we only need a list of key-value pairs right now. (tf 00:53:02)


## CSV - reading different values - sorting using list and dictionary - lambda functions

A lambda function is an anonymous function that has no name, because we
don't need to name it if we are only call it in one place. (tf 00:54:24)


Example 14 - CSV - sorting with list, dictionary and lambda function

```python

    def main():
        students = []
        
        with open("students.csv") as file:
            for line in file:
                name, house = line.rstrip().split(",")
                student = {"name": name, "house": house}
                students.append(student)

        for student in sorted(students, key=lambda student: student["house"]):
            print(f"{student['name']} is in {student['house']}")

```

📝 **Notes:**
+ we use in `lambda` function in the the named parameter key of the sorted function (tf 00:54:30)
+ then we use `student`, which is the name of the parameter it expect to take 
(in this case student is from the for loop). (tf 00:54:35)
+ We don't even need to type return key, we only use `:` to indicate that the next part
would be the return value in this case `student["house"]`
+ To resume we only use lambda keyword, the expected parameter, : to indicate
that the next part is the return value `lambda student: student["house"]`
+ We don't use `def` or `return` keywords or even name the function. (tf 00:54:58)
+ It work the same as last example but is a little better design, since we din't waste
lines of code defining a function that would be only called in one place. (tf 00:55:48)

## Questions

### Can we use lambda twice?

We can define as many as we need, but need to be generally in the context like this:
+ Where you want to pass to some function to a function that itself does not need a name. (tf 00:56:22)

### Can lambda take multiple parameters?

It can, separating each with a comma with the name of those parameters. (tf 00:56:51)

## CSV - ValueError if too many commas in a row

Example 15 - CSV - too many commas in a row

Using the same example as before but changing house for homes in the csv file:

`students.csv`
Harry, Number Four, Privet Drive
Ron, The Burrow
Draco, Malfoy Manor

The code of student.py have to change to reflect it:

```python

    def main():
        students = []
        
        with open("students.csv") as file:
            for line in file:
                name, home = line.rstrip().split(",")
                student = {"name": name, "home": home}
                students.append(student)

        for student in sorted(students, key=lambda student: student["name"]):
            print(f"{student['name']} is from {student['home']}")

```

Output:
`ValueError: too many values to unpack (expected 2)`


📝 **Notes:**
+ The problem comes when it try to unpack the first row for the two variables,
since the address has 2 commas instead of 1 as expected, it generate 3 values,
not two as before. (tf 00:59:57)
+ We may try to solve this with clever ways, but there may come errors down
the line, for that, maybe it would be better to use a library that can deal with this
cases.


## CSV Library

Since is pretty common to store data in files, and csv are incredibly common to
use, python has a library for it, this solve many of the problems we may face on
reading or writing csv files because they have already been solved by others at some
point so we don't have to reinvent the weel.(tf 01:01:02)

link of the documentation:
docs.python.org/3/library/csv.html

Example 16 - CSV Library - reader - solving too many commas (corner case)

+ Using a single variable in the for loop will store a list of values from the reader
that needs to be accessed via list index for the appending.

```python

    import csv

    def main():
        students = []
        
        with open("students.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                students.append({"name": row[0], "home": row[1]})

        for student in sorted(students, key=lambda student: student["name"]):
            print(f"{student['name']} is from {student['home']}")

```

+ Using two variable in the for loop to store the values from reader and use then
in the append.


📝 **Notes:**
+ We `import csv` at the top of our file, to have access to the csv library.
+ This library was written by someone to deal with this corner cases. (tf 01:02:17)
+ We keep the list in which we store all the students.
+ We change using the library syntax the contents bellow `with`
+ From the csv module we use the function `reader` that read the csv file for us
and figure out, where are the commas, where are the quotes, where are all the potential
corner cases and deal then for us. (tf 01:02:47)
+ We use a for loop to iterating the reader that now contains the information, not the file. (tf 01:03:15)
+ In the for loop we append to the students list the dictionary which name has a value of row first value (0)
and home has a value of row second value (1). (tf 01:03:41)
+ Reader for each line of the file, returns a row, but it returns a row that is a list, 
which is to say the first element of that list is the student name, and the next is the
address.
+ To access this elements of a the list we use the index that start with `[0]` `[1]` `[2]`
and so for.
+ If we know the quantity of variables we are gonna unpack, in this case two, we can unpack them
in the same for loop to two variables, so we don't have to use one thats gonna be a list of values
we have to access using index.
+ So we are creating dictionarys like before, where we are grabbing the information from the reader not the file inself,
not using split, since the reader is going to figure out, where are those commas, quotes and so for, solving
the problems for us. (tf 01:04:41)

CSV library get us out of the business of reading each line ourself and reading each of those commas and splitting.

## Questions:
### Can we read and write the file as we go along?

- Yes, but the access is sequential not random access, if we want to get to one point at the end, we need to read all
the file until the place we want.
- The best aproach for small files is to read the file, make the changes and save it.
- If the file is too massive, it could be doable if is too expensive time-wise to change the whole thing.

### Can we write paragraths

Yes, we can write as much text as we want.

### Can a user choose himself a key?

Yes,we can create a program that ask the user for a name and house and write in a csv file.


## CSV - Storing names of columns in a csv file

With CSV library we dont have to rely on either getting a row as list and using bracket 0 or bracket 1 or
unpack things manually. (tf 01:08:32)

Changing students.csv to add name and house in first row, so to make it work with DictReader

```txt

name,home
Harry,"Number Four, Privet Drive"
Ron,The Burrow
Draco,Malfoy Manor

```

Example 17 - CSV DictReader

```python

    import csv

    def main():
        
        students = []
        
        with open("students.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"],"home": row["home"]})

        for student in sorted(students, key=lambda student: student["name"]):
            print(f"{student['name']} is from {student['home']}")

    if __name__ == "__main__":
        main()


```

📝 **Notes:**

+ We can do this like in spread sheets the first row have boldface or contains the names of those columns.
+ In this case we can name our colums in the csv file, `name,home` and in the code instead of using reader
we use the `DictReader`
+ `DictReader` will read the file each line as a row, but loading each line of text not as a list of columns
but as a dictionary of columns. Using the first columm as keys and the subsequent lines as values for each
key. (tf 01:09:25)
+ A reader return lists.
+ A dict reader return dictionarys, one at a time.
+ This make the code more robuts as we can move columns around, since we are not asuming that the first is name
and second home, since DictReader will create the dictionary like it say the first row. (tf 01:10:49)
+ If we change students.csv like this, the code should still work since the DictReader is using the first row as
a guide of what should do:

```txt

home,name
"Number Four, Privet Drive",Harry
The Burrow,Ron
Malfoy Manor,Draco

```

## Questions

### What is the importance of the new line in the CSV file?

+ It's partly a convention, in the world of text files, we humas have just been, for decades, in the habit
of storing data line by line.
+ It s visualy convenient
+ It's easy to extract from the file because you just look for new lines, so the new line just separates some
data from other data.

### What if we want to add house besides home and name?

Yes we can, thats is the power of DictReader, it can change overtime, it can have more and more columns, so the
code wont break because of taking assumptions of what is each columns.

If for example we add the houses:

```txt

name,home,house
Harry,"Number Four, Privet Drive",Griffindor
Ron,The Burrow,
Draco,Malfoy Manor

```

## CSV Library - write data to files

## CSV Writer - Assuming order

```python

    import csv

    def main():
        name = input("What's your name? ")
        home = input("What's your home? ")
        
        with open("student.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([name, home])
            
```

📝 **Notes:**
+ For this students.csv are empty and only leave `name,home` as first row,
since we are anticipating names and homes.
+ We since is mandatory `import csv`, then ask the user for inputs of name and home.
+ `with open("students.csv", "a") as file:` we include this time "a" for append, since we
want to open, append and close the file. as file indicate the convention for
the variable handler that is `file` is as file.
+ `writer` variable, is a variable named as what we need this time that is write to a file.
+ `csv.writer(file)` where .writer() is the function from csv library that write to files, where
it only take as argument the `file` variable.
+ csv.writer writes rows as list of values.
+ `writer.writerow([name, home])` is a method (.writerow) where we pass the line that we want to write
to the file
specifically as a list in this case `[name, home]`. (tf 01:15:10)
+ Running the code and typing: for name Harry and for home Number Four, Privet drive
It append to the students.csv like:
```txt
name,home
Harry,"Number Four, Privet Drive"
```
+ the `writer` handle the case of escaping of any string that themselves contained a commad.
This is to differenciate the commas from the csv comma. (tf 01:16:25)

## CSV DictWriter - Not assuming order, only passing a list

If we're keeping track of what's the name and what's the home, we could use a dictionary
to associate those keys with those values. (tf 01:16:43)

Example 19 - CSV DictWriter - Not assuming order, only passing a list


```python

    import csv

    def main():
        name = input("What's your name? ")
        home = input("What's your home? ")
        
        with open("students.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "home"])
            writer.writerow({"name": name, "home": home})

```


📝 **Notes:**
+ Again for this students.csv we leave only `name,home` as first row,
since this would be our headers. (tf 01:16:48)
+ We state the `with open("students.csv", "a") as file:` as before.
+ csv.DictWriter writes rows as dictionaries where keys correspond to the column names.
+ `writer = csv.DictWriter(file, fieldnames=["name", "home"])` takes as second argument named `fieldnames`
that indicate a hint of the order of the columns that we want to write. These argument are the string names
of the columns, in this case `["name", "home"]`. This ensure that no matter if the order change we still 
write in the correct place.
+ `writer.writerow({"name": name, "home": home})` writerow() method will write a row with the dictionary
+ if we change the order of key/value `writer.writerow({"home": home, "name": name})`, the second argument of open(),
`fieldnames`, ensure that the information go where it should independently of the order inside the dictionaries
because what we need are the keys and values.

## Questions

### What is best to use double or single quotes?
We can use both, but we need to be self-consistent, so to stylistically your code look the same all throughout.


### Can we use multiple csv files in any program?
Yes you can use as many csv files as you want. Its just one of the formats that you can use to save data.

### Is there a way to prevent errors reading and writing csv files?

If the librarys are 100% correct, there nothing should go wrong. The user, the human factor tend to be
the problem.

## Binary files
Is a file that's really just zeros and ones. They can be laid out in any pattern you might want, particularly
if you want to store not textual information, but graphical, or audio, or video information. (tf 01:23:42)

## Pillow

Is a popular library that allows us to navigate image files and to perform operations on image files.
We can apply filters like in instagram, you can animate image as well. (tf 01:24:00)

link of documentation:
pillow.readthedocs.io

## Pillow and Gif files:

Example 20 - Pillow library - Gif animation


📝 **Notes:**
+ first we `import sys` so to have access to sys.argv.
+ second `from PIL import Image` from the pillow library we are going to import support for images specially.
+ third create an empty list to store the images.
+ fourth `for arg in sys.argv[1:]:` create a for loop to catch via sys.argv the name of the images we are
going to append to the empty list `images`
+ fifth `image = Image.open(arg)` indicate that Image.open() will open an image and store the information in 
the variable `image` one of the argument at the time.
`sys.argv`
+ `images.append(image)` indicate that `.append` will append to the `images` list the arg inside `image` variable.
+ `images[0].save` .save method will save the image file starting from index 0.
+ `"costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0`
+   `"costumes.gif"` indicate the name of the file to be save on disk.
+   `save_all=True` indicate to the library to save all of the frames we pass to it.
+   `append_images=[images[1]]` indicate to append a list of images, in this case the next on images list.
+   `duration=200` indicate the duration of 200 miliseconds.
+   `loop=0` indicate with 0 times to loop infinite
+ `sys.argv[1:]` since sys.argv takes the commandline input like a list of strings including the name of the
file as the first string, we need to slice the list so we can start from the next index in this case `[1]`
and to include the rest with `:` to indicate to to take the rest of the strings after. (tf 01:30:10)
