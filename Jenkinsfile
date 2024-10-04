pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat '''@echo off
                echo 'In C or Java, we can compile our program in this step'
                echo 'In Python, we can build our package here or skip this step'
                '''
            }
        }
        stage('Test') {
            steps {
                bat '''@echo off
                echo 'Test Step: We run testing tool like pytest here'

                REM TODO fill out the path to conda here
                call mlip\\Scripts\\activate

                REM TODO Complete the command to run pytest
                pytest

                echo 'pytest completed successfully'
                '''

            }
        }
        stage('Deploy') {
            steps {
                echo 'In this step, we deploy our porject'
                echo 'Depending on the context, we may publish the project artifact or upload pickle files'
            }
        }
    }
}
