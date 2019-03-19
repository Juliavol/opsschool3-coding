
node ('jenkins_node_01'){
   currentBuild.result = "SUCCESS"
   stage('Printing hello world'){
       sh 'echo "Hello World"'
   }
  stage('Printing runnig_tests'){
     sh 'echo "runnig_tests"'
     sh 'wget https://raw.githubusercontent.com/Juliavol/opsschool3-coding/excersise2/home-assignments//session1/excercise2.py'
     sh 'session2.py'
  }
   stage('unit test'){
       sh 'echo "unit test has started"'
   }
   stage('system test'){
       sh 'echo "system test has started"'
   }
   stage('integration test'){
       sh 'echo "integration test has started"'
   }
}
