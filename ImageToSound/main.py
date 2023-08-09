from PIL import Image
import numpy as np
import sounddevice as sd

def image_to_sound(image_path, duration=2.0, amplitude=0.5, base_freq=400, max_freq=800):
    # Load image and convert to grayscale
    img = Image.open(image_path).convert('L')
    
    # Convert the image to numpy array and normalize values between 0 and 1
    data = np.asarray(img) / 255.0
    
    # Get the image dimensions
    height, width = data.shape
    
    # Create a time array
    t = np.linspace(0, duration, int(duration * 44100), endpoint=False)
    
    # For simplicity, we'll use only the first row of the image to generate the sound
    # Convert pixel values to frequencies
    frequencies = np.interp(data[0], [0, 1], [base_freq, max_freq])
    
    # Generate sound waveform
    waveform = amplitude * np.sin(2 * np.pi * frequencies[np.newaxis].T * t)
    
    # Sum all waveforms
    waveform = np.sum(waveform, axis=0)
    
    # Play the sound
    sd.play(waveform, samplerate=44100)

# Test
image_to_sound("imgpath.jpg")
sd.wait()
