pipeline {
    agent any

    environment {
        ALLURE_RESULTS = "${WORKSPACE}/allure-results"
        ALLURE_REPORT = "${WORKSPACE}/allure-report"
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
    }

    post {
        always {
            script {
                allure([
                    reportBuildPolicy: 'ALWAYS',
                    results: [
                        [path: 'allure-results']
                    ]
                ])
            }
        }
    }
}
