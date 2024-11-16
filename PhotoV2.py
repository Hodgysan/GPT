import streamlit as st
import random

# Title of the app
st.title("PhotoYou Learning Hub")

# Instructional Guides
if st.button("Instructional Guides"):
    st.header("Photography Vocabulary")
    vocabulary = [
        "Aperture: The opening in a lens through which light passes to enter the camera.",
        "Shutter Speed: The length of time the camera shutter is open, exposing light onto the camera sensor.",
        "ISO: A camera setting that will brighten or darken a photo.",
        "Depth of Field: The distance between the nearest and the farthest objects that are in acceptably sharp focus.",
        "Rule of Thirds: A composition guideline that places your subject in the left or right third of an image, leaving the other two-thirds more open.",
        "Exposure: The amount of light that reaches your camera sensor or film.",
        "White Balance: The process of removing unrealistic color casts so that objects which appear white in person are rendered white in your photo.",
        "Composition: The placement or arrangement of visual elements in a photograph.",
        "Focus: The process of adjusting the lens to make the subject appear sharp.",
        "Bokeh: The aesthetic quality of the blur produced in the out-of-focus parts of an image."
    ]
    for term in vocabulary:
        st.write(term)

# Project Ideas
if st.button("Project Ideas"):
    st.header("Project Ideas for Photography")
    ideas = [
        "1. Create a photo series capturing different types of lighting (e.g., golden hour, blue hour, artificial light).",
        "2. Document a day in the life of someone you know, capturing candid moments and storytelling images.",
        "3. Experiment with macro photography by photographing small objects or textures in great detail.",
        "4. Create a black-and-white photo collection focusing on shadows and contrast.",
        "5. Capture reflections in different surfaces, such as water, mirrors, or glass.",
        "6. Create a portrait series focusing on emotions, capturing different expressions and moods.",
        "7. Photograph architecture in your city, paying attention to lines, shapes, and patterns.",
        "8. Capture motion using slow shutter speed to create light trails or show movement.",
        "9. Take a series of photos that tell a story, using different compositions to guide the viewer.",
        "10. Experiment with depth of field by taking photos with both shallow and deep focus."
    ]
    for idea in ideas:
        st.write(idea)

# Step-by-Step Breakdowns
if st.button("Step-by-Step Breakdowns"):
    st.header("Step-by-Step Photography Techniques")
    steps = [
        "1. Setting up your camera: Learn how to adjust ISO, aperture, and shutter speed for optimal exposure.",
        "2. Composing a shot: Use the rule of thirds, leading lines, and framing to create interesting compositions.",
        "3. Focusing techniques: Learn how to use autofocus points or manual focus to ensure your subject is sharp.",
        "4. Adjusting white balance: Understand how to use different white balance settings to get accurate colors.",
        "5. Using natural light: Learn how to position your subject relative to the light source for the best effect.",
        "6. Shooting in RAW: Understand the benefits of shooting in RAW format for post-processing flexibility.",
        "7. Post-processing basics: Import your photos to editing software and make basic adjustments like exposure, contrast, and cropping.",
        "8. Working with depth of field: Experiment with different apertures to control the depth of field in your photos.",
        "9. Long exposure photography: Set up a tripod and use slow shutter speeds to capture light trails or flowing water.",
        "10. Capturing action shots: Use fast shutter speeds to freeze motion and ensure your subject is sharp."
    ]
    for step in steps:
        st.write(step)

# Troubleshooting Help
if st.button("Troubleshooting Help"):
    st.header("Troubleshooting Common Photography Issues")
    troubleshooting_tips = [
        "1. Blurry photos: Check your shutter speed, use a tripod, or increase your ISO for faster shutter speed.",
        "2. Overexposed images: Reduce your ISO, use a smaller aperture, or increase shutter speed.",
        "3. Underexposed images: Increase your ISO, use a larger aperture, or decrease shutter speed.",
        "4. Colors look off: Adjust your white balance settings to match the lighting conditions.",
        "5. Grainy images: Lower your ISO or use better lighting to reduce noise in your photos.",
        "6. Harsh shadows: Use a diffuser, shoot in shaded areas, or wait for softer lighting conditions.",
        "7. Uneven focus: Use a smaller aperture to increase depth of field or ensure your autofocus is on the correct subject.",
        "8. Glare in photos: Change your shooting angle or use a polarizing filter to reduce reflections.",
        "9. Dull images: Adjust contrast and saturation in post-processing to make your photos more vibrant.",
        "10. Motion blur: Use a faster shutter speed or stabilize your camera with a tripod."
    ]
    for tip in troubleshooting_tips:
        st.write(tip)

# Glossary of Terms with Flashcards
if st.button("Glossary of Terms"):
    st.header("Glossary of Photography Terms")
    glossary = [
        ("Aperture", "The adjustable opening in a camera lens that controls the amount of light entering the camera."),
        ("Shutter Speed", "The duration for which the camera shutter remains open to allow light to reach the sensor."),
        ("ISO", "The sensitivity of the camera sensor to light; higher ISO means more sensitivity."),
        ("Exposure", "The amount of light that hits the camera sensor, affected by aperture, shutter speed, and ISO."),
        ("White Balance", "A camera setting that adjusts for lighting in order to make white objects appear white in photos."),
        ("Depth of Field", "The range of distance within a photo that appears acceptably sharp."),
        ("Focus", "The process of adjusting the lens to make a subject appear sharp."),
        ("Bokeh", "The quality of the out-of-focus areas of an image, often used to create aesthetic blur."),
        ("Composition", "The arrangement of elements within a photograph to create a pleasing or meaningful image."),
        ("RAW", "A file format that captures all image data recorded by the sensor, providing greater flexibility in editing.")
    ]
    if st.button("Show Flashcard"):
        term, definition = random.choice(glossary)
        st.subheader(term)
        st.write(definition)
