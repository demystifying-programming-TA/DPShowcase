# DP Showcase

## Individual repositories
* https://github.com/demystifying-programming-TA/DP2020/tree/master/DemoProject/Session4_Integration/DPProject (Demo)
* https://github.mit.edu/sameden/DPCourseWork/tree/master/DPProject(Private)
* https://github.com/chrisoconnell27/DPCourseWork (Private)
* https://github.com/rmwebb/dpcoursework (Private)

## Committing to AWS ELB

** See: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html **

### Initialize (ONLY need to perform once)
eb init -p python-3.7 dpshowcase2020 --region us-east-2
eb create flask-env

### Update
eb deploy

### View
eb open 
