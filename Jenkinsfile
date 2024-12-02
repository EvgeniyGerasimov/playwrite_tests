pipeline {
   agent { dockerfile true }
   environment {
       HEADLESS = 'True'
   }
   stages {
      stage('e2e-tests') {
         steps {
            sh 'pytest --html=reports/report.html --self-contained-html'
         }
      }
      stage('reporting') {
         steps {
            publishHTML target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'RCov Report'
            ]
         }
      }
   }
}


