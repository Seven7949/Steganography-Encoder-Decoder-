# Steganography-Encoder-Decoder-
Hide text in images like a spy with lipstick and a mission

# 🕵️‍♀️ Steganography Encoder/Decoder

> Hiding text inside an image — because some secrets deserve a little mystery.

---

## 💡 Features

- Encode any secret message into a `.png` image
- Decode and retrieve messages later
- Uses LSB (Least Significant Bit) technique
- Supports emoji and symbols too 😉

---

## 🧪 Requirements

- Python 3
- Pillow library

```bash
pip install pillow

🚀 Usage

Encode
encode_message("secret_image.png", "This is top secret 💋", "encoded_image.png")
Decode
decode_message("encoded_image.png")
⚠️ Notes

Only works with .png images for now
Don't use huge messages — it’s still basic
👩‍💻 Author

YourGitHub

🔐 Disclaimer

For educational purposes only. Don’t use it to hide state secrets. Unless you’re in a spy movie. 🎬

