# CloudStorageWebApp


![Blank diagram-5](https://github.com/quang2598/CloudStorageWebApp/assets/57729411/a7272b3f-effe-4207-b2aa-fc521ed22f0f)

This is the instruction on how to set up this Cloud Storage:

Setup Web Server:
1) Create Ubuntu EC2 instance
2) Clone this repo from Git
3) Keep the files in config and app folders (loadbalancer is not needed)
4) Update system and download dependences `bash configvm.sh`
5) Copy lb.service and place it under /etc/systemd/system/
6) Run the application `bash runapp.sh`

Setup Load Balancer:
1) Create Ubuntu EC2 instance
2) Clone this repo from Git
3) Keep the files in config and loadbalancer folders (app is not needed)
4) Update system and download dependences `bash configvm.sh`
5) Copy dropboxapp.service and place it under /etc/systemd/system/
6) Run the application `bash runlb.sh`
