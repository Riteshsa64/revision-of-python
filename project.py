import qrcode

# Taking UPI ID as input
upi_id = input("Enter your UPI ID = ")

# Optional details
name = "Recipient Name"
amount = input("Enter amount (leave blank if none) = ")
note = "Payment"

# Base UPI URL format
# upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE

if amount:
    upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR&tn={note}"
else:
    upi_url = f"upi://pay?pa={upi_id}&pn={name}&cu=INR&tn={note}"

# Create QR codes
phonepe_qr = qrcode.make(upi_url)
paytm_qr = qrcode.make(upi_url)
google_pay_qr = qrcode.make(upi_url)

# Save QR images
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

# Show QR codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

print("QR Codes generated successfully!")
