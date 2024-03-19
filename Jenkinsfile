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
			sh 'pytest test.py --junitxml=Lab1/report/out_report.xml'
                	echo 'Pytest is ready'
		}
	}
	stage("Start Main.py") {
		steps {
			sh 'python3 main.py start'
			echo 'Main.py is done'
		}
	}

}
}

