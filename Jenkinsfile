pipeline {
    agent any
    environment {
        CONTAINER_NAME = "greeting-app"
    }
    stages {
        stage('Build Docker image') {
            steps {
                sh 'docker build -t greeting-app .'
            }
        }
        stage('Run Docker container') {
            steps {
                sh '''
                if [ $(docker ps -a -q -f "name=$CONTAINER_NAME") ]; then
                    docker stop $CONTAINER_NAME
                    docker rm $CONTAINER_NAME
                fi
                docker run -d -p 5000:5000 --name $CONTAINER_NAME greeting-app
                '''
            }
        }
    }
}