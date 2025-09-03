pipeline {
    agent ( label 'windows' )
    stages {
        stage('Test Docker') {
            steps {
                bat 'docker version'
            }
        }
    }
}

