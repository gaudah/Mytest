import cgi
import psycopg2
import sys
conn = psycopg2.connect("dbname=aishu user=aishu password=aish host=localhost")
cur = conn.cursor()
print "connected with postges"

form1=b'''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Smart shopper</title>

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
    <td><a href="#" target="_self" onmouseover="MM_swapImage('Image5','','cu2.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="cu1.jpg" name="Image5" width="100%" border="0" id="Image5" /></a></td>
    <td><a href="login.html" target="_self" onmouseover="MM_swapImage('Image10','','login2.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="login1 copy.jpg" name="Image10" width="100%" border="0" id="Image10" /></a><a href="login.html" target="_self" onmouseover="MM_swapImage('Image6','','login2.jpg',1)" onmouseout="MM_swapImgRestore()"></a></td>
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
      <span class="style22">Welcome Here..</span>
    </marquee>
    </p>
   
    <td width="25%" bgcolor="#ffcdd2" valign="top"><p align="center" class="style7"> Quick Links </p>
      <p align="center" class="style8"><span class="style25"><a href="#" onclick="projon()">Today's Deals </a><img src="blinking_new.gif" width="40" height="20" /></span></p><br>
      <p align="center" class="style17"><a href="#" onclick="comp()">Bulk Buying/Reselling</a><span class="style23"><img src="blinking_new.gif" width="40" height="20" /></span></p><br>
  
      <p align="center" class="style8"><span class="style25"><a href="#" onclick="upproj()"> Shop By Category </a></span><img src="blinking_new.gif" width="40" height="20" /></p><br>

      <p align="center" class="style8"><span class="style25"><a href="#" onclick="upproj()"> Your Cart </a></span><img src="cart1.jpeg" width="60" height="30" /></p><br>
      <p align="center" class="style8"><span class="style25"><a href="#" onclick="upproj()"> Your Wishlist </a></span><img src="wish.jpeg" width="60" height="30" /></p><br>
    <p align="center" class="style8">&nbsp;</p>
    <p align="center" class="style8">&nbsp;</p>
    <p align="center" class="style7">Recently Added New Products With Best Offers</p>
    <p align="center" class="style19"><marquee direction="up" onmouseover="this.stop();" onmouseout="this.start();" scrolldelay="150">
    <p align="center" class="style19">1)Johnson's Baby Powder (400g) with Free New Johnson's Baby Soap (100g)</p>
    <p align="center" class="style19">2)Agro Fresh Premium Ground Nut, 500g</p>
     <p align="center" class="style19">3)Agro Fresh Regular Toor Dal, 1kg</p>
    <p align="center" class="style19">4)Shopkins - Supermarket Surprises: Stickers and Activities</p>
    <p align="center" class="style19">5)Agro Fresh Regular Almonds, 100g</p>
    <p align="center" class="style19">6)New Bicycle Tail Light 5 LED + 2 Laser Guide For Safety Blue Colour</p> 
    </marquee></td>
  </tr>
</table>
<table width="80%" border="0" align="center">
  <tr>
    <td height="46" valign="top" bgcolor="#666666"><p class="style32">Copyright@2018,Smart shoppers Pvt. Ltd. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class="style36"><a href="www.facebook.com" target="_blank"><img src="099303-facebook-logo-square.png" width="38" height="37" border="0" /></a><a href="www.twitter.com" target="_blank"><img src="icon-bw-twitter.png" width="34" height="34" border="0" /></a></span><span class="style36"><a href="www.googleplus.com" target="_blank"><img src="google-plus.png" width="30" height="28" border="0" /></a></span></p>      
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






form = b'''

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Smart Shopper</title>

<link rel="stylesheet" type="text/css" href="functions.css" />
<script language="javascript" type="text/javascript" src="functions.js"></script>


</head>

<body onload="MM_preloadImages('Ready.jpeg','/h2.jpg','/ab2.jpg','/comp2.jpg','/cu2.jpg','/login2.jpg');DrawCaptcha();">
<table width="80%" border="0" align="center">
  <tr>
      <td><img src="vowels.jpeg" width="100%" height="242" /></td>

  </tr>
