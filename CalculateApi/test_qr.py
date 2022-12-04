import qrcode
img = qrcode.make('a=1&b=2&c=3')# 二维码扫描后包含的信息
img.save('two.png')

# 高级用法
# import qrcode
# qr = qrcode.QRCode(
#     # version：值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。
#     version = 3,
#     # error_correction：控制二维码的错误纠正功能。可取值下列4个常量。
#     # ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
#     # ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
#     # ROR_CORRECT_H：大约30%或更少的错误能被纠正。
#     error_correction = qrcode.constants.ERROR_CORRECT_L,
#     box_size = 10,
#     border = 4,
# )
# qr.add_data = ('a=1&b=2&c=3')
# qr.make(fit = True)
# img = qr.make_image()
# img.save('four.png')

# import qrcode
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data('Some data')
# qr.make(fit=True)

# # img = qr.make_image(fill_color="black", back_color="white")
# img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
# img.save('three.png')

import cv2
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("two.png"))
print("Decoded text is: ", val)