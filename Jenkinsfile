pipeline {
    agent any

    environment {
        IMAGE_NAME = "greeting-app"
        CONTAINER_NAME = "greeting-app"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Stop & Remove Existing Container') {
            steps {
                powershell """
                if (\$(docker ps -a -q -f "name=\$env:CONTAINER_NAME")) {
                    docker stop \$env:CONTAINER_NAME
                    docker rm \$env:CONTAINER_NAME
                }
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                powershell "docker build -t \$env:IMAGE_NAME ."
            }
        }

        stage('Run Docker Container') {
            steps {
                powershell "docker run -d -p 5000:5000 --name \$env:CONTAINER_NAME \$env:IMAGE_NAME"
            }
        }
    }

    post {
        success {
            echo "✅ Docker container \$env:CONTAINER_NAME is running successfully!"
        }
        failure {
            echo "❌ Build failed! Check the console output."
        }
    }
}