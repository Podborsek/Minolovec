%import model
%visina = igra.visina
%sirina = igra.sirina
%rebase("base.tpl")





<div align="center">
<table>
    %for y in range(visina):
        <tr> 
            %for x in range(sirina):
                <td>
                    %koordinata = (x,y)
                    %slovar = igra.slovar
                    %(bomba, sosede, odkritost) = slovar[(x,y)]
                    %if odkritost == model.ODKRITA:
                      %if sosede == 0:
                        %vrednost = " "
                      %else:
                        %vrednost = sosede
                      %end
                        <button class="dropbtn" style="background-color: #C5CAE9; color:black" disabled="disabled"> <b>{{vrednost}}</b> </button>
                    %elif odkritost == model.ZAKRITA:
                        <div class="dropdown">
                          <button class="dropbtn" disabled="disabled"></button>
                          <div class="dropdown-content">
                            <form action="/igraj" method="POST">
                              <button class="butt" value="o,{{x}},{{y}}" name="gumb"> ⛏️ </button>
                              <button class="butt" value="z,{{x}},{{y}}" name="gumb"> 🚩 </button>
                            </form>
                          </div>
                        </div>
                    %else:
                        <div class="dropdown">
                            <button class="dropbtn" disabled="disabled"> {{"🚩"}}</button>
                            <div class="dropdown-content">
                              <form action="/igraj" method="POST">
                              <button class="butt" value="z,{{x}},{{y}}" name="gumb"> 🚩 </button>
                              </form>
                            </div>
                          </div>
                    %end

                </td>
            %end
        </tr>
    %end
</table>
</div>

