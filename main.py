from PIL import Image, ImageDraw, ImageFont

# Adjust the defaults as needed to get the best performance for your use case
def add_alpha_numeric_grid_to_image(base_image_path, output_path, cell_size=100, grid_color='black', text_opacity=128, text_offset_x=5, label_background_color=(255, 255, 255, 128), font_size=20):
    # Open the base image
    base_image = Image.open(base_image_path).convert("RGBA")

    # Create a new transparent image for the grid and text
    txt = Image.new('RGBA', base_image.size, (255, 255, 255, 0))

    font = ImageFont.truetype("arial.ttf", font_size)

    # Get a drawing context for the grid and text overlay
    d = ImageDraw.Draw(txt)

    # Calculate the number of grid lines needed based on the cell size
    num_x_cells = base_image.width // cell_size
    num_y_cells = base_image.height // cell_size

    # Define a function to convert the cell index to alphanumeric
    def to_alpha_numeric(index):
        if index < 1000:
            return f"{index:03d}"  # 3 digit number with leading zeros
        else:
            index -= 1000  # Adjust index as we start from 1000 for alphabetic
            return f"{chr(65 + index // 100)}{index % 100:02d}"  # Alphabetic prefix with 2 digit number

    # Draw the grid lines and the numbers
    for y in range(num_y_cells + 1):  # Include an extra cell for the partial row
        for x in range(num_x_cells + 1):  # Include an extra cell for the partial column
            # Calculate the position for each cell
            top_left_x = x * cell_size
            top_left_y = y * cell_size
            bottom_right_x = min(top_left_x + cell_size, base_image.width)  # Ensure we do not go beyond the image width
            bottom_right_y = min(top_left_y + cell_size, base_image.height)  # Ensure we do not go beyond the image height

            # Draw the semi-transparent background rectangle for the label
            d.rectangle([top_left_x, top_left_y, bottom_right_x, bottom_right_y], fill=label_background_color)

            # Drawing the grid lines
            d.rectangle([top_left_x, top_left_y, bottom_right_x, bottom_right_y], outline=grid_color)

            # Creating the alphanumeric label for each cell
            label = to_alpha_numeric(x + y * num_x_cells)

            # Calculate text position
            text_x = (top_left_x + bottom_right_x) / 2 - text_offset_x
            text_y = (top_left_y + bottom_right_y) / 2

            # Drawing the label in the middle of the cell, slightly shifted to the left
            d.text((text_x, text_y), label, fill=(0, 0, 0, text_opacity), font=font, anchor="mm")

    # Composite the base image with the grid and text overlay
    combined = Image.alpha_composite(base_image, txt)

    # Save or show the final image
    combined = combined.convert("RGB")  # Remove alpha for saving in jpg format.
    combined.save(output_path)
    combined.show()

# Set the paths for the base image and the output image
base_image_path = 'x.jpg'  # Update to your image file
output_path = 'alpha_numeric_grid_image.jpg'  # Desired output file

# Call the function with the cell size parameter
# You need to play with the grid size number to get a fit for the picture your want to use.
# I have found 100 pixels for 4k and 50 pixels for 1080 works ok.
# Take the alpha_numeric_grid_image.jpg and send that to Chatgpt vision api, you it can now give exact coordinates
# based on the grid cells for objects you can ask it about in natural language.

# I have found using this prompt works very well to give chatgpt vision additional context on how the 
# grids work. Check the prompt.txt file for the prompt info you can use.
add_alpha_numeric_grid_to_image(base_image_path, output_path, cell_size=100)
