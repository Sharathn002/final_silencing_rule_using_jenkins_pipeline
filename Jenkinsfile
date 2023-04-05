pipeline {
    agent any
  parameters {
        string(name: 'UPDATE_CLUSTER', defaultValue: '', description: 'Enter the cluster name')
        string(name: 'api_token', defaultValue: '', description: 'Enter the api token of that monitoring instance')
        string(name: 'duration_in_hours', defaultValue: '1.5', description: 'Enter the duration for the silencing')
    }
  stages {
    stage('silencing alert') {
            steps {
              sh """python3 silencing_rule.py create --cluster_name ${params.UPDATE_CLUSTER} --api_token ${params.api_token} --duration_in_hours ${params.duration_in_hours}"""
            }
          }
  }
  post {
       always {
           sh """python3 silencing_rule.py delete --cluster_name ${params.UPDATE_CLUSTER} --api_token ${params.api_token} """
       }
  }
}
                                                 
