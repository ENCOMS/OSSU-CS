# Final project guidelines

[cs50p final project link](https://cs50.harvard.edu/python/2022/project/)

[] - Your project must be implemented in Python.

[] - Your project must have a `main` function and three or more additional 
  functions. At least three of those additional functions must be 
  accompanied by tests that can be executed with `pytest`.

[] - Your `main` function must be in a file called `project.py`, which 
  should be in the “root” (i.e., top-level folder) of your project.

[] - Your 3 required custom functions other than `main` must also be in 
  `project.py` and defined at the same indentation level as `main` 
  (i.e., not nested under any classes or functions).

[] - Your test functions must be in a file called `test_project.py`, which 
  should also be in the “root” of your project. Be sure they have the 
  same name as your custom functions, prepended with `test_` ( 
  `test_custom_function`, for example, where `custom_function` is a 
  function you’ve implemented in `project.py`).

[] - You are welcome to implement additional classes and functions as 
  you see fit beyond the minimum requirement.

[] - Implementing your project should entail more time and effort than is 
  required by each of the course’s problem sets.

[] - Any pip-installable libraries that your project requires must be 
  listed, one per line, in a file called requirements.txt in the root 
  of your project.


## Getting started

Here are some questions that you should think about as you start:

+ What will your software do?
show comparative stat on power armor with different modules
+ What features will it have?
User Interface (UI):
- Terminal interface
- Color and emoji when avalible.
- Clean and modern design.

Functionality:
- Create, edit, and delete comparative stats
- Get recommended builds.

Performance:
- Quick loading and updating.
- Handle hundreds of combinantion efficiently.

Security: ?
- User authentication (e.g., via Google or email).
- Encrypted data storage.

Support and Maintenance:
- In-app help and tutorials.
- Regular updates to add features and fix bugs.
- Customer support through chat and email.

+ How will it be executed?
On terminals windows and linux.

+ What new skills will you need to acquire?
 - terminal styles
 - mysql for store and retrieve data
 - build a project
 
+ What topics will you need to research?
 - information on stats on power armor and modules that affect 
 functionality
 - information on perk cards that influence performance
 - difference between lvls, hp, ap on each corresponding level.
 - serum stats modifiers

+ If working with one or two classmates, who will do what?

+ In the world of software, most everything takes longer to implement 
than you expect. And so it’s not uncommon to accomplish less in a fixed 
amount of time than you hope. 

 + What might you consider to be a good outcome for your project?
    that at less work for comparing excavetor, sindicate and vulkan
    and with a fair style that permit that the person underthen easily
    
 + A better outcome?
    that it work with more than 6 power armor and the style is good
    readable and functional.
    
 + The best outcome? 
    that it will work for all power armor and show values correctly and
    with a nice style that give the information quick.
    
Consider making goal milestones to keep you on track.

## How to Submit

## Step 1 of 3

[] - Create a short video (that’s no more than 3 minutes in length) in which 
you present your project to the world. Your video must begin with an 
opening section that displays:

+ your project’s title;  []
+ your name; []
+ your GitHub and edX usernames; []
+ your city and country; []
+ and, the date you have recorded this video. []

### Note 1 - How to record:

It should then go on to demonstrate your project in action, as with 
slides, screenshots, voiceover, and/or live action. See 
[howtogeek, how to record on windows, linux, 
android](howtogeek.com/205742/how-to-record-your-windows-mac-linux-android-or-ios-screen)
for tips on how to make a “screencast,” though you’re welcome to use an 
actual camera. Upload your video to YouTube (or, if blocked in your 
country, a similar site) and take note of its URL; it’s fine to flag it 
as “unlisted,” but don’t flag it as “private.”

Submit [this form!](https://forms.cs50.io/5e2dd8e8-3c8b-4eb2-b77d-085836253f26)

## Step 2 of 3

[] - Create a `README.md` text file (named exactly that!) in your `~/project` 
folder that explains your project. This file should include your:
+ Project title. []
+ URL of your video. []
+ A description of your project. You may use the below as a template. []

```txt
    # YOUR PROJECT TITLE
    #### Video Demo:  <URL HERE>
    #### Description:
    TODO
```

### Note 2 - How to use markdown:

If unfamiliar with Markdown syntax, you might find GitHub’s [Basic 
Writing and Formatting 
Syntax](https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/basic-writing-and-formatting-syntax) 
helpful. If you are using the CS50 Codespace and are prompted to “Open 
in CS50 Lab”, you can simply press `cancel` to open in the Editor. You 
can also preview your .md file by clicking the ‘preview’ icon as 
explained here: [Markdown Preview in 
vscode](https://code.visualstudio.com/docs/languages/markdown#_markdown-preview). 
Standard software project `README`s can often run into the thousands or 
tens of thousands of words in length; yours need not be that long, but 
should at least be several hundred words that describe things in 
detail!

### Note 3 - Important points of the README.md file:

+ Your README.md file should:
be minimally multiple paragraphs in length, around 500 words or more. [] 

The readme.md file should explain:

+ What your project is. []
+ What each of the files you wrote for the project contains and does. []
+ If you debated certain design choices, explaining why you made them. []

Ensure you allocate sufficient time and energy to writing a README.md 
that documents your project thoroughly. Be proud of it! A README.md in 
the neighborhood of 500 words is likely to be sufficient for describing 
your project and all aspects of its functionality. If unable to reach 
that threshold, that probably means your project is insufficiently 
complex.

### Submit

Execute the `submit50` command below from within your `~/project` directory 
(or from whichever directory contains `README.md` file and your project’s 
code, which must also be submitted). If your project does not meet all 
the requirements above, it may be rejected, so be sure you have 
satisfied all of the bullet points atop this specification and written 
a thorough `README`:

`submit50 cs50/problems/2022/python/project`

## Step 3 of 3

That’s it! Your project should be graded within a few minutes. Be sure 
to visit your gradebook at [cs50.me/cs50p](https://cs50.me/cs50p) a few 
minutes after you submit. It’s only by loading your Gradebook that the 
system can check to see whether you have completed the course, and that 
is also what triggers the (instant) generation of your free CS50 
Certificate and the (within 30 days) generation of the Verified 
Certificate from edX, if you’ve completed all of the other assignments.

This was CS50P!
