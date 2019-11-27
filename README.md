# API tests for https://petstore.swagger.io/
## Basic scenario is
```
Write a python class/module to:
1. Create and return a new Pet with:
    a. Id
    b. Category_name
    c. Pet_name
    d. Status
    e. tagName
    f. photoUrl
2. Verify The Pet was created with correct data.
3. Update this Pet_name, Verify update and return record.
4. Delete the Pet and demonstrate pet now deleted.
```
## Basic configuration
1. Clone/download project from GIT repository
2. Add demo_pet root directory to PYTHONPATH:

    a. Windows:```PATH=%PATH%;C:\your\path\here\```

    b. Linux: ```PATH=$PATH:~/ paste_your_path_here```
    or ```PATH=~/paste_your_path_here:$PATH```
    
    c. macOS:```PATH: export PATH=$PATH:/new/dir/location1```
    
3. checking PATH:```echo "$PATH"`` **_or_** ``printf "%s\n" $PATH```

4. Make sure that you have Python on your machine.
5. Check that you have valid pip version: ```pip --version```
6. pip upgrading: ```python -m pip install --upgrade pip```
7. pipenv installation process:

    Linux : ```sudo apt install pipenv```
    
    Mac OS : ```brew install pipenv```
    
8. Create independent environment: ```pip install pipenv```
9. Install all dependencies that is available in the Pipfile for current project
10. Check the list of all packages:```pip list```
11. Create virtual environment: ```pipenv install```.
By default, after command execution you will have .virtual.env folder in the root or user folder.
12. To activate the environment: ```pipenv shell```    

###Test execution  - from terminal
1. Activate environment for current project: ```pipenv shell```
2. Go to the ‘feature’ folder (../features)
3. Check that you have ‘behave’ module: ```behave –version```
4. Check the list of available tests in the ‘feature’ folder. The have `.feature` extension.

EXAMPLE : `behave -k --tags @test`
where `@test` is a tag name for the executed test. Each feature file has different tests and
related tags.

###PyCharm test execution
Complete all steps from Base configuration section.

Be sure that you have related folder in .virtualenvs

1. Add Run/Debug configuration. By default, 
This manual is for PyCharm IDE.
Create/Update configuration according to available tags in the tests:
2. All commands related to the test execution should be run in the ‘feature’ folder.
Common command for executing test is ```behave -k --tags @test```
3. When all tests will executed you can check ‘reports’ folder. It should contain ‘pet_logger.log’ with detailed information about each action.
