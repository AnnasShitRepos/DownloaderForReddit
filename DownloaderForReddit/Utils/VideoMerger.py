"""
Downloader for Reddit takes a list of reddit users and subreddits and downloads content posted to reddit either by the
users or on the subreddits.


Copyright (C) 2017, Kyle Hickey


This file is part of the Downloader for Reddit.

Downloader for Reddit is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Downloader for Reddit is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Downloader for Reddit.  If not, see <http://www.gnu.org/licenses/>.
"""


import subprocess
import os
import logging
from distutils.spawn import find_executable

from ..Database.Models import Content
from ..Utils import Injector, SystemUtil
from ..Messaging.Message import Message


logger = logging.getLogger(__name__)

ffmpeg_valid = find_executable('ffmpeg') is not None


# A dict of MergeSet's containing the path of the video and audio files that are to be merged.
videos_to_merge = []


class MergeSet:

    def __init__(self, video_id, audio_id, date_modified=None):
        """
        Holds data about the parts of a reddit video that are to be merged.
        :param video_id: The id of the content which holds the video portion.
        :param audio_id: The id of the content which holds the audio portion
        :param date_modified: The date that the post containing the video was created.  If set in the settings manager,
                              this will be used to set the files date modified time.
        """
        self.video_id = video_id
        self.audio_id = audio_id
        self.date_modified = date_modified


def merge_videos():
    """
    Iterates the MergeSets in the videos_to_merge list and combines the files at the video path and the audio path to
    the output path.  Also sets the output files "date modified" attribute to the date modified specified in the
    MergeSet if the user settings dictate to do so.
    """
    if ffmpeg_valid:
        db = Injector.get_database_handler()
        with db.get_scoped_session() as session:
            failed_count = 0
            for ms in videos_to_merge:
                try:
                    video_content = session.query(Content).get(ms.video_id)
                    audio_content = session.query(Content).get(ms.audio_id)
                    output_path = video_content.full_file_path.replace('(video)', '')
                    cmd = 'ffmpeg -i "%s" -i "%s" -c:v copy -c:a aac -strict experimental "%s"' % \
                          (video_content.full_file_path, audio_content.full_file_path, output_path)
                    subprocess.call(cmd)
                    if Injector.get_settings_manager().match_file_modified_to_post_date:
                        SystemUtil.set_file_modify_time(output_path, ms.date_modified)
                    clean_up(video_content, audio_content, session)
                except:
                    failed_count += 1
                    logger.error('Failed to merge video', extra={'video_id': ms.video_id, 'audio_id': ms.audio_id,
                                                                 'output_path': output_path}, exc_info=True)
            logger.info('Video merger complete', extra={'videos_successfully_merged': len(videos_to_merge) - failed_count,
                                                        'videos_unsuccessfully_merged': failed_count})
            videos_to_merge.clear()
    else:
        logger.warning('Ffmpeg is not installed: unable to merge video and audio files',
                       extra={'videos_to_merge': len(videos_to_merge)})


def clean_up(video_content, audio_content, session):
    content = Content(
        title=video_content.title.replace('(video)', ''),
        extension='mp4',
        url=video_content.url,
        user=video_content.user,
        subreddit=video_content.subreddit,
        post=video_content.post,
        directory_path=video_content.directory_path,
        downloaded=True,
        download_date=video_content.download_date,
        download_error=video_content.download_error,
        download_session_id=video_content.download_session_id,
        comment_id=video_content.comment_id
    )
    session.add(content)
    SystemUtil.delete_file(video_content.full_file_path)
    SystemUtil.delete_file(audio_content.full_file_path)
    video_content.delete()
    audio_content.delete()
    session.commit()

