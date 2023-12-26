pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    echo "Build completed"
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    docker.image('selenium-tests').inside {
                        sh 'pytest -n 2'
                    }
                }
            }
        }
    }
}