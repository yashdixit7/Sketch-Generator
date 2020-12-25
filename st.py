
import streamlit as st 
import cv2 
import numpy as np 
from PIL import Image

st.title("SKETCH GENERATOR")

file = st.file_uploader("Please upload an Image file(jpg/png)", type=["jpg", "png"])

if file is None:
	st.text("You haven't uploaded any Image !!")
else:
	image = Image.open(file)
	img = np.array(image)

if st.button("Draw Sketch"):
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_invert = cv2.bitwise_not(img_gray)
	img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=20, sigmaY=20)
	def dodgeV2(x, y):
	    return cv2.divide(x, 255 - y, scale=256)
	final_img = dodgeV2(img_gray, img_smoothing)

	st.image(final_img, width=500, caption="Your Sketch is Ready!")