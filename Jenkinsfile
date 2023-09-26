
pipeline {
    agent any

    // Define your Docker Hub registry URL
    environment {
        registry = 'manideep183/myflaskapi' // Your Docker Hub repository URL
        registryCredential = 'dockerhub_credentials' // Your Docker Hub credentials ID
        sonarqubeScanner = tool name: 'SonarQubeScanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
        SONAR_TOKEN = 'sqp_b83beec92b173dc7098bb550fa7e75e34caff305' // Replace with your actual SonarQube token
        SONAR_PROJECT_KEY = 'Flask_Docker_Jenkins' // Replace with your actual SonarQube project key
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
