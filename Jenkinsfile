pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''#!/bin/bash
                echo 'In C or Java, we can compile our program in this step'
                echo 'In Python, we can build our package here or skip this step'
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''#!/bin/bash
                #set -e  # Stop on any error
                echo 'Test Step: We run testing tool like pytest here'

                #TODO fill out the path to conda here
                #source /home/stallam/miniconda3/bin/activate mlip

                #TODO Complete the command to run pytest
                /home/stallam/miniconda3/bin/conda run -n mlip pytest --maxfail=1 --disable-warnings

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
