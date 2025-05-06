pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Marcellinus-08/sast-demo-app.git', branch: 'master'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "🔧 Updating pip and installing Bandit..."
                    python3 -m ensurepip || true
                    python3 -m pip install --upgrade pip
                    pip install bandit
                    bandit --version
                '''
            }
        }

        stage('SAST Analysis') {
            steps {
                sh '''
                    echo "🔍 Running Bandit analysis..."
                    bandit -r . -f xml -o bandit-output.xml || true
                    echo "📄 Verifying Bandit output file:"
                    ls -lh bandit-output.xml
                    cat bandit-output.xml | head -n 20
                '''
                // Hanya lanjut jika file output memang ada
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')], skipBlames: true
            }
        }
    }

    post {
        always {
            echo "✅ Pipeline execution completed."
        }
        failure {
            echo "❌ Build failed. Please check Console Output for errors."
        }
    }
}
