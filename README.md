- Expects a new-line separated list of values
- Will fail if anything not parseable as int is included in list, UNLESS line starts with #
- Currenlty rounded to 4 decimal places
- Execution by running `python sdi.py <target_file>`
  - e.g. from this directory `python sdi.py test.txt` should yield "SDI for test.txt is: 1.3269"