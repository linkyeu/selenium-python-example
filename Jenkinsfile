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
        sh '''mkdir ${PWD}/allure-reports
'''
        sh '''echo "Running tests in docker"
docker run -v ${PWD}/allure-reports:/app/allure-reports tests pytest --alluredir=/app/allure-reports .\\tests\\test_simple_form_demo.py '''
      }
    }

  }
  post {
    always {
      sh 'echo $(ls)'
      sh 'echo $(ls /app/allure-reports)'
      archiveArtifacts(artifacts: 'allure-reports/*.*', fingerprint: true)
    }

  }
}