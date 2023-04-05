pipeline {
    agent any
    environment {
    api_token = credentials('sysdig_api_token')
    }
  parameters {
        choice(name: 'UPDATE_CLUSTER', choices: ['second_cluster/cgmehjrf03au3mmcfetg'], description: '')
        string(name: 'TIMEOUT', defaultValue: '4', description: '')
    }
  stages {
    stage('silencing alert') {
            steps {
              sh """python3 silencing_rule.py create --cluster_name ${params.UPDATE_CLUSTER} --api_token ${api_token} --duration_in_hours ${params.TIMEOUT}"""
            }
          }
  }
  post {
   always {
       sh """python3 silencing_rule.py delete --cluster_name ${params.UPDATE_CLUSTER} --api_token ${api_token} """
   }
}

}
                                                 
