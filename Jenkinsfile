pipeline {
    agent any
    stages {
        stage('Build Docker image') {
            steps {
                // Use sh instead of powershell
                sh 'docker build -t greeting-app .'
            }
        }
        stage('Run Docker container') {
            steps {
                // Stop and remove existing container if it exists
                sh 'docker stop greeting-app || true'
                sh 'docker rm greeting-app || true'

                // Run the new container
                sh 'docker run -d -p 5000:5000 --name greeting-app greeting-app'
            }
        }
    }
}