# Requirements
1. Docker
2. Kubectl
3. Minikube


# Command

minikube addons enable ingress -p minikube

minikube ip -p minikube


-------
sudo nano /etc/resolv/conf
sudo systemctl start resolvconf.service
sudo systemctl enable resolvconf.service
