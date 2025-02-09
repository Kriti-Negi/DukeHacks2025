import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import rasterio
import numpy as np
import geoiff
import requests

def display_image(url, key):

    response = requests.get(url)
    response = response.json()

    dsmURL = response['dsmUrl'] + f'&key={key}'
    DMStiff_filename = "dms.tif"

    dsm_response = requests.get(dsmURL)
    if dsm_response.status_code == 200:
        with open(DMStiff_filename, "wb") as file:
            file.write(dsm_response.content)
    else:
        print(f"Failed to download DSM. Status code: {dsm_response.status_code}")

    maskURL = response['maskUrl'] + f'&key={key}'
    MASKtiff_filename = "mask.tif"

    mask_response = requests.get(maskURL)
    if mask_response.status_code == 200:
        with open(MASKtiff_filename, "wb") as file:
            file.write(mask_response.content)
    else:
        print(f"Failed to download RGB. Status code: {mask_response.status_code}")

    rgbURL = response['rgbUrl'] + f'&key={key}'
    RGBtiff_filename = "rgb.tif"

    rgb_response = requests.get(rgbURL)
    if rgb_response.status_code == 200:
        with open(RGBtiff_filename, "wb") as file:
            file.write(rgb_response.content)
    else:
        print(f"Failed to download RGB. Status code: {rgb_response.status_code}")


    monthlyfluxURL = response['monthlyFluxUrl'] + f'&key={key}'
    monthlyflux_filename = "monthlyflux.tif"

    monthly_response = requests.get(monthlyfluxURL)
    if monthly_response.status_code == 200:
        with open(monthlyflux_filename, "wb") as file:
            file.write(monthly_response.content)
    else:
        print(f"Failed to download MonthlyFlux. Status code: {monthly_response.status_code}")

    annualfluxURL = response['annualFluxUrl'] + f'&key={key}'
    annualflux_filename = "annualflux.tif"

    annual_response = requests.get(annualfluxURL)
    if annual_response.status_code == 200:
        with open(annualflux_filename, "wb") as file:
            file.write(annual_response.content)
    else:
        print(f"Failed to download MonthlyFlux. Status code: {annual_response.status_code}")

    List_geotiff_files = [
        MASKtiff_filename,
        annualflux_filename,
        RGBtiff_filename,
        DMStiff_filename,
    ]

    Dict_geotiff_files = {
        'mask': MASKtiff_filename,
        'annual_flux': monthlyflux_filename,
        'rgb': RGBtiff_filename,
        'dsm': DMStiff_filename
    }

    def show_layers(geotiff_files):

        # Step 1: Read the mask file
        with rasterio.open(geotiff_files["mask"]) as mask_src:
            mask = mask_src.read(1)  # Assuming the mask is in the first band

        # Step 2: Read and normalize the RGB image
        with rasterio.open(geotiff_files["rgb"]) as rgb_src:
            red = rgb_src.read(1)
            green = rgb_src.read(2)
            blue = rgb_src.read(3)

            # Normalize RGB bands for display
            def normalize(band):
                return (band - band.min()) / (band.max() - band.min())

            red, green, blue = normalize(red), normalize(green), normalize(blue)
            rgb_image = np.stack((red, green, blue), axis=-1)

        # Step 3: Read all 12 bands of the annual flux data
        with rasterio.open(geotiff_files["annual_flux"]) as flux_src:
            num_bands = flux_src.count  # Should be 12 bands
            print(f"Number of bands: {num_bands}")

            # Step 4: Iterate over each band and generate the images
            for band_index in range(1, num_bands + 1):
                # Read and normalize the flux band
                flux_band = flux_src.read(band_index)
                flux_norm = (flux_band - np.min(flux_band)) / (np.max(flux_band) - np.min(flux_band))

                # Apply a warm colormap
                cmap = plt.cm.plasma  # Choose from 'plasma', 'magma', or 'inferno'
                flux_colored = cmap(flux_norm)[:, :, :3]  # Drop the alpha channel

                # Overlay the flux on the roof areas (mask == 1), else use original RGB
                final_image = np.copy(rgb_image)
                final_image[mask == 1] = 0.6 * flux_colored[mask == 1] + 0.4 * rgb_image[mask == 1]  # Blend

                # Step 5: Display and/or save the image
                plt.figure(figsize=(10, 10))
                plt.imshow(final_image)
                plt.title(f"Annual Flux Band {band_index}")
                plt.axis("off")
                # Save each image (optional)
                # plt.savefig(f"annual_flux_band_{band_index}.png", bbox_inches='tight')

    def show_bands(geotiff_file):

        with rasterio.open(geotiff_file) as src:
            # Get the number of bands and display them
            num_bands = src.count  # Should be 12 for monthly flux
            print(f"Number of bands: {num_bands}")

            # Set up the plot for 12 subplots (one for each month)
            fig, axes = plt.subplots(3, 4, figsize=(15, 10))
            axes = axes.flatten()

            # Iterate through the bands
            for i in range(num_bands):
                band_data = src.read(i + 1)  # Bands are 1-indexed in rasterio

                # Display each band in a subplot
                ax = axes[i]
                im = ax.imshow(band_data, cmap="viridis")  # Change cmap if needed
                ax.set_title(f"Band {i + 1} (Month {i + 1})")
                ax.axis("off")
                fig.colorbar(im, ax=ax, shrink=0.7)

            # Adjust layout and display
            plt.tight_layout()
            #plt.show()

    def show_single(geotiff_file):
        with rasterio.open(geotiff_file) as src:
            red = src.read(1)

            # Stack RGB bands into an image
            rgb_image = np.stack((red), axis=-1)

            # Normalize for display
            rgb_image = (rgb_image / rgb_image.max())  # Rescale to 0-1

            plt.imshow(rgb_image)
            plt.title("Something")
            plt.axis("off")
            #plt.show()

    def interactive_layers(geotiff_files):

        # Step 1: Read the mask file
        with rasterio.open(geotiff_files["mask"]) as mask_src:
            mask = mask_src.read(1)  # Assuming the mask is in the first band

        # Step 2: Read and normalize the RGB image
        with rasterio.open(geotiff_files["rgb"]) as rgb_src:
            red = rgb_src.read(1)
            green = rgb_src.read(2)
            blue = rgb_src.read(3)

            # Normalize RGB bands for display
            def normalize(band):
                return (band - band.min()) / (band.max() - band.min())

            red, green, blue = normalize(red), normalize(green), normalize(blue)
            rgb_image = np.stack((red, green, blue), axis=-1)

        # Step 3: Read all 12 bands of the annual flux data
        with rasterio.open(geotiff_files["annual_flux"]) as flux_src:
            num_bands = flux_src.count  # Should be 12 bands
            print(f"Number of bands: {num_bands}")

            # Set up interactive plotting
            plt.ion()  # Turn on interactive mode
            fig, ax = plt.subplots(figsize=(10, 10))

            # Step 4: Iterate through the 12 bands interactively
            for band_index in range(1, num_bands + 1):
                # Read and normalize the flux band
                flux_band = flux_src.read(band_index)
                flux_norm = (flux_band - np.min(flux_band)) / (np.max(flux_band) - np.min(flux_band))

                # Apply a warm colormap
                cmap = plt.cm.plasma  # Choose from 'plasma', 'magma', or 'inferno'
                flux_colored = cmap(flux_norm)[:, :, :3]  # Drop the alpha channel

                # Overlay the flux on the roof areas (mask == 1), else use original RGB
                final_image = np.copy(rgb_image)
                final_image[mask == 1] = 0.6 * flux_colored[mask == 1] + 0.4 * rgb_image[mask == 1]  # Blend

                # Clear previous image and plot the new one
                ax.clear()
                ax.imshow(final_image)
                ax.set_title(f"Annual Flux Band {band_index} (Month {band_index})")
                ax.axis("off")

                # Display the updated image and wait before switching to the next
                plt.draw()
                plt.pause(1)  # Pause for 1 second before showing the next image

            plt.ioff()  # Turn off interactive mode
            #plt.show()

    # interactive_layers(Dict_geotiff_files)

    show_layers(Dict_geotiff_files)
    plt.savefig("hello.png")
