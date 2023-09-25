// pipeline {
//     agent any

//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout scmGit(branches: [[name: '*/python']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ManideepAppu183/Manideep.git']])
//             }
//         }

//         stage('Build and Push Docker Image') {
//     steps {
//         script {
//             // Build the Docker image
//             dockerImage = docker.build('myflaskapi:v1', '-f Dockerfile .')

//             // Push the Docker image to Docker Hub using your Docker credentials
//             docker.withRegistry('https://hub.docker.com/repository/docker/manideep183/myflaskapi') {
//                 dockerImage.push()
//             }
//         }
//     }
// }
//         stage('Deploy') {
//             steps {
//                 // Deploy the Docker container
//                 bat 'docker-compose up -d'
//             }
//         }
//     }

//     post {
//         always {
//             // Cleanup: Remove Docker containers and images
//             bat "docker-compose down"
//             bat "docker rmi myflaskapi:v1" 
//         }
//     }
// }

pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Check out your source code from the GitHub repository
                checkout([$class: 'GitSCM', branches: [[name: '*/python']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'your-github-credentials', url: 'https://github.com/ManideepAppu183/Manideep.git']]])
            }
        }
        
        stage('Build and Push Docker Image') {
            steps {
                bat 'docker build -t myflaskapi:v1 .'
            }
        }
        
        stage('Deploy') {
            steps {
        // Deploy the Docker container using docker-compose in a Windows batch script
        bat 'docker-compose up'
        }
    }

      stage('Test') {
            steps {
        // Run the command using 'bat' step
        bat 'docker exec rest-api python3 test_api.py'
        }
    }

    }
    
    post {
        always {
            // Cleanup: Remove Docker containers and images
            bat "docker-compose down"
            bat "docker rmi myflaskapi:v1" 
        }
    }
}