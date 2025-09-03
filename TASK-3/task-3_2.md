# Image Processing Techniques

Humans look at a photo and are instantly able to see faces, the sky or that one blurry concert video. Computers? Once again, not really. They only see grids of numbers (pixel values).  
To make sense of images, we run them through **image processing**. These are math tricks that highlight details, shrink file size or switch formats. Basically, it’s prep work that turns raw pixels into something machines can actually use.  

Here are some of the basic **Image Processing Techniques**:



## 1. Blurring (smooth)

Blurring is basically softening the image. You take each pixel and average it with its neighbours, so the whole thing looks smoother.  

- **Gaussian Blur:** classic smooth blur, looks natural  
- **Median Blur:** swaps pixels with the median value which is great for *“salt & pepper”* (random b&w pixels sprinkled over an image) noise  
- **Bilateral Blur:** keeps edges sharp while smoothening the rest  

It is mostly used in noise reduction, artistic filters, prepping images for ML models.  
But over-blur gives a mushy image where nothing looks sharp anymore.  

**How to achieve?**  
- *In Python/OpenCV:* `cv2.GaussianBlur(image, (m, m), sigmaX)` (m = size of filter window, sigmaX = standard deviation in x direction)  
- *In Photoshop or other editors:* Lens blur filters  



## 2. Sharpening (highlighting details)

If blur makes stuff smooth, sharpening makes stuff pop out more. It boosts the edges so details stand out.  

- **Laplacian Filter:** finds spots where pixel intensity changes fast and highlights them  
- **High Boost Filtering:** takes those edges and exaggerates them while keeping smooth areas intact  
- **High-Pass Filters:** let through only high-frequency parts (textures) and suppress smoother regions  
- **Unsharp Masking (USM):** blurs the image a bit → subtracts that from original to isolate edges → adds them back for a crisper image  

Sharpening is great for photos, scanned docs, or any dull image. But overdoing it makes things look artificial, like crunchy textures, halos around objects etc.  

**How to achieve?**  
- *In Python/OpenCV:* `cv2.filter2D()` or `cv2.Laplacian()`  
- *In editors:* Sharpen tools  



## 3. Compression (shrinking file sizes)

The most common (and a bit frustrating) example of compression would be how your 7MB DSLR picture gets smashed down to a 400KB mid-quality picture when you post it on Instagram.  

- **Lossless (PNG, GIF):** keeps every detail, just packs it up smarter. File sizes are still a bit chunky.  
- **Lossy (JPG, HEIC):** tosses out some details humans don’t notice, and gives way smaller file sizes.  

Compression saves storage and bandwidth, but cranking it too high will make your image look like a Minecraft character.  

**How to achieve?**  
In Python:  

```python
cv2.imwrite("output.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
```
Output.jpg -> file name  
img -> image you’re saving  
IMWRITE_JPEG_QUALITY -> tells OpenCV we’re controlling JPEG compression  
70 -> quality value  

### 4. Format Conversion (switching formats for compatibility/quality)  
It’s the same pixels but with a new outfit. Since different formats = different size/quality/transparency/animation etc. Format conversion is basically taking the raw pixel data and re-saving it in a new format that better suits your needs.  

- **JPG -> PNG**: keeps the quality same and allows transparency, but files get heavier.  
- **PNG -> JPG**: shrinks size for web use, but there is loss in transparency and some detail  
- **HEIC -> JPG/PNG**: HEIC is super space-saving, but not widely supported, so conversion is needed for sharing.  
- **GIF -> WebP/MP4**: modern alternatives to reduce file size massively while keeping animations smooth.  

**How is this done?**  
It is done by re-encoding the file in another format:  

**In Python:**  
```python
from PIL import Image
Image.open("input.heic").save("output.png")
```
**With tools:** MS Paint (Windows) or Preview (Mac) or any online converter.  

**The basic flow is (for eg: HEIC to PNG)**  
Decoding -> Re-encoding -> Data preservation -> Restoration of Metadata (in this case, no.) and Transparency (in this case, preserved).  

### Conclusion

Image processing is basically just cleaning, tweaking, and reshaping pixels, so both humans and machines can actually use them, whether for clearer photos, image sharing, or smarter AI models.
