import unittest
from regex_file import extract_markdown_images, extract_markdown_links

class TestRegex(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_two(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertNotEqual([("image", "https://i.imgur.com/zjjcJKZ.jpg")], matches)

    def test_mixed_mardown_images_three(self):
        matches=extract_markdown_images(
            "Here is a ![cat](https://cat.jpg) and a [boot dev](https://boot.dev)"
        )
        self.assertListEqual([("cat","https://cat.jpg")], matches)

    def test_mixed_mardown_links_one(self):
        matches=extract_markdown_links(
            "Here is a ![cat](https://cat.jpg)"
        )
        self.assertListEqual([], matches)

    def test_mixed_mardown_links_two(self):
        matches=extract_markdown_links(
            "Here is a ![cat](https://cat.jpg) and a [boot dev](https://boot.dev)"
        )
        self.assertListEqual([("boot dev","https://boot.dev")], matches)
        





if __name__ == "__main__":
    unittest.main()