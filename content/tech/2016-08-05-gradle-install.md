Title:Install Gradle
Date: 2016-08-05
Category: tech
Tags:gradle
Author: yumebayashi

### install script for centos

```
cd /opt/
sudo wget -N https://services.gradle.org/distributions/gradle-2.6-all.zip
sudo unzip gradle-2.6-all.zip
sudo rm gradle-2.6-all.zip
sudo ln -s gradle-2.6 gradle
sudo printf "export GRADLE_HOME=/opt/gradle\nexport PATH=\$PATH:\$GRADLE_HOME/bin" > /etc/profile.d/gradle-env.sh
source /etc/profile.d/gradle-env.sh
gradle -version
```
