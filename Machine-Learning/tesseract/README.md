# Text Recognize with tesseract
## Building a Simple Text Recognizer in Python

## Install lib 
1. sudo apt-get install tesseract-ocr
2. pip3 install Pillow
3. pip3 install pytesseract

## How to run script
1. python3 tesseract.py

## What is..
1. Optical Character Recognition คือซอฟแวร์ที่แปลงภาพเป็นตัวอักษรดิจิตอล
2. Tesseract OCR เป็น API ของกูเกิ้ลใช้สำหรับการทำ OCR

## Background 
อะไรคือ OCR ?
- เริ่มต้นกันก่อนครับว่าการทำ OCR คืออะไร แล้วประโยชน์ของมันคืออะไร? การทำ OCR โปรแกรม OCR ถูกสร้างขึ้นมาเพื่อแก้ปัญหาอย่างนึงครับ ในยุคที่เราก้าวเข้าสู่โลกดิจิตอล บริษัททั้งหลายก็พยายามเปลี่ยนเอกสารของตน ไปสู่ไฟล์ดิจิตอลเพื่อให้จัดการได้สะดวกยิ่งขึ้น ซึ่งการจะทำยังงั้นจำเป็นต้องมีการพิมพ์คัดลอกเอกสารเดิม ลงไปใส่ในไฟล์ดิจิตอล ซึ่งเป็นอะไรที่ยุ่งยากและเปลืองเวลามากๆ เลยมีคนคิดว่าถ้าเราเปลี่ยนเอกสารไปเป็นไฟล์เลยจะดีกว่ามั้ย ทำให้เริ่มมีคนลงทุนวิจัยพวกโปรแกรม OCR ขึ้นมาครับ