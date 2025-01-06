pipeline {
    agent any

    environment {
        ALLURE_RESULTS = "${WORKSPACE}/allure-results"
        ALLURE_REPORT = "${WORKSPACE}/allure-report"
    }

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
                    echo "Cleaning up previous results..."
                    rm -rf ${ALLURE_RESULTS}
                    rm -rf ${ALLURE_REPORT}
                    
                    echo "Creating allure-results directory..."
                    mkdir -p ${ALLURE_RESULTS}
                    chmod -R 777 ${ALLURE_RESULTS}
                    
                    echo "Created allure-results directory:"
                    ls -la ${ALLURE_RESULTS}
                '''
            }
        }

        stage('Build and Run Tests') {
            steps {
                script {
                    sh '''
                        echo "Building Docker image..."
                        docker build -t playwright-tests .
                        
                        echo "Running tests..."
                        docker run --rm \
                            -v "${WORKSPACE}/allure-results:/tests/allure-results" \
                            playwright-tests \
                            pytest --alluredir=/tests/allure-results
                        
                        echo "Test results:"
                        ls -la ${WORKSPACE}/allure-results/
                    '''
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    sh '''
                        echo "Allure results files:"
                        ls -la ${WORKSPACE}/allure-results/
                    '''
                }
                
                allure([
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: "${WORKSPACE}/allure-results"]]
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts(
                artifacts: 'allure-results/**/*,allure-report/**/*',
                allowEmptyArchive: true
            )
        }
        
        success {
            echo 'Pipeline completed successfully!'
        }
        
        failure {
            echo 'Pipeline failed!'
        }
    }
}
