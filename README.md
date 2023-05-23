# CAN-AutoLoginer
 an auto login tool for CAN (Campus Area Network)

# 使用指南（for Linux only）
### step 1. 首先在浏览器中登录校园网，按 F12 抓包，找到浏览器发送的标头，将其粘贴到 ./auto_login.py 的 header{} 中（记得添加引号与逗号）
### step 2. 自定义 data{} 中的学号与密码，自定义 url 为校园网登录地址
### step 3. 编辑 ./auto_login.sh 中的 cd 语句，定位到你存放该项目的目录
### step 4. 编辑 ./auto_login.service 中的 ExecStart 为【*终端的绝对路径* *auto_login.sh的绝对路径*】
### step 5. 在终端执行命令：sudo systemctl start auto_login.service, sudo systemctl enable auto_login.timer
