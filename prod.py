import cgi
import psycopg2
import sys
import os
from subprocess import call
conn = psycopg2.connect("dbname=aishu user=aishu password=aish host=localhost")
cur = conn.cursor()
print "connected with postges"



form1='''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>

<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Amazon smart shopper</title>

<link rel="stylesheet" type="text/css" href="functions.css" />
<script language="javascript" type="text/javascript" src="functions.js"></script>

</head>



<body onload="MM_preloadImages('h2.jpg','ab2.jpg','comp2.jpg','cu2.jpg','login2.jpg','MAQ-Software-Madhapur1.jpg')">
<table width="100%" border="0" align="center">
  <tr>
    <td><img src="Ready_banner.jpg" width="100%" height="242" /></td>
  </tr>
</table>
<table width="100%" border="0" align="center" bordercolor="#CCCCCC">
  <tr bordercolor="#F0F0F0">
    <td height="57"><a href="hrms.html" target="_self" onmouseover="MM_swapImage('Image2','','h2.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="h1.jpg" name="Image2" width="100%" border="0" id="Image2" /></a></td>

    <td><a href="#" target="_self" onmouseover="MM_swapImage('Image3','','ab2.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="ab1.jpg" name="Image3" width="100%" border="0" id="Image3" /></a></td>
    <td><a href="#" target="_self" onmouseover="MM_swapImage('Image4','','comp2.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="comp1.jpg" name="Image4" width="100%" border="0" id="Image4" /></a></td>
    <td><a href="#" target="_self" onmouseover="MM_swapImage('Image5','','cu2.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="cu1.jpg" name="Image5" width="100%" border="0" id="Image5" /></a></td>
    <td><a href="login.html" target="_self" onmouseover="MM_swapImage('Image10','','login2.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="login1 copy.jpg" name="Image10" width="100%" border="0" id="Image10" /></a><a href="login.html" target="_self" onmouseover="MM_swapImage('Image6','','login2.jpg',1)" onmouseout="MM_swapImgRestore()"></a></td>
  </tr>
</table>
<table width="100%" border="0" align="center">
  <tr>
     <td width="25%" height="575" bordercolor="#FF6633" bgcolor="#ffcdd2" valign="top"><p align="center" class="style1">Best Offers </p>
      
<p>
Best Offers:
<a href="https://www.w3schools.com">
  <img src="14.jpeg" width="100%" height="184" border="0">
</a>
</p>
<br><br>
    <p><a href="https://www.w3schools.com" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image7','','17.jpeg',1)"><img src="18.jpeg" name="Image7" width="100%" height="184" border="0" id="Image7" /></a></p>    </td>
    <td width="50%" valign="top" bordercolor="#CCCCFF" bgcolor="#f5b7b1"><p class="style10">&nbsp;</p>
    <p class="style11"><marquee direction="lest" scrolldelay="150" >
      <span class="style22">Welcome to Amazon Systems</span>
    </marquee>
    </p>




<table width="100%" align="center">
<tr>
    <td height="21" align="left" valign="top" bgcolor="#FF6633"><div align="left" class="style27">Product Information</div></td>
  </tr>
  <tr>
    <td height="417" align="center" valign="top" bgcolor="#ffcdd2">   <p align="center" class="style37"></p>
      <form id="form1" name="form1" method="post">
        <table width="51%" height="336" border="0">
            <tr>
            <td><label>Product name: </label></td>
            <td><p><span id='display0'></span></p></td>
            </tr>
          
          
          <tr>
            <td><label>Product description: </label></td>
            <td><p><span id='display1'></span></p></td>
          </tr>
        </table>
      </form>
      <p align="center">&nbsp;</p>
    <p>&nbsp;</p></td>
  </tr>
</table>
   

</table>
<table width="80%" border="0" align="center">
  <tr>
    <td height="46" valign="top" bgcolor="#666666"><p class="style32">Copyright@2018, Amazon smart shoppers Pvt. Ltd. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class="style36"><a href="www.facebook.com" target="_blank"><img src="099303-facebook-logo-square.png" width="38" height="37" border="0" /></a><a href="www.twitter.com" target="_blank"><img src="icon-bw-twitter.png" width="34" height="34" border="0" /></a></span><span class="style36"><a href="www.googleplus.com" target="_blank"><img src="google-plus.png" width="30" height="28" border="0" /></a></span></p>      
      <hr />
      <span class="style32"><span class="style33">&nbsp;<a href="hrms.html" target="_self">Home</a>|<a href="abtus.html" target="_self">About Us</a>|<a href="company.html" target="_self">Company</a>|<a href="cu.html" target="_self">Contact Us </a></span>&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
    <p align="right" class="style32">  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;  &nbsp;</p></td>
  </tr>
</table>
<p>&nbsp;</p>
<p>&nbsp;</p>

</body>
</html>
'''


def application(environ, start_response):
    html = form1

    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
            

    
    match_str="tea"
    cur.execute("select * from prod1 ;")
       
    
    
    r=cur.fetchall()
    for i in r:
   
        h1=i[0]
        h2=i[1]
    
        
        print "val of h1",h1
        if(match_str==h1):
            html=html+"<html><head><script>document.getElementById('display0').innerHTML = '%s';document.getElementById('display1').innerHTML = '%s';</script></head></html>" %(h1,h2)

    
    conn.commit() 
        
    status = '200 OK'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    #start_response('200 OK', [('Content-Type', 'text/html')])
    return [html]

