pipeline {
    agent any
    options {
        timestamps()
    }
    stages {
        stage("Installing libraries") {
            steps {
                sh 'pip3 install -r requirements.txt'
		echo 'Libraries are ready'
            }
        }
        stage("Start") {
	    parallel {
		stage("Start pytest") {            
			steps {
	                	sh 'python3 -m pytest -v --junitxml=report.xml test.py'
				junit '*.xml'
				echo 'Pytest is ready'
	            	}
	        }
		stage("Start lab_1 program") {
	     		steps {
				sh 'python3 lab_1.py start'
                		echo 'Lab_1 program is ready'
            		}
		}
	}
    }
}
}

