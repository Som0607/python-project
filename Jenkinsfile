pipeline {
    agent any

    environment { 
        registry = "som0607/python-img" 
        registryCredential = 'docker-hub-creds' 
        dockerImage = ''
    }
    stages {
        stage('Build Image') {
            steps {
                script { 
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                }
            } 
            // steps {
            //     echo 'Hello, here i am going to build my image!'
            //     sh 'docker build -t som0607/python-img .'
            // }
        }
        stage('Push Image') {
            steps {
                script { 
                    docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push() 
                    }
                }
                // echo 'Hello, here i am pushing my image to docker hub!'
                // withDockerRegistry([credentialsId: 'docker-hub-creds', url: '']) {
                //     sh 'docker push som0607/python-img'
                // }
            }
        }
    }
}