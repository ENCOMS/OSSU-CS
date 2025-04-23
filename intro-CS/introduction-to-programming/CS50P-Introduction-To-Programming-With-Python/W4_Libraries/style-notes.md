# Topic: Style

## link: https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@ea6fc5c250bc4fc786575db3b93611a5/block-v1:HarvardX+CS50P+Python+type@vertical+block@a474d73bd6034c91ba86bc6baed0ad67


Hope for:
- Strive for well designed code
using relatively few lines
- Ensuring it's readable
- Using functions that save you from reinventing wheels.

But having all those points, maybe is not manifesting the best styles.
In python there are proposals, where 
PEP 8 or Python enhancement proposal.

### PEP 8
peps.python.org/pep-0008

PEP 8 is a set of proposals that the community within the world of python typically generate to not only propose new ideas, but also to codify, ultimately, certain standards.

If a code is hard to read, messy or less maintainable, you're only increasing the probability to introduce bugs down the line.

"Readability counts"

"A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.

can boils down to:
- Indentation
- Tabs or Spaces?
- Maximum Line Length
- Blank Lines
- Imports
- ...

- in python the indentation they prescribed that is 4 spaces.
- in python no tabs, the editor should instead place 4 spaces.
- python have something to sa about how long a line should get.
- Some blank lines between blocks of code and comments.
- Python have preferences where the import statement should be placed.


a possible help to solve this problems is the used of a program called pylint.

### pylint
Is a program, which is an example of what's generally know as a linter, which is a program that rather statically analyzes, read your code top to bottom, left to right and tries to figure out if there are potentially mistakes therein, or at less inconsistencies with something like a prescribed style guide.

for example there are some like pycqa that can be installed by pip

pycodestyle.pycqa.org

or pycodestyle less noise.

or one very popular that can be install by pip is called black.

pip install black

documentation
black.readthedocs.io

so for usign it with in a file, so as to format it with pep 8 guide style, we do as follow.

`> black file_to_process.py`

All done!
1 file reformatted.

and that is it, is formatted with the current pep 8 guidelines.
