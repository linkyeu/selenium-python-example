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
mkdir -p ${PWD}/allure-reports
docker run --rm -v ${PWD}:/app tests bash -c "mkdir -p app/containerdir/testfile.txt; echo \'Hello\' > app/containerdir/testfile.txt"
cat ${PWD}/containerdir/testfile.txt
'''
      }
    }

  }
  post {
    always {
      sh 'echo $(ls)'
      archiveArtifacts(artifacts: 'tests/*.py', allowEmptyArchive: true, fingerprint: true)
    }

  }
}