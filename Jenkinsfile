
pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub')
        IMAGE_NAME = "splegi/my-telebot"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/splegi/my-telebot'
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    sh "echo ${DOCKER_HUB_CREDENTIALS_PSW} | docker login -u ${DOCKER_HUB_CREDENTIALS_USR} --password-stdin"
                }
            }
        }

        stage('Push Docker image') {
            steps {
                script {
                    sh "docker push ${IMAGE_NAME}:${BUILD_NUMBER}"
                }
            }
        }
    }
}