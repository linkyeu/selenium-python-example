pipeline {
    agent any
    stages {
        stage('Run Tests') {
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