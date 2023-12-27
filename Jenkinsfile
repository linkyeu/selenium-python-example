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
docker run -v ${pwd}/allure-reports:/usr/src/app/allure-reports tests pytest --alluredir=/usr/src/app/allure-reports -n 3 '''
      }
    }

  }
  post {
    always {
      sh 'echo $(ls /usr/src/app/allure-reports)'
    }

  }
}