- Expects a new-line separated list of values
OR
- a new-line separated list where each line is an integer followed by a space character (e.g. test2.txt and test3.txt)
- Will fail if anything not parseable as int is included in list, UNLESS line starts with #
- Currenlty rounded to 4 decimal places
- Execution by running `python sdi.py <target_file>`
  - e.g. from this directory `python sdi.py test.txt` should yield "SDI for test.txt is: 1.3269"
