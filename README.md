# talk_to_robot

## 环境配置
需在ubuntu上安装配置ROS和python2，以及flask。

## 运行方法
下载文件，在catkin中创建一个package，放入项目文件，在终端中编译。
```
cd ~/catkin_ws/ 
catkin_make
```
然后打开四个窗口分别运行turtlesim_node，cloud_server.py，test.py三个节点
```
roscore 
rosrun turtlesim turtlesim_node
rosrun talk_to_robot(package name) test.py
rosrun talk_to_robot cloud_server.py
```
打开浏览器（如Chrome），进入127.0.0.1:5000，即可进入一个录音界面，点击record开始录音，点击stop停止，录音不超过 60秒，停止录音后会出现一个wav音频文件，可以在浏览器上点击播放，只要点击音频文件的文件名，就可以将指令传达给turtle，让其根据音频文件的内容运动（目前只能识别“前进”，“后退”，“左转”，“右转”四种情况）。
另外，由于cloud_server.py中调用了讯飞的语音听写webAPI，需要在讯飞上注册并创建应用，获取appid和apikey后在cloud_server.py中修改相应的appid和apikey参数，并且将本机的ip地址在讯飞上加入到应用的ip白名单才可以正常使用。
