pipeline {
   agent { dockerfile true }
   stages {
      stage('e2e-tests') {
         steps {
//             sh 'sudo pip install -r requirements.txt --user'

//             sh 'sudo -H pip install pytest-playwright'

            sh 'pytest -v'
            publishHTML target: [
            allowMissing: false,
            alwaysLinkToLastBuild: false,
            keepAll: true,
            reportDir: 'reports',
            reportFiles: 'index.html',
            reportName: 'RCov Report'
          ]
         }
      }
   }
}



