pipeline {
    agent any
    environment {
    API_TOKEN = credentials('sysdig_api_token')
    }
  parameters {
        choice(name: 'UPDATE_CLUSTER', choices: ['second_cluster/cgmehjrf03au3mmcfetg'], description: '')
        string(name: 'TIMEOUT', defaultValue: '4h', description: '')
    }
  stages {
    stage('silencing alert') {
            steps {
              sh """python3 silencing_rule.py create --UPDATE_CLUSTER ${params.UPDATE_CLUSTER} --API_TOKEN ${API_TOKEN} --TIMEOUT ${params.TIMEOUT}"""
            }
          }
  }
  post {
   always {
       sh """python3 silencing_rule.py delete --UPDATE_CLUSTER ${params.UPDATE_CLUSTER} --API_TOKEN ${API_TOKEN} """
   }
}

}
                                                 
