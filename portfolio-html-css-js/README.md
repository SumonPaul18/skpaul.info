## Portfolio-Website
Portfolio website build using HTML5, CSS3, JavaScript and jQuery.

<a href="https://skpaul.netlify.app/" target="_blank">**Visit Now** 🚀</a>

# How to Deploy myportfolio on Kubernetes

~~~
rm -rf skpaul.info
git clone https://github.com/SumonPaul18/skpaul.info.git
cd skpaul.info
kubectl apply -f skpaul-info-deploy.yaml
kubectl get deploy,pv,pvc,pod,svc
~~~

### Access The Nginx Instance
~~~
kubectl get pod
~~~
#### Delete all to Nginx-Deploy
~~~
kubectl delete deploy skpaul-deployment
kubectl delete pvc skpaul-nfs-pvc
kubectl delete pv skpaul-nfs-pv
kubectl delete svc skpaul-svc
~~~
#

## 📌 Tech Stack
[![HTML](https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white)](https://github.com/SumonPaul18/skpaul.info/blob/main/index.html)&nbsp;
[![CSS](https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white)](https://github.com/SumonPaul18/skpaul.info/tree/main/assets/css)&nbsp;
[![JS](https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://github.com/SumonPaul18/skpaul.info/tree/main/assets/js)&nbsp;
[![jquery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)](https://github.com/SumonPaul18/skpaul.info/tree/main)

### Extras : 
Particle.js, Typed.js, Tilt.js, Scroll Reveal, Tawk.to, Font Awesome and JSON

## 📌 How Looks Like This Portfolio 🙈 :
![hero-section](https://github.com/SumonPaul18/skpaul.info/blob/main/assets/images/hero-section.png?raw=true)
![about-section](https://raw.githubusercontent.com/SumonPaul18/skpaul.info/refs/heads/main/assets/images/about-section.png)
![skils-ection](https://github.com/SumonPaul18/skpaul.info/blob/main/assets/images/skill-section.png?raw=true)

<h2>📬 Contact</h2>


If you want to contact me, you can reach me through below handles.

&nbsp;&nbsp;<a href="https://www.linkedin.com/in/sumonpaul/"><img src="https://www.felberpr.com/wp-content/uploads/linkedin-logo.png" width="30"></img></a>

© 2024 Sumon Paul


[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
