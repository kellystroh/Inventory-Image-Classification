<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Your Closet</title>
    </head>
    <body>
        <h1>Welcome to your account</h1>
        <h2>Upload your inventory</h2>
        <form action = "http://localhost:8087/uploader" method = "POST" 
        enctype = "multipart/form-data">
        <input type = "file" name = "file" />
        <input type = "submit"/>
        </form>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Nullam facilisis arcu vel mollis finibus. Nunc facilisis 
            vel nisl lacinia cursus. Cras suscipit augue sed volutpat 
            tincidunt. Aenean dictum tincidunt urna, quis eleifend 
            quam mattis eu. Integer sollicitudin, nisl faucibus aliquam 
            ullamcorper, metus sapien scelerisque lorem, at ornare dui 
            orci non orci. Integer tempus consectetur metus, vitae 
            blandit nibh aliquam nec. Pellentesque vestibulum arcu eget 
            ante sollicitudin, id accumsan dui molestie. Suspendisse 
            vehicula semper dui id congue. Suspendisse sed velit sit 
            amet velit luctus varius. Ut condimentum tincidunt consequat. 
            Sed eu ligula non magna scelerisque auctor.
        </p>
             
        <p>
            Maecenas feugiat iaculis imperdiet. Duis vitae pellentesque 
            nunc, eget elementum metus. Nulla sollicitudin bibendum nibh, 
            sit amet semper tortor. Nunc rhoncus non arcu in scelerisque. 
            Donec magna mauris, congue ac dignissim rutrum, tincidunt 
            quis leo. Maecenas dictum orci in magna iaculis, in elementum 
            felis viverra. Aenean sit amet sapien odio. Donec molestie 
            est et nisl mattis dictum. Nullam at nibh aliquet, tincidunt 
            lorem et, facilisis enim. Praesent id felis sit amet quam 
            dignissim volutpat. Nam nec cursus mi, quis tincidunt justo.
        </p>
        <table border="1" cellpadding="10" cellspacing="0">
                <tr>
                   <th>Month</th>
                   <th>Rent</th>
                   <th>Utilities</th>
                   <th>Groceries</th>
                   <th>Eating Out</th>
                   <th>Entertainment</th>
                </tr>
                <tr>
                   <td>August</td>
                   <td>$1500</td>
                   <td>$100</td><!-- $150 changed to $100-->
                   <td>$350</td>
                   <td>$100</td>
                   <td>$50</td>
                </tr>
        </table>
        <ul>
            <li>apples</li>
            <li>oranges</li>
            <li>pineapples</li>
            <li>mangoes</li>
            <li>dragonfruit</li>
        </ul>
    </body>
</html>