import cgi
import psycopg2
import sys
import os
from datetime import datetime, timedelta
conn = psycopg2.connect("dbname=aishu user=aishu password=aish host=localhost")
cur = conn.cursor()
cur1 = conn.cursor()
cur11 = conn.cursor()
cur12 = conn.cursor()
#cur17 = conn.cursor()
print "connected with postges"



form2='''

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
    <td height="21" align="left" valign="top" bgcolor="#FF6633"><div align="left" class="style27">Delivery Information</div></td>
  </tr>
  <tr>
    <td height="417" align="center" valign="top" bgcolor="#ffcdd2">   <p align="center" class="style37">Address</p>
      <form id="form1" name="form1" method="post">
        <table width="51%" height="336" border="0">
          <tr>
           <td><label>User Name: </label></td>
            <td><p><span id='name'></span></p></td>
            </tr>

          <tr>
           <td><label>Prod Name: </label></td>
            <td><p><span id='pp'></span></p></td>
            </tr>

            <tr>

            <td><label>date: </label></td>
            <td><p><span id='t1'></span></p></td>
         
          </tr>

          <tr>
           <td><label>time: </label></td>
            <td><p><span id='t2'></span></p></td>

          </tr>

          <tr>
           <td><label>Address: </label></td>
            <td><p><span id='add'></span></p></td>

          </tr>
          <tr>
            <td><lable>Transaction id:</lable></td>
            <td><span id='t3'/></td>
          </tr>

<tr>
        <td><lable>Total:</lable>&nbsp;&nbsp;</td>
            <td><span id='N1'/></td>
</tr>
         
        </table>
        <p>&nbsp;  </p>
        <p>
 
    <input type="submit" name="Sub" value="Place Order" onclick="back1()"/>

 
     </form>
      <button id="b2" onclick="location.href='/alise';" value="Go to Google" />Buy another product</button>
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
    html = form2
    name=""
    tra=""
    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
    
    cur.execute("select * from temporary;")
    rr=cur.fetchall()
    print "result",rr
    cur1.execute("select *,oid from delivery1;")
    r=cur1.fetchall()
    date1= datetime.now() + timedelta(days=2)
    l=str(date1)
    ll=l.split()
    
    cur11.execute("select * from prod1;")
    rrr=cur11.fetchall()
   
    
    cur12.execute("select * from address;")
    r1=cur12.fetchall()
    
    for i in r1:
        if(rr[0][0]==i[0]):
            add=i[1]


    data1=open("../../../../../home/aishu/All_Downloads/filedata","r")
    data11=map(lambda x:x.strip(),data1)

    for y in rrr:
        if(y[0]==data11[0]):
            pp=y[1]
            price=y[5]
    
    info = "<p>Date = '%s',Time = '%s'</p>" % (ll[0],ll[1])
    qua=''
    for i in r:
        print i[2]
        if(rr[0][0]==i[0]):
            print i
            qua=i[2]
            oid=i[3]
            usr_name=i[0]
            print qua,oid
    total=float(qua)*float(price)

    html=html+"<html><head><script>document.getElementById('name').innerHTML = '%s';document.getElementById('pp').innerHTML = '%s';document.getElementById('t1').innerHTML = '%s';document.getElementById('t2').innerHTML = '%s';document.getElementById('add').innerHTML = '%s';document.getElementById('N1').innerHTML = '%s';document.getElementById('t3').innerHTML = '%s';</script></head>minal minalminal</html>"%(usr_name,pp,ll[0],ll[1],add,total,oid)
    html1 ="<html><head><script>alert('Order has been placed thank you!!!Visit again'+'!!!!!');</script></head></html>"
    html=html+html1

    conn.commit()
    print "it's closed"
    conn1 = psycopg2.connect("dbname=aishu user=aishu password=aish host=localhost")
    cur17 = conn1.cursor()

    cur17.execute("delete from temporary")

    print "try to remove"

    #os.remove("python /var/www/html/coding1/hr/Project/rm.py")
    os.system("ls /var/www/html/coding1/hr/Project")

    print "removed"

    conn1.commit() 
       
    status = '200 OK'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    
    return [html]
os.system("python /var/www/html/coding1/hr/Project/rm.py")
os.system("ls /var/www/html/coding1/hr/Project")
