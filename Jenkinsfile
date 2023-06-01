pipeline {
    agent any

    stages {
        stage('Build Image') {
            steps {
                echo 'Hello, here i am going to build my image!'
                sh 'docker build -t som0607/python-img .'
            }
        }
        stage('Push Image') {
            steps {
                echo 'Hello, here i am pushing my image to docker hub!'
                withDockerRegistry([credentialsId: 'docker-hub-creds', url: '']) {
                    sh 'docker push som0607/python-img'
                }
            }
        }
    }
}