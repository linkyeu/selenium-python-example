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
        sh '''
echo "Building docker container..."
docker build -t tests -f docker/Dockerfile.tests .
'''
        sh '''docker stop my-container || true
docker rm my-container || true
docker run --name my-container -d tests tail -f /dev/null
docker exec my-container bash -c "pytest --alluredir=allure-reports; ls"
docker cp my-container:/usr/src/app/allure-reports .
docker stop my-container
docker rm my-container'''
      }
    }

  }
  post {
    always {
      sh 'echo $(ls)'
      archiveArtifacts(artifacts: 'allure-reports/**', allowEmptyArchive: true, fingerprint: true)
      allure(includeProperties: false, jdk: '', results: [[path: 'allure-reports']])
    }

  }
}