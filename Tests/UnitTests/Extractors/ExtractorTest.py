import unittest
from unittest.mock import patch
import logging

from Extractors.Extractor import Extractor
from Utils import Injector
from Tests.MockObjects.MockSettingsManager import MockSettingsManager
from Tests.MockObjects import MockObjects


class ExtractorTest(unittest.TestCase):

    logging.disable(logging.CRITICAL)

    link_dict = {
        'DIRECT': 'https://unsupported_site.com/image/3jfd9nlksd.jpg',
        'IMGUR': 'https://imgur.com/fb2yRj0',
        'GFYCAT': 'https://giant.gfycat.com/KindlyElderlyCony.webm',
        'VIDBLE': 'https://vidble.com/show/toqeUzXBIl',
    }

    def setUp(self):
        Injector.settings_manager = MockSettingsManager()

    def test_assign_extractor_direct(self):
        ex = Extractor.assign_extractor(MockObjects.get_unsuppored_direct_post())
        self.assertEqual('DirectExtractor', ex.__name__)

    def test_assign_extractor_imgur(self):
        ex = Extractor.assign_extractor(MockObjects.get_mock_post_imgur())
        self.assertEqual('ImgurExtractor', ex.__name__)

    def test_assign_extractor_gfycat(self):
        ex = Extractor.assign_extractor(MockObjects.get_mock_post_gfycat())
        self.assertEqual('GfycatExtractor', ex.__name__)

    def test_assign_extractor_vidble(self):
        ex = Extractor.assign_extractor(MockObjects.get_mock_post_vidble())
        self.assertEqual('VidbleExtractor', ex.__name__)

    @patch('Extractors.DirectExtractor')
    def test_handle_content(self, ex_mock):
        mock_user = MockObjects.get_blank_user()
        content_list = ['Failed extract one']
        content_list.extend(MockObjects.get_downloadable_content_list(mock_user))
        ex_mock.extracted_content = content_list
        ex = Extractor(mock_user)
        ex.handle_content(ex_mock)

        self.assertTrue('Failed extract one' in mock_user.failed_extracts)
        self.assertTrue(len(mock_user.content) == 1)

        mock_user = MockObjects.get_blank_user()
        mock_user.avoid_duplicates = False
        ex = Extractor(mock_user)
        ex.handle_content(ex_mock)

        self.assertTrue(len(mock_user.content) == 5)

    def test_filter_content(self):
        user = MockObjects.get_blank_user()
        ex = Extractor(user)
        img_content = MockObjects.create_content(user, None, None)
        vid_content = MockObjects.create_content(user, None, None)
        vid_content.file_ext = '.mp4'

        self.assertTrue(ex.filter_content(img_content))
        self.assertTrue(ex.filter_content(vid_content))
        user.download_images = False
        self.assertFalse(ex.filter_content(img_content))
        self.assertTrue(ex.filter_content(vid_content))

        user.download_images = True

        self.assertTrue(ex.filter_content(img_content))
        self.assertTrue(ex.filter_content(vid_content))
        user.download_videos = False
        self.assertTrue(ex.filter_content(img_content))
        self.assertFalse(ex.filter_content(vid_content))

        user.download_videos = True

        user.previous_downloads.append(img_content.url)
        self.assertFalse(ex.filter_content(img_content))
        user.avoid_duplicates = False
        self.assertTrue(ex.filter_content(img_content))

    def test_unsupported_domain(self):
        user = MockObjects.get_blank_user()
        ex = Extractor(user)
        post = MockObjects.get_generic_mock_post()
        post.url = 'https://unsupported-url.com/a/34ndkoij'
        ex.extract(post)
        failed_post = user.failed_extracts[0]
        self.assertTrue(failed_post.status.startswith('Failed to extract post: Url domain not supported'))


if __name__ == '__main__':
    unittest.main()
