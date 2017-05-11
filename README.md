# Assignments and Graders for Discrete Optimization Coursera

[![Build Status](https://travis-ci.org/discreteoptimization/assignment.svg?branch=master)](https://travis-ci.org/discreteoptimization/assignment)
[![codecov](https://codecov.io/gh/discreteoptimization/assignment/branch/master/graph/badge.svg)](https://codecov.io/gh/discreteoptimization/assignment)

This repository includes all of the tools required for building, deploying, and grading the assignments in the Discrete Optimization course on Coursera (on the 2nd generation platform).  The code for submission and grading are build in Python and are compatible with versions 2 and 3.  The python unit testing framework pytest and pytest-cov are used to ensure quality control.  Build scripts are used to automatically build student handouts, in the form of zip files, and a Coursera compliant docker image for grading submissions.


## Installation

The student handouts and graders have no package dependencies and only require a clean python 2 or 3 installation.
Running the unit tests and coverage reports requires pytest and pytest-cov, see the `requirements.txt` for detailed detailed requirements. 
The courseraprogramming package is used for testing the docker container.


## Usage

Packaging and deployment of the begins with running `save_all.sh`.  
This script runs the provided trivial solvers on all of the graded problems and saves the output to local directories.
Once this is complete, `test.it` is used to run all of the grader unit tests and generate a code coverage report.
A detailed code coverage report can be generated with  `test.it --cov-report=html`.
Assuming all of the unit test pass, `build.sh` is used to build both the student handouts and the grader.
The handouts zips are placed in the "started_files" directory.
The grader zip is placed int he "docker" directory.
Inside the "docker" directory `build.sh` provides the basic instructions for deploying a Cousera docker container.
Once the docker container is built, `grade_in_container.py` can be used to test the containerized grader on all of the submissions that were "saved" with the `save_all.sh` script.
If this test passes, `post.sh` can be used by a course administrator to update all of the assignment graders.

Feedback on how to improve this test-and-build processing is encouraged.  We also welcome other classes to use this code as a basis for developing their own customer grading framework.


## Development

Community-driven development and enhancement of these assignments is welcomed and encouraged.  Please fork this repository and share your contributions to the master with pull requests.


## Acknowledgments

The assignments presented here were inspired by those used in "Solving Hard Problems in Combinatorial Optimization" (i.e. CS 258), a course which Pascal Van Hentenryck developed at Brown University for more than ten years.

This implementation was developed primary by Carleton Coffrin, however many others have contributed to these assignments, including Pascal Van Hentenryck, Andrea Rendl, Mark Mammel, and Victor Pillac.

## Citing Discrete Optimization

If you found this code or this course useful in your work, you may wish to cite the following paper,
```
@inproceedings{VanHentenryck:2014,
  author = {Van Hentenryck, Pascal and Coffrin, Carleton},
  title = {Teaching Creative Problem Solving in a MOOC},
  booktitle = {Proceedings of the 45th ACM Technical Symposium on Computer Science Education},
  series = {SIGCSE '14},
  year = {2014},
  isbn = {978-1-4503-2605-6},
  location = {Atlanta, Georgia, USA},
  pages = {677--682},
  numpages = {6},
  url = {http://doi.acm.org/10.1145/2538862.2538913},
  doi = {10.1145/2538862.2538913},
  acmid = {2538913},
  publisher = {ACM},
  address = {New York, NY, USA},
} 
```

## License

MIT, see LICENSE file for the details.
