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
        sh '''docker stop my-container
docker rm my-container
docker run --name my-container -d tests tail -f /dev/null
docker exec my-container bash -c "pytest --html=report.html; ls"
docker cp my-container:/usr/src/app/report.html .
docker stop my-container
docker rm my-container'''
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