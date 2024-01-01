# Selenium project
```
/
│
├── tests/                       # Directory for Selenium test scripts
│   ├── pages/                   # Page Object Models for web pages
│   └── test_cases/              # Selenium test cases
│
├── reports/                     # Directory for storing Allure reports
├── docker/                      # Docker configurations and files
│   ├── Dockerfile               # Dockerfile for setting up the test environment
│   └── docker-compose.yml       # Docker Compose to orchestrate containers
│
├── grafana/                     # Grafana dashboard configurations
│   └── dashboards/              # JSON files for Grafana dashboards
│
├── utils/                       # Utility scripts and helper functions
├── requirements.txt             # Python dependencies for the project
├── pytest.ini                   # Configuration file for PyTest
├── .allure/                     # Allure configuration files (if needed)
├── .gitignore                   # Standard Git ignore file
└── README.md                    # Project documentation
```
This project is about practicing Selenium and other technologies
like Docker, Allure, PyTest.

The following websites are chosen for practice:
- https://ecommerce-playground.lambdatest.io/

Main pipeline assumes to write functional 2t2 tests for web app
using Python and Selenium WebDriver. Run tests in docker 
container on Jenkins with PyTest as a test runner (test execution layer) 
on different browsers. Report should be shown via Allure. 
Test run reports should be collected in database and then visualized with Grafana.
Main purpose is to pass end to end pipeline for continuous testing process.

### Key skills:
Python, PyTest, Docker, Docker Compose, Allure, Selenium, Grafana, Jenkins.

__Note:__ Do not run Selenium Grid to run tests on different OS, browsers etc.
At least us Selenoid.
Source: https://www.youtube.com/watch?v=vmJv7nFm4yA
    
### Design Pattern used:
- DomainDrivenDesign: Express your tests in the language of the end-user of the app. 
- PageObjects: A simple abstraction of the UI of your web app. 
- LoadableComponent: Modeling PageObjects as components. 
- BotStyleTests: Using a command-based approach to automating tests, rather 
than the object-based approach that PageObjects encourage


Source: https://www.selenium.dev/documentation/test_practices/design_strategies/

## Settings
### Setup Jenkins
- Write dockerfile with default Jenkins and add there docker
- Build
- Run container with mounted docker socket with host socket
docker run -u root -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins-docker
should be root user to have an access to docker socket!
- Run Jenkins and setup (Docker Pipeline plugin)

#### TODO
- [ ] Static analysis of codebase
- [ ] Run tests using Selenoid instead of Selenium Grid
- [ ] Run test cases on Windows, MacOS, Linux
- [ ] Run test cases on different browser versions (Edge, Chrome, Firefox) 
three from the latest versions for each
- [ ] Run tests in parallel
- [ ] Write two more test cases
- [ ] Optional: Add Grafana

    
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

You are required to run the above test in parallel on at least 2 different
browser/OS combinations (for example,
Windows 10 Chrome latest version and macOS Catalina Safari)







