import tkinter as tk
from tkinter import ttk
import random

# Functions to handle button clicks and perform tasks
def open_instructional_guides():
    instructional_window = tk.Toplevel(root)
    instructional_window.title("Instructional Guides")
    instructional_window.geometry("400x300")
    
    label = tk.Label(instructional_window, text="Photography Vocabulary", font=("Helvetica", 14, "bold"))
    label.pack(pady=10)

    # Create a frame for the scrollbar and list
    frame = tk.Frame(instructional_window)
    frame.pack(fill="both", expand=True)

    # Add a canvas widget
    canvas = tk.Canvas(frame)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar to the canvas
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="left", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

    # Create another frame inside the canvas to hold the vocabulary list
    list_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=list_frame, anchor="nw")

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
        term_label = tk.Label(list_frame, text=term, font=("Helvetica", 12), wraplength=350, justify="left")
        term_label.pack(anchor="w", padx=10, pady=5)

def open_project_ideas():
    project_window = tk.Toplevel(root)
    project_window.title("Project Ideas")
    project_window.geometry("400x300")
    label = tk.Label(project_window, text="Project Ideas for Photography", font=("Helvetica", 14, "bold"))
    label.pack(pady=10)

    # Create a frame for the scrollbar and list
    frame = tk.Frame(project_window)
    frame.pack(fill="both", expand=True)

    # Add a canvas widget
    canvas = tk.Canvas(frame)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar to the canvas
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="left", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

    # Create another frame inside the canvas to hold the project ideas list
    list_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=list_frame, anchor="nw")

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
        idea_label = tk.Label(list_frame, text=idea, font=("Helvetica", 12), wraplength=350, justify="left")
        idea_label.pack(anchor="w", padx=10, pady=5)

def open_step_by_step_breakdowns():
    step_window = tk.Toplevel(root)
    step_window.title("Step-by-Step Breakdowns")
    step_window.geometry("400x300")
    label = tk.Label(step_window, text="Step-by-Step Photography Techniques", font=("Helvetica", 14, "bold"))
    label.pack(pady=10)

    # Create a frame for the scrollbar and list
    frame = tk.Frame(step_window)
    frame.pack(fill="both", expand=True)

    # Add a canvas widget
    canvas = tk.Canvas(frame)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar to the canvas
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="left", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

    # Create another frame inside the canvas to hold the step-by-step list
    list_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=list_frame, anchor="nw")

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
        step_label = tk.Label(list_frame, text=step, font=("Helvetica", 12), wraplength=350, justify="left")
        step_label.pack(anchor="w", padx=10, pady=5)

def open_troubleshooting_help():
    troubleshooting_window = tk.Toplevel(root)
    troubleshooting_window.title("Troubleshooting Help")
    troubleshooting_window.geometry("400x300")
    label = tk.Label(troubleshooting_window, text="Troubleshooting Common Photography Issues", font=("Helvetica", 14, "bold"))
    label.pack(pady=10)

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
        tip_label = tk.Label(troubleshooting_window, text=tip, font=("Helvetica", 12), wraplength=350, justify="left")
        tip_label.pack(anchor="w", padx=10, pady=5)

def open_glossary_of_terms():
    glossary_window = tk.Toplevel(root)
    glossary_window.title("Glossary of Terms")
    glossary_window.geometry("400x400")
    label = tk.Label(glossary_window, text="Glossary of Photography Terms", font=("Helvetica", 14, "bold"))
    label.pack(pady=10)

    # Create a frame for the scrollbar and list
    frame = tk.Frame(glossary_window)
    frame.pack(fill="both", expand=True)

    # Add a canvas widget
    canvas = tk.Canvas(frame)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar to the canvas
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="left", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

    # Create another frame inside the canvas to hold the glossary list
    list_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=list_frame, anchor="nw")

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

    for term, definition in glossary:
        term_label = tk.Label(list_frame, text=f"{term}: {definition}", font=("Helvetica", 12), wraplength=350, justify="left")
        term_label.pack(anchor="w", padx=10, pady=5)

    # Flashcard feature
    def show_flashcard():
        nonlocal current_index
        term, definition = glossary[current_index]
        flashcard_window = tk.Toplevel(glossary_window)
        flashcard_window.title("Flashcard")
        flashcard_window.geometry("300x200")
        term_label = tk.Label(flashcard_window, text=term, font=("Helvetica", 16, "bold"))
        term_label.pack(pady=10)
        definition_label = tk.Label(flashcard_window, text=definition, font=("Helvetica", 12), wraplength=250, justify="left")
        definition_label.pack(pady=10)

        def next_flashcard():
            nonlocal current_index
            current_index = (current_index + 1) % len(glossary)
            term, definition = glossary[current_index]
            term_label.config(text=term)
            definition_label.config(text=definition)

        next_button = tk.Button(flashcard_window, text="Next", command=next_flashcard)
        next_button.pack(pady=5)

    current_index = 0
    flashcard_button = tk.Button(glossary_window, text="Show Flashcard", font=("Helvetica", 14), command=show_flashcard)
    flashcard_button.pack(pady=20)

# Create the main window
root = tk.Tk()
root.title("PhotoYou")
root.geometry("800x600")

# Heading label
heading_label = tk.Label(root, text="PhotoYou Learning Hub", font=("Helvetica", 16, "bold"))
heading_label.pack(pady=20)

# Selections buttons
options = [
    ("Instructional Guides", open_instructional_guides),
    ("Project Ideas", open_project_ideas),
    ("Step-by-Step Breakdowns", open_step_by_step_breakdowns),
    ("Troubleshooting Help", open_troubleshooting_help),
    ("Glossary of Terms", open_glossary_of_terms)
]

for option, command in options:
    btn = tk.Button(root, text=option, font=("Helvetica", 14), width=25, command=command)
    btn.pack(pady=5)

# Run the GUI main loop
root.mainloop()
