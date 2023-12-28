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
docker run --rm -v ${PWD}/allure-reports:/usr/src/app tests bash -c "mkdir -p /usr/src/app/containerdir && echo Hello > /usr/src/app/containerdir/testfile.txt"
cat ${PWD}/allure-reports/containerdir/testfile.txt
'''
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