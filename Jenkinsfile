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
docker run tests pytest --alluredir=allure-reports -n 3 '''
        archiveArtifacts(artifacts: 'test_output', fingerprint: true, allowEmptyArchive: true)
      }
    }

  }
}