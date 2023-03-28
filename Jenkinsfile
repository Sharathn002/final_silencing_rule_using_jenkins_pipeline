pipeline {
    agent any
  parameters {
        choice(name: 'UPDATE_CLUSTER', choices: ['webapCluster/cfvdf6ef0lb6gpb1puig',description: 'select the cluster name')
        choice(name: 'region', choices: ['jp_tok','jp_osa','eu_de','eu_gb','us_south','us_east','au_syd','ca_tor', 'br_sao'], description: 'Enter the region where the agent lies ')
        string(name: 'api_token', defaultValue: '3e91771e-40d2-42cd-96ac-ebe08462c96c', description: 'Enter the api token of that region')
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
           sh """python3 deleting_silencing_rule.py ${params.UPDATE_CLUSTER} ${params.region} ${params.api_token} ${params.duration_in_hours}"""
       }
  }
}
                                                 
