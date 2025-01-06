pipeline {
    agent any
    
    tools {
        allure 'allure'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Prepare') {
            steps {
                sh '''
                    rm -rf allure-results || true
                    rm -rf allure-report || true
                    mkdir -p allure-results
                    chmod -R 777 allure-results
                '''
            }
        }
        
        stage('Build and Run Tests') {
            steps {
                script {
                    sh '''
                        docker build -t playwright-tests .
                        docker run --rm \
                            -v "${WORKSPACE}/allure-results:/tests/allure-results" \
                            playwright-tests
                    '''
                }
            }
        }
        
        stage('Generate Allure Report') {
            steps {
                script {
                    // Проверяем содержимое директории
                    sh 'ls -la allure-results/'
                    
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']],
                        report: 'allure-report'
                    ])
                }
            }
        }
    }
    
    post {
        always {
            script {
                // Архивируем отчет как артефакт
                archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
            }
            cleanWs()
        }
    }
}
