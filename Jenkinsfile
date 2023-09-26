
pipeline {
    agent any

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
                
                checkout([$class: 'GitSCM', branches: [[name: '*/python']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'your-github-credentials', url: 'https://github.com/ManideepAppu183/Manideep.git']]])
            }
        }
        
        stage('Building image') {
            steps {
                script {
                
                    dockerImage = docker.build registry + ':v1'
                }
            }
        }
        
        stage('Upload Image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQubeServer') {
                    
                    bat "\"${tool name: 'SonarQubeScanner'}/bin/sonar-scanner.bat\""
                }
            }
        }
        
        stage('Deploy') {
            steps {
                
                bat 'docker run -d -p 5000:5000 --name my-flask-api ' + registry + ':v1'
            }
        }

        stage('Test') {
            steps {
                
                bat 'docker exec my-flask-api python3 test_api.py'
            }
        }
    }
    
    post {
        always {
            
            bat "docker stop my-flask-api"
            bat "docker rm my-flask-api"

            bat "docker rmi " + registry + ':v1'
        }
    }
}
