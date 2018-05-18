import cgi
import psycopg2
import sys
conn = psycopg2.connect("dbname=aishu user=aishu password=aish host=localhost")
cur = conn.cursor()
print "connected with postges"


form='''

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
   '''


form1='''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!--<link rel="stylesheet" type="text/css" href="functions1.css" />-->

<style>
* {
  box-sizing: border-box;
}
body {
  font: 16px Arial;  
}
.autocomplete {
  /*the container must be positioned relative:*/
  position: relative;
  display: inline-block;
}
input {
  border: 1px solid transparent;
  background-color: #f1f1f1;
  padding: 10px;
  font-size: 16px;
}
input[type=text] {
  background-color: #f1f1f1;
  width: 100%;
}
input[type=submit] {
  background-color: DodgerBlue;
  color: #fff;
  cursor: pointer;
}
.autocomplete-items {
  position: absolute;
  border: 1px solid #d4d4d4;
  border-bottom: none;
  border-top: none;
  z-index: 99;
  /*position the autocomplete items to be the same width as the container:*/
  top: 100%;
  left: 0;
  right: 0;
}
.autocomplete-items div {
  padding: 10px;
  cursor: pointer;
  background-color: #fff; 
  border-bottom: 1px solid #d4d4d4; 
}
.autocomplete-items div:hover {
  /*when hovering an item:*/
  background-color: #e9e9e9; 
}
.autocomplete-active {
  /*when navigating through the items using the arrow keys:*/
  background-color: DodgerBlue !important; 
  color: #ffffff; 
}


</style>

</head>     

<body>

<h2>Search Here..</h2>

<p>Start typing:</p>


<form method="post" autocomplete="off">
  <div class="autocomplete" style="width:300px;">
    <input id="myInput" type="text" name="myInput" placeholder="Search for names">
  </div>
  <input type="submit">
</form>


<script>

function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*for each item in the array...*/
      for (i = 0; i < arr.length; i++) {
        /*check if the item starts with the same letters as the text field value:*/
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          /*make the matching letters bold:*/
          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
          /*execute a function when someone clicks on the item value (DIV element):*/
          b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
          });
          a.appendChild(b);
        }
      }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed, prevent the form from being submitted,*/
        e.preventDefault();
        if (currentFocus > -1) {
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
      });
}

/*An array containing all the country names in the world:*/


var countries=["Mobile","Mobile dualsim","Mobile phone protection","Mobile phone protection dustproof protection","Mobile phone protection waterproof protection","Mobile phone weight","Mobile material","Mobile typeofmetal","mobile screen size of mobile phones","percentage of metal used in mobile phone","mobile phone features","Quality of mobile phones","mobile phone copper","stainlessteel mobile phone","aluminium mobile phone","square mobile phone","rectangle mobile phone","screen size of standard mobile phone","screen size of medium mobile phone","screen size of large mobile phone","mobile phone price","mobile phone colour"]


/*initiate the autocomplete function on the "myInput" element, and pass along the countries array as possible autocomplete values:*/
autocomplete(document.getElementById("myInput"), countries);


</script>


</body>
</html>
'''


form2='''

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
    #html=form+"<h1>Hello</h1>"+form2
    html=form+"<center>"+form1+"<label>Features of product: </label><p><span id='display2'></span></p>"+"</center>"+form2
    print "hiiii"
    #html1=""
    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        
        #html1=form+"<h1>Hello</h1>"+form2
        print "hiiii"
        str1=post['myInput'].value
        str2='%'+str1+'%'
        print str2
     
        store='%'
        SQL="select * from recommend1 where (prodname LIKE %s || %s || %s);"
        data=(store,str1,store,)
        cur.execute(SQL,data)
       
        row=cur.fetchall();
        print "result rows obtained",row
        html1=form
        cnt=1
        globvar = ""
        for i in row:
            aa=i[0]
            bb=i[1]
            print "each aa and bb",aa,i[1]
            b1=i[1]
            b2=i[1]
            b3=i[1]
          
           
            html1=html1+"<script language='Javascript' >function download(res){var store=res.src;var pom = document.createElement('a');pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(store));pom.setAttribute('download','filedata');pom.style.display = 'none';document.body.appendChild(pom);pom.click();document.body.removeChild(pom);alert(store);window.open('/prod');}</script></head><body><input type='image' src='%s' id='tt1' name='tt1' alt='Submit' width='111' height='91' onClick='download(this)'></body></html><br>" %(bb)

        html1=html1+form2
        html=html1


          
        print('document.write("HELLO PYTHON VARIABLE!!");')
       
    
    conn.commit();
    status='200 OK'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
   
    return [html]


