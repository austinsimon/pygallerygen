import os
import shutil

# Have user set the title of the gallery, where the final gallery should be outputted, and the current location of photos
pageTitle = input("What is the title of this gallery? ")
photoLocation = input("Where are the photos located? ")
outputFolder = input("What directory should the file be created in? ")

outputLocation = outputFolder + "/" + pageTitle + "-gallery.html"

# If output exists, delete it
if os.path.exists(outputLocation):
    os.remove(outputLocation)

# If the output folder does not exist, create it
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

if not os.path.exists(outputFolder + "/photos"):
    os.makedirs(outputFolder + "/photos")

# Create the new output
outputHTML = open(outputLocation, "w+")

HTMLHead = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="http://gatormotorsports.com/framework/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css?family=Exo:600|Open+Sans" rel="stylesheet">
    <link rel="stylesheet" href="http://gatormotorsports.com/css/lightbox.min.css">
    <link rel="stylesheet" href="http://gatormotorsports.com/css/main.css">
    <title>Gator Motorsports - Media</title>
    <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
    <meta name="msapplication-TileColor" content="#da532c">
    <meta name="theme-color" content="#ffffff">
</head>

<body>

<div class="social-media-menu">
    <div class="container">
        <ul>
            <li><a href="https://www.facebook.com/gatormotorsports"><i class="fab fa-facebook-square"></i></a></li>
            <li><a href="https://www.instagram.com/gator.motorsports/"><i class="fab fa-instagram"></i></a></li>
            <li><a href="mailto:uffsae@gmail.com"><i class="fas fa-envelope"></i></a></li>
        </ul>
    </div>
</div>
<nav class="navbar navbar-expand-lg navbar-dark nav-alt" id="navbar">
    <div class="nav-container">
        <a class="navbar-brand" href="index.html">
            <img src="http://gatormotorsports.com/img/logo.png" class="logo" alt="">
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                    <a class="nav-link" href="http://gatormotorsports.com/about.html">ABOUT</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="http://gatormotorsports.com/media.html">MEDIA</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="http://gatormotorsports.com/sponsors.html">SPONSORS</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="http://gatormotorsports.com/join.html">JOIN</a>
                </li>
            </ul>
        </div>
    </div>
</nav>

<div class="page-content-norm">

<div class="page-intro media-intro">
    <div class="page-title">
        <h1>MEDIA</h1>   
    </div>
</div>

<div class="container">
    <div class="content-p" style="padding-bottom:0px;">
        <div class="row">
            <div class="col">
                <h1 class="text-center">""" + pageTitle + """ Gallery</h1>
            </div>
        </div>
    </div>
    <div class="content-p">
        <div class="row">
"""

outputHTML.write(HTMLHead)

photoCounter = 0;

# Iterate through each file in directory
for filename in os.listdir(photoLocation):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print(photoLocation + "/" + filename)
        print(outputFolder)
        shutil.copy(photoLocation + "/" + filename, outputFolder + "/photos/")

        HTMLPhoto = """
        <div class="col-md-3">
            <a href=" """ + "photos/" + filename + """ "  data-lightbox="gallery">
                <div class="card" style="width: 100%;">
                    <img class="card-img-top" src=" """ + "photos/" + filename + """ " alt="loading...">
                </div>
            </a>
        </div>
        """

        outputHTML.write(HTMLPhoto)

        photoCounter += 1

        if photoCounter % 4 == 0:
            outputHTML.write('</div></div><div class="content-p"><div class="row">')

if photoCounter % 4 != 0:
    outputHTML.write("</div>")

HTMLFooter = """
</div>
</div>

<footer>
    <div class="content-p">
        <div class="container">
            <div class="row">
                <div class="col">
                    <h6>Mailing Address</h6>
                    <p>Attn: Gator Motorsports</p>
                    <p>237 MAE-B</p>
                    <p>University of Florida</p>
                    <p>Gainesville, Florida 32611</p>
                </div>
                <div class="col">
                    <h6>Shipping Address</h6>
                    <p>Attn: Gator Motorsports</p>
                    <p>133-134 MAE-C</p>
                    <p>University of Florida</p>
                    <p>Gainesville, Florida 32611</p>
                </div>
                <div class="col">
                    <h6>Contact</h6>
                    <p>Phone: <a href="tel:5614278468">(561) 427-8468</a></p>
                    <p>Fax: (352) 392-1071</p>
                    <p>Email: <a href="mailto:uffsae@gmail.com">uffsae@gmail.com</a></p>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <hr>
                    <p class="copyright">Copyright © Gator Motorsports 2018</p>
                </div>
            </div>
        </div>
    </div>
</footer>

</div>

   <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>

    <script src="http://gatormotorsports.com/framework/js/bootstrap.min.js"></script>
    
    <script src="http://gatormotorsports.com/js/lightbox.min.js"></script>

    <script>

        window.onscroll = function() {myFunction()};

        var navbar = document.getElementById("navbar");

        var sticky = navbar.offsetTop;

        function myFunction() 
        {
            if (window.pageYOffset >= sticky) {
                navbar.classList.add("fixed-top")
            } else {
                navbar.classList.remove("fixed-top");
            }
        } 
    
    </script>

</body>

</html>


"""

outputHTML.write(HTMLFooter)

outputHTML.close()