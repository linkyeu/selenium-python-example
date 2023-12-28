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
        sh 'mkdir allure-reports'
        sh 'docker run -u root -v ${PWD}:/usr/src/app tests pytest --alluredir=/usr/src/app/allure-reports'
      }
    }

  }
  post {
    always {
      sh 'echo $(ls)'
      sh 'echo $(ls allure-reports)'
      archiveArtifacts(artifacts: 'allure-reports/*.*', fingerprint: true)
    }

  }
}