from .BaseExtractor import BaseExtractor
from ..Database.Models import Content
from ..Utils import SystemUtil


class SelfPostExtractor(BaseExtractor):

    def __init__(self, post, **kwargs):
        super().__init__(post, **kwargs)
        self.download_session_id = kwargs.get('download_session_id', None)

    def extract_content(self):
        try:
            ext = self.settings_manager.self_post_file_format
            directory = self.make_dir_path()
            self.create_dir_path(directory)
            self.make_content(self.url, ext)
        except Exception as e:
            self.failed_extraction = True
            self.failed_extraction_message = f'Failed to save self post.  ERROR: {e}'
            self.logger.error('Failed to save self post',
                              extra={'url': self.url, 'user': self.user, 'subreddit': self.subreddit}, exc_info=True)

    def make_content(self, url, extension, count=None, name_modifier=None):
        if self.check_duplicate_content(url):
            content = Content(
                extension=extension,
                url=url,
                user=self.user,
                subreddit=self.subreddit,
                post=self.post,
            )
            content.title = self.make_title(content)
            content.directory_path = self.make_dir_path(content)
            content.make_download_title()
            self.download_text_post(content)
            session = self.post.get_session()
            session.add(content)
            session.commit()
            return content

    def download_text_post(self, content):
        try:
            with open(content.full_file_path, 'w') as file:
                if content.extension == 'txt':
                    file.write(self.post.text)
                else:
                    file.write(self.post.text_html)
                content.set_downloaded(self.download_session_id)
        except Exception as e:
            content.set_download_error('Failed to save text post', extra={'error': e})

    def create_dir_path(self, dir_path):
        try:
            SystemUtil.create_directory(dir_path)
        except PermissionError:
            self.logger.error('Could not create directory path', extra={'directory_path': dir_path}, exc_info=True)
