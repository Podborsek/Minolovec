%rebase("base.tpl")
%if int(tezavnost) == 10:
%   visina = 8
%   sirina = 8
%else:
%   visina = 12
%   sirina = 20
%end


<div align="center">
    <table>
        %for y in range(visina):
        <tr>
            %for x in range(sirina):
            <td>
                %koordniata = (x,y)
                <div class="dropdown">
                    <form action="/igraj" method="POST">
                        <button class="dropbtn" value="n,{{visina}},{{sirina}},{{tezavnost}},{{x}},{{y}}" name="ugib"></button>
                    </form>
                    <div class="dropdown-content">
                        <button class="butt" disabled="disabled">🚩</button>
                    </div>
                </div>
            </td>
            %end
        </tr>
        %end
    </table>
</div>