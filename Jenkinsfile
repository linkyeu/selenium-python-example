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
        sh '''docker run --name my-test-container -d tests
docker exec --name my-test-container ls
docker stop my-test-container
docker rm my-test-container'''
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