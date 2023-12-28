pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Build process'
        sh 'echo $(ls)'
      }
    }

    stage('Test') {
      steps {
        echo 'Run functional tests'
        sh '''echo "Building docker container..."
docker build -t tests -f docker/Dockerfile.tests .'''
        sh '''mkdir -p ${PWD}/allure-reports
docker run -rm -v ${PWD}:/usr/src/app tests pytest --html=./report.html --alluredir=./allure-reports'''
      }
    }

  }
  post {
    always {
      sh 'echo $(ls)'
      sh 'echo $(ls allure-reports)'
      archiveArtifacts(artifacts: 'tests/*.py', allowEmptyArchive: true, fingerprint: true)
    }

  }
}