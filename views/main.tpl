%import model

<head>
    <title>Minolovec</title>
</head>

<style>
table {
    border-collapse: collapse;
  }
  
  table, th, td {
    border: 1px solid black;
  }
  
  .butt {
     border: 1px outset;
     background-color: darkgray;
     height:50px;
     width:50px;
     cursor:pointer;
  }
  
  
  .butt:hover {
     background-color: gainsboro;
     color:white;
  }


  #square {
   width: 100%;
   height: 0;
   padding-bottom: 100%;
  }



  .dropbtn {
  background-color: #4CAF50;
  color: white;
  height:50px;
  width:50px;
  padding: 16px;
  font-size: 16px;
  border: none;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  height:50px;
  width:50px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {background-color: #ddd;}

.dropdown:hover .dropdown-content {display: block;}

.dropdown:hover .dropbtn {background-color: gainsboro;}
</style>



<table>
    %for y in range(12):
        <tr> 
            %for x in range(12):
                <td>
                    %koordinata = (x,y)
                    %slovar = igra.slovar
                    %(bomba, sosede, odkritost) = slovar[(x,y)]
                    %if odkritost == model.ODKRITA:
                    %    vrednost = sosede
                    %elif odkritost == model.ZAKRITA:
                    %    vrednost = "?"
                    %else:
                    %    vrednost = "🚩"
                    %end
                      <div class="dropdown">
                        <button class="dropbtn" disabled="disabled"> {{vrednost}}</button>
                        <div class="dropdown-content">
                          <form action="/igraj" method="POST">
                          <button class="butt" value="o,{{x}},{{y}}" name="gumb"> ⛏️ </button>
                          <button class="butt" value="z,{{x}},{{y}}" name="gumb"> 🚩 </button>
                          </form>
                        </div>
                      </div>
                </td>
            %end
        </tr>
    %end
</table>

