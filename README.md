# Image2String  
Convert a image into .txt with 8 characters, the output will be saved in **.txt** and we will create a **QRcode** to store this output.  
## Installation 
First we need to download python3 for this program et we need some python extension packages: **pillow** and **qrcode**.  
### Install pillow    
#### For Linux  
`sudo pip3 install pillow` 
#### For Windows
`python -m pip install pillow`   
### Install qrcode  
#### For Linux   
`sudo pip3 install qrcode`  
#### For Windows
`python -m pip install qrcode`  
## Build
By default, resize=0.07.    
`python Img2Str.py --image_dir=<location of the image> --resize=<rate of resize> --qrcode=<create a qrcode>`  
## Result
Input:  
![](https://github.com/AkiraXD0712/Image2String/blob/master/res/input.jpg?raw=true)
***
Output:  
![](https://github.com/AkiraXD0712/Image2String/blob/master/res/output.jpg?raw=true)
## Help
problem with qrcode, the data becommes strange after scanning the qrcode.  
QRcode:  
![](https://github.com/AkiraXD0712/Image2String/blob/master/res/qrcode.png?raw=true)
