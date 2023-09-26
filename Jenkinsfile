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

    // Define your Docker Hub registry URL
    environment {
        registry = 'manideep183/myflaskapi' // Your Docker Hub repository URL
        registryCredential = 'dockerhub_credentials' // Your Docker Hub credentials ID
        sonarqubeScanner = tool name: 'SonarQubeScanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
    }
    stages {
        stage('Checkout') {
            steps {
                // Check out your source code from the GitHub repository
                checkout([$class: 'GitSCM', branches: [[name: '*/python']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'your-github-credentials', url: 'https://github.com/ManideepAppu183/Manideep.git']]])
            }
        }
        
    // Building Docker images
        stage('Building image') {
            steps {
                script {
                    // Build the Docker image
                    dockerImage = docker.build registry + ':v1'
                }
            }
        }
        
        // Uploading Docker images into Docker Hub
        stage('Upload Image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }

        // Analyze code with SonarQube
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQubeServer') {
                    // Execute the SonarQube Scanner
                    bat "\"${tool name: 'SonarQubeScanner'}/bin/sonar-scanner.bat\""
                }
            }
        }
        
        stage('Deploy') {
            steps {
                // Deploy the Docker container in a Windows batch script
                bat 'docker run -d -p 5000:5000 --name my-flask-api ' + registry + ':v1'
            }
        }

        stage('Test') {
            steps {
                // Run the command using 'bat' step
                bat 'docker exec my-flask-api python3 test_api.py'
            }
        }
    }
    
    post {
        always {
            // Cleanup: Stop and remove the Docker container
            bat "docker stop my-flask-api"
            bat "docker rm my-flask-api"

            // Cleanup: Remove Docker image
            bat "docker rmi " + registry + ':v1'
        }
    }
}
