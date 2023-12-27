pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Build process'
      }
    }

    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            echo 'Run functional tests'
          }
        }

        stage('Build docker container') {
          steps {
            sh '''echo "Building docker container..."
docker build -t tests -f docker/Dockerfile.tests .'''
          }
        }

        stage('Run tests in Docker') {
          steps {
            sh '''echo "Running tests in docker"
docker run tests pytest -n 3'''
          }
        }

      }
    }

  }
}