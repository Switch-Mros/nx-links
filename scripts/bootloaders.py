from basemodule import BaseModule


class Bootloaders(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "CTCaer",
                "reponame": "hekate",
                "assetPatterns": [".*hekate_ctcaer.*\\.zip"]
            },
        ]
        BaseModule.__init__(self)
