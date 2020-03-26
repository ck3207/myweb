import os

import requests
from django.conf import settings

class Download:
    """Deload package from https://scm.hundsun.com/"""
    URL = "https://scm.hundsun.com/pkgManage/pkg/downloadFile.htm?downloadPath=%255Bpkg%255D/pkg/%25u676D%25u5DDE%25u4E91%25u7EAA"
    def __init__(self, file_path, headers):
        self.file_path = file_path
        self.headers = headers
        self.basename = os.path.basename(file_path)
        
    def to_unicode(self):
        """Transfer file_path to unicode.
        Attention: when transfer Chinese characters  to unicode, you should add %25 before each Chinese character.
        """
        url = ""
        for character in self.file_path:
            if self.is_chinese_character(character):
                url += str(character.encode('unicode_escape'))
            else:
                url += character
        return url.replace("b'\\\\", "%25").replace("'", "")
        
    def is_chinese_character(self, character):
        """Whether the character is Chinese character or not."""
        if character >= u'\u4e00' and character<=u'\u9fa5':
            return True
        else:
            return False

    def get_download_url(self):
        return Download.URL+self.to_unicode()+"&serverType=test"
        
    def download(self, save_path):
        url = self.get_download_url()
        try:
            r = requests.get(url=url, headers=self.headers, verify=False)
            with open(file=os.path.join(save_path, self.basename), mode="wb") as f:
                f.write(r.content)
        except Exception as e:
            print("Download File Failed From URL:{0}".format(url))
            print(str(e))
        return
        
if __name__ == "__main__":
    download = Download(file_path=r'/iSee智能投顾/test/集成包/h5-isee-manage-geek/SVN24919-h5-isee-manage-geek-20200326-21.30.19.zip', 
    headers={"Cookie": "JSESSIONID=FDF44865889AC6CE70D963446BA7431B"})
    download.download()