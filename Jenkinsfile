pipeline {
    agent any

    stages {
        stage('Build Image') {
            steps {
                echo 'Hello, here i am going to build my image!'
                dockerImage = docker.build("som0607/python-img") 
            }
        }
        stage('Push Image') {
            steps {
                echo 'Hello, here i am pushing my image to docker hub!'
                withDockerRegistry([ credentialsId:"dockerhubaccount", url: "" ]) {
                    dockerImage.push()
                }
            }
        }
    }
}