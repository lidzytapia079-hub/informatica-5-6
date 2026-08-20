import qrcode

def main():
    song ="https://www.youtube.com/watch?v=q7F83UQXf-Q&list=RDq7F83UQXf-Q&start_radio=1"
    qr = qrcode.QRCode(version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(song)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("my-qrcode.png")


if __name__=="__main__":
    main()





