from django.shortcuts import render
import pyqrcode
import png

# Create your views here.


#function generates url for email mesage
def generate_mail_qr(request):
    if request.method =="POST":
        # String which represents the QR code
        text = f"mailto:{request.POST['to']}?subject={request.POST['subject']}&body={request.POST['body']}"
        try:
            # Generate QR code
            image = pyqrcode.create(text)

             # Create and save the png file naming 
            fileNamePNG = f"{request.POST['filename']}" + ".png"
            image.png(fileNamePNG, scale=5)

            # Create and save the svg file naming 
            fileNameSVG = f"{request.POST['filename']}" + ".svg"
            image.svg(fileNameSVG, scale = 8)

            """NB: add check to decide which file gets rendered ,
               used fileNameePNG for testing
            """
            return render(request, 'home.html',{'qr_code':fileNamePNG})
        except:
            return ('Bad Request')

#function generated qr for website link
def generate_web_qr(request):
    image1=''
    if request.method =="POST":
        # String which represents the QR code
        text =request.POST['url']
        
            # Generate QR code
        image = pyqrcode.create(text)
        

            # Create and save the png file naming 
        foo=fileNamePNG = f"{request.POST['file_name']}" + ".png"
        image.png(fileNamePNG, scale=5)

            # Create and save the svg file naming 
        fileNameSVG = f"{request.POST['file_name']}" + ".svg"
        image.svg(fileNameSVG, scale = 8)
        """NB: add check to decide which file gets rendered ,
               used fileNameeSVG for testing
        """
        image1=foo
        return render(request, 'home.html',{'qr_code':foo})
       
    return render(request, 'home.html', {'qr_code':image1})