</table>
<table width="80%" border="0" align="center">
  <tr>
    <td height="57"><a href="hrms.html" target="_self" onmouseover="MM_swapImage('Image2','','/h2.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="/h1.jpg" name="Image2" width="100%" border="0" id="Image2" /></a></td>
  
 <td><a href="#" target="_self" onmouseover="MM_swapImage('Image3','','/ab2.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="/ab1.jpg" name="Image3" width="100%" border="0" id="Image3" /></a></td>
     <td><a href="#" target="_self" onmouseover="MM_swapImage('Image4','','/comp2.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="/comp1.jpg" name="Image4" width="100%" border="0" id="Image4" /></a></td>
         <td><a href="#" target="_self" onmouseover="MM_swapImage('Image5','','/cu2.jpg',1)" onmouseout="MM_swapImgRestore()"><img src="/cu1.jpg" name="Image5" width="100%" border="0" id="Image5" /></a></td>


    <td><a href="login.html" target="_self"><img src="/login1 copy.jpg" name="Image6" width="100%" border="0" id="Image6" /></a><a href="login.html" target="_self" onmouseover="MM_swapImage('Image6','','/login2.jpg',1)" onmouseout="MM_swapImgRestore()"></a></td>
  </tr>
</table>
<table width="80%" align="center">
  <tr>
    <td height="21" align="left" valign="top" bgcolor="#FF6633"><div align="left" class="style27">User Information</div></td>
  </tr>
  <tr>
    <td height="417" align="center" valign="top" bgcolor="#ffcdd2">   <p align="center" class="style37">Sign Up</p>
        <form id="form1" name="form1" method="post">
        <table width="51%" height="336" border="0">
          <tr>
            <td width="41%"><span class="style27">User Name:</span>&nbsp;&nbsp;</td>
            <td width="59%"><input type="text" name="t1" width="150px;" /></td>
          </tr>
          <tr>
            <td><span class="style27">Password: </span> &nbsp;</td>
            <td><input type="password" name="t2" width="150px;"/></td>
          </tr>
          <tr>
            <td><span class="style27">Email id:</span></td>
            <td><input type="text" name="t3" id="t3" width="150px;"/></td>
          </tr>
          <tr>
            <td><span class="style27">Contact Number:</span>&nbsp;</td>
            <td><input type="text" name="t4" width="150px;"/></td>
          </tr>
        </table>
        <p>&nbsp;  </p>
        <p>
 
 <input type="submit" name="submit" value="Sign Up" onclick='Javascript:checkEmail();' />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp; 
          <input type="button" name="Submit22" value="Back" onclick="back()"/>
  &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;
          <input type="submit" name="Submit2" value="Clear" />
          </p>
      </form>      
 
  <button id="b6" onclick="location.href='/serverlogin';" value="Go to Google" />Login here</button>
 <p align="center">&nbsp;</p>
    <p>&nbsp;</p></td>
  </tr>
</table>
<table width="80%" border="0" align="center">
  <tr>
    <td height="46" valign="top" bgcolor="#666666"><p class="style32">Copyright@2018,Smart shoppers Pvt. Ltd. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class="style36"><a href="www.facebook.com" target="_blank"><img src="/099303-facebook-logo-square.png" width="38" height="37" border="0" /></a><a href="www.twitter.com" target="_blank"><img src="/icon-bw-twitter.png" width="34" height="34" border="0" /></a></span><span class="style36"><a href="www.googleplus.com" target="_blank"><img src="/google-plus.png" width="30" height="28" border="0" /></a></span></p>
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

def application(environ, start_response):
    html = form

    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
       

        html = b'Hello1, ' + post['t1'].value + '!'+'Hello2, ' + post['t2'].value + '!'+'Hello4, ' + post['t3'].value + '!'+'Hello4, ' + post['t4'].value +'!!!!!'
        str1=(post['t1'].value)
        str2=(post['t2'].value)
        str3=(post['t3'].value)
        str4=(post['t4'].value)

       
        SQL="INSERT into signup (s1,s2,s3,s4) VALUES(%s,%s,%s,%s);"
        data=(str1,str2,str3,str4,)
        cur.execute(SQL,data)
        
        #html=html+"<html><button id='b6' onclick='location.href='/serverprod101';' value='Go to Google' /></button></html>"
        #html=html+form1

        cur.execute("select * from signup ;")
        conn.commit() 
        html=html+form

    #conn.close()
    status = '200 OK'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    #start_response('200 OK', [('Content-Type', 'text/html')])
    return [html]


        
    




