docker stop $(docker ps -q)
docker rm $(docker ps -q -a)
docker rmi $(docker images -q)
#docker container prune
#docker volume prune