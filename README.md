# Selenium project
```
/
├── pages/                       # Page Object Models for web pages
├── tests/                       # Directory for Selenium test scripts
├── utilities/                   # Utility scripts and helper functions
├── conftest.py                  # PyTest fixtures
├── Dockerfile                   # Dockerfile for setting up the test environment│
├── Jenkinsfile                  # Jenkins Declarative pipeline
├── pytest.ini                   # Configuration file for PyTest
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies for the project
```

## Goals
QA Engineering practice:
- [ ] Tests shall be developed with Selenium WebDriver
- [ ] PyTest shall be used as test runner
- [ ] Docker shall be used as env isolation tool
- [ ] Jenkins shall be used as CI/CD tool
- [ ] Allure shall be used as reporting tool
- [ ] Selenium Grid, Kubernetes shall be used to run tests on different envs
- [ ] Static code analysis shall be taken on testing code base
- [ ] Tests code base shall be shall run in parallel
- [ ] Tests shall be developed following best practices
- - [ ] DomainDrivenDesign: Express your tests in the language of the end-user of the app. 
- - [ ] PageObjects: A simple abstraction of the UI of your web app. 
- - [ ] LoadableComponent: Modeling PageObjects as components. 
- - [ ] BotStyleTests: Using a command-based approach to automating tests, rather than the object-based approach that PageObjects encourage
Source: https://www.selenium.dev/documentation/test_practices/design_strategies/
- [ ] Tests shall run on Windows 10 and Linux (Ubuntu LTS)
- [ ] Tests shall run of Edge, Firefox, Chrome (three latest versions)
- [ ] Tests technics shall be applied to decrease number of combinations
- [ ] Tests shall run in parallel
- [ ] The following website shall be used as playground: https://ecommerce-playground.lambdatest.io/

### ToBeAutomated
    Test Scenario 2:
1. Open the https://www.lambdatest.com/selenium-playground page and
click “Drag & Drop Sliders” under “Progress Bars & Sliders”.
2. Select the slider “Default value 15” and drag the bar to make it 95 by
validating whether the range value shows 95.


Test Scenario 3:
1. Open the https://www.lambdatest.com/selenium-playground page and
click “Input Form Submit” under “Input Forms”.
2. Click “Submit” without filling in any information in the form.
3. Assert “Please fill in the fields” error message.
4. Fill in Name, Email, and other fields.
5. From the Country drop-down, select “United States” using the text
property.
6. Fill all fields and click “Submit”.
7. Once submitted, validate the success message “Thanks for contacting
us, we will get back to you shortly.” on the screen.

## Key skills:
Python, OOP, Patterns, PyTest, Docker, Allure, Selenium, Selenium Grid, Kubernetes, Jenkins, (Grafana).