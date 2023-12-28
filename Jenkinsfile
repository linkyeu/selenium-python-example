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
        sh '''
mkdir -p C:\\Users\\DFilippov\\Downloads\\PERSONAL\\portfolio\\selenium-ci-cd\\allure-reports
docker run --rm -v C:\\Users\\DFilippov\\Downloads\\PERSONAL\\portfolio\\selenium-ci-cd:/app tests
'''
      }
    }

  }
  post {
    always {
      sh 'echo $(ls)'
      archiveArtifacts(artifacts: 'report.html', allowEmptyArchive: true, fingerprint: true)
    }

  }
}