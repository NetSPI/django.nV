#ZAP Docker
docker run -d --name zap --link django-nV -p 127.0.0.1:8080:8080 -i owasp/zap2docker-stable zap.sh -daemon -host 0.0.0.0 -port 8080 -config api.disablekey=true
docker ps -a

## Selenium and ZAP requirements
pip install selenium
pip install requests
pip install python-owasp-zap-v2.4
pip install prettytable
pip install bandit

##Docker bench security
git clone https://github.com/docker/docker-bench-security.git
