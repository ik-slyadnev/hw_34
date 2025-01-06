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
                    
                    # Проверяем создание директории
                    echo "Created allure-results directory:"
                    ls -la allure-results
                '''
            }
        }
        
        stage('Build and Run Tests') {
            steps {
                script {
                    sh '''
                        docker build -t playwright-tests .
                        
                        # Добавляем больше прав для монтирования и владельца
                        docker run --rm \
                            -v "${WORKSPACE}/allure-results:/tests/allure-results:rw" \
                            --user root \
                            playwright-tests
                            
                        # Проверяем результаты после выполнения тестов
                        echo "Contents of allure-results after tests:"
                        ls -la allure-results/
                        
                        # Исправляем права на файлы после запуска Docker
                        chmod -R 777 allure-results
                    '''
                }
            }
        }
        
        stage('Generate Allure Report') {
            steps {
                script {
                    // Проверяем содержимое директории
                    sh '''
                        echo "Contents before generating report:"
                        ls -la allure-results/
                        
                        # Показываем содержимое одного из JSON файлов для проверки
                        cat allure-results/*.json || true
                    '''
                    
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: "${WORKSPACE}/allure-results"]],
                        report: "${WORKSPACE}/allure-report"
                    ])
                }
            }
        }
    }
    
    post {
        always {
            script {
                // Архивируем и результаты, и отчет
                archiveArtifacts artifacts: 'allure-results/**/*', allowEmptyArchive: true
                archiveArtifacts artifacts: 'allure-report/**/*', allowEmptyArchive: true
            }
            // Перенесли cleanWs в конец
            cleanWs()
        }
    }
}
