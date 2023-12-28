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
docker run --rm -v ${PWD}/allure-reports:/containerdir tests sh -c "echo Hello > /containerdir/testfile.txt"
cat ${PWD}/allure-reports/testfile.txt\'
// docker run --rm -v ${PWD}:/usr/src/app tests bash -c "pytest --html=./report.html --alluredir=./allure-reports; ls"'''
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