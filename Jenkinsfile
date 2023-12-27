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

        stage('') {
          steps {
            sh '''echo "Building docker container..."
docker build -t tests -f docker/Dockerfile.tests .'''
          }
        }

      }
    }

  }
}