pipeline {
    agent any
    options {
        timestamps()
    }
    stages {
	stage("Install Libraries") {
		steps {
			sh 'pip3 install -r requirements.txt'
		}
	}
	stage("Start Pytest") {
		steps {
			sh 'pytest test.py --junitxml=Lab_1/report/out_report.xml'
                	echo 'Pytest is ready'
		}
	}
	stage("Start Lab_1.py") {
		steps {
			sh 'python3 lab_1.py start'
			echo 'Lab_1.py is done'
		}
	}

}
}

