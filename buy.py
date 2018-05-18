import cgi
import psycopg2
import sys
from datetime import datetime, timedelta
conn = psycopg2.connect("dbname=aishu user=aishu password=aish; host=localhost")
cur = conn.cursor()
cur1 = conn.cursor()
cur2 = conn.cursor()
print "connected with postges"



form1='''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Amazon System</title>

<link rel="stylesheet" type="text/css" href="functions.css" />
<script language="javascript" type="text/javascript" src="functions.js"></script>
</head>


<body onload="MM_preloadImages('h2.jpg','ab2.jpg','comp2.jpg','cu2.jpg','login2.jpg');DrawCaptcha();">
<table width="80%" border="0" align="center">
  <tr>
      <td><img src="Ready_banner.jpg" width="100%" height="242" /></td>
  </tr>
</table>
<table width="80%" border="0" align="center">
  <tr>
    <td height="57"><a href="hrms.html" target="_self" onmouseover="MM_swapImage('Image2','','h2.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="h1.jpg" name="Image2" width="100%" border="0" id="Image2" /></a></td>
  
 <td><a href="#" target="_self" onmouseover="MM_swapImage('Image3','','ab2.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="ab1.jpg" name="Image3" width="100%" border="0" id="Image3" /></a></td>
     <td><a href="#" target="_self" onmouseover="MM_swapImage('Image4','','comp2.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="comp1.jpg" name="Image4" width="100%" border="0" id="Image4" /></a></td>
         <td><a href="#" target="_self" onmouseover="MM_swapImage('Image5','','cu2.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="cu1.jpg" name="Image5" width="100%" border="0" id="Image5" /></a></td>


    <td><a href="login.html" target="_self"><img src="login1 copy.jpg" name="Image6" width="100%" border="0" id="Image6" /></a><a href="login.html" target="_self" onmouseover="MM_swapImage('Image6','','login2.jpg',1)" onmouseout="MM_swapImgRestore()"></a></td>
  </tr>
</table>

<table width="80%" align="center">
  <tr>
   <td height="21" align="left" valign="top" bgcolor="#FF6633"><div align="left" class="style27"></div></td>
  </tr>
  <tr>
    <td height="417" align="center" valign="top" bgcolor="#ffcdd2">   <p align="center" class="style37">Buy Now</p>
      <form id="form1" name="form1" method="post">
        <table width="51%" height="336" border="0">
          <tr>
          <td><input type="radio"  name="input1" id="latin" value="cash on delivery" />Cash on dilivery</td>
	  </tr>
          <tr>
          <td><input type="radio"  name="input1" id="devnagari" value="collect from wearhousem" />Collect from wearhouse</td>
          </tr>
          <tr>
          <td><span class="style27">Qauntity:</span>&nbsp;&nbsp;</td>
            <td><input type="text" name="t2" width="150px;" /></td>
          </tr>
          <tr>
          <td><lable>price</lable>&nbsp;&nbsp;</td>
            <td><span id="t3" /></td>
          </tr>
        </table>
        <p>&nbsp;  </p>
        <p>

 <button id="b13" onclick="location.href='/alise';" value="Go to Google" />Submit</button>

          </p>
      </form>
 <button id="b2" onclick="location.href='/ship1';" value="Go to Google" />GoTo Next</button>

    <p align="center">&nbsp;</p>
    <p>&nbsp;</p></td>
  </tr>
</table>
<table width="80%" border="0" align="center">
  <tr>
    <td height="46" valign="top" bgcolor="#666666"><p class="style32">Copyright@2018, Amazon smart shoppers Pvt. Ltd. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class="style36"><a href="www.facebook.com" target="_blank"><img src="099303-facebook-logo-square.png" width="38" height="37" border="0" /></a><a href="www.twitter.com" target="_blank"><img src="icon-bw-twitter.png" width="34" height="34" border="0" /></a></span><span class="style36"><a href="www.googleplus.com" target="_blank"><img src="google-plus.png" width="30" height="28" border="0" /></a></span></p>
        <hr />
        <span class="style32"><span class="style33">&nbsp;<a href="hrms.html" target="_self">Home</a>|<a href="abtus.html" target="_self">About Us</a>|<a href="company.html" target="_self">Company</a>|<a href="cu.html" target="_self">Contact Us </a></span>&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        <p align="right" class="style32"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;  &nbsp;</p></td>
  </tr>
</table>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>

</body>
</html>
'''



from datetime import datetime, timedelta

def application(environ, start_response):
    html = form1
    str1=""
    price=""
    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        str4=(post['input1'].value)
        str2=(post['t2'].value)
       
        print str4,str1,str2
        cur2.execute("select * from temporary;")
        res1=cur2.fetchall();
        print "res1",res1
        store=res1[0][0]
        
        SQL="INSERT into delivery1 (loginid,choice,qty) VALUES(%s,%s,%s);"
       	data=(store,str4,str2,)
       	cur.execute(SQL,data)
       
    cur1.execute("select * from prod1;")
    r=cur1.fetchall()
    print r,"yes i am r"
    name=r[0]
    print name 
    data1=open("../../../../../home/aishu/All_Downloads/filedata","r")
    data11=map(lambda x:x.strip(),data1)


    for rr in r:
        if(rr[0]==data11[0]):
            print rr[0]
            price=rr[5]
            print "price",rr[5]
    html1 ="<html><head><script>alert('Order in processing'+'!!!!!');</script></head></html>"
    html=form1+html1+"<html><head><script>document.getElementById('t3').innerHTML = '%s';</script></head></html>"%(price)
      
    conn.commit() 
    status = '200 OK'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    return [html]

