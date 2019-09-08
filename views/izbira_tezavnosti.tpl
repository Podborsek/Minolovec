%rebase("base.tpl")


<table style="width: 100%">
    <tr>
        <th>
            <form action="/nova_igra" method="post">
                <button class="butt2" value="8" name="tezavnost">LAHKO: <br> Polje velikosti 8x8 z 8 minami</button>
            </form>
        </th>
        <th>
            <form action="/nova_igra" method="post">
                <button class="butt2" value="45" name="tezavnost">SREDNJE: <br> Polje velikosti 20x12 z 45 minami</button>
            </form>
        </th>
        <th>
            <form action="/nova_igra" method="post">
               <button class="butt2" value="70" name="tezavnost">TEŽKO: <br> Polje velikosti 20x12 z 70 minami</button>
            </form>
        </th>
    </tr>
</table>

<h2>Navodila:</h2>
<p>
    Cilj igre je označiti vse mine. Številka v polju pove koliko min je na sosednjih poljih. Če mislite, da je polje varno ga lahko s klikom odkrijete. Polja na katerih so mine označite z zastavico. Igra se konča, ko označite vse mine ali ko odkopljete mino.
    <br>
    Kliknite na željeno težavnost za začetek!
</p>