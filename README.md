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
- https://demoqa.com/
- https://the-internet.herokuapp.com/
- https://www.way2automation.com/demo.html

Main pipeline assumes to write functional 2t2 tests for web app
using Python and Selenium WebDriver. Run tests in docker 
container on Jenkins with PyTest as a test runner (test execution layer) on different
browsers. Tests should be logged. Generate html report and present results in Allure. 
Test run reports should be collected in database and then 
visualized with Grafana.

### Key skills:
Python, PyTest, Docker, Allure, Selenium, Grafana, Jenkins.
    
### Design Pattern used:
- DomainDrivenDesign: Express your tests in the language of the end-user of the app. 
- PageObjects: A simple abstraction of the UI of your web app. 
- Lo`adableComponent: Modeling PageObjects as components. 
- BotStyleTests: Using a command-based approach to automating tests, rather than the object-based approach that PageObjects encourage


Source: https://www.selenium.dev/documentation/test_practices/design_strategies/



`





