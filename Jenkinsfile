pipeline {
    agent any
    stages {
        stage('Build Docker image') {
            steps {
                powershell 'docker build -t greeting-app .'
            }
        }
        stage('Run Docker container') {
            steps {
                powershell 'docker stop greeting-app -ErrorAction SilentlyContinue; docker rm greeting-app -ErrorAction SilentlyContinue'
                powershell 'docker run -d -p 5000:5000 --name greeting-app greeting-app'
            }
        }
    }
}