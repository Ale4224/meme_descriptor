# this is a markdown generator
from mdutils import MdUtils, Html


class MDGenerator:
    def __init__(self, file_name):
        self.mdFile = MdUtils(file_name=file_name, title="Programming Memes")

    def generate(self, data):
        for meme in data:
            self.mdFile.new_header(level=1, title=meme["title"])
            self.mdFile.new_line(
                Html.image(path=meme["image_path"], size="600", align="center")  # type: ignore
            )

            self.mdFile.new_paragraph(
                meme["sarcastic_sentence"], align="center", bold_italics_code="i"
            )
            self.mdFile.new_paragraph(meme["useful_explenation"])
            self.mdFile.new_line()
        self.mdFile.new_table_of_contents(table_title="Index", depth=1)
        self.mdFile.create_md_file()
