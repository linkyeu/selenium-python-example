pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Build process'
      }
    }

    stage('Test') {
      steps {
        echo 'Run functional tests'
        sh '''echo "Building docker container..."
docker build -t tests -f docker/Dockerfile.tests .'''
        sh '''echo "Running tests in docker"
docker run -v allure-report:allure-report tests pytest --alluredir=allure-reports -n 3 '''
        sh 'echo $(ls allure-reports)'
      }
    }

  }
  post {
    always {
      sh 'echo $(ls allure-reports)'
    }

  }
}