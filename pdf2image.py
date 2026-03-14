import fitz  # PyMuPDF
import os

input_folder = "."
output_root = "results"

os.makedirs(output_root, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith(".pdf"):
        pdf_path = os.path.join(input_folder, file)
        pdf_name = os.path.splitext(file)[0]

        output_folder = os.path.join(output_root, pdf_name)
        os.makedirs(output_folder, exist_ok=True)

        doc = fitz.open(pdf_path)

        img_count = 0

        for page_index in range(len(doc)):
            page = doc.load_page(page_index)
            images = page.get_images(full=True)

            for img_index, img in enumerate(images):
                xref = img[0]
                base_image = doc.extract_image(xref)

                image_bytes = base_image["image"]
                image_ext = base_image["ext"]

                img_filename = f"{pdf_name}_p{page_index+1}_{img_index+1}.{image_ext}"
                img_path = os.path.join(output_folder, img_filename)

                with open(img_path, "wb") as f:
                    f.write(image_bytes)

                img_count += 1

        print(f"{file}: {img_count} images extracted")

print("Done!")