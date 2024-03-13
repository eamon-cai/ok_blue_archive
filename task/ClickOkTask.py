from scene.OkDialogScene import OkDialogScene
from typing_extensions import override

from autohelper.task.FindFeatureTask import FindFeatureTask


class ClickOkTask(FindFeatureTask):

    @override
    def run_frame(self):
        if self.is_scene(OkDialogScene):
            self.logger.info(f"ClickOkTask: click ok")
            self.click_box(self.scene.dialog_ok)
            self.sleep(1)
            return True
