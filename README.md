![Intro page](./images/lua-to-python2.gif)

# Smart Summaries

[![License](https://img.shields.io/github/license/jayrajmulani/group1-se-homeworks)](https://github.com/jayrajmulani/group2-se-homeworks/blob/main/LICENSE)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Build](https://github.com/jayrajmulani/group1-se-homeworks/actions/workflows/auto-test.yml/badge.svg)](https://github.com/jayrajmulani/group1-se-homeworks/actions/workflows/auto-test.yml)
[![Travis](https://app.travis-ci.com/jayrajmulani/group1-se-homeworks.svg?branch=main)](https://app.travis-ci.com/github/jayrajmulani/group2-se-homeworks/pull_requests)
![Repo size](https://img.shields.io/github/repo-size/jayrajmulani/group1-se-homeworks)
[![Contributors](https://img.shields.io/github/contributors/jayrajmulani/group1-se-homeworks.svg)](https://github.com/jayrajmulani/group2-se-hw1/graphs/contributors)
[![DOI](https://zenodo.org/badge/532305928.svg)](https://zenodo.org/badge/latestdoi/532305928)

Python scripts for creating Smart Summaries for CSV files by translating a lua system to python.

## Table of Contents

1. [Background](#background)
2. [Getting started](#getting-started)
3. [File and function mapping](#file-and-function-mapping)
4. [License](#license)
5. [Contributors](#contributors)

## Background

Lua is a powerful programming language with several salient features like:

- Lightweight : Because of the small number of core libraries required
- Fast : As it is mapped to C in many ways, the execution of Lua codes are very fast
- Flexible : Lua is a very versatile programming language as well

Lua has been in use in several prominent sites on the internet such as alibaba.com and roblox.

This repo aims to convert a sample code in Lua to Python, preserving the core logic of the code.

## Getting Started

### Pre-requisites

Ensure python is installed. You can check the version of python in the system using:

```bash
python --version
```

Check if pip is installed. This can be done with the command:

```bash
pip --version
```

The csv file can be accessed in the [Data folder](./data/file.csv)

### Installation

Clone this repository using

```bash
git clone https://github.com/jayrajmulani/group2-se-homeworks.git
```

You can download all the dependencies required to run the file using:

```bash
pip install -r requirements.txt
```

## File and function mapping

The implementations for `Num`, `Sym`, `Cols`, `Row` and `Data` classes are done in this repo.

The scripts for test cases `the`, `sym`, `num`, `bignum`, `eg.csv`, `eg.data` and `eg.stats` are also prepared [here](./tests/tests.py). A custom test engine has also been developed to run the test cases.

The Lua classes and corresponding python implementation scripts are listed below:

| Class | Corresponding python script |
| ----- | --------------------------- |
| Num   | [Num](./code/num.py)        |
| Sym   | [Sym](./code/sym.py)        |
| Cols  | [Cols](./code/cols.py)      |
| Row   | [Row](./code/row.py)        |
| Data  | [Data](./code/data.py)      |

## Code Coverage

| Name                               | Stmts | Miss | Cover |
| ---------------------------------- | ----- | ---- | ----- |
| [tests/tests.py](./tests/tests.py) | 119   | 8    | 93%   |
| [code/cli.py](./code/cli.py)       | 49    | 8    | 8%    |
| [code/cols.py](./code/cols.py)     | 27    | 1    | 96%   |
| [code/config.py](./code/config.py) | 1     | 0    | 100%  |
| [code/data.py](./code/data.py)     | 40    | 2    | 95%   |
| [code/main.py](./code/main.py)     | 15    | 1    | 93%   |
| [code/num.py](./code/num.py)       | 52    | 0    | 100%  |
| [code/row.py](./code/row.py)       | 6     | 0    | 100%  |
| [code/sym.py](./code/sym.py)       | 29    | 0    | 100%  |
| [code/utils.py](./code/utils.py)   | 39    | 4    | 90%   |
| TOTAL                              | 377   | 24   | 94%   |

## License

This project is licensed under [MIT](https://mit-license.org/).

Further details regarding the license can be found [here](https://github.com/jayrajmulani/group1-se-homeworks/blob/main/LICENSE).

## Contributors

- [Jayraj Mulani](https://github.com/jayrajmulani)
- [Yashasya Shah](https://github.com/Yashasya)
- [Harshil Sanghvi](https://github.com/Harshil47)
- [Dhrumil Shah](https://github.com/Dhrumil0310)
- [Anisha Chazhoor](https://github.com/anishasc99)

---

## Homework 5

| Notes                                                                                                                                                                                    | evidence                                                                                                                                                                   | [Group-12](https://github.com/team-12-csc-510/hw2) | [Group-26](https://github.com/ekanshsinghal/se-hw2-fall22) | [Group-13](https://github.com/sankettangade/aGoodRepoSE) | [Group-10](https://github.com/boscosylvester-john/se_hw_LuaToPython) | [Group-6](https://github.com/MitanshuShaBa/SE-hw2345/tree/main) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------- |
| Video1                                                                                                                                                                                   | For people starting with 2020 or 2021 projects, 2min video of old functionality                                                                                            | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Video2                                                                                                                                                                                   | For people starting with 2020 or 2021 projects, 2min video of new functionality, showing a significant delta from old. For everyone else, 2min video of all functionality. | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Workload is spread over the whole team (one team member is often Xtimes more productive than the others... but nevertheless, here is a track record that everyone is contributing a lot) | evidence in GH                                                                                                                                                             | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Number of commits                                                                                                                                                                        | in GH                                                                                                                                                                      | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Number of commits: by different people                                                                                                                                                   | in GH                                                                                                                                                                      | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Issues reports: there are **many**                                                                                                                                                       | -                                                                                                                                                                          | -                                                  | -                                                          | -                                                        | -                                                                    |
| Issues are being closed                                                                                                                                                                  | evidence in GH                                                                                                                                                             | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| DOI badge: exists                                                                                                                                                                        | in GH                                                                                                                                                                      | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Docs: doco generated, format not ugly                                                                                                                                                    | in GH                                                                                                                                                                      | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Docs: what: point descriptions of each class/function (in isolation)                                                                                                                     | -                                                                                                                                                                          | -                                                  | -                                                          | -                                                        | -                                                                    |
| Docs: how: for common use cases X,Y,Z mini-tutorials showing worked examples on how to do X,Y,Z                                                                                          | doc page entries                                                                                                                                                           | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Docs: why: docs tell a story, motivate the whole thing, deliver a punchline that makes you want to rush out and use the thing                                                            | -                                                                                                                                                                          | -                                                  | -                                                          | -                                                        | -                                                                    |
| Docs: short video, animated, hosted on your repo. That convinces people why they want to work on your code.                                                                              | -                                                                                                                                                                          | -                                                  | -                                                          | -                                                        | -                                                                    |
| Use of version control tools                                                                                                                                                             | -                                                                                                                                                                          | -                                                  | -                                                          | -                                                        | -                                                                    |
| Use of style checkers                                                                                                                                                                    | config files in GH showing your config                                                                                                                                     | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Use of code formatters.                                                                                                                                                                  | config files in GH showing your this formatter's config                                                                                                                    | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Use of syntax checkers.                                                                                                                                                                  | config files iin GH showing this checker's config                                                                                                                          | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Use of code coverage                                                                                                                                                                     | config files in GH                                                                                                                                                         | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Other automated analysis tools                                                                                                                                                           | config files in GH                                                                                                                                                         | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Test cases exist                                                                                                                                                                         | dozens of tests and those test cases are more than 30% of the code base                                                                                                    | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Test cases are routinely executed                                                                                                                                                        | E.g. travis-com.com or github actions or something                                                                                                                         | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| The files CONTRIBUTING.md lists coding standards and lots of tips on how to extend the system without screwing things up                                                                 | -                                                                                                                                                                          | -                                                  | -                                                          | -                                                        | -                                                                    |
| Issues are discussed before they are closed                                                                                                                                              | even if you discuss in slack, need a sumamry statement here                                                                                                                | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Chat channel: exists                                                                                                                                                                     | Link or screenshots                                                                                                                                                        | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Test cases: a large proportion of the issues related to handling failing cases.                                                                                                          | If a test case fails, open an issue and fix it                                                                                                                             | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
| Evidence that the whole team is using the same tools: everyone can get to all tools and files                                                                                            | -                                                                                                                                                                          | -                                                  | -                                                          | -                                                        | -                                                                    |
| Evidence that the whole team is using the same tools (e.g. config files in the repo, updated by lots of different people)                                                                | -                                                                                                                                                                          | -                                                  | -                                                          | -                                                        | -                                                                    |
| Evidence that the whole team is using the same tools (e.g. tutor can ask anyone to share screen, they demonstrate the system running on their computer)                                  | -                                                                                                                                                                          | -                                                  | -                                                          | -                                                        | -                                                                    |
| Evidence that the members of the team are working across multiple places in the code base                                                                                                | -                                                                                                                                                                          | -                                                  | -                                                          | -                                                        | -                                                                    |
| Short release cycles                                                                                                                                                                     | (hard to see in short projects) project members are committing often enough so that everyone can get your work                                                             | -                                                  | -                                                          | -                                                        | -                                                                    | -                                                               |
