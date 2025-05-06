pipeline {
    agent any

    tools {
        // Gunakan Git tool yang dikonfigurasi di Jenkins > Global Tool Configuration
        git 'Default'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/your-username/sast-demo-app.git', branch: 'master'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install bandit'
            }
        }
        stage('SAST Analysis') {
            steps {
                // Analisis dengan Bandit dan simpan hasilnya dalam format XML
                sh 'bandit -f xml -o bandit-output.xml -r . || true'
                
                // Rekam hasil analisis dan tampilkan di Jenkins
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
}
