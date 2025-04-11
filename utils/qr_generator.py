import qrcode

def generate_qr_code(content):
    """
    生成二维码并保存为临时文件
    :param content: 二维码内容
    :return: 二维码图片文件路径
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    file_path = "temp_qr.png"
    img.save(file_path)
    return file_path