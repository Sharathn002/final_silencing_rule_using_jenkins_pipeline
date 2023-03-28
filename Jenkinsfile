pipeline {
    agent any
  parameters {
        string(name: 'UPDATE_CLUSTER', defaultValue: 'None', description: 'Enter the cluster name')
        choice(name: 'region', choices: ['jp_tok','jp_osa','eu_de','eu_gb','us_south','us_east','au_syd','ca_tor', 'br_sao'], description: 'select the region where the monitoring instance lies ')
        string(name: 'api_token', defaultValue: 'None', description: 'Enter the api token of that monitoring instance')
        string(name: 'duration_in_hours', defaultValue: '1.5', description: 'Enter the duration for the silencing')
    }
  stages {
    stage('silencing alert') {
            steps {
              sh """python3 creating_silencing_rule.py ${params.UPDATE_CLUSTER} ${params.region} ${params.api_token} ${params.duration_in_hours}"""
            }
          }
  }
  post {
       always {
           sh """python3 deleting_silencing_rule.py ${params.UPDATE_CLUSTER} ${params.region} ${params.api_token} """
       }
  }
}
                                                 
