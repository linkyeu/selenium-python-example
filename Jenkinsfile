pipeline {
    agent any
    stages {
        stage('Run Tests') {
            steps {
                script {
                    docker.image('selenium-test').inside {
                        sh 'pytest -n 2'
                    }
                }
            }
        }
    }
}