pipeline {
   agent { dockerfile true }
   stages {
      stage('e2e-tests') {
         steps {
            sh 'pytest -v --html=reports/report.html --self-contained-html'
            sh 'pytest -v --html=reports/report.html --self-contained-html'

         }
      }
      stage('reporting'){
        steps{
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



