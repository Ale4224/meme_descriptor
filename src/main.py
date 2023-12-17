import os
import json
import time
from AIDataGenerator import AIDataGenerator
from MDGenerator import MDGenerator
from dotenv import load_dotenv
from meme_urls import MEME_URLS

load_dotenv()


def get_data():
    if os.environ.get("MOCK_DATA") == "true":
        return get_mock_data()

    use_local_images = os.environ.get("USE_LOCAL_IMAGES") == "true"
    images_to_generate = os.environ.get("NUMBER_OF_MEMES_TO_GENERATE")

    memes_data = []
    if use_local_images:
        meme_dir = "memes"
        meme_images = [
            os.path.join(meme_dir, file)
            for file in os.listdir(meme_dir)
            if file.endswith((".png", ".jpg", ".jpeg"))
        ]

        if images_to_generate is not None:
            meme_images = meme_images[: int(images_to_generate)]

        print(f"Found {len(meme_images)} images")

        for image in meme_images:
            print(f"Generating data for {image}")
            aiDataGenerator = AIDataGenerator(image_path=image)
            data = aiDataGenerator.generate_data()
            memes_data.append(data)
    else:
        urls = MEME_URLS
        if images_to_generate is not None:
            urls = MEME_URLS[: int(images_to_generate)]
        for image_url in urls:
            print(f"Generating data for {image_url}")
            aiDataGenerator = AIDataGenerator(image_url=image_url)
            data = aiDataGenerator.generate_data()
            memes_data.append(data)

    if os.environ.get("SAVE_MOCK_DATA") == "true":
        # save data as json
        with open("./src/mockdata.json", "w") as outfile:
            json.dump(memes_data, outfile, indent=4)

    return memes_data


def get_mock_data():
    with open("./src/mockdata.json") as json_file:
        return json.load(json_file)


def main():
    time_start = time.time()

    mdGenerator = MDGenerator("memes.md")
    memes_data = get_data()
    mdGenerator.generate(memes_data)

    time_end = time.time()
    print(f"Time taken: {time_end - time_start}")


if __name__ == "__main__":
    main()
