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
docker run -v ${pwd}/allure-report:/usr/src/app/allure-report tests pytest --alluredir=allure-reports -n 3 '''
        sh 'echo $(ls /usr/src/app/allure-reports)'
      }
    }

  }
  post {
    always {
      sh 'echo $(ls allure-reports)'
    }

  }
}