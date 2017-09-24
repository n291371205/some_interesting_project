#coding=utf-8

#中间遍历学号写的有点差劲，错误率很高，待改进
import urllib
import urllib2
import cookielib
import requests
count=0
for xueyuan in range(16,17):
    if xueyuan < 10:
        xueyuan = '0{}'.format(xueyuan)
    else:
        xueyuan = '{}'.format(xueyuan)
    for year in range(16,17):
        if year < 10:
            year = '0{}'.format(year)
        else:
            year = '{}'.format(year)
        for classes in range(101,999):
            if classes < 10:
                classes = '00{}'.format(classes)
            elif classes < 100:
                classes = '0{}'.format(classes)
            else: 
                classes = '{}'.format(classes)
            for number in range(1,60):
                if number < 10:
                    number = '0{}'.format(number)
                else: 
                    number = '{}'.format(number)
                xuehao = xueyuan + year + classes + number
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                    'Host': 'ded.nuaa.edu.cn',
                    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                    'Referer': 'http://ded.nuaa.edu.cn/netean/com/jbqkcx.asp',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
                    'Cookie': 'ASPSESSIONIDCQAQDCRS=OKBMJDCDKANKPNMHIPLKACNN; ASPSESSIONIDCQBRDDTQ=BMJOHJGDPHOHGJFHDHNNDFEF;ASP.NET_SessionId=y5jpls55haaugobito3x3ynh; DedHasLogin=1; CanViewPhotoFilter=161610336',
                }
                mycookie = {"ASP.NET_SessionId":"y5jpls55haaugobito3x3ynh","ASPSESSIONIDCQAQDCRS":"OKBMJDCDKANKPNMHIPLKACNN","ASPSESSIONIDCQBRDDTQ":"BMJOHJGDPHOHGJFHDHNNDFEF","CanViewPhotoFilter":"161610336","DedHasLogin":"1"}
                x = requests.session()

                res = x.get("http://ded.nuaa.edu.cn/netean/GetPic.asp?pic=xh&xh="+xuehao,cookies = mycookie, headers = headers)
                print(xuehao)
                if res.status_code == 500:
                    count+=1
                    if (count==2):
                        count=0
                        break
                    continue

                with open(xuehao+'.jpg', 'wb') as file:
                    file.write(res.content)
