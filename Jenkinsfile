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
                sh '''
                if [ $(docker ps -a -q -f "name=$CONTAINER_NAME") ]; then
                    docker stop $CONTAINER_NAME
                    docker rm $CONTAINER_NAME
                fi
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME ."
            }
        }
        stage('Run Docker Container') {
            steps {
                sh "docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME"
            }
        }
    }
    post {
        success {
            echo "✅ Docker container $CONTAINER_NAME is running successfully!"
        }
        failure {
            echo "❌ Build failed! Check the console output."
        }
    }
}