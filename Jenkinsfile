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
        stage('Build and Run Tests') {
            steps {
                script {
                    // Создаем временную директорию для результатов
                    sh 'mkdir -p allure-results'

                    // Собираем и запускаем тесты в Docker
                    sh '''
                        docker build -t playwright-tests .
                        docker run -v ${WORKSPACE}/allure-results:/tests/allure-results playwright-tests
                    '''
                }
            }
        }
        stage('Generate Allure Report') {
            steps {
                script {
                    // Генерируем отчет Allure
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']]
                    ])
                }
            }
        }
    }
}
