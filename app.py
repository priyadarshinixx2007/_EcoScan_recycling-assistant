import streamlit as st
import pytesseract
from PIL import Image

# Tesseract path for MacPorts
pytesseract.pytesseract.tesseract_cmd = "/opt/local/bin/tesseract"

# Page configuration
st.set_page_config(
    page_title="EcoScan",
    page_icon="♻️",
    layout="centered"
)

st.title("EcoScan")
st.subheader("Smart Product Recycling Assistant")

st.write(
    "Upload a product or package image. EcoScan uses OCR "
    "to read the information printed on the package and "
    "identify available recycling information."
)

# Upload image
uploaded_file = st.file_uploader(
    "Upload a product image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Product",
        use_container_width=True
    )

    if st.button("Scan Product"):

        with st.spinner("Reading product information..."):

            text = pytesseract.image_to_string(image)

        st.success("Scan completed!")

        st.subheader("Extracted Information")

        if text.strip():

            st.text_area(
                "OCR Result",
                text,
                height=250
            )

            text_lower = text.lower()

            st.subheader("Recycling Information")

            materials = []

            # Check non-recyclable instruction first
            if "do not recycle" in text_lower:
                materials.append(
                    "The package indicates that it should not be recycled."
                )

            if "pet" in text_lower:
                materials.append("PET plastic detected.")

            if "hdpe" in text_lower:
                materials.append("HDPE plastic detected.")

            if "plastic" in text_lower:
                materials.append("Plastic packaging detected.")

            if "paper" in text_lower or "carton" in text_lower:
                materials.append("Paper or carton packaging detected.")

            if "glass" in text_lower:
                materials.append("Glass packaging detected.")

            if (
                "recyclable" in text_lower
                or "recycle" in text_lower
            ) and "do not recycle" not in text_lower:
                materials.append(
                    "Recycling information was found on the package."
                )

            if materials:

                for item in materials:
                    st.write("•", item)

            else:

                st.info(
                    "No clear recycling information was detected. "
                    "Please check the package label and local "
                    "recycling guidelines."
                )

        else:

            st.warning(
                "No readable text was detected. "
                "Try uploading a clearer image with larger "
                "printed text."
            )
