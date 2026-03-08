pipeline {
    agent any
    environment {
        CONTAINER_NAME = 'greeting-app'
    }
    stages {
        stage('Build Docker image') {
            steps {
                sh 'docker build -t greeting-app .'
            }
        }
        stage('Run Docker container') {
            steps {
                // Stop and remove existing container if it exists
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'

                // Run the new container
                sh 'docker run -d -p 5000:5000 --name $CONTAINER_NAME greeting-app'
            }
        }
    }
}