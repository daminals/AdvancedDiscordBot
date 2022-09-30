aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 318710067667.dkr.ecr.us-east-1.amazonaws.com
docker build -t examplebot ./
docker tag examplebot:latest 318710067667.dkr.ecr.us-east-1.amazonaws.com/examplebot:latest
docker push 318710067667.dkr.ecr.us-east-1.amazonaws.com/examplebot:latest