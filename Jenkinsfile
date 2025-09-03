pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/splegi/my-telebot'
            }
        }
        
        stage('Test Message') {
            steps {
                echo "🚀 Hello, Jenkins! This is a test run."
            }
        }

        stage('Build Docker image') {
            steps {
                bat 'docker build -t my-telebot .'
            }
        }

        stage('Run container locally') {
            steps {
                bat 'docker run -d --name my-telebot --rm my-telebot'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub',
                                                 usernameVariable: 'DOCKER_USER',
                                                 passwordVariable: 'DOCKER_PASS')]) {
                    bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"
                }
            }
        }

        stage('Push Docker image') {
            steps {
                bat 'docker tag my-telebot splegi/my-telebot:latest'
                bat 'docker push splegi/my-telebot:latest'
            }
        }
    }
}
